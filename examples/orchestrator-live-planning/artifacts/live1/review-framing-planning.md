# Review Framing (planning)

## Summary of Work Done

Planning package for a small descriptive comparison of male vs female body mass within each Palmer penguins species. Question/claim level (D-2), data source and acquisition rule (D-3), exclusions (D-4), method/metrics (D-5) and Decision-Rights Map (D-6) were each approved at a Tier 1 checkpoint (synthetic approvals). A light prior-work scan was done from recalled knowledge; no data values were viewed (header and row count only). Every package sentence was checked against the D-2 claim level: the package makes no claims about results, only plans.

## Known Risks or Open Questions

- Citations in the prior-work scan and the CC0 licence are recalled, not re-verified.
- Researcher agent (Claude Code) differs from `roles` (codex) with no logged override; config gates `real` vs D-1 `synthetic`.
- "differ" could be read as wanting inference; the package fixes a descriptive level (D-2, D-5).
- Per-cell n unknown until Modeling.
- All approvals are synthetic, so none reflects real user judgment.

## Specific Questions for the Reviewer

- Are the acceptance checks in the Method Blueprint sufficient for a descriptive claim?
- Is skipping venue calibration and the external tool scan acceptable for an internal demo?
- Does anything in the package exceed the D-2 claim level or lack a decision-log authorizer?
