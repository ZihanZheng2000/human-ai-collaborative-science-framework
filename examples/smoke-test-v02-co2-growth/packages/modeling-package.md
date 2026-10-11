# Model Package

## Modeling Workflow Identity

- package status: approved (synthetic Modeling Gate, D-13)
- Modeling Researcher: Claude Code (D-8, escalated E-1)
- Modeling Reviewer: Claude Code, separate headless process
- reviewer file: `docs/reviewer-agents/modeling-reviewer-agent.md`
- reviewer mode: critique-only
- review mode: standard
- reviewer rights: advisory + escalation (default)
- decision log: `decision-log.md`
- Modeling Review status: completed
- researcher-agent response status: completed
- Modeling Gate status: approved (synthetic, D-13)

## Modeling Goal

Produce the locked descriptive comparison (D-4, D-9) of decadal Mauna Loa CO2
growth rates with one table, one figure, a rerun check, and a claim-readiness
note, ready for the Modeling Gate.

## Run Manifest and Logs

- run log: `artifacts/smoke-v02-co2-2026-10-10/run_log.md`
- code: `artifacts/code/analyze_growth.py`; environment: `artifacts/code/requirements.txt` (venv, Python 3)

## Modeling Contract

Approved Planning Package (D-10): question D-2, source D-3, locked choices D-4 + D-9.

### Locked Analysis Choices

| Choice | Locked value | Decision ID | Changed after results? | Change decision ID |
|---|---|---|---|---|
| growth definition | first differences of annual means | D-4 | no | |
| comparison units | six complete decades 1960-2019 | D-4 | no | |
| decision rule | 2010s > 1960s AND OLS slope > 0 | D-9 | no | |
| slope uncertainty | HAC SE, lag 2, descriptive | D-9 | no | |
| sensitivity | decades shifted by one year | D-9 | no | |
| partial 2020s row | not in the locked contract | D-4 | **yes**: added to outputs after results were visible, without a decision; now labeled context only | D-12 |

## Exploratory Demo Phase

Not used: the full analysis is 67 rows.

## Data Acquisition Success

All seven D-9 acquisition checks pass (`artifacts/tables/summary.json`); accepted at D-11.

## Data Source Identity

As in the Planning Package. Values are as published by the datasets/co2-ppm mirror of NOAA GML.

## Results

### Headline

Decadal mean growth rose from **0.86 ppm/yr (1960s)** to **2.40 ppm/yr
(2010s)**; the OLS slope of annual growth on year (1960-2019) is 0.028 ppm/yr²
(HAC SE 0.002, Newey-West, Bartlett weights, lag 2, no small-sample correction;
descriptive only). Decision rule D-9 → "increase". Values as published by the
datasets/co2-ppm mirror of NOAA GML.

### Tables

`artifacts/tables/decadal_growth.csv`:

| decade | n_years | mean growth (ppm/yr) |
|---|---|---|
| 1960-1969 | 10 | 0.86 |
| 1970-1979 | 10 | 1.22 |
| 1980-1989 | 10 | 1.64 |
| 1990-1999 | 10 | 1.53 |
| 2000-2009 | 10 | 1.91 |
| 2010-2019 | 10 | 2.40 |
| 2020-2025 (partial, context only, D-12) | 6 | 2.62 |

Sensitivity (`artifacts/tables/decadal_growth_shifted.csv`): 0.88, 1.31, 1.57, 1.53, 2.04, 2.41 for 1961-1970 … 2011-2020.

OLS slope of g_t on year, 1960-2019: 0.028 ppm/yr² (HAC SE 0.002, lag 2).

Decision rule (D-9): 2.40 > 0.86 and slope > 0 → **increase**.

### Figures

`artifacts/figures/annual_growth_decadal_means.png`: annual growth bars with decadal means; the compared 1960s and 2010s means are drawn heavier; the partial 2020s line is dashed and labeled context only.

## Validation Summary

| Check | Result | Artifact |
|---|---|---|
| acquisition rule | pass | `summary.json` |
| rerun reproducibility | identical tables (determinism only; hashes and command recorded) | `artifacts/validation/rerun_check.md` |
| independent hand check | 1960s mean 0.864 from raw values | `artifacts/validation/rerun_check.md` |
| cleaned vs raw | numerically equal; formatting differs on 4 lines | `summary.json` |
| telescoping identity | holds | `summary.json` |

## Claim Readiness Matrix

| Claim | Status | Evidence |
|---|---|---|
| decadal mean growth rose from 0.86 (1960s) to 2.40 (2010s) ppm/yr | supported (descriptive) | table, slope |
| the 1990s decadal mean (1.53) is 0.11 below the 1980s (1.64); with shifted decades the gap is 0.04 | supported (descriptive), endpoint-dependent | tables |
| partial 2020s value | context only, no claim (D-12) | table |

## Failure or Limitation Register

| Item | Note |
|---|---|
| mirror vs official source | NOAA not reachable; values as published by the mirror |
| endpoint dependence | decade means depend on two annual values each (PR-3); slope and sensitivity agree |
| synthetic authorizations | PR-9; D-11, D-12 also synthetic |
| open escalation E-1 | researcher role override and same-model reviewer (PR-1), pending real user |
| post-visibility change | D-12 partial-decade row (MR-1) |
| summary.json precision | working precision; D-9 display precision applies to tables and packages |

## Modeling Reviewer Critique

Full critique: `artifacts/smoke-v02-co2-2026-10-10/reviewer-critique-modeling.md` (standard mode).

| Finding ID | Severity | Concern | Route | Blocks gate? |
|---|---|---|---|---|
| MR-1 | major | headline and a claim rest on an unlocked partial 2020s decade; locked table said nothing changed | Modeling | yes |
| MR-2 | minor | "acceleration" wording and non-monotonic claim exceed locked analysis | Modeling | no |
| MR-3 | minor | HAC variant unstated; summary.json precision differs from D-9 | Modeling | no |
| MR-4 | minor | cleaned vs raw text differences not shown | Modeling | no |
| MR-5 | minor | rerun check thin; script does not create dirs | Modeling | no |
| MR-6 | minor | E-1 not in limitation register | Modeling | no |
| MR-7 | minor | request cites superseded D-1 | Modeling | no |
| MR-8 | accepted limitation | mirror source; endpoint dependence | Reporting | no |
| MR-9 | suggestion | figure lacks legend; locked pair not marked | Reporting | no |

## Researcher-Agent Response to Modeling Review

| Finding ID | Response status | Change made or planned | Blocks gate? | Escalated to user? | User ruling | Notes |
|---|---|---|---|---|---|---|
| MR-1 | accepted and fixed | headline restored to locked result; "highest yet" claim removed; row relabeled context only and logged as D-12 with results-visible flag; locked-choices table corrected | — | no | n.a. | seeded error S1 |
| MR-2 | accepted and fixed | locked phrasing; 0.11 gap and 0.04 shifted gap stated | no | no | n.a. | |
| MR-3 | accepted and fixed | HAC variant stated; precision note in code and register | no | no | n.a. | |
| MR-4 | accepted and fixed | numeric equality check added to script and validation | no | no | n.a. | |
| MR-5 | accepted and fixed | hashes, command, determinism scope, hand check; script creates dirs | no | no | n.a. | |
| MR-6 | accepted and fixed | E-1 and D-11/D-12 synthetic status in register | no | no | n.a. | |
| MR-7 | accepted and fixed | package cites D-8; later requests cite D-8 | no | no | n.a. | request file kept as sent |
| MR-8 | accepted limitation | carried to Reporting | no | no | n.a. | |
| MR-9 | accepted and fixed | legend; compared pair drawn heavier | no | no | n.a. | |

## Modeling Gate Decision

- decision: approve for Reporting
- decision-log ID: D-13
- approval quality: synthetic
- escalated findings ruled on: none new; E-1 pending real user
- open objections carried forward: E-1
- user notes: synthetic gate
- required changes before Reporting: none

## Handoff to Reporting

- claims supported: decadal mean growth 0.86 → 2.40 ppm/yr (1960s → 2010s); positive slope; verdict "increase" (descriptive)
- claims supported only with caveat: 1990s below 1980s (small, endpoint-dependent)
- claims not supported: any cause of the change; "highest yet" for the 2020s; significance claims from the HAC SE
- figures and tables to cite: `decadal_growth.csv`, `decadal_growth_shifted.csv`, `annual_growth_decadal_means.png`
- limitations to acknowledge: mirror source; endpoint dependence; synthetic authorizations; E-1
