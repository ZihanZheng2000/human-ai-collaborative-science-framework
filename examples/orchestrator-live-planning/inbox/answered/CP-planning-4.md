# Checkpoint: Method family and metrics

- Type: tier-1 checkpoint
- Stage: planning
- Raised by: researcher

## Decision needed

Choose the summary statistics and outputs used to compare male and female body
mass within each species. This is locked before any values are viewed. It fixes
what the Modeling stage computes and what the descriptive claim can cite.

## Proposal

Descriptive summary only, on the analysis set locked in D-4 (complete-case on
sex and `body_mass_g`):

- Table: for each species x sex, n, mean, median, SD, min, max (grams).
- Per species: mean difference (male minus female, grams) and median difference.
  Ratio (male mean / female mean) as a unit-free companion.
- Dropped-row report as specified in D-4.
- One figure: per species, side-by-side strip/box plot of body mass by sex
  (all points shown). No smoothing, no model fit.
- Explicitly not computed: p-values, confidence intervals, effect-size
  inference, regression, covariate adjustment, pooling across species, tests
  of any kind. Any wording in Reporting must stay at "in this dataset's
  sampled birds" (claim level of D-2).
- Software: Python standard library plus pandas and matplotlib in a
  project-scoped environment; fixed random seed is unnecessary (no randomness).
- Acceptance checks for Modeling: n per cell sums to the analysis-set size;
  recomputed means match a second independent computation (e.g. csv-module
  recomputation); figure plots every analysis-set row.

## Evidence

- `inbox/answered/CP-planning-1.md` (D-2): descriptive claim level.
- `inbox/answered/CP-planning-3.md` (D-4): analysis-set rule.
- `packages/planning-package.md`: Selected route table, row "method family and metrics".

## Alternatives

- Add a Welch t-test or bootstrap CI for the male-female difference: would
  support inference beyond the sample; exceeds the approved descriptive claim
  level (D-2) and would need a claim-level change as its own decision.
- Table only, no figure: smaller, but the figure is cheap and shows overlap
  between sexes that summary numbers hide.
- Add Cohen's d: it is a standardized descriptive number but invites
  inferential reading; not proposed.

## Open objections

None raised yet (reviewer pass has not run). Uncertainty: "differ" in the
request could be read as wanting a test; the proposal follows the user's
"descriptive and small" instruction and D-2. Minimum-per-cell n is unknown
until data are viewed; if a cell is very small, Modeling reports it as such and
does not change the rule.

## Reversibility

Easy to change now; no data have been viewed. After results are visible, adding
or swapping a statistic is a new decision that must state results were already seen.

## Options

1. Approve as proposed: descriptive table (n, mean, median, SD, range, differences) plus one by-sex plot per species, no inferential statistics (recommended)
2. Table only, no figure
3. Add an inferential step (test or CI); this requires revisiting the claim level of D-2
4. Ask for more checks before deciding

## Decision


Approve as proposed: descriptive table (n, mean, median, SD, range, differences) plus one by-sex plot per species, no inferential statistics (recommended)
synthetic: recommended option taken

_Recorded 2026-10-10 by orchestrator (synthetic gate)._

