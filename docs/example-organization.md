# Example Organization

This document defines the recommended file layout for worked examples. The goal is to keep each example inspectable without leaving stage packages, notes, scripts, raw data, validation outputs, and final deliverables mixed in one directory.

## Recommended Layout

Each example should use this structure unless there is a clear reason to deviate:

```text
examples/<example-name>/
  README.md
  decision-log.md
  run-notes.md
  packages/
    planning-package.md
    modeling-package.md
    reporting-package.md
    reviewing-package.md
  deliverables/
    manuscript-draft.md
    manuscript-revised.md
    report.md
    skill.md
  notes/
    literature-review.md
    feasibility-analysis.md
    external-tool-scan.md
    method-notes.md
  artifacts/
    <run_id>/
      run_manifest.json
      run_log.md
      run_summary.md
      agent/
    input/
    data/
    code/
    logs/
    tables/
    figures/
    validation/
  archive/
```

## What Belongs Where

| Location | Purpose | Examples |
|---|---|---|
| `README.md` | Stable orientation for the example | goal, status, how to rerun, main outputs |
| `decision-log.md` | Shared research state for decisions | Tier 1 checkpoints, gates, escalations, reconfigurations |
| `run-notes.md` | Provisional lessons and workflow evaluation for one run | friction, evaluation measures, follow-up rules |
| `packages/` | Approved stage handoff packages | planning, modeling, reporting, reviewing packages |
| `deliverables/` | Reader-facing final or near-final outputs | manuscript, revised draft, report, reusable skill |
| `notes/` | Working notes that inform packages but are not packages | literature review, feasibility notes, method sketches |
| `artifacts/input/` | User-supplied or route-defining inputs | draft, venue guidelines, author notes |
| `artifacts/data/` | Acquired or derived datasets | corpus files, metadata, cleaned tables |
| `artifacts/code/` | Scripts and notebooks used in the example | acquisition, analysis, validation scripts |
| `artifacts/<run_id>/` | Run-scoped execution record | run manifest, run log, run summary, agent artifacts |
| `artifacts/logs/` | Shared execution logs and run records | command logs, environment repair logs |
| `artifacts/tables/` | Generated analytical tables | frequency, keyness, validation tables |
| `artifacts/figures/` | Generated figures | plots, workflow diagrams, result visuals |
| `artifacts/validation/` | Validation inputs and outputs | review samples, rubric outputs, LLM checks |
| `archive/` | Superseded outputs kept for traceability | old package versions, abandoned drafts |

## Naming Rules

- Use stage names consistently: `planning`, `modeling`, `reporting`, and `reviewing`.
- Keep the approved stage packages in `packages/`.
- Put final or near-final outputs in `deliverables/`, not beside the packages.
- Put exploratory notes in `notes/`; summarize stable decisions back into the relevant package.
- Put machine-generated files under `artifacts/`, grouped by type.
- Use version suffixes only when the old version remains meaningful, for example `validation-results-v2.md`.
- If a file is superseded and not needed for the current README path, move it to `archive/` or list it as legacy material.

## Root Directory Rule

The example root should stay sparse. In normal use it should contain only:

- `README.md`
- `decision-log.md`
- `run-notes.md`
- `packages/`
- `deliverables/`
- `notes/`
- `artifacts/`
- `archive/`

This keeps the root readable and makes it clear which files are approved handoffs, which are final outputs, and which are supporting evidence.

## Migration Rule For Existing Examples

For existing flat examples, do not move files blindly. First add a migration map to the example README:

| Current file | New location | Reason |
|---|---|---|
| `plan-package.md` | `packages/planning-package.md` | approved Planning handoff |
| `model-package.md` | `packages/modeling-package.md` | approved Modeling handoff |
| `review-package.md` | `packages/reviewing-package.md` | approved Reviewing handoff |

If an old `writing-package.md` contains a manuscript, paper, report, slides, or other final deliverable, map it to `deliverables/` and summarize its evidence status in `packages/reporting-package.md`. Use content, not filename alone, to decide.

After the map is reviewed, files can be moved in a separate cleanup commit or release-prep step.
