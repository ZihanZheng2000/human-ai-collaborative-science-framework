# Review Stage Specification

## Purpose

The Review stage stress-tests the approved Planning, Modeling, and Reporting
packages before the workflow moves into finalization, release, submission, or
archive. It is not primarily an editorial prose review. Its job is to find
scientific, methodological, provenance, evidence, routing, deliverable-quality,
and claim-strength problems while the work is still easy to correct.

Review turns the workflow into a controlled revision loop. Findings should be
actionable and routed back to the correct stage: Planning for question, scope,
novelty, or feasibility issues; Modeling for data, code, extraction,
validation, robustness, or empirical evidence issues; Reporting for packaging,
traceability, deliverable argument, citation/source support, format, or
human-inspection issues; and Terminate when the project is not defensible under
current constraints.

## Core Principle

Review is **adversarial, actionable, route-aware, and evidence-aware**.

The default Review stage has two layers:

1. **Researcher-agent self review**: the researcher agent reviews the upstream work, identifies issues, and may fix issues that clearly belong to the current agent and do not require user approval.
2. **Reviewer-agent critique**: a separate reviewer agent may critique the whole package, but by default it should only raise findings and should not modify files. Findings return to the researcher agent for triage, user discussion when needed, and implementation.

An external agent should modify files only when the user explicitly asks for that agent to perform edits.

## Internal Flow

1. Ingest approved Planning, Modeling, and Reporting packages
2. Check package completeness and route consistency
3. Run Internal Self Review
4. Fix clearly local issues or record routed findings
5. Run reviewer-agent critique when available and approved
6. Consolidate findings, severity labels, and routed actions
7. Decide whether the work is ready for finalization/release, needs revision/addendum, or should backtrack
8. Produce one Review Package
9. Pause at the Reviewing Gate

## 1. Ingest Review Materials

Required inputs:

- Approved Planning Package
- Modeling Package
- Reporting Package
- reader-facing deliverables listed by Reporting
- data/source provenance inventory
- run manifest, run log, and run summary when available
- figures, tables, extracted data, scripts, prompts, or model outputs
- known limitations and addendum requests

Optional inputs:

- external tool logs or reviewer-agent critique
- user/domain-owner comments

If a required upstream package is missing or not approved, Review should flag the workflow as not ready for final review. It may still perform a limited diagnostic review, but it should not label the work ready for finalization or external sharing.

## 2. Package Completeness and Route Audit

Review should check whether upstream packages agree with each other.

Checks:

- gate mode and approval status are explicit
- Planning records idea maturity, planning depth, research purpose, target output, feasibility, and prior-work/novelty status
- Modeling records the contract, acquisition success counts, source identity, run logs, environment decisions, validation, critic pass, and claim-readiness notes
- Reporting records deliverables, evidence inventory, provenance, findings, synthesis notes, limitations, and addendum requests
- candidate links, search results, or metadata are not counted as usable data
- raw data host, official source, documentation source, and citation source are distinguished when different
- validated findings are separated from preliminary or unsupported observations
- downstream stages did not create unvalidated empirical evidence
- unresolved limitations are visible rather than softened into stronger claims
- every major problem is routed to Planning, Modeling, Reporting, Review, or Terminate

## 3. Internal Self Review

The researcher agent should review its own work before asking the user to trust the package.

Internal Self Review should look for:

- missing files or broken artifact paths
- inconsistent stage names, package references, or gate decisions
- unsupported claims in the Reporting Package
- evidence that does not trace back to source artifacts
- validation or provenance gaps
- overclaiming relative to the Modeling Package
- addendum requests that should have been resolved before Review
- package sections that are too vague for the next stage

The researcher agent may directly fix local packaging, labeling, cross-reference, or consistency issues. It should not silently change research question, data source, method, claim level, or scope.

## 4. Reviewer-Agent Critique

Reviewer-agent critique should be used when a separate reviewer agent is
available and approved. It reduces blind spots before the user Reviewing Gate.
Use `reviewer-agents/reviewing-reviewer-agent.md` when reviewing the Review
Package itself.

Default rule:

- The reviewer agent critiques and may escalate (see `decision-rights.md#reviewer-rights`).
- It does not modify files.
- The Reviewing stage uses **blind** review mode by default: the reviewer reads
  the packages, deliverables, and artifacts and writes independent findings
  before reading the researcher's summary and questions (see
  `coordination.md#reviewer-information-modes`).
- It returns findings with severity, evidence, and route.
- The researcher agent consolidates the findings and performs revisions unless the user explicitly asks the reviewer agent to edit.

The external review prompt should ask the agent to inspect:

- scientific validity
- method and reproducibility
- source/data provenance
- claim strength
- evidence gaps
- route correctness
- whether the package is ready for finalization, release, submission, archive, or another routed cycle

## 5. Review Criteria

Core criteria:

- research question clarity
- contribution, novelty, or output value
- fit between question, data, method, and claims
- evidence support for findings
- claim strength and evidence-tier alignment
- reproducibility and execution traceability
- source/data provenance
- data quality and validation
- limitation honesty
- reporting/package inspectability
- readiness for finalization, release, submission, or archive
- ethical, licensing, disclosure, or responsible-AI concerns
- accountability: every consequential decision is reconstructable from the
  decision log (proposer, evidence, objections, authorizer); nominal approvals
  and unresolved escalations are visible

For manuscript or paper outputs, add:

- manuscript argument
- citation validity
- venue fit
- disclosure and submission readiness
- prose clarity and structure

## 6. Severity Labels

Each finding should receive a severity label:

- **Blocker**: the workflow should not move forward until fixed.
- **Major**: substantial revision is needed, but the project remains viable.
- **Minor**: local correction or clarification.
- **Suggestion**: optional improvement.
- **Accepted limitation**: issue is real but can be disclosed rather than fixed.

## 7. Routing Rules

Every actionable finding should be routed.

| Route | Used when |
|---|---|
| Planning | research question, scope, prior-work/novelty basis, target output, feasibility, source strategy |
| Modeling | data, code, extraction, validation, robustness, empirical figures/tables, reproducibility |
| Reporting | package clarity, evidence inventory, provenance summaries, finding labels, deliverable organization, manuscript or slide argument, citation placement, venue or format compliance, limitation language |
| Review | reviewer disagreement, severity calibration, acceptance of limitations |
| Terminate | project is infeasible, noncompliant, or misleading under current constraints |
| User decision | a judgment only the user or a domain expert should make; also every deferred or rejected blocker/major |

If findings show that the current Decision-Rights Map no longer fits (for
example, repeated domain errors in one decision class), recommend a
reconfiguration in addition to routing the finding.

## 8. Revision Execution Plan

The Review Package should include a prioritized action plan:

- finding ID
- severity
- route
- required action
- evidence or artifact needed
- owner or user decision needed
- feasibility
- completion criterion
- whether the item blocks Reviewing Gate approval

This plan should be directly usable as the next task queue.

## 9. Reviewing Gate

After review and revision planning, pause for a Reviewing Gate.

Gate questions:

- Are all Blocker issues resolved or routed?
- Are Major issues feasible to fix?
- Does the evidence package remain scientifically defensible?
- Are provenance, reproducibility, and validation risks acceptable?
- Are claim-strength risks acceptable?
- Is the work ready for finalization/release, another Modeling/Reporting cycle, Planning revision, archive, or termination?
- If reviewer-agent critique was used, were its findings triaged and either fixed, routed, or explicitly rejected?
- Do you uphold or overturn the researcher's response to each escalated finding?
- Are there nominal upstream approvals that should be re-done substantively before release?

Possible decisions:

- approve for finalization/release/submission/archive
- approve as limited/demo output
- revise Reporting
- request Modeling addendum
- backtrack to Planning
- run another reviewer-agent critique
- reconfigure the Decision-Rights Map and re-check affected decisions
- accept limitations and proceed
- terminate

The Review Package recommendation must be one of the concrete gate options,
each with its consequence. "Approve limited" or "archive" must state what the
output may and may not be used for while escalations remain open.

### Workflow Evaluation Record

Before writing the Reviewing-stage review request, fill the Workflow Evaluation
section of the project's
`run-notes.md` (see `workflow-evaluation.md`) so the reviewer can check it; update it after the gate: claim-support audit, trajectory-
changing findings, decision traceability, nominal vs substantive approvals,
escalations, and human effort. This evaluates the collaboration itself, not
only the deliverable.

## 10. Review Package

The Review stage outputs one compact Review Package.

Use the template in `../templates/review-package.md`.
