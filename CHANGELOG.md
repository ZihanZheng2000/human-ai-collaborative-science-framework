# Changelog

## v0.3.0-dev

Renamed to the **Human–AI Collaborative Science Framework** (repository
`human-ai-collaborative-science-framework`) to match the companion paper.

Added:

- `orchestrator/`: runs the four stages automatically with any configured
  agents and stops only at human nodes (setup, Tier 1 checkpoints, stage gates,
  human tasks, stuck states). Terminal answers or a file inbox
  (`inbox/pending/`) that can be answered later. The orchestrator records
  every human decision in the decision log and computes approval quality.
  Blind review is enforced by withholding the framing file (CLI) or by a
  two-call review (API). Standard library only.
- Agent adapters: `cli` (any command-line agent), `anthropic` (Claude via the
  Anthropic SDK; reviewer), `openai_compatible` (any chat-completions endpoint;
  reviewer), `human` (a person in either role). Per-stage reviewer assignment.
- `workflow.config.json` / `workflow.config.example.json`; `docs/orchestration.md`;
  `templates/checkpoint-request.md`, `templates/gate-request.md`; `tests/`.
- `GEMINI.md`; `CLAUDE.md`, `AGENTS.md`, and `GEMINI.md` are identical,
  generated from `docs/agent-roles/`.

- Projects can live anywhere; agents run inside the project folder and read
  the framework through `{framework_dir}` (Claude Code `--add-dir`). `init`
  writes pointer instruction files in external projects.
- `review` command: run only the reviewer pass (manual runs).
- Session policy (`workflow.sessions`): by default the researcher keeps one
  conversation for the whole project and the reviewer gets a new conversation
  per stage; a blind independent pass is always new. `fresh_researcher_at`,
  the `new-session` command, and a gate option start new conversations on
  request. Tested with Claude Code `--output-format json` / `--resume`.
- Synthetic gates no longer auto-answer stuck states.
- Reviewer guard: the run stops if a CLI reviewer changes any file besides its
  critique.
- Default configuration: Claude Code researcher, Codex CLI reviewer.

Changed:

- Roles are no longer tied to products: Config A/B and `WORKFLOW-CONFIG.md`
  are replaced by `roles` in `workflow.config.json`.

Removed:

- `WORKFLOW-CONFIG.md`, `scripts/run_reviewer_claude.ps1`,
  `scripts/run_reviewer_codex.ps1` (replaced by the orchestrator).

## v0.2.0-dev

Framework revision aligning the workflow kit with the three-layer design
(organization, coordination, evaluation). The four stages are unchanged.

Added:

- `docs/decision-rights.md`: activity / actor / authority separation, action
  types, decision tiers (Tier 0 routine, Tier 1 decision checkpoint, Tier 2
  stage gate), default Decision-Rights Map, reviewer rights, substantive vs
  nominal approval
- `docs/coordination.md`: shared research state, scientific accountability loop,
  automatic escalation of deferred or rejected blocker/major findings, blind
  review mode, informal early-look reviews, substantive gate presentation,
  adaptive reconfiguration triggers and procedure
- `docs/workflow-evaluation.md`: four evaluation dimensions, design comparisons,
  validation types
- `templates/decision-log.md` and a README status block for each project
- Decision-Rights Map section in the Planning Package; Locked Analysis Choices
  in the Modeling Package; accountability audit and reconfiguration
  recommendations in the Review Package
- Workflow Evaluation section in `templates/example-run-notes.md`
- `docs/agent-roles/` as the single source for researcher and reviewer
  instructions, and `scripts/build_agent_instructions.py` to generate
  `CLAUDE.md` and `AGENTS.md`

Changed:

- `CLAUDE.md` researcher role now includes Pre-Planning Session Setup (previously
  only in `AGENTS.md`)
- one findings table format for all reviewer stages (`PR-`, `MR-`, `RR-`, `RVR-`
  prefixes; `Blocks gate?` column; `user decision` route)
- review requests declare review mode and reviewer assignment; the request is
  authoritative and overrides must cite a user decision
- run-scoped paths unified as `<run_dir>`; domain materials moved to
  `research/<name>/artifacts/input/domain-materials/` for real projects
- "Model Gate" renamed "Modeling Gate"; Planning template renamed "Planning
  Package" until approved
- gate language no longer hard-codes Codex as the researcher
- reviewer wrapper scripts follow the new assignment and blind-review rules

Fixed after the v0.2 smoke test (`examples/smoke-test-v02-co2-growth/`):

- per-stage review file names (`review-request-<stage>.md`,
  `reviewer-critique-<stage>.md`); stages no longer overwrite each other
- researcher framing moved to a separate `review-framing-<stage>.md` so blind
  review is enforceable
- reviewer role states the documented reconfiguration thresholds; a researcher
  self-check is a mitigation, not a reconfiguration
- seeded-fault protocol in `docs/workflow-evaluation.md`
- Review Package recommendation must name a concrete option and permitted use;
  run notes filled before the Reviewing review request
- researcher runs a sentence-by-sentence claim check before each review request,
  and the Reporting reviewer has a required claim audit of every deliverable
  sentence (user ruling D-19 in the smoke test)
- `.gitignore` anchored `/notes/` and `/research/` so example `notes/` folders
  are tracked

Removed:

- stale references to `docs/paper.md`, `examples/`, and `notes/`

## v0.1.0-dev

Initial public-preparation version.

Added:

- Four-stage workflow: Planning, Modeling, Reporting, Reviewing
- Stage package templates
- Smoke-Test Mode and compact smoke-test package
- Skill strategy for external-tool reuse and internal workflow-native skills
- Workflow-native skills:
  - venue calibration
  - research-skill-card distillation
  - model-contract running
  - figure/table narrative design
  - claim-evidence mapping
  - route-aware review
  - gate management
- Example organization rules for future smoke tests and case studies
- GitHub release metadata: README, LICENSE, CONTRIBUTING, CITATION, `.gitignore`
