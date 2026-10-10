# Rerun Check

Command (from the example root, venv with `artifacts/code/requirements.txt`):

```
python -I artifacts/code/analyze_growth.py .
```

Two consecutive runs after the MR-1/MR-5 revision produced identical tables:

```
25f7927377797807195d6a92fe8e554af8952a16cacfe00a980dd64438cbb40f  artifacts/tables/decadal_growth.csv
6df134d75dc79264a7784e8168d04075f6099355cef85eb4bcf8d636ac997716  artifacts/tables/decadal_growth_shifted.csv
```

Scope: this checks **determinism only**, not correctness.

Correctness checks:

- Hand check from the raw file, independent of the script: 1960s decadal mean =
  (1969 mean 324.62 − 1959 mean 315.98) / 10 = 0.864 ppm/yr; the script reports 0.864.
- Telescoping identity holds for all six decades (`summary.json`).
- Cleaned file equals raw file numerically (`cleaned_equals_raw_numerically: true`);
  text differs only in float formatting on four lines (MR-4).
- Acquisition rule (D-9): all seven checks true; raw sha256 matches the logged value.
