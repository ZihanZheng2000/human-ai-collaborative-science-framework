# Contributing

Thank you for helping improve Human–AI Collaborative Science Framework.

This repository is a research workflow kit. Contributions should preserve the core design:

- human-gated stage transitions
- evidence-grounded claims
- reproducible data/model artifacts
- route-aware review and backtracking
- clear distinction between real user gates and synthetic smoke-test gates

## Useful Contribution Types

- Improve stage specifications in `docs/`.
- Improve package templates in `templates/`.
- Add or refine workflow-native skills in `skills/`.
- Edit researcher/reviewer agent instructions in `docs/agent-roles/`, then run `python scripts/build_agent_instructions.py` to regenerate `CLAUDE.md`, `AGENTS.md`, and `GEMINI.md` (do not edit those files directly).
- Improve the orchestrator (`orchestrator/`) or add agent adapters; add a test in `tests/` with the scripted agent in `tests/fake_agent.py`.
- Add small, reproducible examples in `examples/`.
- Improve the organization, coordination, and evaluation layers (`docs/decision-rights.md`, `docs/coordination.md`, `docs/workflow-evaluation.md`).
- Report workflow evaluation results from real or smoke-test runs (see `templates/example-run-notes.md`).
- Add tests or smoke tests that reveal workflow gaps.

## Example Requirements

Examples should include:

- a clear purpose
- data source identity: raw host, official source, documentation source, version/access date, and license/access status
- acquisition success counts
- code or notebook that can be rerun
- generated figures or tables when relevant
- a short report or review artifact
- the decision log and run notes (with the Workflow Evaluation section)
- known limitations

For framework-only tests, use `templates/smoke-test-package.md`.

## Style

- Prefer compact Markdown packages over scattered notes.
- Keep claims tied to evidence, citations, or artifacts.
- Do not present synthetic gates as real user approval.
- Do not count links, metadata, or inaccessible files as usable data.
- Use project-specific skills inside `examples/` until they prove reusable.
