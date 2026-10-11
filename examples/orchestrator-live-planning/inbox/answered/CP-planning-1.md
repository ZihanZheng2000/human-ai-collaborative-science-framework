# Checkpoint: Research question and claim level

- Type: tier-1 checkpoint
- Stage: planning
- Raised by: researcher

## Decision needed

Confirm the research question and the maximum claim level for this project, so
that later choices (exclusions, metrics, method) are locked against a fixed target.

## Proposal

Research question: "Within each of the three species (Adelie, Chinstrap, Gentoo), how do the body-mass distributions of male and female penguins in the Palmer penguins dataset compare?"

Claim level: **descriptive only**. Allowed statements: per species x sex counts, mean, median, SD, range, and the male-minus-female difference in mean, all about the birds in this dataset. Not allowed: significance tests, p-values, confidence intervals interpreted as population claims, causal or biological-mechanism explanations, comparisons across species as a headline, or novelty claims. This follows the user's wording "Keep it descriptive and small."

Follow-up checkpoints (one per unit, step-by-step mode) will cover: data source pinning and acquisition success rule, handling of rows with missing sex/mass, and method/metrics, all before any values are viewed.

## Evidence

- `research/live-penguins/README.md`: the user's verbatim request.
- `research/live-penguins/notes/prior-work-scan.md`: light scan; question is well studied, so no novelty is claimed. Citations are recalled and not re-verified.
- `research/live-penguins/packages/planning-package.md`: draft skeleton with the proposed route.
- Data reachability: public CSV returned HTTP 200, 344 rows; no values inspected.

## Alternatives

- Descriptive plus a simple test (e.g. Welch t-test per species) and effect sizes: stronger statement, but goes beyond "descriptive and small".
- Include other traits (flipper length, bill): wider scope than requested.

## Open objections

None raised yet (reviewer pass has not run). Uncertainty: "differ" in the request could be read as asking for inference; the proposal reads it as descriptive per the user's explicit instruction.

## Reversibility

Easy to change now; no data values have been viewed. Widening the claim level later would be a new Tier 1 decision.

## Options

1. Approve as proposed: descriptive question and claim level (recommended)
2. Allow a simple test and CI per species in addition (state the widened claim level in the Decision notes)
3. Ask for more checks before deciding

## Decision



Approve as proposed: descriptive question and claim level (recommended)
synthetic: recommended option taken

_Recorded 2026-10-10 by orchestrator (synthetic gate)._

