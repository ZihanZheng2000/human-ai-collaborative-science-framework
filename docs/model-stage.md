# Model Stage Specification

## Purpose

The Model stage converts the Approved Plan Package into executable research artifacts: data acquisition, analysis code, experiment logs, figures, tables, and a validated result summary. It is one of the most important stages because it determines whether downstream outputs are grounded in reproducible analysis rather than persuasive prose.

Model is not just "write code and run it." It is an execution-controlled research loop with explicit acquisition success rules, preflight checks, bounded repair, preliminary finding checks, evidence deepening, validation, and stopping rules.

Existing auto-research systems often emphasize closed-loop generation, execution, evaluation, and revision. This stage uses that insight, but narrows it for a human-gated workflow: the goal is not to let the system keep searching until it finds an impressive result, and it is also not to stop as soon as one script runs. The goal is to produce a reproducible and reviewable evidence package that either supports the approved plan, exposes limitations, recommends bounded evidence-deepening analyses, or triggers a controlled backtrack.

## Core Principle

Model is **execution-grounded, evidence-building, and stop-aware**.

The system should generate and run code, but it should not optimize indefinitely or silently change the research question. It must know when to continue, when to repair, when to deepen the evidence, when to simplify, when to ask the user, and when to backtrack to Plan.

Model may use external packages, APIs, datasets, compute tools, or experiment frameworks selected in the Plan Package. These tools are execution aids, not substitutes for the modeling contract. Their inputs, versions, outputs, limitations, and verification status must be recorded in the Model Package.

The key control rule is:

> Do not deepen a result until the preliminary finding has passed a correctness check. Do not pass a correct result to Reporting until it has passed a sufficiency check, or until the user explicitly accepts a limited demo or preliminary claim.

## Exploratory Demo Phase

When the workflow, data source, extraction method, model, or agentic procedure is new or uncertain, Modeling should usually begin with a small exploratory demo instead of full-scale execution.

The demo should be large enough to test the whole workflow shape but small enough to inspect manually. It should run the same kind of steps expected in the full workflow, such as data collection, parsing, extraction, validation, synthesis, figure generation, or reporting preparation. The purpose is not to maximize coverage; it is to learn whether the method is useful, readable, traceable, and worth scaling.

The demo should produce:

- a scoped demo contract
- a small source/data sample
- executable scripts or repeatable manual-agent steps
- outputs that resemble the intended full-scale outputs
- a demo run log
- a short demo summary
- issues found and changes proposed before scale-up

The demo is part of Modeling. It does not have a separate gate. When the demo
finds issues, the researcher agent records them in the Model Package and either
continues within the approved contract, revises the Modeling approach, asks for
a user decision, backtracks to Planning, or terminates. The user decision, when
needed, is handled through the Modeling Gate or an ordinary user-decision point,
not a separate stage-level gate.

Demo-phase questions:

- Did the small sample exercise the complete intended workflow?
- Are the outputs useful enough to scale?
- Are provenance, logs, and validation sufficient?
- What needs to change before full-scale execution?
- Is the full-scale scope still appropriate?
- Is scale-up still justified within the Modeling contract?

If the demo supports scale-up, continue Modeling at the agreed scale using the
revised method and the same logging discipline. If the demo fails, revise the
demo, backtrack to Planning, or terminate.

## Modeling Goal Control

For agentic execution environments, the Model stage should begin with a concrete **Modeling Goal**. The goal is an execution-continuity device: it keeps the researcher agent working past the first runnable script, table, or figure. The gate remains the control device: it prevents the agent from moving into Reporting without approval.

Use this distinction:

- **Goal** keeps Model work moving until the Model Package is gate-ready or a route decision is required.
- **Modeling Gate** decides whether the Model Package can move downstream to Reporting.

A good Modeling Goal should state that the agent must continue until one of these conditions is met:

1. the Model Package is complete and ready for the Modeling Gate;
2. the approved modeling contract is impossible under current data, tools, permissions, or runtime;
3. a user/domain decision is required;
4. the workflow must backtrack to Plan;
5. the user explicitly pauses or stops.

Suggested goal text:

```text
Complete the Model stage for the approved plan. If the workflow is new or uncertain, first run a small exploratory demo phase before scaling up. Do not stop after the first successful script, table, or figure. Continue until usable data acquisition, preflight checks, data-quality audit, executable analysis, output validation, Preliminary Finding Brief, correctness check, sufficiency check, Model Critic Pass, Next Analysis Queue decision, claim-readiness notes, and the Model Package are ready for the Modeling Gate, or until a user decision, Plan backtrack, or termination condition is required.
```

## Internal Flow

1. Ingest the Approved Plan Package
2. Lock the modeling contract
3. Decide demo-first or full-scale execution mode
4. Prepare data and environment
5. Record run manifest, run log, data source identity, and acquisition criteria
6. Acquire data under explicit success rules
7. Run preflight checks
8. Audit data quality and clean data when justified
9. Generate a minimal executable analysis
10. Execute and capture logs
11. Validate outputs against the modeling contract
12. Write a Preliminary Finding Brief
13. Run an auto-research-inspired control pass
14. Diagnose failures, weak results, data-quality problems, or insufficient evidence
15. Repair environment, data, code, or evidence within bounded loops
16. Prepare reporting-support artifacts and claim-readiness notes
17. Run Modeling Reviewer critique and researcher-agent response when available and approved
18. Stop, escalate, or pass through the Modeling Gate
19. Output one Model Package

The final output should be one **Model Package**. It combines code location, data provenance, acquisition success counts, execution environment, run manifest, run log, validation checks, preliminary finding briefs, model state updates, critic notes, reviewer-agent critique when used, next-analysis queue, result tables, figure inventory, iteration history, evidence-deepening decisions, stopping decision, and handoff notes for Reporting.

## 1. Ingest the Approved Plan Package

The Model stage starts from the approved Plan output. It should not freely reinterpret the research question.

Required inputs:

- approved research question
- selected research-skill cards
- data plan
- method blueprint
- expected figures and tables
- assumptions and risks
- Model-stage acceptance rubric

If any required input is missing, the Model stage should request clarification or backtrack to Plan.

## 2. Lock the Modeling Contract

Before code generation, the system creates a short modeling contract.

The contract should specify:

- target analysis
- allowed data sources
- allowed external tools, packages, APIs, datasets, or compute services
- allowed transformations
- key variables
- expected outputs
- validation checks
- maximum iteration budget
- conditions that require user approval
- conditions that require Plan backtracking

This contract prevents the system from silently changing the study while trying to make the analysis work.

External tools should be rejected or paused when their outputs cannot be inspected, reproduced, cited, or validated enough for the accepted claim level.

## 3. Decide Demo-First or Full-Scale Execution Mode

Before data acquisition, decide whether this Modeling run starts as:

- **Demo-first**: a small sample that exercises the whole workflow before scale-up.
- **Full-scale**: appropriate when the method, source access, validation, and output structure are already stable.
- **Addendum**: a bounded follow-up requested by Reporting or Reviewing.

Record the mode in the Model Package. For demo-first runs, define the demo sample, success criteria, and scale-up decision criteria before executing.

## 4. Prepare Data and Environment

The system should prepare the execution environment before analysis.

Minimum requirements:

- data access path or download script
- raw data preservation
- cleaned data output path
- environment specification
- package installation notes
- project-scoped dependency file, such as `requirements.txt`, `pyproject.toml`, or `environment.yml`, when dependencies beyond the language standard library are used
- project-scoped runtime environment, such as a local `.venv`, Conda environment, container, or managed runtime, rather than unrecorded global-package installation
- random seed, if applicable
- directory structure for code, data, outputs, and logs

The default expectation is **one isolated environment per experiment or project**. The system should not silently install packages into a shared global interpreter. For Python projects, a local project environment such as `.venv` is usually sufficient; for heavier or cross-language studies, Conda, Docker, or another managed runtime may be more appropriate. The environment choice should match the accepted claim level and expected reproducibility burden.

The system should prefer the simplest reproducible environment that can run the approved method. For a tiny smoke test, standard-library code or a script plus `requirements.txt` may be enough. For a formal manuscript, benchmark, or analysis with nontrivial dependencies, the Model stage should record enough environment detail for a later rerun.

Recommended environment setup flow:

1. Check whether the project already declares an environment through `.venv`, `requirements.txt`, `pyproject.toml`, `environment.yml`, `Dockerfile`, notebook metadata, or a package manager lock file.
2. If no suitable environment exists and dependencies beyond the standard library are needed, create a project-scoped environment for this experiment rather than using global packages.
3. Install declared dependencies into that project-scoped environment.
4. If execution reveals a missing dependency that is consistent with the modeling contract, install it into the project-scoped environment, update the dependency file or environment notes, and log the action.
5. If the missing dependency is heavy, unstable, unavailable, changes the method, or creates licensing/runtime risk, record an Environment Repair Decision before installing, simplifying, containerizing, changing runtime, reducing scope, asking the user, or backtracking.
6. After a successful run, record the actual interpreter/runtime, dependency file path, important package versions, and any lock/freeze output that is practical for the project.

Dependency installation is allowed when it is necessary for the approved analysis, but it must be local to the experiment and traceable. "Install whatever is missing" is acceptable only inside the project environment, only when the dependency fits the modeling contract, and only when the installation is recorded. Unrecorded global installation should be treated as a reproducibility risk.

If the first executable run fails because of missing packages, incompatible versions, unavailable binaries, shell differences, or hardware limits, the system should make an explicit environment repair decision before continuing. Acceptable repair paths include installing dependencies, switching to a simpler implementation, using a container or managed runtime, changing hardware, reducing scope, or backtracking to Plan. The decision and outcome should be logged.

## 5. Record Run Manifest, Data Source Identity, and Acquisition Criteria

For substantial runs, create or update:

- `<run_dir>/run_manifest.json`
- `<run_dir>/run_log.md`
- `<run_dir>/run_summary.md`

The run manifest should record run id, date, scope, mode, approved package inputs, data/source targets, scripts or tools used, output locations, validation status, and gate status. The run log should record chronological actions, Tier 0 decisions, failures, and repairs; Tier 1 and Tier 2 decisions and user approvals go in the project `decision-log.md`. The run summary should explain what this run proved in human-readable form.

Before acquisition, Model should confirm the source identity fields from the Plan Package:

- exact raw data host or query endpoint
- official data source or owner
- documentation source
- citation source
- data version, release date, query date, or access date
- license, terms of use, or access constraints

If these differ, Model should preserve the distinction. A documentation page for one version, mirror, package, or derivative dataset should not be treated as proof of the exact raw data used unless that relationship is verified.

## 6. Acquire Data Under Explicit Success Rules

Data acquisition should be success-driven. The Model stage should not count a candidate source, metadata record, URL, search result, or inaccessible file as usable data.

A data item counts only when it satisfies the acquisition success rule in the Approved Plan Package. For example:

- a table counts only when it has been downloaded or queried and required variables can be read;
- a document counts only when the full text, required section, or required metadata can be extracted;
- an API record counts only when the response contains the fields needed by the analysis;
- an image, PDF, or media file counts only when the required content can be accessed or converted without unacceptable quality loss.

The acquisition log should record:

- target count
- attempted count
- successfully retrieved count
- usable count
- failed count
- failure reasons
- source replacements or fallbacks
- stop rule

If the preferred data sources cannot produce enough usable data, the system should apply the approved fallback, ask the user, or backtrack to Plan. It should not quietly lower the data standard or pretend that candidate links are data.

## 7. Run Preflight Checks

Preflight checks happen before substantive modeling.

Examples:

- data file exists or API query succeeds
- required columns exist
- units are known
- date ranges and geographic coverage match the plan
- missingness is measurable
- sample size is plausible
- identifiers are unique when required
- outcome and predictor variables are not obviously malformed
- licensing or access constraints are not violated
- modality-specific extraction works, such as text extraction, table parsing, image access, or API field retrieval

If preflight fails, the system should not proceed to modeling just to produce an output. It should repair data access, request user input, or backtrack.

## 8. Audit Data Quality and Clean Data

Data quality is part of modeling, not a side issue. Poor data can produce weak, misleading, or unstable results even when the code is correct.

The system should run a data-quality audit before the primary analysis.

Data-quality checks may include:

- missingness by variable and subgroup
- duplicated rows or identifiers
- impossible or out-of-range values
- inconsistent units
- inconsistent date formats or time intervals
- unexpected category labels
- extreme outliers
- sample imbalance
- coverage gaps across time, geography, or population groups
- mismatch between metadata and observed data
- changes in definitions across releases or data vintages

Cleaning is allowed, but it must be explicit and justified. The system should preserve raw data, write cleaned data separately, and log every cleaning decision.

Allowed cleaning actions:

- standardize column names
- parse dates and numeric fields
- harmonize units when the conversion is documented
- remove exact duplicate records
- recode obvious category variants
- filter to the approved sample frame
- flag or winsorize outliers only when justified by the approved method or domain norms
- impute missing values only when the method and assumptions are explicitly approved

Not allowed without user approval:

- dropping large portions of data
- excluding inconvenient outliers
- changing the sample frame
- changing variable definitions
- imputing key variables in a way that affects the main claim
- mixing data vintages without logging release dates

If data quality is too poor to support the approved plan, the system should stop and ask whether to revise the data plan, simplify the method, backtrack to Plan, or terminate.

## 9. Generate a Minimal Executable Analysis

The first code pass should be minimal and faithful.

It should prioritize:

- loading data
- cleaning only what the plan requires
- computing descriptive statistics
- running the primary method
- producing the expected core table or figure
- saving outputs in predictable locations

The first pass should not include excessive model variants, decorative figures, or speculative extensions.

## 10. Execute and Capture Logs

Every run should produce an execution record.

The record should include:

- command or notebook cell sequence
- start and end time
- data version or query timestamp
- code version or file path
- warnings and errors
- generated artifacts
- changed assumptions

The goal is to make failures useful rather than hidden.

## 11. Validate Outputs

Validation checks whether the outputs satisfy the modeling contract.

Validation should include:

- code runs from a fresh session
- required figures and tables exist
- outputs match expected schema
- variable transformations are logged
- values fall in plausible ranges
- no obvious leakage or post-treatment control is introduced
- robustness checks required by the skill card are either completed or explicitly deferred
- limitations are recorded for Reporting deliverables

Validation is not the same as getting statistically significant results. A null or weak result can be a valid result if the analysis is correct and interpretable.

## 12. Write a Preliminary Finding Brief

After the first executable result, the system should produce a short Preliminary Finding Brief before deciding whether to stop, deepen, repair, or ask the user.

The brief should include:

- initial finding: what the first result appears to show
- correctness check: whether the data, variables, transformations, method, and figures match the approved plan
- confidence level: high, medium, or low
- sufficiency check: whether the correct result is enough to support the approved research purpose and intended manuscript
- missing evidence: what is still needed for Results, Discussion, robustness, validation, or interpretation
- next action: pass, repair, deepen evidence, ask user, backtrack, or terminate

Correctness must be checked before sufficiency. If the result may be wrong, the system should enter a repair, data audit, or method fidelity loop before drawing substantive conclusions. If the result is technically correct but its field meaning, adequacy, or acceptable claim level is uncertain, the system should ask the user rather than over-deciding.

## 13. Run an Auto-Research-Inspired Control Pass

The Model stage may borrow control mechanisms from auto-research systems, but it remains contract-bounded and human-gated. It should not autonomously change topics, chase significance, substitute methods, or escalate claims without approval.

After each Preliminary Finding Brief, the system should update three control artifacts.

### Model State Tracker

The state tracker records where the Model stage is and what the next valid action is.

Suggested states:

- `data_acquisition`
- `preflight`
- `minimal_result_ready`
- `correctness_check`
- `correctness_failed`
- `correctness_passed`
- `evidence_sufficiency_check`
- `evidence_insufficient`
- `evidence_deepening`
- `user_decision_needed`
- `model_gate_ready`
- `backtrack_to_plan`
- `terminate`

The state tracker should prevent two common failures: stopping just because one output exists, and continuing without a clear reason.

### Model Critic Pass

The critic pass stress-tests the preliminary finding before the system commits to additional analysis or downstream packaging.

It should ask:

- Does the result actually answer the approved research question?
- Does the figure or table support the claim being considered?
- Are variables, filters, units, labels, and sample definitions correct?
- Is there an untested alternative explanation?
- Is a baseline, control, robustness check, validation set, or sensitivity analysis missing?
- Is there leakage, circularity, overfitting, or metric-method overlap?
- Is the result merely technically valid but too thin to be a research contribution?
- Would the current claim be overstated in a manuscript?

The critic pass should produce a short decision: pass to sufficiency check, repair, deepen evidence, ask user, backtrack, or terminate.

### Next Analysis Queue

If a result is correct but insufficient, the system should build a next-analysis queue instead of vaguely saying that more work is needed.

Each queue item should include:

- proposed analysis, figure, table, robustness check, validation, or diagnostic
- purpose
- claim or uncertainty addressed
- expected value for Results or Discussion
- expected cost or runtime
- priority
- whether it stays inside the modeling contract
- whether user approval is required

The system should execute high-priority queue items within the approved evidence-deepening budget. It should stop or ask the user when the queue requires new data, new methods, domain judgment, or claim escalation.

## 14. Diagnose Failures, Weak Results, Data-Quality Problems, or Insufficient Evidence

Failures, weak results, and thin evidence should be classified before the system tries to fix or extend them. A weak result may be scientifically valid, but it may also be caused by poor data quality, wrong transformations, incomplete coverage, or a mismatch between the data and the approved method.

| Failure type | Example | Default response |
|---|---|---|
| Execution error | package missing, syntax error, API timeout | repair within budget |
| Data error | missing required variable, wrong unit, incomplete coverage | repair if possible, otherwise ask user or backtrack |
| Data-quality problem | high missingness, duplicate identifiers, unstable units, extreme outliers | clean if justified, otherwise ask user or backtrack |
| Contract violation | code changes method or data beyond approved plan | stop and restore contract |
| Validity risk | leakage, confounding, invalid comparison group | ask user or backtrack to Plan |
| Weak result | effect is small, noisy, or null | report honestly; do not optimize for significance |
| Thin evidence | one result or figure is correct but not enough for a manuscript | propose bounded evidence deepening |
| User/domain uncertainty | result is technically valid but field interpretation is uncertain | ask user or domain reviewer |
| Scope creep | system adds unapproved analyses | remove or request user approval |

## 15. Repair, Cleaning, Optimization, Environment Repair, and Evidence-Deepening Loops

The Model stage may iterate, but each loop must have a reason and a budget. Repair, cleaning, optimization, and evidence deepening are different actions and should not be collapsed into one generic "try again" loop.

### Repair Loop

Used when code or data access fails.

Allowed actions:

- fix syntax or package issues
- correct file paths
- adjust API calls
- repair parsing or type conversions
- add missing preflight checks

Stop when:

- the same error recurs after the repair budget
- the fix requires changing the approved data or method
- required data is unavailable
- user input is needed

### Data Cleaning Loop

Used when the data-quality audit finds issues that can be corrected without changing the approved research question or method.

Allowed actions:

- standardize formats
- remove exact duplicates
- apply documented unit conversions
- recode obvious category variants
- filter to the approved sample frame
- flag outliers for reporting
- apply approved missing-data handling

Stop when:

- cleaning would change the sample frame or main variables
- cleaning choices materially affect the main claim
- missingness or coverage gaps make the method invalid
- user approval is required

### Method Fidelity Loop

Used when the code runs but does not match the approved method.

Allowed actions:

- align variables with the method blueprint
- restore required controls or grouping variables
- correct transformations
- implement required robustness checks

Stop when:

- the method requires unavailable data
- assumptions are violated
- the approved method no longer fits the data

### Result Quality Loop

Used only after the primary analysis is correct.

Allowed actions:

- improve figure readability
- add approved robustness checks
- test sensitivity to reasonable parameter choices
- compare approved baselines
- improve table formatting

Not allowed:

- trying many unplanned specifications to chase significance
- silently dropping inconvenient observations
- changing the research question to fit the data
- adding unapproved methods that alter the claim

Stop when:

- required outputs are valid and interpretable
- additional iterations produce no substantive improvement
- optimization would change the approved plan
- the iteration budget is reached

### Evidence-Deepening Loop

Used when a preliminary finding is technically correct but not yet enough to support the approved research purpose, Results section, or Discussion.

Allowed actions:

- add descriptive context needed to interpret the main result
- add approved baselines or control comparisons
- run required robustness or sensitivity checks
- add subgroup, heterogeneity, or error analysis when justified by the plan
- add validation or placebo checks when they test the method rather than chase a desired conclusion
- add diagnostic figures or tables that clarify limitations, coverage, or alternative explanations
- refine figures so the evidence narrative is visible

Not allowed:

- changing the research question to match the first result
- trying many unplanned specifications to find a stronger or significant result
- adding analyses with no claim they support
- silently changing the data source, sample frame, or validation target
- continuing indefinitely after the evidence is sufficient for the accepted claim level

Each evidence-deepening iteration should state:

- what claim or uncertainty it addresses
- why the current evidence is insufficient
- what analysis or figure will be added
- whether it stays within the modeling contract
- what stopping condition applies

Stop when:

- the evidence is sufficient for the approved claim level
- remaining gaps require new data, new methods, or user/domain judgment
- additional analyses would be speculative or unapproved
- the iteration budget is reached

## 16. Prepare Reporting-Support Artifacts and Claim-Readiness Notes

The Model stage should not write the final report, review, manuscript, slide deck, web page, or software package, but it should prepare the evidence needed for downstream Reporting. Many weak AI-generated outputs become short reports because the next stage receives only tables and figures, not enough interpretation scaffolding.

After the primary analysis is validated, the system should produce reporting-support artifacts:

- main empirical findings, including null or weak results
- result surprises or contradictions relative to the Plan-stage literature
- robustness checks completed and not completed
- data-quality issues that affect interpretation
- assumptions that held, failed, or remain uncertain
- plausible alternative explanations
- limitations that must be acknowledged
- figures or tables that are essential for argumentation
- candidate follow-up analyses that would strengthen the Discussion
- claim-readiness notes: what can be claimed strongly, what must be framed as preliminary, what cannot be claimed, and what needs user or expert judgment

This is not the final Discussion. It is a structured handoff so that Reporting can build evidence-bound deliverables rather than merely stitch together outputs.

### Downstream Figures and Additional Analyses

Figures or analyses that are based on data, model outputs, robustness checks, sensitivity analysis, or additional experiments belong to Model. Reporting or Reviewing may identify that an additional comparison, diagnostic figure, robustness table, or exploratory visualization is needed, but downstream stages should not silently create new empirical evidence.

If a downstream stage needs additional empirical support, it should create a **Model Addendum Request**. The request should specify:

- the discussion claim or uncertainty that needs support
- the requested figure, table, robustness check, or analysis
- whether the request stays within the approved modeling contract
- whether user approval is required

The Model stage then performs a bounded addendum run, validates the new artifact, updates the Model Package, and returns to the requesting stage. Conceptual diagrams, workflow figures, and non-empirical explanatory visuals may be created in Reporting, but empirical figures must be produced or validated by Model.

## Decision Checkpoints During Modeling

These Modeling decisions are Tier 1 checkpoints (see `decision-rights.md`) and
go in `decision-log.md`:

- the locked modeling contract, including labels, exclusion rules, evaluation
  metrics, model search space, and validation split — locked **before** the
  results they affect are visible;
- acceptance of acquired data and any exclusions;
- any change to a locked choice after results were seen (the entry must say
  results were visible);
- interpretation of results that makes causal, domain, or operational claims;
- scale-up from exploratory demo to full study.

Repairs, retries, cleaning within the locked rules, and code structure are
Tier 0: the researcher decides and records them in the run log. If a Tier 0
repair would change a Tier 1 choice, stop and raise a checkpoint.

## 17. Modeling Reviewer Pass

Before the Modeling Gate, a reviewer agent should critique the Model Package when
a separate reviewer agent is available and approved. Use
`reviewer-agents/modeling-reviewer-agent.md`.

The reviewer should inspect:

- whether the approved modeling contract was followed
- whether acquisition success, provenance, and source identity are explicit
- whether code, environment, run logs, and outputs are reproducible enough for the accepted claim level
- whether validation checks match the method and claims
- whether figures and tables trace back to data or model artifacts
- whether weak, null, or failed results are preserved honestly
- whether Reporting can use the outputs without reconstructing scattered context

The researcher agent must respond to reviewer findings before the Modeling Gate.
Findings should be accepted and fixed, accepted but deferred, rejected with
reason, or escalated for user decision. Deferred or rejected blocker and major
findings are escalated to the user automatically.

## 18. Stopping Rules

The Model stage should stop under any of these conditions:

- **Pass**: required outputs satisfy the modeling contract.
- **Pass with limitations**: outputs are valid and sufficient for a limited claim, but limitations must be carried into Reporting.
- **Deepen evidence**: preliminary results are correct but not yet sufficient for the approved research purpose.
- **Needs user decision**: multiple valid paths exist or a domain judgment is required.
- **Model gate ready**: the state tracker, critic pass, and sufficiency check all support handoff.
- **Backtrack to Plan**: data, method, or assumptions no longer support the approved plan.
- **Terminate**: the task is infeasible under available data, time, or ethical constraints.

Stopping is not failure. In an AI-native research workflow, stopping is part of scientific control. However, the system should not stop merely because it produced one table, one figure, or one executable result. It should stop when the result is correct and sufficient for the accepted claim level, or when further progress requires user judgment, new data, or a backtrack.

## 19. Modeling Gate

After execution and validation, the workflow must pause for a Modeling Gate. The user should approve, edit, reject, request another bounded iteration, or backtrack the Model Package. The system should not automatically pass results into Reporting just because code ran successfully.

Gate questions:

- Did the code run?
- Are the data sources and transformations acceptable?
- Were data-quality problems handled appropriately?
- Are cleaning decisions acceptable?
- Do the results answer the approved research question?
- Did preliminary findings pass correctness checks?
- Did the model critic identify unresolved blocking issues?
- Is the next-analysis queue empty, completed, or intentionally deferred?
- Are the current results sufficient for the user's intended product, or only for a demo/preliminary claim?
- Are figures and tables interpretable?
- Are assumptions and limitations explicit?
- Is there enough reporting-support evidence for Reporting to package the results transparently?
- Did the system stay within the approved plan?
- Were locked analysis choices kept, or were changes after seeing results logged?
- Do you uphold or overturn the researcher's response to each escalated finding?
- Should Reporting begin, should Model iterate, or should Plan be revised?

Possible decisions:

- approve for Reporting
- approve with limitations
- edit required tables, figures, labels, or cleaning notes
- request discussion-support addendum
- request evidence deepening
- revise Model within the approved contract
- backtrack to Plan
- terminate

## 20. Model Package

The Model stage outputs one compact Model Package.

Use the template in `../templates/model-package.md`.
