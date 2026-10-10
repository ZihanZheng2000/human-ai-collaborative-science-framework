# Research Project Organization

This document defines the default layout for real research projects. Each new
research workflow should get its own folder under `research/` before substantive
Planning work begins.

## Default Layout

Use a descriptive, stable slug:

```text
research/<research-name>/
  README.md
  decision-log.md
  run-notes.md
  packages/
    planning-package.md
    modeling-package.md
    reporting-package.md
    reviewing-package.md
  deliverables/
  notes/
  artifacts/
    <run_id>/
      review-request.md
      reviewer-critique.md
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

At the beginning of a new real research project, the researcher agent should:

1. propose a `research/<research-name>/` slug;
2. create the default folder skeleton after the user confirms or when the slug is safe to infer;
3. create `README.md` (with the status block), `decision-log.md`, and `run-notes.md`;
   record the Pre-Planning setup choices as `D-1`;
4. create or revise only the active stage package in `packages/`;
5. put detailed stepwise discussion artifacts in `notes/`;
6. put review requests and reviewer critiques under `artifacts/<run_id>/`.

For framework tests or tiny smoke tests, a shorter layout is acceptable, but the
run must still record where packages, notes, artifacts, and deliverables live.

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

## Root Directory Rule

Do not create new real-project packages directly under the repository-level
`packages/` or new real-project run artifacts directly under the repository-level
`artifacts/` unless the user explicitly requests a legacy layout. Those root
folders may remain for older runs, templates, or migration staging, but new
research projects should live under `research/<research-name>/`.

## Stepwise Work Rule

The project folder supports gradual collaboration:

- draft long reviews and source scans in `notes/`;
- discuss one unit with the user;
- summarize only accepted decisions back into `packages/planning-package.md`;
- send the package for reviewer critique only after the major Planning units
  are discussed or accepted.
