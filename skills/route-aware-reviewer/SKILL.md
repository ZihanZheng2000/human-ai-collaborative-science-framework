---
name: route-aware-reviewer
description: Use during Review when a Reporting Package and its deliverables need upstream completeness checks, scientific, methodological, claim-strength, provenance, citation/source-support, output-quality, ethics, and readiness review with findings routed back to Planning, Modeling, Reporting, Reviewing, or termination.
---

# Route-Aware Reviewer

## Use When

- Reporting Gate is approved
- a manuscript, paper, slide deck, web page, dashboard, software package, or review packet needs structured review after Reporting
- an evidence package needs internal self-review or external-agent critique
- revision comments must be routed to the correct workflow stage

## Inputs

- Approved Planning Package
- Modeling Package
- Reporting Package
- reader-facing deliverables, if any
- artifacts and known limitations

## Procedure

1. Run upstream package completeness audit.
2. Check gate mode: real user gates, synthetic gates, or mixed gates.
3. Run Internal Self Review and fix local packaging or consistency issues when safe.
4. Audit evidence tier and claim strength, especially Abstract, Results, Discussion, and Conclusion.
5. Review method, data source identity, acquisition success, validation, environment repair decisions, and reproducibility.
6. Audit evidence packaging, source support, accepted citation threshold, and claim-by-claim evidence use when relevant.
7. Run reviewer-agent critique as critique-only when requested or useful. Use blind review mode by default in the Reviewing stage.
8. Audit accountability: every Tier 1/2 decision in the decision log has proposer, evidence, objections, and authorizer; flag nominal approvals, unresolved escalations, and locked analysis choices changed after results.
9. Review deliverable structure, venue/format fit, and output-mode requirements when relevant.
10. Check ethics, disclosure, responsible AI use, and human/expert review status.
11. Simulate adversarial objections and likely response demands.
12. Label severity and route each finding.
13. Check revision feasibility and completion criteria.
14. Run submission-readiness check only when applicable.
15. Produce a response-to-review summary and Review Package.

## Outputs

- Review Package
- upstream completeness audit
- claim-by-claim evidence and strength audit
- findings table
- internal self-review summary
- reviewer-agent critique triage, if used
- accountability audit and reconfiguration recommendations
- routed revision execution plan
- submission-readiness check, when applicable
- accepted limitations

## Guardrails

- Lead with substantive risks, not style nits.
- Every actionable issue needs a route.
- Every blocker or major issue needs a feasibility judgment and completion criterion.
- Do not demand Model addenda for issues fixable in Reporting.
- Do not mark a manuscript submission-ready if upstream completeness, citation integrity, disclosure, or submission-readiness checks have unresolved blockers.
- Do not treat synthetic gates as real user, domain-owner, or expert approval.
- Do not ignore mismatches between raw data hosts, official sources, documentation sources, and citation sources.
- Do not let a reviewer agent modify files unless the user explicitly requested that agent to edit.
- Every deferred or rejected blocker or major finding is escalated to the user; do not close it in the Review Package.
- Recommend a reconfiguration when findings show the Decision-Rights Map no longer fits.
