# Planning Package

This package becomes the **Approved Planning Package** only after the Planning
Gate is approved. Smoke test: sections not relevant to a small public-data test
are marked `n/a (smoke test)`.

## Planning Workflow Identity

- package status: approved (synthetic Planning Gate, D-10)
- Planning Researcher: Claude Code (role override, D-8, escalated as E-1)
- Planning Reviewer: Claude Code, separate headless process (`claude -p`)
- reviewer file: `docs/reviewer-agents/planning-reviewer-agent.md`
- reviewer mode: critique-only
- review mode: standard
- reviewer rights: advisory + escalation (default)
- decision log: `decision-log.md`
- Planning Review status: completed
- researcher-agent response status: completed
- user Planning Gate status: approved (synthetic, D-10)

## User-Need Profile

| User-need field | Proposed answer | User correction or addition |
|---|---|---|
| research area | atmospheric CO2 record (test domain only) | user asked for a smoke test; domain not specified |
| intended output | internal smoke-test report | — |
| workflow mode | auto-until-needed (D-1) | — |
| research purpose | exercise the v0.2 workflow rules end to end | — |
| practical success criterion | every Tier 1/2 decision logged; reviewer passes run; escalation and blind review exercised; workflow evaluation filled | — |
| data/source direction | public data | — |
| novelty expectation | no novelty claim (D-5) | — |
| gate mode | synthetic gates | — |
| reviewer strategy | use reviewer (D-1) | — |

## Domain Onboarding

- status: skipped — no user materials

## Prior Work Scan

Deferred (D-5). Risk accepted: the descriptive expectation (growth accelerated) is unreferenced in this run, so the output must not be reused as a literature-grounded claim (PR-8).
Revisit trigger: the output is reused beyond this smoke test.

## Planning Depth Decision

| Item | Decision | Reason |
|---|---|---|
| idea maturity | mature (well-documented phenomenon) | test content chosen for low ambiguity |
| literature/prior-work scan depth | deferred (D-5) | no novelty claim |
| novelty assessment depth | skipped | no novelty claim |
| venue/output calibration depth | skipped | internal report only |

## Feasibility and Cost Check

| Item | Assessment | Evidence or test | Fallback |
|---|---|---|---|
| data access | feasible | annual and monthly CSVs downloaded from the GitHub mirror (HTTP 200) | none needed |
| official host access | blocked | gml.noaa.gov denied by egress proxy | use mirror; record mismatch risk |
| candidate sources vs usable data | annual file usable; monthly file has column misalignment | `notes/route.md` | monthly file not used |
| runtime/storage | trivial | 67 rows | — |
| API/token cost | reviewer passes only | — | — |
| licensing | ODC-PDDL-1.0 (mirror); NOAA public-domain terms with attribution/no-endorsement conditions | mirror README | — |

## Data Source Identity

| Role | Source name or URL | Version/date/access date | License/access status | Notes |
|---|---|---|---|---|
| raw data host | https://raw.githubusercontent.com/datasets/co2-ppm/main/data/co2-annmean-mlo.csv | accessed 2026-10-10; sha256 b1548ede…c33c4 | ODC-PDDL-1.0 | mirror, not NOAA |
| official data source | NOAA GML, Trends in Atmospheric Carbon Dioxide, Mauna Loa (gml.noaa.gov/ccgg/trends) | not accessible from this environment | public domain with NOAA conditions | mirror may lag NOAA revisions |
| documentation source | datasets/co2-ppm README; NOAA GML trends pages | accessed 2026-10-10 (README only) | — | — |
| citation source | Tans (NOAA/ESRL) and Keeling (Scripps), as cited in the mirror README | — | — | — |

## Selected or Confirmed Research Route

| Route element | Selected value | Evidence or reason | User confirmation status | Decision ID |
|---|---|---|---|---|
| working research question | Did the Mauna Loa annual-mean CO2 growth rate increase across complete decades 1960s-2010s? | `notes/route.md` | synthetic | D-2 |
| intended output and claim level | internal report; descriptive only, no attribution | smoke test | synthetic | D-2 |
| data/source strategy | GitHub mirror of NOAA annual means | official host blocked | synthetic | D-3 |
| method family | first differences + decadal means + OLS trend | simplest adequate method | synthetic | D-4 |
| future-work boundary | causes of acceleration; seasonal amplitude; global series | outside run evidence | synthetic | D-2 |

## Decision-Rights Map

Default map from `docs/decision-rights.md` (D-6).

| Decision class | Performed by | Authority | Tier | Domain judgment supplied by | Notes |
|---|---|---|---|---|---|
| research purpose, question, claim level | researcher proposes | user (synthetic here) | 1 (2 at gate) | n/a | |
| prior-work / novelty depth, skip or defer | researcher proposes | user (synthetic) | 1 | n/a | D-5 |
| data source and acquisition success rule | researcher proposes | user (synthetic) | 1 | n/a | |
| labels, inclusion/exclusion rules | researcher proposes | user (synthetic) | 1 | n/a | lock before results |
| method, metrics, comparisons | researcher proposes | user (synthetic) | 1 | n/a | lock before results (D-4) |
| analysis execution and repair within locked contract | researcher | researcher | 0 | | |
| repair, cleaning, retries within locked contract | researcher | researcher; escalate if it changes a Tier 1 choice | 0 | | |
| critique of a package | reviewer | advisory; may escalate | — | | |
| output route, venue, audience | researcher proposes | user (synthetic) | 1 | | internal report |
| researcher / reviewer assignment | anyone proposes | **real user** | 1 | | D-8, escalated E-1 (PR-7) |
| claims beyond the locked contract | researcher runs sentence-by-sentence claim check before each review request | user (synthetic) | 1 | | added by reconfiguration D-14 |
| interpretation, causal or domain claims | researcher proposes | user (synthetic) | 1 | n/a | causal claims out of scope (D-2) |
| response to blocker/major findings (defer or reject) | researcher proposes | **real user** | 1 | | escalations in a smoke test still go to the real user at the end of the run |
| stage transition, backtrack, release, terminate | researcher proposes | user (synthetic) | 2 | | |
| workflow mode, reviewer strategy, this map | anyone proposes | user | 1 | | D-1, D-6 |

- reviewer rights: advisory + escalation
- stages using blind review: Reviewing
- domain expert involvement: none
- decision ID confirming this map: D-6

### Locked Analysis Choices

Locked at D-4 and amended at D-9, both before any growth rate was computed.

| Choice | Locked value |
|---|---|
| growth definition | g_t = annual mean_t − annual mean_{t−1} (ppm/yr) |
| comparison units | growth years 1960-1969, 1970-1979, …, 2010-2019 (six complete decades only) |
| metric | decadal mean of g_t |
| comparisons | first vs last complete decade; OLS slope of g_t on year, 1960-2019 |
| decision rule for "increase" | 2010s mean > 1960s mean AND OLS slope > 0; otherwise "mixed", no increase claim (D-9) |
| slope uncertainty | Newey-West HAC SE, lag 2, descriptive only (D-9) |
| precision | full precision in computation; 2 decimals in display (3 for slopes) (D-9) |
| sensitivity | decades shifted by one year (1961-1970 … 2011-2020), reported, not used for the claim (D-9) |
| exclusions | none |
| files | annual-mean file only; monthly file not used; Uncertainty column carried, not used |

Note on the metric (PR-3): a decadal mean of first differences telescopes to
(end-year mean − prior end-year mean)/10, so each decade depends on two annual
values; the OLS slope and the shifted-decade sensitivity check reduce that
endpoint dependence.

The decade scheme follows from the complete-decade rule, not from the 2023-2025
tail values seen during acquisition (PR-4).

## External Tool and Skill Scan

n/a (smoke test): Python with pandas and matplotlib in a project-scoped venv.

## Planning Reviewer Critique

Full critique: `artifacts/smoke-v02-co2-2026-10-10/reviewer-critique-planning.md` (standard mode).

| Finding ID | Severity | Concern | Route | Blocks gate? |
|---|---|---|---|---|
| PR-1 | major | role override not approved by a user who saw it; D-1 bundled four decisions | user decision | no (synthetic) |
| PR-2 | major | locked choices lack a decision rule, SE method, rounding, typing, Uncertainty use, checksum rule | Planning | yes for a real gate |
| PR-3 | minor | decade metric depends on endpoints only | Planning | no |
| PR-4 | minor | decade lock made after tail values were seen | Planning | no |
| PR-5 | minor | acquisition rule checks structure only | Planning | no |
| PR-6 | minor | mirror provenance asserted, not verified | Planning | no |
| PR-7 | minor | "default" map omits default rows | Planning | no |
| PR-8 | minor | "risk accepted: none" for deferred scan | Planning | no |
| PR-9 | accepted limitation | all Tier 1 decisions synthetic | user decision | no |
| PR-10 | suggestion | per-stage critique filename deviates from protocol | Planning | no |

## Researcher-Agent Response to Planning Review

| Finding ID | Response status | Change made or planned | Blocks gate? | Escalated to user? | User ruling | Notes |
|---|---|---|---|---|---|---|
| PR-1 | needs user decision | D-1 split into D-7 (setup) and D-8 (role override); D-8 escalated as E-1 | no (synthetic) | yes | pending | shown to the real user at end of run |
| PR-2 | accepted and fixed | D-9 locks decision rule, HAC SE, precision, typing, Uncertainty use, checksum rule before results | — | no | n.a. | |
| PR-3 | accepted and fixed | metric note + shifted-decade sensitivity (D-9) | no | no | n.a. | |
| PR-4 | accepted and fixed | sentence added to Locked Analysis Choices and D-9 | no | no | n.a. | |
| PR-5 | accepted and fixed | acquisition rule extended (D-9) | no | no | n.a. | |
| PR-6 | accepted and fixed | "as published by the mirror" wording required | no | no | n.a. | |
| PR-7 | accepted and fixed | omitted default rows restored, incl. assignment row | no | no | n.a. | |
| PR-8 | accepted and fixed | accepted risk stated | no | no | n.a. | |
| PR-9 | accepted limitation | carried forward | no | no | n.a. | |
| PR-10 | accepted and fixed | stdout moved to `agent/`; naming gap recorded as framework lesson F1 | no | no | n.a. | |

## Approved Research Question

`Did the Mauna Loa annual-mean CO2 growth rate (ppm/yr) increase across the complete decades 1960s-2010s?`

## Hypotheses or Expected Claims

- Descriptive expectation: decadal mean growth is higher in the 2010s than in the 1960s. No causal claim.

## Data Plan

- primary data source: annual-mean file (D-3)
- acquisition success rule: parses; unique years continuous 1959 to ≥2020; no missing or sentinel values (≤0, −9.99); Mean within 300-450 ppm; sha256 matches the logged value (D-9)
- reporting wording: values are "as published by the datasets/co2-ppm mirror of NOAA GML" (PR-6)
- unit of analysis: year
- time coverage: 1959-2025 available; 1960-2019 growth years used

## Method Blueprint

1. Validate acquisition rule; copy to `artifacts/data/cleaned/` unchanged except typing.
2. Compute g_t and decadal means for the six locked decades.
3. OLS slope of g_t on year (1960-2019) with standard error.
4. One table, one figure; rerun check.

## Expected Package

- table: decadal mean growth; figure: annual growth with decadal means
- limitations: mirror vs official source; annual means only; descriptive only

## Risks and Gate Notes

| Risk | Severity | Mitigation |
|---|---|---|
| mirror differs from current NOAA release | minor | record checksum and access date; descriptive claim tolerates small revisions |
| same-model reviewer limits independence | minor | recorded in D-1; evaluate in run notes |

## Planning Gate Decision

- decision: approve for Modeling
- gate mode: synthetic gate
- decision maker: researcher agent (synthetic)
- decision-log ID: D-10
- approval quality: synthetic
- escalated findings ruled on: PR-1 -> pending real user (E-1)
- open objections carried forward: E-1
- required changes before Modeling: none beyond D-9 (done)
- accepted limitations: PR-9 (synthetic authorizations); mirror vs official source

## Acceptance Rubric for Modeling Stage

- question, claim level, source, and locked choices are recorded (D-2, D-3, D-4)
- acquisition success rule is explicit
- reviewer findings are triaged; every escalated blocker/major has a user ruling or is carried as an open escalation
