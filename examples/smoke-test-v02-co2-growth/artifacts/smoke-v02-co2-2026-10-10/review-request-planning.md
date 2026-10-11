# Review Request

## Header

- Stage: Planning
- Run ID: smoke-v02-co2-2026-10-10
- Run directory: examples/smoke-test-v02-co2-growth/artifacts/smoke-v02-co2-2026-10-10/
- Gate mode: synthetic gate
- Review mode: standard
- Stage package path: examples/smoke-test-v02-co2-growth/packages/planning-package.md
- Decision log path: examples/smoke-test-v02-co2-growth/decision-log.md
- Researcher agent: Claude Code
- Reviewer agent: Claude Code (separate headless process)
- Assignment source: WORKFLOW-CONFIG.md (Config A assigns Claude Code as reviewer); researcher role override recorded as D-1
- Reviewer rights: advisory + escalation (default)
- Date: 2026-10-10

## Artifacts to Inspect

- examples/smoke-test-v02-co2-growth/packages/planning-package.md
- examples/smoke-test-v02-co2-growth/decision-log.md
- examples/smoke-test-v02-co2-growth/notes/route.md
- examples/smoke-test-v02-co2-growth/artifacts/data/raw/co2-annmean-mlo.csv
- examples/smoke-test-v02-co2-growth/artifacts/data/raw/co2-mm-mlo.csv
- examples/smoke-test-v02-co2-growth/artifacts/smoke-v02-co2-2026-10-10/run_log.md

## Researcher Framing

### Summary of Work Done

Smoke test of the v0.2 framework rules on a small descriptive question about
the Mauna Loa CO2 growth rate. Planning set the question and descriptive claim
level, chose a GitHub mirror because the NOAA host is blocked, locked the
analysis choices before computing results, deferred the literature scan, and
adopted the default Decision-Rights Map.

### Known Risks or Open Questions

- Mirror vs official source.
- Researcher role override (D-1) and same-model reviewer.

### Specific Questions for the Reviewer

1. Are the locked analysis choices specific enough to detect later drift?
2. Is the D-1 role override handled correctly under the decision-rights rules?
