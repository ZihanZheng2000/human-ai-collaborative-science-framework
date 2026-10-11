# Review Package

## Review Identity

- project title:
- review date:
- review status: initial / post-revision / final
- review scope: evidence package / workflow demo / manuscript or paper / slide deck / web or dashboard / software package / submission package / other
- gate mode: real user gates / synthetic gates / mixed
- recommendation: approve for finalization or release / approve limited package / revise Reporting / request Model addendum / backtrack to Plan / terminate
- permitted use while escalations are open (required for limited or archive): may / may not
- Reviewing Researcher: researcher agent name or runtime
- Reviewing Reviewer: reviewer agent name or runtime / skipped
- reviewer file: `docs/reviewer-agents/reviewing-reviewer-agent.md`
- reviewer mode: critique-only / edits explicitly authorized by user / skipped
- review mode: blind (default for Reviewing) / standard
- reviewer rights: advisory + escalation (default) / other per Decision-Rights Map
- decision log: `decision-log.md`
- Reviewing Review status: pending / completed / skipped
- researcher-agent response status: pending / completed / not applicable

## Inputs Reviewed

| Input | Status | Notes |
|---|---|---|
| Approved Planning Package |  |  |
| Modeling Package |  |  |
| Reporting Package |  |  |
| Run manifest/log/summary |  |  |
| Data/source artifacts |  |  |
| Reader-facing deliverables |  |  |

## Upstream Completeness Audit

| Audit item | Pass/Concern/Fail | Evidence checked | Route if concern |
|---|---|---|---|
| gate mode and approval status are explicit |  |  | Review |
| Planning records idea maturity and planning depth |  |  | Plan |
| prior-work/novelty status matches claim level |  |  | Plan |
| Modeling mode is recorded: demo-first/full-scale/addendum |  |  | Model |
| exploratory demo phase is summarized when used before scale-up |  |  | Model / Review |
| run manifest, run log, and run summary exist when needed |  |  | Model |
| source/data provenance is traceable |  |  | Plan / Model |
| usable evidence is distinguished from candidate material |  |  | Model |
| Reporting separates supported/preliminary/uncertain/unsupported findings |  |  | Reporting |
| limitations and failures remain visible |  |  | Reporting |
| every Tier 1/2 decision in the decision log has proposer, evidence, objections, and authorizer (outcome may be pass / concern / synthetic) |  |  | Review / user decision |
| nominal or synthetic approvals of consequential decisions are identified and counted |  |  | user decision |
| seeded faults, if any, are disclosed in the decision log |  |  | Review |
| run-notes.md Workflow Evaluation is filled |  |  | Review |
| open escalations and deferred items are listed, none silently closed |  |  | user decision |
| locked analysis choices were not changed after results without a logged decision |  |  | Model |

## Internal Self Review

| Finding | Severity | Route | Fix made? | Artifact changed | Remaining risk |
|---|---|---|---|---|---|
|  | blocker / major / minor / suggestion / accepted limitation | Plan / Model / Reporting / Review / Terminate | yes / no / deferred |  |  |

## Reviewer-Agent Critique

- reviewer used? yes / no
- reviewer/tool:
- review mode: critique only / allowed to edit by explicit user request
- packet path or prompt path:
- output path:

Independent (blind) findings and follow-up findings are kept separate in the
critique file; note which block each finding came from.

| Reviewer finding | Block | Severity | Accepted? | Researcher-agent response | Escalated to user? | User ruling | Route | Action |
|---|---|---|---|---|---|---|---|---|
|  | independent / follow-up | blocker / major / minor / suggestion / accepted limitation | yes / no / partial / deferred |  | yes / no | upheld / overturned / pending / n.a. | Plan / Model / Reporting / Review / Terminate / user decision |  |

## Review Criteria

| Criterion | Pass/Concern/Fail | Notes |
|---|---|---|
| research question and scope discipline |  |  |
| planning-depth decision fits the project |  |  |
| prior-work/novelty basis fits the intended claim |  |  |
| question-data-method-claim fit |  |  |
| source/data provenance |  |  |
| acquisition and validation success |  |  |
| reproducibility and run logging |  |  |
| claim strength and evidence tier alignment |  |  |
| synthesis quality and uncertainty handling |  |  |
| reporting readability and traceability |  |  |
| ethics/licensing/disclosure |  |  |
| accountability and decision traceability |  |  |
| readiness for next route |  |  |

## Findings Table

| ID | Finding | Source | Severity | Route | Required action | Completion criterion | Blocks approval? | Status |
|---|---|---|---|---|---|---|---|---|
| R1 |  | internal / reviewer / user / tool | blocker / major / minor / suggestion / accepted limitation | Plan / Model / Reporting / Review / Terminate |  |  | yes / no | open |

## Response-to-Review Summary

| Finding ID | Decision | Action taken or planned | Artifact changed | Remaining risk |
|---|---|---|---|---|
|  | accepted / rejected / deferred / accepted limitation |  |  |  |

## Readiness Decision

| Possible route | Ready? | Reason |
|---|---|---|
| another Modeling iteration | yes / no / maybe |  |
| Reporting revision | yes / no / maybe |  |
| finalization or release | yes / no / maybe |  |
| limited internal sharing | yes / no / maybe |  |
| external expert review | yes / no / maybe |  |
| public sharing/submission | yes / no / maybe |  |
| archive or terminate | yes / no / maybe |  |

## Reconfiguration Recommendations

| Signal | Decision class affected | Recommended change | Decision ID if adopted |
|---|---|---|---|
|  |  |  |  |

## Accepted Limitations

| Limitation | Why accepted | Where disclosed |
|---|---|---|
|  |  |  |

## Review Gate Decision

- decision: approve for finalization or release / approve limited package / revise Reporting / request Model addendum / backtrack to Plan / run another reviewer-agent critique / accept limitations and finalize / terminate
- decision-log ID:
- approval quality: substantive / nominal (what was missing) / synthetic
- escalated findings ruled on: finding ID -> upheld / overturned
- open objections carried forward:
- workflow evaluation recorded in run-notes.md: yes / no
- user notes:
- blocker issues remaining:
- major issues remaining:
- reviewer findings unresolved:
- upstream package gaps remaining:
- evidence-tier or claim-strength concerns:
- next stage:

## Handoff

- if revising Reporting:
- if returning to Model:
- if backtracking to Plan:
- if ready for limited sharing/finalization:
