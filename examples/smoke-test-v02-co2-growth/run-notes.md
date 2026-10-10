# Run Notes

## Run Identity

- Run name: smoke-test-v02-co2-growth (run `smoke-v02-co2-2026-10-10`)
- Date: 2026-10-10
- Mode: smoke test of framework v0.2 (decision tiers, decision log, escalation, blind review, reconfiguration, workflow evaluation)
- Gate mode: synthetic gates; two escalations (E-1, E-2) go to the real user
- Topic or task: Mauna Loa CO2 growth rate, 1960s vs 2010s (descriptive)
- Stage coverage: Planning / Modeling / Reporting / Reviewing, one reviewer pass each

## Workflow Configuration

- workflow mode: auto-until-needed (D-7)
- reviewer strategy: use reviewer; a separate headless Claude Code process per stage (`claude -p`, same prompt as `scripts/run_reviewer_claude.ps1`)
- review modes used: standard (Planning, Modeling, Reporting); blind (Reviewing; only partly blind, RVR-9)
- researcher agent / reviewer agent: Claude Code / Claude Code (role override D-8; Codex CLI not installed)
- domain expert involved: none
- reconfigurations during the run: D-14 (claims beyond the locked contract), triggered by seeded faults; pending real-user confirmation (E-2)
- seeded faults: S1 (Modeling), S2 (Reporting); sealed record `artifacts/validation/seed-record.md`

## Workflow Evaluation

### Scientific outcome

| Measure | Value | Notes |
|---|---|---|
| substantive claims: supported / limited / unsupported / removed | 7 / 1 / 0 / 1 | report claim map; removed = seeded causal sentence |
| reproducibility rerun | pass (determinism) | identical table hashes; plus an independent hand check |
| validation type(s) used | reproducibility; seeded error | no known-outcome or expert check |

### Collaboration process

| Measure | Value | Notes |
|---|---|---|
| reviewer findings total | 40: 8 major, 22 minor, 4 suggestion, 5 accepted limitation, 1 none found | PR 10, MR 9, RR 8, RVR 13 |
| trajectory-changing reviewer findings | 7 | PR-1 (split D-1, E-1), PR-2 (D-9 lock amendment), MR-1 (D-12), RR-1 (claim removed), RR reconfiguration signal (D-14), RVR-1 (D-16), RVR-2 (D-17 archive scope) |
| seeded faults caught at their own stage | 2 / 2 | S1 by MR-1, S2 by RR-1 |
| unseeded researcher errors caught by review | ≥ 6 | PR-2 open decision rule, PR-7 dropped map rows, MR-7 superseded citation, RVR-1 undisclosed seeding, RVR-3 generous audit, RVR-6 missing run notes |
| trajectory-changing user corrections | 0 | user gave one instruction |
| duplicated or lost work | low | `notes/route.md` was silently untracked by `.gitignore` (F2) |

### Reliability and accountability

| Measure | Value | Notes |
|---|---|---|
| Tier 1 / Tier 2 decisions logged | 17 rows (4 gates, 1 reconfiguration, 1 disclosure, 1 skip-defer) | `decision-log.md` |
| rows with proposer, evidence, objections, authorizer | 17 / 17 | but authorizer is "synthetic" for most |
| approvals: substantive / nominal / synthetic | 2 / 1 / 15 | substantive = the two real-user rulings D-18, D-19 |
| escalations raised / upheld / replaced | 2 / 1 / 1 | E-1 upheld for smoke test only (D-18); E-2: D-14 replaced by reviewer claim audit (D-19) |
| decisions reopened or superseded | 1 superseded (D-1); 1 post-visibility change (D-12) | |
| reviewer-triage closure rate | 38 / 40 closed by researcher or accepted; 2 escalated | |

### Human effort

| Measure | Value | Notes |
|---|---|---|
| checkpoints and gates presented to the real user | 0 during the run; 2 escalations at the end, answered in one structured question | synthetic run |
| user domain corrections | 0 | |
| re-runs or rewrites requested by the user | 0 | |
| reviewer runtime | about 1-2 minutes per pass | headless process |
| where user effort went | judgment only (E-1, E-2) | |

### Reading the numbers

- The reviewer loop worked as designed: both seeded faults were caught at the
  stage where they were planted, and most reviewer value came from unseeded
  issues (an undefined decision rule, missing map rows, gate vagueness).
- The accountability record is complete in form but empty in substance: no
  consequential decision had a human authorizer. That is expected for a
  synthetic run and is the main reason it must not be reused.
- Same-model review is the largest independence caveat; it remains E-1.

## Framework Findings

| ID | Issue | Evidence | Fix |
|---|---|---|---|
| F1 | One run directory, four stages, but the protocol names a single `review-request.md` / `reviewer-critique.md`; stages overwrite each other | PR-10 | name files per stage: `review-request-<stage>.md`, `reviewer-critique-<stage>.md` |
| F2 | `.gitignore` patterns `notes/` and `research/` match nested folders, so example `notes/` were silently untracked | `notes/route.md` missing from `git status` | anchor to repo root: `/notes/`, `/research/` |
| F3 | Blind mode cannot be enforced when the framing sits in the request file | RVR-9 | put the framing in a separate `review-framing-<stage>.md`; blind reviewer opens it only after the independent block |
| F4 | Reporting reviewer proposed a three-instance reconfiguration threshold while `coordination.md` says two passes | RR reconfiguration signal, RVR-10 | state trigger thresholds in the reviewer role so reviewers apply the documented rule |
| F5 | A reconfiguration that only adds a researcher self-check does not move authority, but the coordination table allowed it | RVR-4 | for reviewer-major recurrences, require a change of actor or authority (reviewer audit duty, blind review, expert, or user co-sign) |
| F6 | Review Package recommendation could be vague ("approve limited"), and run notes were not required before the Reviewing review | RVR-2, RVR-6 | require concrete gate options with consequences and archive scope; fill run notes before the Reviewing review request |
| F7 | Seeded-error testing had no procedure; the seed label leaked into a package before the next seeded stage was reviewed | D-16 | add a seeded-fault protocol: sealed record, no labels until all seeded stages are reviewed, disclosure entry in the decision log |
| F8 | Audit template rows invite "pass" when authorizers are synthetic | RVR-3 | add "synthetic" as an explicit audit outcome |
| F9 | The user's own words cited as authority were not interpretable later | RVR-13 | quote the user and state what it authorized |

Status: F1-F9 were applied to the framework on 2026-10-10, after this run. This
example keeps the file layout it was run with (stage-suffixed request files, no
separate framing file).

## Candidate Formal Updates

| Candidate update | Target file | Decision |
|---|---|---|
| F1 per-stage file names | `docs/reviewer-agents/cross-agent-handoff.md`, role files | update formal docs |
| F2 gitignore anchoring | `.gitignore` | update now |
| F3 separate framing file | `cross-agent-handoff.md`, reviewer role, scripts | update formal docs |
| F4 thresholds in reviewer role | `docs/agent-roles/reviewer-role.md` | update formal docs |
| F5 reconfiguration must move authority | `docs/coordination.md` | update formal docs |
| F6 concrete gate options + run notes before Reviewing review | `docs/review-stage.md`, `templates/review-package.md` | update formal docs |
| F7 seeded-fault protocol | `docs/workflow-evaluation.md` | update formal docs |
| F8 synthetic audit outcome | `templates/review-package.md` | update formal docs |
| F9 quote user authority | `templates/decision-log.md` | update formal docs |

## After-Action Review

- Repeat: sealed seeded faults; one reviewer pass per stage; decision log as the single place to reconstruct the run.
- Avoid: labeling seeds in packages before every seeded stage has been reviewed; bundling several Tier 1 choices in one decision row.
- Needs another test: blind review with a separate framing file; D-14-style reconfiguration under real (unseeded) recurrence; a different-model reviewer (Codex) to measure independence.
