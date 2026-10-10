# Modeling Package

## Modeling Workflow Identity

- package status: draft for Modeling Review / revised after Modeling Review / approved
- Modeling Researcher: researcher agent name or runtime
- Modeling Reviewer: reviewer agent name or runtime / skipped
- reviewer file: `docs/reviewer-agents/modeling-reviewer-agent.md`
- reviewer mode: critique-only / edits explicitly authorized by user / skipped
- review mode: standard / blind
- reviewer rights: advisory + escalation (default) / other per Decision-Rights Map
- decision log: `decision-log.md`
- Modeling Review status: pending / completed / skipped
- researcher-agent response status: pending / completed / not applicable
- Modeling Gate status: pending / approved / revise / backtrack / terminate

## Modeling Goal

- goal statement:
- goal start trigger:
- execution mode: demo-first / full-scale / addendum
- goal stop condition: Modeling Package ready for Modeling Gate / user decision needed / backtrack to Plan / terminate / user paused
- first successful script/table/figure treated as final stop? no

## Run Manifest and Logs

- run ID:
- run manifest path:
- run log path:
- run summary path:
- agent artifacts path, if any:
- exploratory demo phase used? yes / no
- scale-up status: not applicable / not needed / continued within contract / user decision needed / completed / rejected

## Modeling Contract

- approved research question:
- selected skill cards:
- external tools/packages/APIs allowed:
- target analysis:
- allowed data sources:
- key variables:
- expected figures:
- expected tables:
- iteration budget:
- evidence-deepening budget:
- accepted claim level: full manuscript / preliminary manuscript / demo / internal check
- backtrack conditions:

### Locked Analysis Choices

Choices locked at a Tier 1 checkpoint before results were visible. Any later
change needs a new decision that says results were already seen.

| Choice | Locked value | Decision ID | Changed after results? | Change decision ID |
|---|---|---|---|---|
| labels / event definitions |  |  | no / yes |  |
| inclusion / exclusion rules |  |  | no / yes |  |
| evaluation metrics |  |  | no / yes |  |
| model search space |  |  | no / yes |  |
| validation split |  |  | no / yes |  |

## Exploratory Demo Phase

Use this section when Modeling starts with a small exploratory demo.

| Item | Value |
|---|---|
| demo sample or scope |  |
| workflow steps exercised |  |
| demo success criteria |  |
| issues found |  |
| changes needed before scale-up |  |
| scale-up recommendation | continue within contract / user decision needed / revise demo / narrow scope / backtrack to Plan / terminate |

### Demo-Phase Scale-Up Decision

- decision: continue within contract / user decision needed / revise demo / narrow scope / backtrack to Plan / terminate / not used
- decision notes:
- approved full-scale scope:
- required changes before scale-up:

## External Tool and Package Use Log

Record external packages, APIs, datasets, compute tools, or experiment frameworks used during Model. External outputs still require preflight, validation, and claim-readiness checks.

| Tool/package/API/dataset | Version/access date | Task | Input | Output artifact | Verification status | Limitation |
|---|---|---|---|---|---|---|
|  |  | data acquisition / extraction / modeling / visualization / validation / other |  |  | verified / unresolved / failed |  |

## Data Acquisition Success

| Data source | Target count | Attempted | Retrieved | Usable | Failed | Failure reasons | Stop rule met? |
|---|---:|---:|---:|---:|---:|---|---|
|  |  |  |  |  |  |  |  |

Only usable data count toward the approved data scale. Candidate links, metadata records, search hits, or inaccessible files do not count unless the plan explicitly defines them as data.

## Data Provenance

| Data source | Access method | Version/date | Raw location | Cleaned location | Notes |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## Data Source Identity

Distinguish the exact raw data used from official documentation, mirrors, package excerpts, and citation sources.

| Role | Source name or URL | Version/release/access date | License/access status | Verified relationship to raw data |
|---|---|---|---|---|
| raw data host or query endpoint |  |  |  |  |
| official data source or owner |  |  |  |  |
| documentation source |  |  |  |  |
| citation source |  |  |  |  |

## Environment

- execution format: notebook / script / container
- language:
- environment strategy: project `.venv` / Conda / container / managed runtime / standard library only / existing environment / other
- environment path or identifier:
- dependency declaration file: `requirements.txt` / `pyproject.toml` / `environment.yml` / `Dockerfile` / lock file / none
- package file:
- dependency installation policy: install into project environment only / use predeclared dependencies only / standard library only / other
- dependency freeze or version record:
- random seed:
- operating assumptions:

## Environment Repair Decisions

Use this section when execution fails because of missing packages, incompatible versions, shell differences, hardware limits, unavailable binaries, or runtime constraints.

| Problem | Options considered | Decision | Outcome | Logged in execution history? |
|---|---|---|---|---|
|  | install dependency into project environment / simplify implementation / use container / change runtime or hardware / reduce scope / ask user / backtrack to Plan / none encountered |  |  | yes / no |

## Dependency Change Log

Record dependency changes made during Model. Do not silently install packages into a global/shared interpreter.

| Dependency or environment change | Reason | Scope | Command or method | Dependency file updated? | Outcome |
|---|---|---|---|---|---|
|  |  | project environment / container / managed runtime / global exception / none |  | yes / no / not applicable |  |

## Preflight Checks

| Check | Status | Notes |
|---|---|---|
| required data accessible |  |  |
| required columns present |  |  |
| acquisition success rule satisfied |  |  |
| modality-specific extraction works |  |  |
| units and coverage checked |  |  |
| missingness measured |  |  |
| sample size plausible |  |  |
| licensing/access acceptable |  |  |

## Data Quality Audit

| Check | Status | Issue found | Decision |
|---|---|---|---|
| missingness by key variable |  |  |  |
| duplicate rows or identifiers |  |  |  |
| impossible or out-of-range values |  |  |  |
| unit consistency |  |  |  |
| date/time consistency |  |  |  |
| category-label consistency |  |  |  |
| outliers |  |  |  |
| coverage gaps |  |  |  |
| metadata-data consistency |  |  |  |

## Data Cleaning Log

| Cleaning action | Reason | Affected data | Approved by user? | Notes |
|---|---|---|---|---|
|  |  |  |  |  |

## Code Artifacts

| Artifact | Path | Purpose |
|---|---|---|
|  |  |  |

## Execution Log Summary

| Run | Purpose | Status | Key output | Notes |
|---|---|---|---|---|
|  |  |  |  |  |

## Results

### Tables

| Table | Path | What it supports | Validation status |
|---|---|---|---|
|  |  |  |  |

### Figures

| Figure | Path | What it supports | Validation status |
|---|---|---|---|
|  |  |  |  |

## Preliminary Finding Briefs

Write a brief after the first executable result and after major evidence-deepening iterations.

| Brief | Initial finding | Correctness check | Confidence | Sufficiency check | Missing evidence | Next action |
|---|---|---|---|---|---|---|
|  |  | pass / concern / fail | high / medium / low | sufficient / insufficient / uncertain |  | pass / repair / deepen / ask user / backtrack |

## Model State Tracker

| Step | State | Evidence or trigger | Next valid action |
|---|---|---|---|
|  | data_acquisition / preflight / minimal_result_ready / correctness_check / correctness_failed / correctness_passed / evidence_sufficiency_check / evidence_insufficient / evidence_deepening / user_decision_needed / model_gate_ready / backtrack_to_plan / terminate |  |  |

## Model Critic Pass

| Finding or output reviewed | Critic question | Concern | Decision |
|---|---|---|---|
|  | Does this support the claim? Are variables, units, filters, labels, baselines, robustness, validation, leakage, circularity, and overclaiming acceptable? |  | pass / repair / deepen / ask user / backtrack / terminate |

## Next Analysis Queue

Used when a correct result is not yet sufficient.

| Proposed analysis or artifact | Purpose | Claim or uncertainty addressed | Expected value | Cost/runtime | Priority | Within contract? | User approval needed? | Status |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  | high / medium / low | yes / no / uncertain | yes / no | queued / running / done / deferred / rejected |

## Validation Summary

- code reruns from a fresh session:
- outputs match expected schema:
- transformations logged:
- data-quality issues handled or carried forward:
- cleaning decisions logged:
- values in plausible ranges:
- leakage or invalid controls checked:
- required robustness checks:
- preliminary findings passed correctness checks:
- model critic blocking issues resolved or deferred:
- next-analysis queue completed or intentionally deferred:
- evidence is sufficient for accepted claim level:
- limitations to carry into Reporting:

## Evidence-Deepening Log

Used when a correct preliminary result is not yet sufficient for the research purpose or manuscript.

| Iteration | Claim or uncertainty addressed | Why current evidence was insufficient | Added analysis/figure | Within contract? | Outcome | Stop/continue reason |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

## Reporting-Support Artifacts

- main findings:
- null or weak findings:
- surprising or contradictory findings:
- robustness checks completed:
- robustness checks not completed:
- data-quality issues affecting interpretation:
- assumptions supported:
- assumptions violated or uncertain:
- plausible alternative explanations:
- limitations that must be acknowledged:
- candidate follow-up analyses:

## Claim Readiness Matrix

| Claim candidate | Evidence supporting it | Readiness | Required wording | Remaining need |
|---|---|---|---|---|
|  |  | strong / preliminary / unsupported / needs user judgment |  |  |

## Downstream Figure and Addendum Needs

| Need | Type | Reason | Must return to Model? | User approval needed? |
|---|---|---|---|---|
|  | empirical figure / robustness table / diagnostic plot / conceptual diagram |  | yes / no / depends |  |

## Iteration History

| Iteration | Trigger | Action | Outcome | Stop/continue reason |
|---|---|---|---|---|
|  |  |  |  |  |

## Failure or Limitation Register

| Issue | Type | Severity | Decision | Reporting note |
|---|---|---|---|---|
|  |  |  |  |  |

## Modeling Reviewer Critique

Use `docs/reviewer-agents/modeling-reviewer-agent.md` before the Modeling Gate when a separate reviewer agent is available and approved.

| Finding ID | Severity | Concern | Evidence or reasoning | Route | Blocks gate? | Recommended action |
|---|---|---|---|---|---|---|
| MR-1 | blocker / major / minor / suggestion / accepted limitation |  |  | Planning / Modeling / Reporting / Reviewing / Terminate / user decision | yes / no |  |

If Modeling Review was skipped, record why:

- skipped reason:
- risk accepted:
- revisit trigger:

## Researcher-Agent Response to Modeling Review

Blocker and major findings that are deferred or rejected are escalated: add
them to the decision log's Open Escalations and quote them at the gate. Only the
user can uphold the response.

| Finding ID | Response status | Change made or planned | Blocks gate? | Escalated to user? | User ruling | Notes |
|---|---|---|---|---|---|---|
| MR-1 | accepted and fixed / accepted but deferred / rejected with reason / needs user decision |  | yes / no | yes / no | upheld / overturned / pending / n.a. |  |

## Modeling Gate Decision

- decision: approve for Reporting / approve with limitations / edit required / request reporting-support addendum / revise Model / backtrack to Plan / terminate
- decision-log ID:
- approval quality: substantive / nominal (what was missing) / synthetic
- escalated findings ruled on: finding ID -> upheld / overturned
- open objections carried forward:
- user notes:
- data-quality or cleaning concerns:
- finding correctness concerns:
- model critic concerns:
- evidence sufficiency concerns:
- deferred next-analysis items:
- required changes before Reporting:

## Handoff to Reporting

- claims supported by results:
- claims supported only as preliminary:
- claims not supported:
- figures and tables to cite:
- reporting-support points:
- empirical addenda still needed:
- methods details to report:
- limitations to acknowledge:

## Model Addendum Log

Used when Reporting or Reviewing requests an additional empirical figure, table, robustness check, or analysis.

| Addendum | Requested by | Downstream need | Action taken | Validation status | Returned to requester? |
|---|---|---|---|---|---|
|  |  |  |  |  |  |
