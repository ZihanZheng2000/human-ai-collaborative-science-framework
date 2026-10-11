"""Mauna Loa CO2 growth-rate analysis for smoke-v02-co2-2026-10-10.

summary.json keeps working precision (4-5 decimals); D-9 display precision
applies to tables and packages. HAC SE: Newey-West, Bartlett weights, lag 2,
no small-sample correction.

Implements the locked analysis choices D-4 and D-9 in ../../decision-log.md.
Usage: python analyze_growth.py <example_root>
"""

import hashlib
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

EXPECTED_SHA256 = "b1548ededea6f9b7eecac370753de8d8da6e0afafe1041f749a11db78c2e33c4"
HAC_LAG = 2


def acquisition_check(raw_path: Path):
    digest = hashlib.sha256(raw_path.read_bytes()).hexdigest()
    if digest != EXPECTED_SHA256:
        raise SystemExit(f"checksum mismatch: {digest}")
    df = pd.read_csv(raw_path)
    df["Year"] = df["Year"].astype(int)
    df["Mean"] = df["Mean"].astype(float)
    df["Uncertainty"] = df["Uncertainty"].astype(float)
    years = df["Year"].tolist()
    checks = {
        "unique_years": df["Year"].is_unique,
        "continuous": years == list(range(years[0], years[-1] + 1)),
        "starts_1959": years[0] == 1959,
        "reaches_2020": years[-1] >= 2020,
        "no_missing": not df[["Year", "Mean"]].isna().any().any(),
        "no_sentinels": bool((df["Mean"] > 0).all() and (df["Mean"] != -9.99).all()),
        "range_300_450": bool(df["Mean"].between(300, 450).all()),
    }
    if not all(checks.values()):
        raise SystemExit(f"acquisition rule failed: {checks}")
    return df, checks, digest


def hac_ols(x: np.ndarray, y: np.ndarray, lag: int):
    X = np.column_stack([np.ones_like(x), x])
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    e = y - X @ beta
    xe = X * e[:, None]
    S = xe.T @ xe
    for l in range(1, lag + 1):
        w = 1 - l / (lag + 1)
        G = xe[l:].T @ xe[:-l]
        S += w * (G + G.T)
    XtX_inv = np.linalg.inv(X.T @ X)
    V = XtX_inv @ S @ XtX_inv
    return beta[1], float(np.sqrt(V[1, 1]))


def decade_means(g: pd.Series, starts):
    rows = []
    for s in starts:
        span = g.loc[s : s + 9]
        rows.append({"decade": f"{s}-{s + 9}", "n_years": len(span), "mean_growth_ppm_per_yr": span.mean()})
    return pd.DataFrame(rows)


def main(root: Path) -> None:
    art = root / "artifacts"
    for sub in ("data/cleaned", "tables", "figures"):
        (art / sub).mkdir(parents=True, exist_ok=True)
    df, checks, digest = acquisition_check(art / "data/raw/co2-annmean-mlo.csv")
    df.to_csv(art / "data/cleaned/co2-annmean-mlo-typed.csv", index=False)
    raw_vals = pd.read_csv(art / "data/raw/co2-annmean-mlo.csv")
    cleaned_equal = bool(np.array_equal(raw_vals.to_numpy(dtype=float), df.to_numpy(dtype=float)))

    s = df.set_index("Year")["Mean"]
    g = s.diff().dropna()

    main_tbl = decade_means(g, range(1960, 2020, 10))
    sens_tbl = decade_means(g, range(1961, 2021, 10))
    partial = g.loc[2020:]
    main_tbl = pd.concat(
        [main_tbl, pd.DataFrame([{"decade": f"2020-{partial.index.max()} (partial, context only, D-12)", "n_years": len(partial),
                                  "mean_growth_ppm_per_yr": partial.mean()}])],
        ignore_index=True,
    )

    gw = g.loc[1960:2019]
    slope, se = hac_ols(gw.index.to_numpy(dtype=float), gw.to_numpy(), HAC_LAG)

    first, last = main_tbl.iloc[0, 2], main_tbl.iloc[5, 2]
    verdict = "increase" if (last > first and slope > 0) else "mixed"

    # Telescoping identity check (PR-3): decade mean == (end - prior end) / 10
    ident = all(
        abs(main_tbl.iloc[i, 2] - (s[1969 + 10 * i] - s[1959 + 10 * i]) / 10) < 1e-9 for i in range(6)
    )

    main_tbl.round(2).to_csv(art / "tables/decadal_growth.csv", index=False)
    sens_tbl.round(2).to_csv(art / "tables/decadal_growth_shifted.csv", index=False)

    fig, ax = plt.subplots(figsize=(7, 3.6))
    ax.bar(g.index, g.values, color="#9bb7d4", label="annual growth (ppm/yr)")
    for i in range(6):
        y0 = 1960 + 10 * i
        compared = i in (0, 5)
        ax.hlines(main_tbl.iloc[i, 2], y0 - 0.5, y0 + 9.5, color="#1f3b73", lw=3 if compared else 1.5,
                  label="decadal mean (1960s and 2010s compared, D-4)" if i == 0 else None)
    ax.hlines(main_tbl.iloc[6, 2], 2019.5, partial.index.max() + 0.5, color="#c05030", lw=1.5, linestyles="dashed",
              label="2020-2025 partial, context only (D-12)")
    ax.legend(fontsize=7, loc="upper left")
    ax.set_xlabel("year")
    ax.set_ylabel("ppm per year")
    ax.set_title("Mauna Loa annual-mean CO2 growth (mirror of NOAA GML)")
    fig.tight_layout()
    fig.savefig(art / "figures/annual_growth_decadal_means.png", dpi=150)

    summary = {
        "raw_sha256": digest,
        "acquisition_checks": checks,
        "years_available": [int(df.Year.min()), int(df.Year.max())],
        "decade_first_1960s": round(first, 4),
        "decade_last_2010s": round(last, 4),
        "ols_slope_ppm_per_yr2": round(slope, 5),
        "hac_se_lag2": round(se, 5),
        "verdict": verdict,
        "telescoping_identity_holds": ident,
        "cleaned_equals_raw_numerically": cleaned_equal,
        "hand_check_1960s": round((s[1969] - s[1959]) / 10, 4),
        "partial_2020s_mean": round(partial.mean(), 4),
    }
    (art / "tables/summary.json").write_text(json.dumps(summary, indent=2))
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main(Path(sys.argv[1]).resolve())
