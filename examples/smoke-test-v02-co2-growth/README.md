# Smoke Test v0.2: Mauna Loa CO2 Growth-Rate Acceleration

Framework smoke test of the v0.2 rules (decision tiers, decision log,
escalation, blind review, substantive gates, workflow evaluation). The research
content is deliberately small and well known; the object under test is the
workflow.

## Status

- current stage: archived (internal smoke-test output, D-17)
- active package: none
- last decision: D-17 (2026-10-10) — Reviewing Gate: archive (synthetic); D-16 seeded-fault disclosure
- open escalations: E-1 (role override, PR-1) and E-2 (confirm D-14) — for the real user
- deferred items due soon: none
- current workflow mode and reviewer strategy: Auto-until-needed; Use reviewer (headless Claude Code)
- next action: real user rules on E-1 and E-2
- user decision needed now: E-1, E-2

## Layout

- `decision-log.md` — decisions (shared research state)
- `packages/` — stage packages
- `artifacts/smoke-v02-co2-2026-10-10/` — run directory: review requests, critiques, run log
- `artifacts/data/`, `code/`, `tables/`, `figures/` — evidence
- `deliverables/` — reader-facing report
- `run-notes.md` — lessons and workflow evaluation
