# Reporting / Packaging Stage Specification

## Purpose

The Reporting / Output Packaging stage converts approved Modeling outputs into
one compact, inspectable package and the reader-facing deliverables needed for
the project. A paper, report, slide deck, dashboard, web page, software package,
technical appendix, decision brief, or review packet is a Reporting output mode.
Manuscript and prose writing are handled as Reporting output modes.

This stage should answer:

- What was done?
- What evidence was produced?
- What can be claimed from that evidence?
- What remains uncertain, weak, missing, or blocked?
- What should a reviewer or user inspect next?

Reporting may create reader-facing summaries, technical appendices, evidence
tables, dashboards, demo reports, manuscripts, slide decks, web pages, software
documentation, or release packages. It should not introduce new empirical
results, run unapproved analyses, or inflate findings into claims. If a missing
figure, data check, robustness run, or extraction pass is needed, Reporting
should request a Modeling addendum.

## Core Principle

Reporting is **evidence-bound output production**.

The system should organize outputs from Planning and Modeling so that the user,
reviewer, or next agent can inspect the work without reconstructing it from
scattered files. It should preserve uncertainty and provenance. It can
synthesize, summarize, compare evidence, and shape a deliverable argument, but
it must keep a clear boundary between validated results, preliminary
observations, interpretation, and open questions.

## Internal Flow

1. Ingest the approved Planning Package and Modeling Package
2. Confirm that required Modeling artifacts exist and are traceable
3. Identify the intended output mode: demo report, technical appendix, decision brief, dashboard, manuscript/paper, slides, web page, software package, or review packet
4. Build an evidence inventory
5. Build a claim-readiness summary
6. Summarize methods, data/source provenance, and execution logs
7. Design the output architecture for the selected mode
8. Build or update the claim-evidence map and source-support checks
9. Summarize key findings and uncertainties
10. Package figures, tables, source lists, artifact paths, and deliverables
11. Identify missing evidence and route addendum requests
12. Run the Reporting Reviewer critique and researcher-agent response
13. Produce one Reporting Package
14. Pause at the Reporting Gate

## 1. Ingest Approved Inputs

Reporting starts from:

- Approved Planning Package
- Modeling Package
- Modeling Gate decision, or a clearly labeled limited/demo decision
- validated data/source inventory
- run manifest, run log, and run summary when available
- scripts, notebooks, extracted data, tables, figures, or model outputs
- known limitations, failures, and unresolved questions

If Modeling has not produced enough evidence for the intended report mode, Reporting should label the output as limited and route missing items back to Modeling.

## 2. Select Output Mode

The output mode should match the user's current need:

| Mode | Use when | Output character |
|---|---|---|
| Demo report | A small sample proves the workflow shape | short, concrete, transparent about scope |
| Technical appendix | The user needs auditability | detailed artifact paths, methods, logs, provenance |
| Decision brief | The user needs to choose next steps | concise findings, options, risks, recommendations |
| Review packet | The next step is formal Review | claim-readiness, gaps, routed issues |
| Dashboard or table package | The result is exploratory or operational | inspectable tables/charts with provenance |
| Manuscript or paper | The output is an article, preprint, thesis chapter, or formal paper | argument architecture, citation integrity, venue fit, claim-evidence grounding |
| Slide deck | The output is a talk, class presentation, pitch, or review meeting | concise narrative, readable figures, speaker notes when needed |
| Web page or interactive report | The output is public-facing, exploratory, or shareable online | source traceability, caveats, interaction checks, accessibility basics |
| Software package or tool release | The output is code, a reusable workflow, dataset utility, or skill | README, examples, reproducibility, license, API/CLI docs, tests or validation notes |

Reporting may create more than one reader-facing deliverable, but it should
still produce one Reporting Package that summarizes all deliverables and their
status.

## 3. Evidence Inventory

Reporting should list the main evidence objects and where they live:

- raw inputs and official/source locations
- processed text, data, or extracted records
- scripts or notebooks used to transform data
- tables, figures, dashboards, or JSON outputs
- logs and manifests
- prompts, model settings, or agent skills when material
- validation checks and known failures

The inventory should distinguish candidate material from usable evidence. A link, search result, or downloaded file is not automatically usable evidence unless it passed the acquisition or validation rule in the approved plan.

## 4. Claim-Readiness Summary

Reporting should translate Modeling outputs into claim-readiness, not polished manuscript prose.

Each major finding should be labeled:

- **Supported**: backed by validated artifacts and enough provenance for the current output type
- **Preliminary**: useful but limited by sample size, validation, source coverage, or method maturity
- **Uncertain**: plausible but requires more data, review, or analysis
- **Unsupported**: should not be used as a claim yet
- **Not evaluated**: outside the completed work

For each finding, record:

- evidence source or artifact path
- support strength
- limitation or caveat
- whether it can be used in Review
- whether it needs Modeling, Planning, or user input

## 5. Findings and Synthesis

Reporting can synthesize across artifacts when the synthesis is grounded in the Modeling outputs. Useful synthesis types include:

- common findings across sources or runs
- complementary evidence that explains different parts of the same problem
- apparent contradictions that may be resolvable by context
- true conflicts that require user or domain review
- operational tensions, tradeoffs, or decision constraints
- evidence gaps and uncertainties
- next analysis needs, when requested

Synthesis should cite or point to the supporting artifacts. It should not make a broad novelty, policy, scientific, or operational claim that the evidence package cannot support.

## 6. Output Architecture and Deliverable Checks

Reporting should design the deliverable around the selected output mode rather
than merely listing what happened.

For manuscript or paper outputs, Reporting should include:

- contribution framing after seeing the modeled evidence
- manuscript architecture and section-level argument plan
- citation-grounded claim map
- citation sufficiency and source-support check
- venue or format calibration when a target is known
- abstract, conclusion, limitation, disclosure, and availability checks
- report-like writing check, so the paper argues from evidence rather than only recounting workflow steps

For slide outputs, Reporting should include:

- audience and occasion
- slide narrative order
- figure readability and caption checks
- speaker-note or handout needs
- claim-strength and caveat placement

For web or dashboard outputs, Reporting should include:

- user path through the evidence
- chart, filter, and interaction checks
- provenance and caveat placement
- accessibility and mobile/readability basics when relevant
- public-sharing risk review

For software or tool outputs, Reporting should include:

- README or usage guide
- install/run instructions
- API, CLI, or workflow examples
- license, data, and dependency notes
- test, smoke-test, or validation status
- known limitations and support boundary

Conceptual diagrams, workflow figures, method schematics, graphical abstracts,
and explanatory tables may be created in Reporting when they explain approved
evidence or method structure. Empirical figures, robustness tables, diagnostic
plots, sensitivity analyses, and data-derived tables must come from Modeling or
a documented Modeling addendum.

## 7. Addendum Requests

Reporting should request a Modeling addendum when it discovers missing empirical evidence:

- a required source was not collected or parsed
- extraction coverage is visibly incomplete
- deduplication or validation is insufficient
- a table, figure, metric, or robustness check is missing
- an output cannot be traced to raw material
- a claim would require more analysis than the approved Modeling run performed

Reporting should request a Planning addendum when the issue is about scope, research question, source strategy, target output, or claim level.

## 8. Reporting Reviewer Pass

Before the user Reporting Gate, a reviewer agent should critique the Reporting
Package and deliverables. The reviewer agent should be separate from the
researcher agent when available and approved. Use
`reviewer-agents/reporting-reviewer-agent.md`.

The reviewer should inspect:

- whether deliverables match the selected output mode
- whether claims are supported by artifacts, citations, or accepted limitations
- whether evidence, provenance, and caveats are visible to the intended reader
- whether citation and source-support checks match the output type
- whether missing empirical evidence is routed to Modeling instead of patched in Reporting
- whether the deliverable is ready for Reviewing or needs local Reporting revision

The researcher agent must respond to reviewer findings before the Reporting
Gate. Findings should be accepted and fixed, accepted but deferred, rejected
with reason, or escalated for user decision. Deferred or rejected blocker and
major findings are escalated to the user automatically.

The claim level used in the deliverable must not exceed the level authorized in
the decision log. Raising it is a Tier 1 checkpoint; if it needs new evidence,
route it to Modeling.

## 9. Reporting Gate

After packaging, pause for a Reporting Gate.

Gate questions:

- Is the evidence package and selected deliverable understandable without reconstructing scattered files?
- Are source/data provenance and artifact paths traceable?
- Are validated findings separated from preliminary or unsupported observations?
- Are uncertainties, failures, and limitations visible?
- Does the deliverable match its output mode, such as paper, report, slides, web, dashboard, software, or review packet?
- Have Reporting Reviewer findings been fixed, deferred, rejected with reason, or escalated for user decision?
- Are any missing evidence items routed back to Modeling or Planning?
- Does the deliverable stay within the authorized claim level?
- Do you uphold or overturn the researcher's response to each escalated finding?
- Is the package ready for Review, or should Reporting revise locally?
- Does the user approve moving to Review?

Possible decisions:

- approve for Review
- approve as a limited/demo package
- revise Reporting
- request Modeling addendum
- request Planning addendum
- terminate or archive

## 10. Reporting Package

The Reporting stage outputs one compact Reporting Package.

Use the template in `../templates/reporting-package.md`.
