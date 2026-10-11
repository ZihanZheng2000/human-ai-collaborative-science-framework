# Skills

This folder contains internal workflow-native skills for the Human–AI Collaborative Science Framework.

These skills are written and maintained in this repository. They are not meant to replace mature external research tools. They are small reusable control modules that help the four stages stay inspectable, evidence-bound, and human-gated.

## Skill Strategy

Use the strategy in `../docs/skill-strategy.md`:

1. Reuse mature external tools for standardized research operations.
2. Use workflow-native skills to orchestrate, verify, package, and route outputs.
3. Create project-specific skills only when the needed operation is not already covered well enough.
4. Promote project-specific skills into this folder only after reuse and review.

Recommended external research skills are listed in `../docs/skill-strategy.md#recommended-external-research-skills`. Keep those tools outside this `skills/` folder unless this project later adds a thin adapter skill that exposes inputs, outputs, evidence logs, and failure modes.

## Current Internal Workflow-Native Skills

| Skill | Main role | External tool relationship |
|---|---|---|
| `venue-calibration/` | Calibrate a project to target venue, audience, official requirements, and exemplar patterns | Wraps venue websites, author guidelines, templates, and exemplar papers |
| `research-skill-card-distiller/` | Convert prior work into reusable research-skill cards or method patterns | May use external literature-search or deep-research outputs as input |
| `model-contract-runner/` | Run Modeling-stage work under explicit contracts, success rules, and bounded loops | Orchestrates Python, R, Jupyter, containers, APIs, or domain packages rather than replacing them |
| `figure-table-narrative/` | Plan visual evidence, claim alignment, placement, and caption limits around Reporting deliverables | Hands method/conceptual visuals to CCF-Figure or diagram tools; hands empirical visuals to Model/plotting tools |
| `claim-evidence-mapper/` | Tie claims to citations, model artifacts, limitations, or approved user knowledge | May use citation, retrieval, or metadata tools, but keeps the final map internal |
| `route-aware-reviewer/` | Review evidence packages or deliverables and route findings to Planning, Modeling, Reporting, Reviewing, or termination | May use reviewer simulation or checklists, but keeps routing decisions internal |
| `gate-manager/` | Present gates and Tier 1 checkpoints substantively, record decisions in the decision log, and manage stage advancement, backtracking, or reconfiguration | Mostly framework-native; not replaced by external tools |

In short: external tools perform research operations; internal skills preserve the framework's control logic, evidence records, handoffs, and gates.

## External Handoff Expectations

When a skill uses or recommends an external tool, the stage package should record:

- tool or source name
- version, access date, API endpoint, model, package version, or template version when relevant
- input query, prompt, file, dataset, or manuscript section
- output artifact path or citation
- verification status
- limitations or known failure modes
- whether the output is evidence, a suggestion, formatting support, or a convenience artifact

## Project-Specific Skills

Project-specific skills should usually live in the project or run artifacts while they are being tested, for example `<run_dir>/agent/` (see `../docs/stage-handoffs.md`). They can be promoted into `skills/` only when they are reusable across projects, documented, and clearly add workflow value beyond external tools.
