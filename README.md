# Human–AI Collaborative Science Framework

A workflow framework for research in which humans and AI agents work on the same
inquiry: research questions, literature, public or local data, and domain
expertise are turned into inspectable research packages through four gated
stages, with explicit decision rights and a shared research state.

It is for researchers who want AI agents to plan, execute, report, and review,
but do **not** want an opaque fully autonomous research agent. Agents run the
workflow automatically; people step in at defined decision points. Any agent can
be plugged in: command-line agents such as Claude Code, Codex, or Gemini CLI,
model APIs, or people.

## Relationship to the 9A Framework

This is **one reference implementation**, not the definition of the [9A Framework for Human–AI Collaborative Science](https://github.com/ZihanZheng2000/human-ai-collaborative-science). The companion theory distinguishes **Organization** (Activity, Actor, Authority), **Coordination** (Awareness, Accountability, Adaptability), and **Evaluation** (Achievement, Attribution, Assurance). This repository turns selected design implications into a configurable research workflow.

See **[Design Rationale](docs/design-rationale.md)** for the theory → requirement → mechanism → implementation → evaluation mapping, implementation boundaries, and open questions.

**Important distinctions:**

- **Activity is not Stage.** Scientific activities (hypothesizing, retrieving evidence, modeling, critiquing, reframing) may recur across stages. Planning → Modeling → Reporting → Reviewing is the current **default workflow template**, not a required scientific discovery sequence.
- **Human approval is not automatically collaboration.** This implementation is human-gated. Substantive human–AI collaboration additionally requires reciprocal engagement that materially shapes scientific reasoning, judgment, or research direction; gate counts alone cannot demonstrate it.
- **Approval is not validation.** Decision authority, epistemic expertise, and scientific evidence are distinct. A recorded authorization does not establish scientific correctness.
- **Execution is not efficacy.** Existing smoke tests and examples show particular workflows can run; they do not yet establish system-design gain or generalizable improvements in scientific research.

The four stages, decision tiers, gate frequency, reviewer setup, bundled skills, and on-disk file formats are **implementation choices**. They can be evaluated and revised without changing the nine theoretical concepts.

## What It Is

The framework is implemented through a four-stage workflow:

1. **Planning**: clarify the research purpose, run Domain Onboarding on user-supplied materials, scan prior work, check feasibility, calibrate venue/output, and produce one Approved Planning Package.
2. **Modeling**: acquire real usable data, run exploratory demos or full execution, validate outputs, produce figures/tables, and write one Modeling Package.
3. **Reporting**: package evidence, provenance, findings, uncertainties, and final deliverables such as reports, papers, slides, dashboards, web pages, software packages, or review packets.
4. **Reviewing**: run reviewer-agent critique, consolidate findings, and route issues back to the correct stage or to finalization.

Each stage ends with a gate. A real research project uses real user gates. A framework test can use synthetic gates, but they must be labeled as synthetic.

Each stage uses a maker-checker loop before the user gate: the researcher agent drafts the stage package, a separate reviewer agent critiques it, the researcher agent responds and fixes or routes the findings, and only then does the user approve, revise, or reject the gate.

## Three Layers Around the Four Stages

The four stages provide the **current workflow order**, while the three cross-cutting
layers describe how the human–AI research arrangement is organized,
coordinated, and evaluated. Scientific activities can span or recur across stages:

| Layer | Document | Core idea |
|---|---|---|
| **Organization** | [docs/decision-rights.md](docs/decision-rights.md) | Separate *who does the work* from *who may decide*. Each project has a Decision-Rights Map. Decisions are Tier 0 (routine: researcher decides), Tier 1 (decision checkpoint inside a stage: user decides), or Tier 2 (stage gate). The reviewer has advisory and escalation rights, never approval. |
| **Coordination** | [docs/coordination.md](docs/coordination.md) | A shared research state (README status block + `decision-log.md` + stage packages); an accountability loop (propose → critique → respond → authorize → act → record); automatic escalation of rejected or deferred reviewer blockers; blind review; substantive gate presentation; adaptive reconfiguration when the arrangement stops fitting. |
| **Evaluation** | [docs/workflow-evaluation.md](docs/workflow-evaluation.md) | Each run records scientific outcome, collaboration process, accountability, and human effort, so the workflow itself can be evaluated and compared across designs. |

A human approval counts as real oversight only when the user could inspect the
evidence and objections and could override. Approvals that lacked this are
recorded as *nominal*.

When the runtime supports structured choices, gate decisions are presented as
clickable options such as approve, revise, or backtrack. The same gate can still
accept a free-form condition or correction from the user.

Planning is not just a form to fill before execution. For real research, the
researcher agent should do a focused prior-work and novelty calibration before
the full Planning Package is treated as ready. That calibration can be light,
but it should ask whether the idea has already been studied, what adjacent work
did, what gap or value remains, and whether the project is worth framing as a
paper, demo, replication, tool, dataset, or internal report. It may be skipped
or deferred only when the user explicitly chooses that route, and the package
must record the accepted risk and revisit trigger.

Modeling starts only after the Planning Gate is approved. A user confirming the
topic, research interest, or rough direction is not the same as Planning Gate
approval.

The researcher agent is responsible for leading the workflow step by step. It
should state the current stage, active package, next concrete action, and any
needed user decision whenever work begins or pauses. Users provide domain
judgment and gate decisions; they should not have to remind the agent what the
next workflow step is.

## Why This Exists

Many AI research tools can retrieve literature, write text, generate code, or automate agent loops. This framework focuses on a narrower practical problem: helping non-CS domain researchers build a traceable academic research package without losing control of evidence, claims, methods, and responsibility.

The core design choices are:

- human-gated rather than fully autonomous
- evidence-grounded rather than memory-driven
- skill-guided rather than monolithic
- execution-aware rather than prose-only
- route-aware, so problems go back to Planning, Modeling, Reporting, Reviewing, or termination
- authority-explicit, so who proposed, who objected, and who authorized each consequential decision can be reconstructed
- domain-aware, so non-CS researchers can supply their own field materials at the start of Planning

## Agents: Anything Can Fill a Role

Roles (researcher, reviewer) are assigned in [workflow.config.json](workflow.config.json);
[workflow.config.example.json](workflow.config.example.json) shows every option.

| Agent kind | Examples | Can be researcher | Can be reviewer |
|---|---|---|---|
| `cli` | Claude Code, Codex, Gemini CLI, Aider, your own script | yes | yes |
| `anthropic` | Claude via the Anthropic API | not yet | yes |
| `openai_compatible` | OpenAI API, hosted or local OpenAI-compatible servers | not yet | yes |
| `human` | you, a collaborator, a domain expert | yes | yes |

The reviewer can differ by stage (for example a domain expert reviews Modeling
and an API model does the blind final review). Instruction files for the common
agent runtimes ([CLAUDE.md](CLAUDE.md), [AGENTS.md](AGENTS.md),
[GEMINI.md](GEMINI.md)) are generated from one source and are identical, so no
runtime is special.

## Quick Start

**Automatic run (recommended):** the orchestrator hands work between agents and
asks you only at setup, Tier 1 decision checkpoints, and stage gates.

```bash
# default agents: Claude Code researcher, Codex CLI reviewer (edit workflow.config.json to change)
python -m orchestrator init ~/papers/my-study --topic "what I want to study"
python -m orchestrator run ~/papers/my-study                  # answers at the terminal
python -m orchestrator run ~/papers/my-study --inbox-only     # or answer files later
```

The project folder can be anywhere on your computer; agents are started inside
it. See [docs/orchestration.md](docs/orchestration.md).

**For users:** read [USER_NOTE.md](USER_NOTE.md): what you will be asked, what a
substantive gate looks like, and how to answer.

**Manual run (an agent in a chat session):**

1. Tell the agent its role, or let it read `roles` in [workflow.config.json](workflow.config.json).
2. The agent reads its instruction file ([CLAUDE.md](CLAUDE.md), [AGENTS.md](AGENTS.md), or [GEMINI.md](GEMINI.md)).
3. Read [docs/quickstart.md](docs/quickstart.md).
4. Choose full workflow mode or smoke-test mode.
5. Run the Pre-Planning Session Setup (workflow mode and reviewer strategy), create the project folder (default `research/<research-name>/`) with its README status block, `decision-log.md`, and `run-notes.md`, then check for user-supplied domain materials in its `artifacts/input/domain-materials/` and run Domain Onboarding if present.
6. For a real project, run a focused literature/prior-work and novelty check
   before finalizing the Planning Package. Store detailed notes outside the
   package and summarize the implications in [templates/plan-package.md](templates/plan-package.md).
7. Start from [templates/plan-package.md](templates/plan-package.md) for a real project, or [templates/smoke-test-package.md](templates/smoke-test-package.md) for a framework test.
8. Run Planning -> Modeling -> Reporting -> Reviewing using the stage specs in [docs/](docs/).
9. Record every stage output as a package and every consequential decision in the decision log; write a review request for the reviewer agent before each gate.

Researcher agents must lead one active stage at a time. Do not pre-fill
downstream stage packages before their upstream gates are approved, except as
empty scaffold placeholders.

## Repository Map

| Path | Purpose |
|---|---|
| [workflow.config.json](workflow.config.json) | Which agents exist and which role each holds; workflow mode, reviewer strategy, gate mode |
| [orchestrator/](orchestrator/) | Runs the workflow automatically with any configured agents ([docs/orchestration.md](docs/orchestration.md)) |
| [CLAUDE.md](CLAUDE.md), [AGENTS.md](AGENTS.md), [GEMINI.md](GEMINI.md) | Identical agent instructions for different runtimes; generated |
| [docs/agent-roles/](docs/agent-roles/) | Single source for the researcher and reviewer role instructions; run `python scripts/build_agent_instructions.py` after editing |
| [USER_NOTE.md](USER_NOTE.md) | User guide: how to interact with the agents, gate language, handoff scripts |
| [docs/](docs/) | Stage specifications, handoff rules, organization/coordination/evaluation layers, skill strategy, reviewer-agent prompts, quick start |
| [templates/](templates/) | Package templates for Planning, Modeling, Reporting, Reviewing, the decision log, run notes, smoke tests, and research-skill cards |
| [scripts/](scripts/) | The agent-instruction builder |
| [tests/](tests/) | Orchestrator tests with scripted agents (`python -m unittest discover -s tests`) |
| [examples/](examples/) | Worked examples, including the v0.2 smoke test |
| [skills/](skills/) | Workflow-native skills used inside stages |
| [.claude/commands/](.claude/commands/) | Claude Code slash commands for all seven workflow-native skills |
| `research/` | Real research projects, one folder each (local; ignored by git) |

## Stage Outputs

| Stage | Specification | Main package |
|---|---|---|
| Planning | [docs/plan-stage.md](docs/plan-stage.md) | [templates/plan-package.md](templates/plan-package.md) |
| Modeling | [docs/model-stage.md](docs/model-stage.md) | [templates/model-package.md](templates/model-package.md) |
| Reporting | [docs/reporting-stage.md](docs/reporting-stage.md) | [templates/reporting-package.md](templates/reporting-package.md) |
| Reviewing | [docs/review-stage.md](docs/review-stage.md) | [templates/review-package.md](templates/review-package.md) |
| Smoke-test mode | all stage specs | [templates/smoke-test-package.md](templates/smoke-test-package.md) |

See [docs/stage-handoffs.md](docs/stage-handoffs.md) for package flow, backtracking rules, and gate semantics.

## Skills

The workflow uses small reusable internal skills rather than one all-purpose agent. Each skill has a `SKILL.md` in `skills/` and a matching Claude Code slash command in `.claude/commands/`. External tools and installable skills may still be used for literature search, analysis, citation management, writing, or visualization; the internal skills keep those outputs tied to stage packages, evidence records, review routes, and gates.

| Skill | Slash command | Used mainly in | Responsibility | External relationship |
|---|---|---|---|---|
| [venue-calibration](skills/venue-calibration/SKILL.md) | `/venue-calibration` | Planning, Reporting | Calibrate target journal, conference, preprint, policy note, or other output route | Wraps venue pages, templates, and exemplars |
| [research-skill-card-distiller](skills/research-skill-card-distiller/SKILL.md) | `/research-skill-card-distiller` | Planning | Convert retrieved papers or user-supplied domain materials into reusable research-skill cards | Uses external literature/deep-research outputs as input when useful |
| [model-contract-runner](skills/model-contract-runner/SKILL.md) | `/model-contract-runner` | Modeling | Execute the approved modeling contract with acquisition checks and bounded loops | Orchestrates Python, R, Jupyter, APIs, containers, or domain packages |
| [figure-table-narrative](skills/figure-table-narrative/SKILL.md) | `/figure-table-narrative` | Reporting | Decide visual purpose, evidence status, claim alignment, and caption limits | Hands method/conceptual visuals to CCF-Figure or diagram tools; hands empirical visuals to Model/plotting tools |
| [claim-evidence-mapper](skills/claim-evidence-mapper/SKILL.md) | `/claim-evidence-mapper` | Reporting, Reviewing | Tie research-output claims to citations, artifacts, results, or limitations | May use citation/retrieval tools, but keeps the final map internal |
| [route-aware-reviewer](skills/route-aware-reviewer/SKILL.md) | `/route-aware-reviewer` | Reviewing | Stress-test the research output and route findings to the correct stage | May use external reviewer simulation or checklists |
| [gate-manager](skills/gate-manager/SKILL.md) | `/gate-manager` | All stages | Present gates and Tier 1 checkpoints substantively; record decisions in the decision log | Mostly framework-native |

See [docs/skill-strategy.md](docs/skill-strategy.md) for when to use external tools versus internal skills, and for built-in capability coverage by agent.

## Domain Onboarding

Non-CS researchers often have domain materials the AI has not seen: institutional reports, field-specific papers, data dictionaries, or policy documents. The Planning stage begins with a **Domain Onboarding** step that reads user-supplied materials, extracts a Domain Knowledge Summary, and produces skill cards — before any literature scan or plan writing begins.

Place domain materials in `artifacts/input/domain-materials/` inside the project folder and tell the researcher agent at the start of Planning. See [USER_NOTE.md](USER_NOTE.md) for the exact prompt to use.

## Cross-Agent Handoff

The researcher and reviewer agents communicate through two files written to the run directory (`artifacts/<run_id>/` inside the project folder):

- `review-request-<stage>.md` — written by the researcher; declares the stage, gate mode, review mode (standard or blind), and the reviewer assignment
- `review-framing-<stage>.md` — the researcher's summary, risks, and questions, kept separate so a blind reviewer can read it last
- `reviewer-critique-<stage>.md` — written by the reviewer with a structured findings table

Blocker or major findings that the researcher defers or rejects are escalated to
the user. The Reviewing stage uses blind review by default: the reviewer forms
independent findings before reading the researcher's framing.

See [docs/reviewer-agents/cross-agent-handoff.md](docs/reviewer-agents/cross-agent-handoff.md) for the full protocol and file formats.

In orchestrated runs the orchestrator starts the reviewer, withholds the framing
file during a blind pass, and records the user's gate decision. In manual runs
the user hands the files between agents; the protocol is the same.

## Examples

Example folders follow [docs/example-organization.md](docs/example-organization.md). Real research runs live under `research/` and are kept local (git-ignored) so private notes, large generated artifacts, and copyright-sensitive materials are not accidentally published.

- [examples/smoke-test-v02-co2-growth/](examples/smoke-test-v02-co2-growth/): four-stage smoke test of the v0.2 rules with seeded faults, a decision log, escalations, and a filled workflow evaluation.
- [examples/orchestrator-live-planning/](examples/orchestrator-live-planning/): a real orchestrated Planning stage (Claude Code as researcher and as reviewer, synthetic gates): six checkpoints, a reviewer pass, triage, and a gate, with no human input after `init`.

## Paper

The repository's name and design are informed by the companion conceptual paper, *Designing
Human–AI Collaborative Science: Organization, Coordination, and Evaluation*
(Zheng, Pan, and Lan; in preparation, maintained separately). The paper's organization layer (activity, actor, authority) maps to
[docs/decision-rights.md](docs/decision-rights.md) and the agent roster in
`workflow.config.json`; its coordination layer (shared research state,
scientific accountability loop, adaptive reconfiguration) maps to
[docs/coordination.md](docs/coordination.md) and the
[orchestrator](docs/orchestration.md); its evaluation layer maps to
[docs/workflow-evaluation.md](docs/workflow-evaluation.md).
This repository is one concrete instantiation of that framework for academic
research, not a claim of full scientific automation, substantive collaboration in every run,
or demonstrated improvement in scientific outcomes. See [Design Rationale](docs/design-rationale.md).

## Current Status

This is an early research-framework repository (v0.3-dev). The workflow docs, templates, skills, orchestrator, and a smoke-test example are present. Next:

- an API researcher (tool-using agent loop), so a single API key can run the whole workflow
- one domain case study
- workflow evaluation results from at least one real run (`docs/workflow-evaluation.md`)
- comparative tests of whether authority, state, and critique mechanisms improve research outcomes relative to simpler workflows, accounting for human and compute costs

## License

MIT License. See [LICENSE](LICENSE).
