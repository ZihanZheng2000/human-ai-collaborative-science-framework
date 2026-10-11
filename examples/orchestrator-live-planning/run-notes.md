# Run Notes: Live Orchestrated Planning Stage

## Run Identity

- Run: `live1`, 2026-10-10
- Mode: framework trial of the orchestrator with real agents, Planning stage only (`run --until planning`)
- Agents: researcher = Claude Code (`claude -p`), reviewer = Claude Code (separate process), both `cli`
- Settings: step-by-step, use reviewer, **synthetic gates** (the orchestrator took each recommended option)
- Topic: "Using the public Palmer penguins dataset, check whether male and female penguins differ in body mass within each species. Descriptive and small."
- Config used: a copy of `workflow.config.json` with both roles set to `claude-code` and `gates: synthetic` (kept in the session scratchpad; this run predates the config snapshot fix below)

## What Happened

| Step | Result |
|---|---|
| researcher `work` ×6 | five Tier 1 checkpoints raised one at a time (question/claim level, data source + acquisition rule, exclusion rule, method/metrics, decision-rights map), each answered synthetically and fed back; sixth session wrote the review request and framing |
| reviewer (standard) | 9 findings, 2 major |
| researcher `triage` | fixed PR-3..PR-7, deferred PR-8, escalated PR-1 and PR-2 verbatim in the gate request |
| Planning Gate | taken synthetically (D-7); open escalations listed in the gate |

8 agent calls in total; no human input after `init`.

## Workflow Evaluation (Planning only)

| Measure | Value |
|---|---|
| Tier 1 / Tier 2 decisions logged by the orchestrator | 6 / 1 |
| approval quality | 7 synthetic |
| checkpoints with all substantive sections | 5 / 5 |
| reviewer findings / major | 9 / 2 |
| escalations raised / ruled | 2 / 0 (synthetic run) |
| escalations quoted verbatim at the gate | 2 / 2 |

## Findings About the Framework

| ID | Finding | Fix |
|---|---|---|
| L1 | PR-1: the run used a config outside the repository, but D-1 said "from workflow.config.json" and agents compared against the repository's config, which assigned different roles. A real orchestrator defect. | The orchestrator now snapshots the config it runs with into `.workflow/config.json`, cites the real source in D-1, tells agents to use the snapshot, and logs a `reconfiguration` row whenever agents or roles change between runs. |
| L2 | PR-2: the researcher settled several Tier 1 choices (prior-work depth, skipped venue calibration and tool scan, output route) without checkpoints. The reviewer caught it. | The researcher prompt now lists skip/defer/lighten choices and the output route as Tier 1 explicitly, and allows grouping closely related minor choices in one checkpoint. |
| L3 | Step-by-step Planning cost six researcher sessions; each re-reads the shared state. | Expected trade-off; `auto-until-needed` batches checkpoints into fewer sessions. Worth measuring in a comparison run. |
