---
name: model-contract-runner
description: Use during Model when an Approved Planning Package must be turned into reproducible data retrieval, data quality checks, analysis code, preliminary finding checks, model critic passes, next-analysis queues, bounded evidence-deepening loops, figures, tables, and a Modeling Package.
---

# Model Contract Runner

## Use When

- Planning Gate is approved
- data must be retrieved, cleaned, matched, or analyzed
- results need a reproducible Modeling Package

## Inputs

- Approved Planning Package
- data plan
- method blueprint
- acceptance rubric
- user constraints

## Procedure

1. State a concrete Modeling Goal for the run: continue until the Modeling Package is ready for the Modeling Gate, or until a user decision, Plan backtrack, or termination condition is required.
2. Lock the modeling contract from the approved plan. Present labels, exclusion rules, metrics, model search space, and validation split as a Tier 1 decision checkpoint and record the user's decision in `decision-log.md` before running the analyses they affect.
3. Record data source identity: raw host, official source, documentation source, citation source, version/access date, and license/access status.
4. Retrieve raw data under explicit acquisition success rules and save provenance.
5. Run preflight and data quality checks before analysis.
6. Build a minimal executable analysis.
7. Generate the first expected figures and tables.
8. Validate outputs against the modeling contract.
9. If execution fails because of environment problems, record an environment repair decision before continuing.
10. Write a Preliminary Finding Brief: first check correctness, then check sufficiency.
11. Update the Model State Tracker.
12. Run a Model Critic Pass.
13. If the result is correct but insufficient, build a Next Analysis Queue.
14. Run bounded repair, cleaning, environment repair, method-fidelity, result-quality, or evidence-deepening loops only when justified.
15. Stop, escalate, or pass through the Modeling Gate.

## Outputs

- Modeling Package
- raw and cleaned data notes
- data acquisition success counts
- data source identity notes
- environment repair decisions
- code and run logs
- preliminary finding briefs
- model state tracker
- model critic notes
- next-analysis queue
- figures and tables
- evidence-deepening log
- claim-readiness matrix
- limitations and addendum requests

## Guardrails

- Make Tier 0 choices (repairs, retries, code structure, cleaning within locked rules) yourself and record them in the run log; stop and raise a Tier 1 checkpoint if a repair would change a locked choice.
- If a locked choice changes after results were visible, log a new decision that says so.

- Do not change the research question or method without user approval.
- Do not stop merely because a script ran, a table was produced, or a figure exists.
- Do not optimize until a desired result appears.
- Do not count candidate links, metadata, or inaccessible files as usable data unless the plan explicitly defines them as data.
- Do not treat documentation, mirrors, package excerpts, or official pages as the exact raw data source unless the relationship is verified.
- Do not continue after an environment failure without choosing and logging a repair path: install dependencies, simplify implementation, use a container/runtime, change hardware, reduce scope, or backtrack.
- Do not deepen a result until the preliminary finding has passed a correctness check.
- Do not pass a correct result to Reporting until it is sufficient for the accepted claim level, or until the user accepts a limited demo or preliminary claim.
- Do not continue evidence deepening unless each queued analysis supports a claim, uncertainty, validation need, or discussion need.
- Do not use auto-research loops to change topics, chase significance, substitute unapproved methods, or escalate claims silently.
- Weak or null results may be valid and should be passed to Reporting when defensible and sufficient for the accepted claim level.
