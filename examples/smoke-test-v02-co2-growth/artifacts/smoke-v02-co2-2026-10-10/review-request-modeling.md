# Review Request

## Header

- Stage: Modeling
- Run ID: smoke-v02-co2-2026-10-10
- Run directory: examples/smoke-test-v02-co2-growth/artifacts/smoke-v02-co2-2026-10-10/
- Gate mode: synthetic gate
- Review mode: standard
- Stage package path: examples/smoke-test-v02-co2-growth/packages/modeling-package.md
- Decision log path: examples/smoke-test-v02-co2-growth/decision-log.md
- Researcher agent: Claude Code
- Reviewer agent: Claude Code (separate headless process)
- Assignment source: WORKFLOW-CONFIG.md (Config A assigns Claude Code as reviewer); researcher role override recorded as D-1
- Reviewer rights: advisory + escalation (default)
- Date: 2026-10-10

## Artifacts to Inspect

- examples/smoke-test-v02-co2-growth/packages/modeling-package.md
- examples/smoke-test-v02-co2-growth/packages/planning-package.md
- examples/smoke-test-v02-co2-growth/decision-log.md
- examples/smoke-test-v02-co2-growth/artifacts/code/analyze_growth.py
- examples/smoke-test-v02-co2-growth/artifacts/tables/decadal_growth.csv
- examples/smoke-test-v02-co2-growth/artifacts/tables/decadal_growth_shifted.csv
- examples/smoke-test-v02-co2-growth/artifacts/tables/summary.json
- examples/smoke-test-v02-co2-growth/artifacts/figures/annual_growth_decadal_means.png
- examples/smoke-test-v02-co2-growth/artifacts/validation/rerun_check.md
- examples/smoke-test-v02-co2-growth/artifacts/smoke-v02-co2-2026-10-10/run_log.md

## Researcher Framing

### Summary of Work Done

Ran the locked analysis. Acquisition checks pass, outputs reproduce on rerun,
and the decision rule returns "increase". The Planning reviewer's PR-1 is open
as escalation E-1 for the real user.

### Known Risks or Open Questions

- Endpoint dependence of decade means (PR-3).
- Mirror vs official source.

### Specific Questions for the Reviewer

1. Does the code implement D-4 and D-9 exactly?
2. Is the package ready for Reporting?
