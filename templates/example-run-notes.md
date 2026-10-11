# Example Run Notes

Use this file as `research/<research-name>/run-notes.md` (real projects) or `examples/<run-name>/run-notes.md` (examples and smoke tests) for lessons learned during one workflow run. Run notes are provisional, but they should stay attached to the project that produced them.

The Workflow Evaluation section applies `docs/workflow-evaluation.md`. Fill it at the Reviewing Gate, or when the run stops, using the decision log and stage packages.

## Run Identity

- Run name:
- Date:
- Mode: real project / smoke test
- Gate mode: real user gates / synthetic gates / mixed
- Topic or task:
- Stage coverage: Plan / Model / Reporting / Review

## Workflow Configuration

- workflow mode: auto-until-needed / step-by-step discussion (changes: D-<n>)
- reviewer strategy: use reviewer / skip reviewer (changes: D-<n>)
- review modes used: standard / blind
- researcher agent / reviewer agent:
- domain expert involved: none / who, for which decision classes
- reconfigurations during the run: none / D-<n>: what changed and why

## Workflow Evaluation

### Scientific outcome

| Measure | Value | Notes |
|---|---|---|
| substantive claims: supported / limited / unsupported / removed |  |  |
| reproducibility rerun | pass / fail / not run |  |
| validation type(s) used | known outcome / seeded error / reproducibility / expert adjudication / delayed / none |  |

### Collaboration process

| Measure | Value | Notes |
|---|---|---|
| reviewer findings total (by severity) |  |  |
| trajectory-changing reviewer findings (changed the route or a Tier 1 decision) |  | list IDs |
| trajectory-changing user corrections |  | list decision IDs |
| problems caught at their own stage vs found later |  |  |
| duplicated or lost work |  |  |

### Reliability and accountability

| Measure | Value | Notes |
|---|---|---|
| Tier 1 / Tier 2 decisions logged |  |  |
| decisions with proposer, evidence, objections, and authorizer all recorded |  | share |
| approvals: substantive / nominal / synthetic |  |  |
| escalations raised / upheld / overturned |  |  |
| decisions reopened or superseded |  |  |
| reviewer-triage closure rate |  | closed findings / total |

### Human effort

| Measure | Value | Notes |
|---|---|---|
| checkpoints and gates presented |  |  |
| user domain corrections (hidden repair) |  |  |
| re-runs or rewrites requested by the user |  |  |
| approximate user time at gates |  |  |
| where user effort went | mostly judgment / mostly routine verification / mixed |  |

### Reading the numbers

- Many checkpoints with few trajectory changes: tiers may be set too low.
- Repeated domain corrections in one area: consider reconfiguration.
- Many nominal approvals: gate presentation is not giving the user enough to judge.

## Useful Observations

Record things that helped this run work better.

- Observation:
- Stage:
- Why it helped:
- Evidence or example from this run:
- Possible permanent home: docs / templates / skills / examples / none

## Friction or Failures

Record anything that slowed the run, caused confusion, produced weak output, or required manual repair.

- Issue:
- Stage:
- What happened:
- Root cause, if known:
- Fix used during this run:
- Should this become a formal rule? yes / no / unsure

## Prompt or Instruction Lessons

Record prompt wording, instruction changes, or agent-control ideas that improved this run.

- Lesson:
- Before:
- After:
- Why it matters:
- Candidate update target:

## Data, Tool, or Environment Lessons

Record reusable lessons about data access, packages, APIs, environment setup, execution, or reproducibility.

- Lesson:
- Data/tool/environment involved:
- Reusable check or rule:
- Candidate update target:

## Stage Package Lessons

Record whether the package templates captured the right information.

- Package:
- Missing field or confusing field:
- Suggested change:
- Evidence from this run:

## Candidate Formal Updates

At the end of the run, move only stable lessons here.

| Candidate update | Target file | Reason | Evidence from this example | Decision |
|---|---|---|---|---|
|  |  |  |  | keep in example / update formal docs / reject |

## After-Action Review

- What should be repeated next time?
- What should be avoided next time?
- What needs another test before becoming a formal rule?
- What should be updated now?
