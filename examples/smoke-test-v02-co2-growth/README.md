# Smoke Test v0.2: Mauna Loa CO2 Growth-Rate Acceleration

> Historical record: this run used the v0.2 conventions (Config A/B in
> `WORKFLOW-CONFIG.md`, the PowerShell reviewer wrapper, single-file review
> requests). Those were replaced in v0.3 by `workflow.config.json`, the
> orchestrator, and separate framing files. The files below are kept as they
> were produced.

Framework smoke test of the v0.2 rules (decision tiers, decision log,
escalation, blind review, substantive gates, workflow evaluation). The research
content is deliberately small and well known; the object under test is the
workflow.

## Status

- current stage: archived (internal smoke-test output, D-17)
- active package: none
- last decision: D-17 (2026-10-10) — Reviewing Gate: archive (synthetic); D-16 seeded-fault disclosure
- open escalations: none (E-1 → D-18, E-2 → D-19, ruled by the real user)
- deferred items due soon: none
- current workflow mode and reviewer strategy: Auto-until-needed; Use reviewer (headless Claude Code)
- next action: none (archived)
- user decision needed now: none

## Layout

- `decision-log.md` — decisions (shared research state)
- `packages/` — stage packages
- `artifacts/smoke-v02-co2-2026-10-10/` — run directory: review requests, critiques, run log
- `artifacts/data/`, `code/`, `tables/`, `figures/` — evidence
- `deliverables/` — reader-facing report
- `run-notes.md` — lessons and workflow evaluation
