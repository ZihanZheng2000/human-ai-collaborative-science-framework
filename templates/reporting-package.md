# Reporting Package

## Report Identity

- project title:
- run ID:
- output mode: demo report / technical appendix / decision brief / review packet / dashboard or table package / manuscript or paper / slide deck / web page or interactive report / software package or tool release / other
- output type: internal / demo / preliminary / review-ready / release-ready
- report date:
- gate mode: real user gate / synthetic gate / mixed
- status: draft / revised / ready for Review
- Reporting Researcher: researcher agent name or runtime
- Reporting Reviewer: reviewer agent name or runtime / skipped
- reviewer file: `docs/reviewer-agents/reporting-reviewer-agent.md`
- reviewer mode: critique-only / edits explicitly authorized by user / skipped
- review mode: standard / blind
- reviewer rights: advisory + escalation (default) / other per Decision-Rights Map
- decision log: `decision-log.md`
- Reporting Review status: pending / completed / skipped
- researcher-agent response status: pending / completed / not applicable

## Upstream Inputs

| Input | Status | Notes |
|---|---|---|
| Approved Plan Package |  |  |
| Modeling Package |  |  |
| exploratory demo phase summary, if used |  |  |
| Modeling Gate decision |  |  |
| run manifest |  |  |
| run log |  |  |
| run summary |  |  |

## Reader-Facing Deliverables

| Deliverable | Path | Audience | Status | Notes |
|---|---|---|---|---|
|  |  | user / reviewer / collaborator / public | draft / ready / limited / release-ready |  |

## Evidence Inventory

| Evidence object | Type | Path or source | Provenance status | Validation status | Notes |
|---|---|---|---|---|---|
|  | raw input / processed data / extracted text / table / figure / code / log / prompt / model output / other |  | traceable / partial / missing | validated / preliminary / failed / not checked |  |

## Data and Source Provenance Summary

| Item | Raw host | Official source or owner | Documentation source | Citation/source reference | Version or access date | License/access status |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

## Method and Execution Summary

- approved modeling contract:
- actual execution summary:
- scripts/notebooks used:
- environment path or dependency file:
- important tool/model/API versions:
- major repairs or deviations:
- unresolved execution issues:

## Key Findings

| Finding | Evidence/artifact | Claim-readiness | Limitation or caveat | Downstream use |
|---|---|---|---|---|
|  |  | supported / preliminary / uncertain / unsupported / not evaluated |  | can use in Review / needs Modeling addendum / needs Planning addendum / user judgment needed |

## Synthesis Notes

Use only synthesis that is grounded in the evidence inventory.

| Synthesis type | Summary | Supporting artifacts | Confidence | Route |
|---|---|---|---|---|
| common finding |  |  | high / medium / low | Review / Modeling / Planning |
| complementary evidence |  |  | high / medium / low | Review / Modeling / Planning |
| apparent contradiction |  |  | high / medium / low | Review / Modeling / Planning |
| true conflict |  |  | high / medium / low | Review / Modeling / Planning / user |
| operational tension or tradeoff |  |  | high / medium / low | Review / Modeling / Planning / user |
| evidence gap or uncertainty |  |  | high / medium / low | Modeling / Planning / user |

## Figures, Tables, and Visuals

| Visual/table | Path | Source | Main message | Validation status | Caveat |
|---|---|---|---|---|---|
|  |  | Modeling / Reporting packaging / external source |  | validated / preliminary / not checked |  |

## Output Architecture and Mode-Specific Checks

Use only the rows relevant to the selected output mode.

| Output mode | Required check | Status | Notes |
|---|---|---|---|
| manuscript or paper | argument architecture and section plan |  |  |
| manuscript or paper | citation-grounded claim map |  |  |
| manuscript or paper | citation integrity and source-support check |  |  |
| manuscript or paper | venue or format fit |  |  |
| manuscript or paper | abstract, conclusion, limitation, disclosure, and availability checks |  |  |
| slide deck | audience, occasion, and narrative order |  |  |
| slide deck | figure readability and caveat placement |  |  |
| web page or interactive report | provenance/caveat placement and interaction checks |  |  |
| web page or interactive report | public-sharing and accessibility/readability risk |  |  |
| dashboard or table package | metric/chart definitions, filters, and interpretation risks |  |  |
| software package or tool release | README, install/run instructions, examples, license/dependencies |  |  |
| software package or tool release | smoke test, validation status, and support boundary |  |  |

## Claim-Evidence and Source-Support Map

| Claim or deliverable message | Evidence type | Source/artifact | Support status | Output location | Notes |
|---|---|---|---|---|---|
|  | citation / model artifact / figure / table / user knowledge / limitation |  | supported / weak / unsupported / unresolved |  |  |

## Addendum Requests

### Modeling Addendum Requests

| Request | Why needed | Artifact requested | Within approved contract? | Blocks Review? |
|---|---|---|---|---|
|  |  |  | yes / no / uncertain | yes / no |

### Planning Addendum Requests

| Request | Why needed | Decision needed | Blocks Review? |
|---|---|---|---|
|  |  |  | yes / no |

## Limitations and Uncertainties

| Limitation | Affected finding or claim | Severity | Disclosure needed |
|---|---|---|---|
|  |  | blocker / major / minor / accepted limitation |  |

## Review Readiness

| Check | Status | Notes |
|---|---|---|
| evidence package is understandable without reconstructing scattered files |  |  |
| source/data provenance is traceable |  |  |
| validated findings are separated from preliminary observations |  |  |
| uncertainties and failures are visible |  |  |
| missing evidence is routed |  |  |
| deliverables are linked and current |  |  |
| output-mode checks are complete |  |  |
| reviewer-agent findings are resolved or routed |  |  |

## Reporting Reviewer Critique

Use `docs/reviewer-agents/reporting-reviewer-agent.md` before the Reporting Gate when a separate reviewer agent is available and approved.

| Finding ID | Severity | Concern | Evidence or reasoning | Route | Blocks gate? | Recommended action |
|---|---|---|---|---|---|---|
| RR-1 | blocker / major / minor / suggestion / accepted limitation |  |  | Planning / Modeling / Reporting / Reviewing / Terminate / user decision | yes / no |  |

If Reporting Review was skipped, record why:

- skipped reason:
- risk accepted:
- revisit trigger:

## Researcher-Agent Response to Reporting Review

Blocker and major findings that are deferred or rejected are escalated: add
them to the decision log's Open Escalations and quote them at the gate. Only the
user can uphold the response.

| Finding ID | Response status | Change made or planned | Blocks gate? | Escalated to user? | User ruling | Notes |
|---|---|---|---|---|---|---|
| RR-1 | accepted and fixed / accepted but deferred / rejected with reason / needs user decision |  | yes / no | yes / no | upheld / overturned / pending / n.a. |  |

## Reporting Gate Decision

- decision: approve for Review / approve as limited demo / revise Reporting / request Modeling addendum / request Planning addendum / terminate or archive
- decision-log ID:
- approval quality: substantive / nominal (what was missing) / synthetic
- escalated findings ruled on: finding ID -> upheld / overturned
- open objections carried forward:
- user notes:
- required changes before Review:
- approved limitations:
- next stage:

## Handoff to Review

- main evidence to inspect:
- strongest supported findings:
- weakest or most uncertain findings:
- known provenance concerns:
- known validation concerns:
- addendum requests:
- user decisions needed:
