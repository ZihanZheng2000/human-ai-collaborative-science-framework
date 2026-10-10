# Orchestration: Running the Workflow Automatically

The orchestrator runs the four-stage workflow with whatever agents you
configure, hands work between them, and stops only where a person should
decide. It implements the coordination layer
([coordination.md](coordination.md)) as a program: the shared research state is
on disk, every human decision is logged by the orchestrator itself, and blind
review is enforced mechanically.

It is plain Python (standard library only). API agents need their provider's
SDK (`pip install anthropic` or `pip install openai`).

## Quick Start

```bash
# from the framework folder; edit workflow.config.json first if you want other agents
python -m orchestrator init ~/papers/my-study --topic "what I want to study, in my own words"
python -m orchestrator run ~/papers/my-study
```

The project folder can be anywhere: inside this repository (for example
`research/my-project`) or any folder on your computer, including one that
already holds your data. Agents are started **inside the project folder**, the
way you would open Claude Code or Codex there yourself, and read the framework's
rules from this repository (Claude Code via `--add-dir {framework_dir}`). For a
project outside the repository, `init` also writes small `CLAUDE.md`,
`AGENTS.md`, and `GEMINI.md` pointer files (never overwriting existing ones) so
an agent opened there by hand finds the framework too.

`run` keeps going until it needs you. At the terminal it shows the decision and
its options; type a number or your own answer. Type `later` (or run with
`--inbox-only`) to leave the decision in `research/my-project/inbox/pending/`,
answer it by filling the file's **Decision** section whenever you like, then run
again. `python -m orchestrator status research/my-project` shows where things stand.

| Command | What it does |
|---|---|
| `init <project> --topic "..."` | Creates the project folder, decision log, run notes, and the three setup questions |
| `run <project>` | Runs until a person is needed or the workflow ends (exit 0 done, 2 waiting) |
| `run <project> --until planning` | Stops once that stage's gate is approved |
| `run <project> --inbox-only` | Never asks at the terminal; for long or unattended runs |
| `status <project>` | Stage, step, pending decisions, open escalations |
| `new-session <project> --role researcher\|reviewer` | The next call for that role starts a new conversation |
| `review <project> --stage S [--revision N] [--run-id R]` | Runs only the reviewer pass on an existing `review-request-<stage>.md`. For manual runs: you work with an agent in a chat session and hand only the review to the configured reviewer. Does not advance the workflow. |

## When You Are Asked

The orchestrator stops at these human nodes, and nowhere else:

| Node | Raised by | Why |
|---|---|---|
| Setup (workflow mode, reviewer strategy, gate mode) | orchestrator, once | Pre-Planning Session Setup |
| Tier 1 checkpoint (`CP-<stage>-<n>.md`) | researcher agent | a consequential in-stage decision ([decision-rights.md](decision-rights.md)) |
| Stage gate (`GATE-<stage>-r<n>.md`) | researcher agent, after the reviewer pass and triage | Tier 2 gate; open escalations are listed in it |
| Human task (`TASK-...md`) | orchestrator | a role in the config is assigned to a person (for example a domain-expert reviewer) |
| Stuck (`STUCK-...md`) | orchestrator | an agent failed or stopped without its handoff file several times |

In **step-by-step** mode the researcher stops at each checkpoint. In
**auto-until-needed** mode it batches checkpoints and stops only when it cannot
go on without answers. With **synthetic** gates (framework tests only) the
orchestrator takes the recommended option and records the decision as
synthetic; a human task still waits for a person.

## What Happens in Each Stage

```text
work    researcher builds the stage package; may raise checkpoints;
        ends by writing review-request-<stage>.md + review-framing-<stage>.md
review  reviewer writes reviewer-critique-<stage>.md
        (blind mode: two passes; the framing file is withheld in the first)
triage  researcher triages findings, escalates deferred/rejected blockers and
        majors, writes gate-request-<stage>.md
gate    you decide: approve -> next stage / revise -> revision r2 /
        backtrack -> earlier stage / terminate
```

With `"reviewer": "skip"`, `work` ends with the gate request and there is no
review or triage step. A revision or backtrack reuses the same run directory
with `-r2`, `-r3` file names.

Every prompt tells the agent to read the shared research state first: the
project README status block, `decision-log.md`, the stage packages, and
`inbox/answered/`. Whether the agent also keeps its earlier conversation is set
by the session policy below.

### Sessions: when agents keep their conversation

Default behaviour, like working with Claude Code yourself:

| Role | Default | Meaning |
|---|---|---|
| researcher | `run` | one conversation for the whole project; checkpoint answers, triage, and the next stage continue it |
| reviewer | `stage` | a new conversation for every stage; later review passes in the same stage (for example `-r2` after a revision) continue it |
| blind review, independent pass | always new | the reviewer must not have seen any framing; the follow-up pass continues the independent pass, and the next pass starts fresh again |

Set the policy in `workflow.config.json`:

```json
"workflow": {
  "sessions": {"researcher": "run", "reviewer": "stage", "fresh_researcher_at": ["reporting"]}
}
```

Values are `run`, `stage`, or `off` (a new conversation at every step).
`fresh_researcher_at` lists stages where the researcher starts a new
conversation. You can also start one whenever you like:

- `python -m orchestrator new-session <project> --role researcher` (or `reviewer`);
- at a stage gate, the option "Approve for <next stage> and start it with a new
  researcher session", which the orchestrator adds when the researcher keeps one
  conversation.

How to continue a conversation is set per agent with a `session` spec (the
default config has the one for Claude Code: `--output-format json` to read the
session id, `--resume <id>` to continue). Agents without it, including API
reviewers, start fresh every time.

Two things stay true whatever the setting:

- Files remain the authority. A long conversation gets compacted, and the next
  agent may be a different product, so decisions, reasoning, and status must be
  written to the decision log, notes, packages, and the README status block.
- Conversation memory never changes who decided what: human decisions only enter
  through the inbox and are logged by the orchestrator.

The reviewer defaults to a new conversation per stage because a reviewer that
has followed the researcher through every stage has read all of its reasoning
and gradually stops being independent. You can set `"reviewer": "run"`; record
the reason in the decision log.

## Who Writes the Decision Log

The orchestrator writes every decision-log row whose authority is a person (or
a synthetic gate): setup, checkpoint answers, gate decisions, and stuck-state
choices. Agents never write those rows, so no agent can record an approval that
did not happen. Approval quality is computed from the request file: an approval
is **substantive** only if the request showed a proposal, evidence,
alternatives, open objections, consequences, and options; otherwise it is
recorded as **nominal** with what was missing.

The researcher still maintains the Open Escalations and Deferred Items tables;
the orchestrator lists open escalations in every gate it presents.

## Configuring Agents

`workflow.config.json` has three parts: `agents`, `roles`, and `workflow`.
`workflow.config.example.json` shows every kind.

| Kind | What it is | Roles |
|---|---|---|
| `cli` | Any command-line agent: Claude Code, Codex, Gemini CLI, Aider, or your own script. `command` is the argument list; `{prompt}` is replaced by the prompt text, `{prompt_file}` by a file holding it, `{project_dir}` by the project folder, and `{framework_dir}` by this repository. `role_commands` gives a different command per role (for example tighter tool permissions for the reviewer). `"stdin": true` sends the prompt on standard input. `"reviewer_output": "stdout"` lets a read-only reviewer print its critique for the orchestrator to save. | researcher, reviewer |
| `anthropic` | Claude through the official Anthropic SDK. The orchestrator sends the review request, the listed artifacts, and the framework docs, and saves the reply as the critique. Uses adaptive thinking, the configured `effort`, and server-side refusal fallbacks. | reviewer |
| `openai_compatible` | Any endpoint that speaks the OpenAI chat-completions API (hosted or local, set `base_url`). Same read-only pattern as `anthropic`. | reviewer |
| `human` | A person fills the role. Tasks arrive in the inbox as `TASK-...md`. | researcher, reviewer |

**Codex CLI** can sign in with a ChatGPT account or use an API key; as a `cli`
agent it can open files and rerun code itself, which makes it a stronger
reviewer than an API model that only sees the files sent to it.

**Reviewer guard.** Before and after a CLI reviewer runs, the orchestrator
records the size and modification time of every file in the project (and in
this repository). If the reviewer changed anything besides its critique, the run
stops with a `STUCK` item listing the files, so a reviewer with write access
cannot silently edit the work it reviews.

The researcher must be a `cli` or `human` agent because it edits files and runs
code. API agents can be reviewers; an API researcher would need a tool-using
agent loop and is not supported yet.

`roles.reviewer` may be one agent name or a per-stage map:

```json
"roles": {
  "researcher": "claude-code",
  "reviewer": {"default": "codex", "reviewing": "claude-api", "modeling": "domain-expert"}
}
```

Assigning different agents (or a person) to different stages is how the
reconfiguration decisions in [coordination.md](coordination.md#adaptive-reconfiguration)
are carried out: edit `roles`, and record the change in the decision log.

`workflow` options:

| Key | Values | Default |
|---|---|---|
| `mode` | `step-by-step` / `auto-until-needed` | `step-by-step` |
| `reviewer` | `use` / `skip` | `use` |
| `gates` | `real` / `synthetic` | `real` |
| `review_modes` | per-stage `standard` / `blind` | `blind` for Reviewing, `standard` otherwise |
| `max_attempts` | researcher retries before a stuck item | 3 |
| `max_review_context_chars` | upper limit for API reviewer context; the orchestrator refuses rather than truncates | 1,500,000 |

The setup questions at `init` override `mode`, `reviewer`, and `gates` for that
project; `init --use-config-defaults` skips the questions and records the
config values as a nominal approval.

## Files the Orchestrator Adds to a Project

| Path | Purpose |
|---|---|
| `inbox/pending/` | decisions waiting for a person |
| `inbox/answered/` | answered requests, linked from the decision log |
| `.workflow/state.json` | stage, step, revision, settings, history |
| `artifacts/<run_id>/agent/` | prompts and output of every agent call |
| `artifacts/<run_id>/gate-request-<stage>.md` | the researcher's gate presentation |

## Limits

- Blind review is enforced by withholding the framing file. A CLI reviewer with
  broad filesystem access could still find earlier critiques or notes that
  mention the framing; keep framing content in the framing file.
- The orchestrator cannot judge whether an agent's work is good; that is what
  the reviewer and the gates are for. It only checks that each step produced its
  handoff file.
- The reviewer guard detects changes; it does not prevent them. Undo unwanted
  changes from version control or the agent log before continuing.
- CLI flags for third-party agents change between versions. The example config
  lists commands that worked when written; check them against your installed
  version.
