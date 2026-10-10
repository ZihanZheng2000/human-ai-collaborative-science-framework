# Reporting Package

## Report Identity

- project title: Mauna Loa CO2 growth rate, 1960s–2010s (smoke test)
- run ID: smoke-v02-co2-2026-10-10
- output mode: demo report
- output type: internal
- gate mode: synthetic gate
- status: ready for Review (synthetic Reporting Gate, D-15)
- Reporting Researcher: Claude Code (D-8, E-1)
- Reporting Reviewer: Claude Code, separate headless process
- reviewer file: `docs/reviewer-agents/reporting-reviewer-agent.md`
- reviewer mode: critique-only
- review mode: standard
- reviewer rights: advisory + escalation (default)
- decision log: `decision-log.md`
- Reporting Review status: completed
- researcher-agent response status: completed

## Upstream Inputs

- Approved Planning Package (D-10), Modeling Package (D-13)

## Reader-Facing Deliverables

| Deliverable | Path | Audience | Status |
|---|---|---|---|
| report | `deliverables/report.md` | user | revised after Reporting Review |

## Claim-Evidence and Source-Support Map

Every substantive sentence in the report is mapped (reconfiguration D-14: the
map is checked sentence by sentence before each review request).

| Claim in report | Evidence | Status |
|---|---|---|
| 1960s average 0.86, 2010s average 2.40 ppm/yr | `decadal_growth.csv` rows 1, 6; figure | supported |
| straight-line trend over 1960–2019 rises (≈0.028 ppm/yr per year) | `summary.json` `ols_slope_ppm_per_yr2` | supported (descriptive) |
| rule met → "increased" | `summary.json` `verdict`; rule D-9 | supported |
| 1990s (1.53) slightly below 1980s (1.64); boundary-dependent | `decadal_growth.csv` rows 3-4; `decadal_growth_shifted.csv` | supported, endpoint-dependent |
| shifted decades: 0.88 first, 2.41 last | `decadal_growth_shifted.csv` | supported |
| decade average = (end − start)/10 | `summary.json` `telescoping_identity_holds`; hand check in `validation/rerun_check.md` | supported |
| data provenance (URL, date, checksum, licence, citation) | Planning Package Data Source Identity; `summary.json` `raw_sha256` | supported |
| partial 2020–2025 is context only | D-12 | supported |
| removed: "the acceleration is driven by rising fossil-fuel emissions" | none; outside claim level D-2 | **removed** (RR-1) |

## Limitations and Uncertainties

| Limitation | Where disclosed |
|---|---|
| mirror source, NOAA revisions | report Data, Limitations |
| endpoint dependence | report Method, Limitations |
| HAC SE descriptive only | report Limitations |
| prior-work scan deferred (D-5) | report Limitations |
| synthetic approvals; same-model review; E-1 open | report Limitations |

## Reporting Reviewer Critique

Full critique: `artifacts/smoke-v02-co2-2026-10-10/reviewer-critique-reporting.md` (standard mode).

| Finding ID | Severity | Concern | Route | Blocks gate? |
|---|---|---|---|---|
| RR-1 | major | causal sentence exceeds descriptive claim level D-2; absent from the claim map | Reporting | yes |
| RR-2 | minor | "acceleration" reintroduced after MR-2 | Reporting | no |
| RR-3 | minor | claim map incomplete | Reporting | no |
| RR-4 | minor | limitations thin; E-1, D-5, NOAA revisions missing | Reporting | no |
| RR-5 | minor | readability gaps for non-specialists | Reporting | no |
| RR-6 | minor | provenance incomplete in report | Reporting | no |
| RR-7 | suggestion | researcher framing too brief | Reporting | no |
| RR-8 | accepted limitation | mirror, endpoints, synthetic approvals | Reporting | no |

## Researcher-Agent Response to Reporting Review

| Finding ID | Response status | Change made or planned | Blocks gate? | Escalated to user? | User ruling | Notes |
|---|---|---|---|---|---|---|
| RR-1 | accepted and fixed | sentence removed; listed as removed in claim map | — | no | n.a. | seeded error S2 |
| RR-2 | accepted and fixed | "acceleration" removed; "increased" per rule | no | no | n.a. | |
| RR-3 | accepted and fixed | claim map now sentence by sentence | no | no | n.a. | |
| RR-4 | accepted and fixed | limitations expanded in report and package | no | no | n.a. | |
| RR-5 | accepted and fixed | plain-language method, rule outcome stated, IDs removed from report text | no | no | n.a. | |
| RR-6 | accepted and fixed | URL, licence, citation, years used | no | no | n.a. | |
| RR-7 | accepted but deferred | longer framing at the Reviewing request | no | no | n.a. | minor; researcher may close |
| RR-8 | accepted limitation | carried forward | no | no | n.a. | |

Reconfiguration: MR-1 and RR-1 are majors in the same area (claims added
beyond the locked contract) across two passes, which meets the trigger in
`docs/coordination.md`. Adopted as D-14.

## Reporting Gate Decision

- decision: approve for Reviewing
- decision-log ID: D-15
- approval quality: synthetic
- escalated findings ruled on: none new; E-1 pending real user
- open objections carried forward: E-1
- user notes: synthetic gate
- required changes before Review: none
