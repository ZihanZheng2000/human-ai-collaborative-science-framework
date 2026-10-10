# Stage Handoffs

This document summarizes how the workflow stages connect. Each stage outputs one compact package. Downstream stages should read the approved package rather than reconstructing context from scattered notes.

## Framework Layers

The four stages say *what work* happens and in what order. Three cross-cutting
documents say how the human–AI research system around those stages is
organized, kept coherent, and evaluated:

| Layer | Document | What it governs |
|---|---|---|
| Organization | [decision-rights.md](decision-rights.md) | who performs each activity, who authorizes each decision class, decision tiers, reviewer rights, substantive vs nominal approval |
| Coordination | [coordination.md](coordination.md) | shared research state (README status + decision log + packages), the accountability loop, escalation, blind review, gate presentation, adaptive reconfiguration |
| Evaluation | [workflow-evaluation.md](workflow-evaluation.md) | how each run measures outcome, collaboration process, accountability, and human effort |

[orchestration.md](orchestration.md) describes the orchestrator, which runs the
stages with any configured agents and stops only at human nodes.

Stage gates are the Tier 2 decisions in this design. Tier 1 decision checkpoints
happen inside stages; Tier 0 routine choices are made by the researcher.

## Pre-Planning Session Setup

Before the workflow enters Planning, a short setup gate runs. In orchestrated
runs the orchestrator asks these questions at `init`; in manual runs the
researcher agent asks them. This setup gate is not a research stage and does not produce a
Planning package. It determines how the rest of the workflow should be led.

The setup gate has two decisions:

1. Confirm the active role assignment from `roles` in `workflow.config.json`.
2. Ask the user to choose the workflow mode and reviewer strategy.

Workflow mode choices:

| Mode | Meaning | Default use |
|---|---|---|
| Auto-until-needed | The researcher agent proceeds through the workflow and stops only at gates, missing information, route-changing decisions, or genuine uncertainty/problems. | smoke tests, mature ideas, speed-first internal work |
| Step-by-step discussion | The researcher agent discusses each meaningful step or decision with the user before expanding the package or moving on. | broad, uncertain, high-stakes, or collaborative projects |

Reviewer strategy choices:

| Option | Meaning |
|---|---|
| Use reviewer | Run the maker-checker loop before the user gate: review request, reviewer critique, researcher response, then gate. |
| Skip reviewer | Record the skipped-review reason, accepted risk, and revisit trigger in the package before the user gate. |

Recommended default for real research: **Step-by-step discussion** plus
**Use reviewer**. Recommended default for smoke tests: **Auto-until-needed** plus
synthetic gates and either skipped reviewer with recorded risk or a clearly
labeled synthetic reviewer pass.

For a real project, record the setup choices as the first entry (`D-1`) in
`research/<research-name>/decision-log.md`. Changing either choice later is a
reconfiguration and gets its own entry.

After the setup gate, the researcher begins Planning orientation using the
selected mode.

For real research projects, Planning orientation is followed by at least a
focused prior-work and novelty calibration before the Planning Package is
treated as gate-ready. The calibration may be light, but it should check whether
the idea has already been studied, what adjacent work did, and what research
value remains. It may be skipped or deferred only when the user explicitly
chooses that route or the project is clearly a smoke test/demo, and the package
must record the skipped/deferred reason, accepted risk, and revisit trigger.

## Linear Path

| Stage | Primary input | Primary output | Gate |
|---|---|---|---|
| Planning | user need, focused prior-work/novelty calibration or explicit skip/defer rationale, idea maturity, feasibility checks, research-skill cards or skill candidates, Planning Reviewer critique, researcher-agent response/fix | Approved Planning Package | Planning Gate after reviewer response |
| Modeling / Execution | Approved Planning Package | Modeling Package, often after an exploratory demo phase inside Modeling | Modeling Gate |
| Reporting / Output Packaging | Approved Planning Package + Modeling Package | Reporting Package and reader-facing deliverables | Reporting Gate |
| Reviewing | Approved Planning Package + Modeling Package + Reporting Package | Review Package | Reviewing Gate |

## Default Route

The default route is:

1. Planning
2. Modeling / Execution, usually starting with a small exploratory demo when the workflow is new or uncertain
3. Reporting / Output Packaging
4. Reviewing

Reporting produces the reader-facing outputs. A paper, report, slide deck,
dashboard, web page, software package, technical appendix, or review packet is
a Reporting output mode, not a separate stage. Reviewing happens after
Reporting because reviewer agents need a concrete package and deliverables to
inspect.

## Researcher-Led Step Protocol

The researcher agent is responsible for driving the workflow. The user should
not need to remind the agent what the next stage action is.

At the start of every stage, the researcher agent should state:

1. current stage
2. package path being created or revised
3. immediate next action
4. expected stop condition
5. user decision needed now, if any

At the start of Planning, the researcher agent should use a confirmation-led
orientation:

1. "I understand you want to do X."
2. "I propose to run this workflow as Y."
3. "The active stage is Planning, and I will create or revise Z package."
4. "If that is right, I will proceed; if not, correct the part that is wrong."

This orientation is not a questionnaire. The researcher may ask a concise
question only when the answer would change the route, such as the research
question, final output, gate mode, domain/source choice, implementation
location, or claim level. Once the intent is clear enough to plan, the
researcher should start the Planning package rather than keep asking for
preferences.

The researcher agent should proceed within the current stage until a real stop
condition is reached: missing information, missing files or permissions,
reviewer handoff, user gate, or an explicit user pause. When it stops, it should
name the next concrete action or decision rather than ending with an open-ended
request.

For real projects, Planning begins with orientation and proposed user-need confirmation,
not with filling every package. Modeling, Reporting, and Reviewing remain
inactive until the upstream gate approves them. Existing downstream templates in
a scaffold are placeholders only and should stay marked as not started.

User confirmation of the topic or rough research direction is not Planning Gate
approval. Do not start Modeling after the user merely agrees that the proposed
research idea is interesting or worth exploring. First complete or explicitly
defer the prior-work/novelty calibration, write the Planning Package, run or
record the reviewer pass, and ask for the Planning Gate decision.

User-need confirmation does not mean waiting for the user to design the
workflow. The researcher owns the next proposed action. It should make a
reasonable proposal, present likely answers for decision-shaping fields, surface
assumptions that would materially affect the project, and then move once the
user confirms or corrects the proposal.

## Stage Maker-Checker Rule

Each stage uses the same internal pattern before its user gate:

```text
Researcher agent produces or revises the stage package
-> Reviewer agent critiques the package and deliverables
-> Researcher agent responds, fixes, defers, rejects with reason, or escalates
-> User gate
```

Reviewer agents critique and may escalate; they do not approve gates and do not
modify files unless the user explicitly authorizes an edit. Reviewer findings
should be recorded in the stage package or linked as an agent artifact. The
researcher-agent response must classify each finding as accepted and fixed,
accepted but deferred, rejected with reason, or needing user decision.

A `blocker` or `major` finding that the researcher defers or rejects is
escalated: it is added to the decision log's Open Escalations and shown to the
user at the gate in the reviewer's original wording. Only the user can uphold
the researcher's response. See [decision-rights.md](decision-rights.md#reviewer-rights).

The Reviewing stage uses **blind** review mode by default; other stages use
**standard** mode unless the user or the Decision-Rights Map says otherwise.
See [coordination.md](coordination.md#reviewer-information-modes).

## Decision Checkpoints Inside Stages

Stage gates are not the only place the user decides. Consequential choices made
inside a stage are **Tier 1 decision checkpoints**: the researcher proposes
(with evidence, alternatives, and known objections), the user decides, and the
decision is appended to `decision-log.md`. Typical checkpoints:

- Planning: research question and claim level, literature-scan depth or skip,
  source strategy, labels/event definitions, method family, output route, the
  Decision-Rights Map itself
- Modeling: acquired data and exclusions, model search space and metrics
  (locked before results are seen), interpretation of results, scale-up from
  demo to full study
- Reporting: claim level in the deliverable, inclusion of preliminary findings
- Any stage: skipping a planned check, changing workflow mode or reviewer
  strategy, reconfiguration

Checkpoints are lighter than gates: no reviewer pass is required. They still
need the substantive presentation items in
[decision-rights.md](decision-rights.md#substantive-versus-nominal-approval).
Stage packages cite the decision IDs rather than restating the history.

If a reviewer-agent pass is skipped for any stage, the stage package must record
the reason, accepted risk, and revisit trigger before the user gate is presented
as ready.

## Backtracking Rules

Backtracking is normal. It is not a system failure.

| Trigger | Typical route |
|---|---|
| research question, idea maturity, or scope is wrong | Reviewing/Reporting/Modeling -> Planning |
| prior-work or novelty basis is too weak for the target claim | Reviewing/Reporting -> Planning or targeted literature addendum |
| data cannot support the approved method | Modeling/Reviewing -> Planning |
| exploratory demo does not pass basic feasibility or value checks | Modeling -> Planning or revise Modeling demo |
| code, robustness, extraction, validation, or empirical figure is missing | Reporting/Reviewing -> Modeling |
| evidence package is hard to inspect or lacks provenance | Reviewing -> Reporting |
| target venue or output route does not fit | Reviewing/Reporting -> Planning or Reporting |
| citation, source-support, or deliverable gap is local | Reviewing -> Reporting or targeted literature addendum |
| manuscript, slide, web, dashboard, or software-package argument is weak or report-like | Reviewing -> Reporting |
| project is infeasible, noncompliant, or misleading | Any stage -> Terminate |

Backtracking changes the inquiry. When the problem is instead *who* is doing or
deciding something (repeated domain corrections, repeated escalations of the
same decision class, a changed research object), propose a **reconfiguration**
of the Decision-Rights Map. See
[coordination.md](coordination.md#adaptive-reconfiguration).

## Package Discipline

The workflow should avoid creating many unreviewed side artifacts. Extra files can exist for code, data, figures, validation outputs, working notes, and drafts, but each stage should summarize them in its package.

For real research projects, create a dedicated project folder under
`research/<research-name>/` and use the layout in
[research-organization.md](research-organization.md). New project packages
belong in `research/<research-name>/packages/`; detailed notes belong in
`research/<research-name>/notes/`; run-scoped review requests, critiques,
manifests, and logs belong in `research/<research-name>/artifacts/<run_id>/`.

Each real project also keeps `research/<research-name>/decision-log.md`
(template: `templates/decision-log.md`) and a status block in its `README.md`.
Together with the stage packages, these are the project's shared research state.

For discussion-first projects, do not force all work into the stage package at
once. Use supporting notes or matrices for detailed exploration, and keep the
stage package as the compact checkpoint that records accepted decisions, open
questions, evidence status, and links to details. The researcher should
consolidate only after the relevant sub-step has been discussed or accepted by
the user.

Only the active stage package should be substantively edited. Downstream package
templates may be created for scaffolding only when useful, but they must not be
filled, interpreted as progress, or presented as active stage outputs before the
workflow reaches those stages.

Required packages:

- `templates/plan-package.md`
- `templates/model-package.md`
- `templates/reporting-package.md`
- `templates/review-package.md`

Supporting templates:

- `templates/decision-log.md`
- `templates/research-skill-card.md`
- `templates/smoke-test-package.md`
- `templates/example-run-notes.md`

Worked examples should not keep every file in the example root. Use the layout in [example-organization.md](example-organization.md):

- `packages/` for approved Planning, Modeling, Reporting, and Reviewing handoffs
- `deliverables/` for final or near-final reader-facing outputs
- `notes/` for literature, feasibility, method, and other working notes
- `artifacts/` for input, data, code, logs, tables, figures, validation outputs, and run-specific agent artifacts
- `archive/` for superseded files kept only for traceability

The example root should usually contain only `README.md`, `run-notes.md`, and the main folders above. This keeps the approved package flow separate from generated evidence and exploratory notes.

## Run Logs and Agent Artifacts

`<run_dir>` is `research/<research-name>/artifacts/<run_id>/` for real projects
and `artifacts/<run_id>/` for smoke tests or legacy runs.

For substantial runs, especially exploratory demos that may later scale up, maintain:

- `<run_dir>/run_manifest.json` for version, scope, inputs, outputs, tools, and status
- `<run_dir>/run_log.md` for chronological execution events, Tier 0 decisions, failures, repairs, and gate notes
- `<run_dir>/run_summary.md` for the human-readable summary of what the run proved

If agent-specific skills, prompts, critiques, or coordination notes are created during a run, store them under:

- `<run_dir>/agent/`

Promote only reusable, evidence-backed agent methods into `skills/`. Keep run-specific agent material in artifacts.

## Human Gates

Each gate should answer three questions:

1. Is the stage output scientifically acceptable for its stated claim level?
2. What must be changed before downstream use?
3. Should the workflow proceed, revise locally, backtrack, scale up, finalize, release, archive, or terminate?

A gate approval counts as substantive human oversight only when the user was
shown the proposal, the evidence paths, alternatives, open objections (including
escalated reviewer findings verbatim), consequences, and the option to ask for
more checks or override. Otherwise the decision log records the approval as
**nominal** with what was missing.

For autonomous framework tests, gate decisions must be labeled as **synthetic gates** rather than real user approvals. Synthetic gates are acceptable for smoke tests and QA runs, but they do not replace user, domain-owner, or expert approval in a real research project.

When the runtime provides a structured user-choice tool such as
`request_user_input`, the researcher agent should present each real user gate
with clickable choices instead of relying only on free-text replies. The prompt
should still summarize the package, reviewer findings, researcher response, and
consequences of approval before asking for the choice.

Use 2-3 mutually exclusive gate choices. Put the recommended choice first and
label it as recommended only when the evidence supports that recommendation.
Always leave room for the user's free-form correction or condition. If the
structured-choice tool is unavailable, present the same choices as plain text.

Default gate choices:

| Gate | Structured choices |
|---|---|
| Planning Gate | Approve for Modeling / Revise Planning / Backtrack or terminate |
| Modeling Gate | Approve for Reporting / Revise Modeling / Backtrack to Planning |
| Reporting Gate | Approve for Reviewing / Revise Reporting / Request Modeling or Planning addendum |
| Reviewing Gate | Finalize or archive / Revise routed issues / Backtrack to earlier stage |

## Approval Semantics

Gate approval is an action, not only a status label. When the user approves a stage, the default behavior is to immediately begin the next downstream stage in the same turn if there is enough context and no explicit pause request.

Default transitions:

| User approval | Default next action |
|---|---|
| Planning Gate approved | Start Modeling by locking the modeling contract and, when appropriate, running a small exploratory demo first; this requires recorded Planning Reviewer critique or a recorded skip rationale plus researcher-agent response |
| Modeling Gate approved | Start Reporting / Output Packaging by ingesting the approved Planning and Modeling packages |
| Reporting Gate approved | Start Reviewing by stress-testing the evidence package and writing a Review Package |
| Reviewing Gate approved | Finalize, submit, share, archive, run a routed Modeling/Reporting addendum cycle, backtrack, or terminate according to the selected route |

The workflow should pause after approval only when:

- the user explicitly says to stop, pause, or wait
- the next stage needs information that cannot be inferred safely
- required data, tools, permissions, or files are unavailable
- the approval is conditional and the condition must be resolved first

If a stage is approved but the next stage cannot begin, the package should state why and list the smallest next action.

## Gate Language

At each gate, the researcher agent guides the user with the substantive gate
presentation from [coordination.md](coordination.md#substantive-gate-presentation):

- decision needed and the recommended choice
- what was completed and the package path
- three to five evidence paths worth opening
- open objections: escalated reviewer findings in the reviewer's wording,
  deferred items and their triggers, and whether the reviewer pass was skipped
- alternative routes and what each would cause
- what will happen if the user approves, and how it could be reversed
- structured clickable choices when available, including "ask for more checks",
  with a free-form path for conditions or corrections

Use concrete language such as:

```text
This completes the Modeling package (packages/modeling-package.md). Evidence to
open: artifacts/tables/main_results.csv, artifacts/figures/fig2.png,
artifacts/validation/rerun_check.md. The reviewer raised MR-3 (major): "the
exclusion rule was tightened after the first results were visible." I deferred
it because the change is logged as D-14; you need to uphold or overturn that.
If you approve the Modeling Gate, I will move to Reporting and carry the
exclusion change as a disclosed limitation. Alternatives: revise Modeling to
rerun with the original rule, or return to Planning.
```
