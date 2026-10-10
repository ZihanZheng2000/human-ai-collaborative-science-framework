# Quick Start

This repository is a workflow kit for AI-assisted academic research. It is not a fully autonomous research agent and not a Python package.

## Choose a Mode

Every new session should start with a short Pre-Planning Session Setup before
Planning begins.

1. Confirm the role configuration from `WORKFLOW-CONFIG.md`.
2. Ask the user to choose a workflow mode:

| Mode | Meaning |
|---|---|
| Auto-until-needed | Proceed through the workflow and stop only at gates, missing information, route-changing decisions, or genuine uncertainty/problems. |
| Step-by-step discussion | Discuss each meaningful step or decision with the user before expanding the package or moving on. |

3. Ask the user to choose a reviewer strategy:

| Option | Meaning |
|---|---|
| Use reviewer | Run review-request -> reviewer-critique -> researcher response before each user gate. |
| Skip reviewer | Record skipped-review reason, accepted risk, and revisit trigger before the user gate. |

4. For a real project, create `research/<research-name>/` with `README.md`
   (status block), `decision-log.md`, and `run-notes.md`, and record these
   setup choices as `D-1`.

For real research, recommend **Step-by-step discussion** and **Use reviewer**.
For smoke tests, recommend **Auto-until-needed** with synthetic gates.

### Full Workflow Mode

Use this for a real research project.

1. The researcher agent reads the startup files and announces the current stage,
   package path, immediate next action, and stop condition.
2. Start Planning with proposed user-need confirmation and Domain Onboarding checks.
3. Before writing the full Planning package, run a focused literature/prior-work
   and novelty calibration unless the user explicitly chooses to skip or defer
   it. The light version should still check whether the idea has already been
   studied, what adjacent work did, and what gap or value remains.
4. Create or revise only the Planning package until it is ready for reviewer
   critique.
5. Run Planning Reviewer critique with a separate reviewer agent when available
   and approved.
6. Have the researcher agent respond to reviewer findings, revise or route
   issues, and then ask for the user Planning Gate.
7. Move to Modeling only after the Planning Gate is approved. Do not treat
   user agreement with the topic, rough idea, or literature-scan direction as
   Planning Gate approval.
8. Repeat the same pattern for Modeling, Reporting, and Reviewing: current-stage
   package, reviewer critique, researcher response, user gate.
9. Finalize, release, archive, or backtrack according to the Reviewing Gate
   decision.

The researcher agent leads the next action at each step. The user supplies
domain judgment and gate decisions, but should not need to remind the agent what
the workflow step is.

### Smoke-Test Mode

Use this to test the framework on a small public-data task.

1. Start from `templates/smoke-test-package.md`.
2. Select a small question and public dataset.
3. Use synthetic gates and label them as synthetic. Record decisions in the smoke-test package's Decision Notes table.
4. Download or read real usable data.
5. Run a minimal executable analysis.
6. Generate at least one table and one figure.
7. Produce one compact Reporting Package and one route-aware Review Package.
8. Record framework issues discovered by the run.

## Minimum Standards

For any mode:

- Candidate links do not count as data.
- The researcher agent must lead the step sequence and state the next concrete
  action or decision whenever it pauses.
- Do not pre-fill downstream stage packages before their upstream gates are
  approved, except as clearly empty scaffold templates.
- For real research, Planning should include a focused prior-work/novelty check
  before the full Planning Package is gate-ready, unless the user explicitly
  accepts a skip/defer rationale and revisit trigger.
- Each stage gate should happen after reviewer-agent critique and researcher-agent response, or after an explicit skipped-review rationale is recorded.
- Consequential in-stage choices are Tier 1 decision checkpoints: the researcher proposes, the user decides, and the decision goes in the decision log (`docs/decision-rights.md`).
- Reviewer blockers and majors that the researcher defers or rejects are escalated to the user.
- Gates are presented substantively: evidence paths, open objections in the reviewer's wording, alternatives, and consequences (`docs/coordination.md`).
- Each substantial run records workflow evaluation measures in `run-notes.md` (`docs/workflow-evaluation.md`).
- Data count only when usable under the acquisition success rule.
- Raw data host, official source, documentation source, version/access date, and license/access status should be recorded.
- Environment failures should trigger an environment repair decision.
- Claims should be tied to citations, artifacts, model outputs, or explicit limitations.
- New or uncertain workflows should usually start with a small Modeling demo before full-scale execution.
- Substantial runs should record `run_manifest.json`, `run_log.md`, and `run_summary.md`.
- Citation strictness should match the output type.

## Suggested First Test

Run a smoke test with a small public CSV dataset and organize it according to `docs/example-organization.md`.

## Suggested Prompt for a New Researcher Session

```text
Please run a complete smoke test of this repository's workflow.

Use `templates/smoke-test-package.md`.
Do not ask me for a research idea; choose a small public-data question yourself.
Lead the process step by step and state the current stage, next action, and stop
condition as you go. Run Planning -> Modeling -> Reporting -> Reviewing.
Download or read real usable data locally.
Generate a script, cleaned data, at least one table, and at least one figure.
If the environment fails, record an Environment Repair Decision and continue.
During Modeling, create a concrete Modeling Goal and usually begin with a small exploratory demo phase before scale-up. Do not stop after the first successful script, table, or figure; continue until the Model Package is ready for the Modeling Gate, or until a route decision is required.
Use synthetic gates and label them as synthetic.
Write the final summary in Chinese.
```
