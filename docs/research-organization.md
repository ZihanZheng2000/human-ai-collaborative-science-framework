# Research Project Organization

This document defines the layout of a research project folder. Each project gets
its own folder before substantive Planning work begins. With the orchestrator
the folder can be anywhere (`python -m orchestrator init <folder> --topic ...`
creates the layout below). In manual runs inside this repository, the default
location is `research/<research-name>/`, which git ignores.

## Default Layout

Use a descriptive, stable slug:

```text
research/<research-name>/
  README.md
  decision-log.md
  run-notes.md
  inbox/
    pending/        # decisions waiting for a person
    answered/
  .workflow/
    state.json      # orchestrator state (orchestrated runs)
  packages/
    planning-package.md
    modeling-package.md
    reporting-package.md
    reviewing-package.md
  deliverables/
  notes/
  artifacts/
    <run_id>/
      gate-request-<stage>.md
      review-request-<stage>.md
      review-framing-<stage>.md
      reviewer-critique-<stage>.md
      run_manifest.json
      run_log.md
      run_summary.md
      agent/
    input/
      domain-materials/
    data/
    code/
    logs/
    tables/
    figures/
    validation/
  archive/
```

## What Belongs Where

| Location | Purpose |
|---|---|
| `README.md` | Status block (see below) plus research question and important paths |
| `decision-log.md` | Shared research state for decisions: every Tier 1 checkpoint, Tier 2 gate, escalation, reconfiguration, and informal review (template: `templates/decision-log.md`) |
| `inbox/` | Checkpoint, gate, and task requests for people; answered requests are kept and linked from the decision log |
| `.workflow/state.json` | Orchestrator state: stage, step, revision, settings, history |
| `run-notes.md` | Provisional lessons, friction, and the workflow evaluation record (template: `templates/example-run-notes.md`) |
| `packages/` | Compact stage handoff packages only |
| `deliverables/` | Reader-facing outputs such as manuscript drafts, reports, slides, dashboards, or software packages |
| `notes/` | Discussion notes, literature reviews, problem taxonomies, source notes, method sketches |
| `artifacts/<run_id>/` | Run-scoped review requests, critiques, manifests, logs, summaries, and agent artifacts |
| `artifacts/input/` | User-supplied files and route-defining inputs; `domain-materials/` holds Domain Onboarding materials |
| `artifacts/data/` | Raw and cleaned datasets or literature/source matrices |
| `artifacts/code/` | Scripts and notebooks |
| `artifacts/logs/` | Command logs, environment repair logs, execution traces |
| `artifacts/tables/` | Generated analytical tables |
| `artifacts/figures/` | Generated figures and diagrams |
| `artifacts/validation/` | Validation inputs and outputs |
| `archive/` | Superseded files kept for traceability |

## Startup Rule

With the orchestrator, `python -m orchestrator init research/<research-name> --topic "..."`
creates this layout. In manual runs, at the beginning of a new real research
project, the researcher agent should:

1. propose a `research/<research-name>/` slug;
2. create the default folder skeleton after the user confirms or when the slug is safe to infer;
3. create `README.md` (with the status block), `decision-log.md`, and `run-notes.md`;
   record the Pre-Planning setup choices as `D-1`;
4. create or revise only the active stage package in `packages/`;
5. put detailed stepwise discussion artifacts in `notes/`;
6. put review requests and reviewer critiques under `artifacts/<run_id>/`.

For framework tests or tiny smoke tests, a shorter layout is acceptable, but the
run must still record where packages, notes, artifacts, and deliverables live.

## Optional decision-relevant research summary (proposed)

See [Shared Research State Contract](shared-research-state-contract.md). A future
pilot may add `notes/current-research-state.md` for current claims, supporting
evidence, open disputes, authorizations, and next scientific actions. This is
**optional and not created automatically**; the existing status block, packages,
and decision log remain the sources of record. Do not assume it exists in older runs.

## README Status Block

Keep this block at the top of the project README and update it whenever the
researcher stops:

```markdown
## Status

- current stage:
- active package:
- last decision: D-<n> (date) — one line
- open escalations: none / list
- deferred items due soon: none / list
- current workflow mode and reviewer strategy:
- next action:
- user decision needed now: none / what
```

## Stepwise Work Rule

The project folder supports gradual collaboration:

- draft long reviews and source scans in `notes/`;
- discuss one unit with the user;
- summarize only accepted decisions back into `packages/planning-package.md`;
- send the package for reviewer critique only after the major Planning units
  are discussed or accepted.
