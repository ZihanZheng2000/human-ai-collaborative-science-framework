# Planning Package

Package status: REVIEWED, READY FOR PLANNING GATE (revision 1, two majors escalated). Question and claim level
(D-2), data source (D-3), exclusions (D-4), method/metrics (D-5) and the
Decision-Rights Map (D-6) are approved (all synthetic gates/approvals).

## Planning Workflow Identity

- Planning Researcher: Claude Code runtime, started by orchestrator (config `roles` names `codex` as researcher; no user override is logged in the decision log, so the assignment mismatch is disclosed here for the reviewer)
- Planning Reviewer: per `workflow.config.json` roles: claude-code
- review mode: standard
- decision log: `decision-log.md` (setup: D-1, synthetic gates, step-by-step, use reviewer)
- Planning Review status: done; response recorded below
- user Planning Gate status: pending (synthetic gate)

## User-Need Profile (proposed; user request is the only authority so far)

| Field | Proposed answer | Source |
|---|---|---|
| research area | Zoology / descriptive statistics on Pygoscelis penguins | request |
| intended output | Small descriptive workflow demo with a short summary table and figure | "framework trial", "small" |
| purpose | Workflow test | "framework trial" |
| success criterion | A traceable, descriptive comparison of male vs female body mass within each species, produced through all gated stages | request |
| audience | Framework maintainers / internal | inferred |
| data/source | Public Palmer penguins dataset | request |
| novelty expectation | none claimed | inferred; see prior-work scan |
| constraints | small, descriptive; no heavy tooling | "Keep it descriptive and small" |
| avoid-list | no inference beyond description, no causal or biological-mechanism claims, no extra variables | proposed, needs confirmation |
| gate / reviewer | synthetic gates / use reviewer | D-1 |

## Prior Work Scan

Light scan done: `notes/prior-work-scan.md`. Summary: question is well studied
and the dataset is a standard teaching dataset; no novelty is claimed. Citations
there are recalled, not re-verified. Planning depth: light scan, no venue
calibration (internal demo output); revisit trigger: before any external
sharing of the output.

## Feasibility (data access)

Public CSV reachable (HTTP 200), 344 rows, columns include species, sex,
body_mass_g. Only the header and row count were inspected; no values or
distributions have been viewed. Licence: CC0 per the package DESCRIPTION (v0.1.1), recalled and not re-verified in this session; record the licence from the source at acquisition.
Data source and pinning approved in D-3; full Data Source Identity is recorded at acquisition in Modeling.

## Selected or Confirmed Research Route

| Element | Selected value | Status | Decision ID |
|---|---|---|---|
| working research question | Within each of the three species, how do the body-mass distributions of male and female penguins in this dataset compare? | approved (synthetic) | D-2 |
| claim level | Descriptive statements about the sampled birds in this dataset only (group n, mean, median, SD, range, male-minus-female mean difference; D-5 extends this list with the median difference and male/female mean ratio, still descriptive, see PR-5); no hypothesis test, no generalization to populations | approved (synthetic) | D-2 |
| data/source strategy | palmerpenguins CSV pinned by access date + SHA-256, 4-part acquisition success rule | approved (synthetic) | D-3 |
| inclusion/exclusion | complete-case on sex (male/female) and body mass; no other exclusions; dropped-row report | approved (synthetic) | D-4 |
| method family and metrics | per species x sex: n, mean, median, SD, min, max; male-minus-female mean and median difference and mean ratio; one by-sex strip/box plot per species showing all points; no inferential statistics | approved (synthetic) | D-5 |
| Decision-Rights Map | below | approved (synthetic) | D-6 |
| target venue/output | internal workflow-trial demo (short table + figure); no venue | provisional (inferred from "framework trial"); revisit before any external sharing | none yet |
| future-work boundary | inference (tests/CIs), covariates (island, year, bill/flipper size), and cross-species pooling are out of scope | provisional | none yet |

## Planning Depth Decision

| Item | Decision | Reason | Downstream implication |
|---|---|---|---|
| idea maturity | mature | question and data fully specified by the request | no candidate-route comparison needed |
| prior-work scan depth | light | well-known teaching dataset; no novelty claimed (`notes/prior-work-scan.md`) | citations recalled, unverified; verify before any citation is used |
| novelty assessment depth | light | none claimed | none |
| venue calibration depth | skipped | internal demo output | revisit before any external sharing |
| external tool scan | skipped | pandas/matplotlib (or stdlib) suffice; no new skill needed | none |

## Feasibility and Cost Check

| Item | Assessment | Evidence | Fallback |
|---|---|---|---|
| data access | feasible | HTTP 200, 344 rows, header only inspected (`notes/prior-work-scan.md`) | `palmerpenguins` package copy of same file |
| candidate vs usable data | the URL is a candidate until the D-3 success rule is met in Modeling | D-3 | stop and report |
| scale | 344 rows; seconds of compute | row count | none needed |
| API/token cost | none | | |
| licensing | CC0 per package DESCRIPTION (recalled, not re-verified; re-record at acquisition) | | |

## Data Plan

- primary data source: palmerpenguins `penguins.csv` (raw GitHub URL in `notes/prior-work-scan.md`)
- acquisition success rule, pinning, and full Data Source Identity: per D-3, recorded at acquisition in Modeling
- key variables: `species`, `sex`, `body_mass_g`
- unit of analysis: individual sampled bird
- analysis set: complete cases on sex and body mass (D-4); dropped rows reported by species
- minimum viable scale: every species x sex cell non-empty; per-cell n unknown until Modeling and reported as found

## Method Blueprint (locked by D-2..D-5)

1. Acquire and verify raw CSV (D-3); keep raw and cleaned files separate.
2. Apply the D-4 rule; write the dropped-row report.
3. Compute the D-5 table and differences; plot every analysis-set row.
4. Acceptance checks (extended per PR-6):
   - every table statistic (n, mean, median, SD, min, max, differences, ratio) matches an independent csv-module recomputation;
   - per-cell n sums to the analysis-set size; dropped + kept = 344, and the dropped-row report (per-species counts and reasons) reconciles;
   - `sex` values are exactly male/female after inspection for case or whitespace variants, handled only as a logged Tier 0 repair if found;
   - D-3 hash, access date and four-part success rule are recorded;
   - figure plots every analysis-set row;
   - no inferential output (tests, CIs, p-values) is produced.

## Expected Output Package

- tables: species x sex summary; male-minus-female differences; dropped-row report
- figures: one by-sex plot per species
- limitations to acknowledge: single dataset, one site (Palmer Station) and three years; sampled birds only; no inference; missing-sex rows excluded
- claim-evidence map: every Reporting sentence must cite a table/figure row and stay within the D-2 claim level

## Risks and Gate Notes

| Risk | Severity | Mitigation |
|---|---|---|
| "differ" read as a request for a significance test | low | D-2/D-5 fix the descriptive level; adding inference is a new Tier 1 decision |
| Small or empty sex x species cell | low | report n as found; rule is not changed |
| File on `main` changes after download | low | SHA-256 pin (D-3) |
| Researcher agent differs from `roles` (codex) with no logged override | low | disclosed for reviewer; user may log override or reassign |
| Gate mode: config says `real`, D-1 records `synthetic` | low | disclosed; D-1 is the live decision |
| Unverified recalled citations | low | not to be cited until verified |

## Decision-Rights Map

Confirmed in D-6 (synthetic).

| Decision class | Performed by | Authority | Tier | Domain judgment supplied by | Notes |
|---|---|---|---|---|---|
| research purpose, question, claim level | researcher proposes | user | 1 (2 at gate) | user request only; no domain expert; recalled literature is not a judgment source (PR-4) | D-2 |
| prior-work / novelty depth, skip or defer | researcher proposes | user | 1 | | light scan; skipped venue calibration noted in package |
| data source and acquisition success rule | researcher proposes | user | 1 | | D-3 |
| labels, inclusion/exclusion rules | researcher proposes | user | 1 | | D-4, locked before results |
| method family, metrics | researcher proposes | user | 1 | | D-5, locked before results |
| analysis execution and repair within locked contract | researcher | researcher | 0 | | escalate if a repair changes a Tier 1 choice |
| interpretation, causal or domain claims | researcher proposes | user | 1 | no domain expert assigned; biological interpretation is out of claim level | |
| response to blocker/major findings (defer or reject) | researcher proposes | user | 1 | | |
| output route, venue, audience | researcher proposes | user | 1 | | internal demo for now |
| stage transition, backtrack, release, terminate | researcher proposes | user | 2 | | synthetic gates (D-1) |
| workflow mode, reviewer strategy, this map | anyone proposes | user | 1 | | |

- reviewer rights: advisory + escalation (default)
- stages using blind review: Reviewing only (per `workflow.config.json`)
- domain expert involvement: none
- analysis choices locked before results: exclusion rule (D-4), metrics and plot (D-5), data source and success rule (D-3); no validation split (no model)
- decision ID confirming this map: D-6 (synthetic)

## Planning Reviewer Critique

Done: `artifacts/live1/reviewer-critique-planning.md` (2 major, 5 minor, 1 suggestion, 1 accepted limitation).

## Researcher-Agent Response to Planning Review

Triage of `artifacts/live1/reviewer-critique-planning.md` (revision 1). Escalated items are in the decision log Open Escalations table.

| Finding | Severity | Response | Detail |
|---|---|---|---|
| PR-1 | major | needs user decision (escalated) | The researcher cannot close this. The user must state whether the claude-code researcher and synthetic gate mode are intended and log an override. D-1's evidence column is wrong (the config says `gates: real`); the orchestrator owns D-1, so the correction is requested at the gate, not made by me. |
| PR-2 | major | needs user decision (escalated) | Prior-work depth, venue-calibration skip, tool-scan skip, output route/audience, future-work boundary, avoid-list and idea maturity have no authorizer. Proposed for the gate: user confirms the User-Need Profile and Planning Depth table as a whole, with accepted risk and revisit triggers (now in Deferred Items). Not self-closed. |
| PR-3 | minor | accepted and fixed | Removed "checked 2026-10-10" in `notes/prior-work-scan.md`; licence is recalled, to be recorded at acquisition. |
| PR-4 | minor | accepted and fixed | Removed Gorman et al. as a domain-judgment source in the map; "do not cite until verified" retained. |
| PR-5 | minor | accepted and fixed | Claim-level row now states D-5 extends D-2's list (median difference, ratio). Both are descriptive; the user approved D-5. |
| PR-6 | minor | accepted and fixed | Method Blueprint step 4 extended. |
| PR-7 | minor | accepted and fixed | Deferred Items table populated. Deferring decision IDs are "pending PR-2". |
| PR-8 | suggestion | accepted, deferred to Reporting | Reporting must state the descriptive reading of "differ" in the first paragraph. Added to Deferred Items. |
| PR-9 | accepted limitation | acknowledged | All approvals D-1..D-6 are synthetic; a real user must re-authorize if the project goes beyond a framework trial. |

## Planning Gate Decision

pending (synthetic gate)

## Acceptance Rubric for Model Stage

Modeling may begin only after Planning Gate approval and only if: the D-3 acquisition success rule is met; D-2..D-5 are applied unchanged; the Decision-Rights Map is confirmed; and the D-5 acceptance checks pass. Reviewer findings must be fixed, or escalated and ruled on by the user.
