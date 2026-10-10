# Checkpoint: Inclusion/exclusion rule for missing sex or body mass

- Type: tier-1 checkpoint
- Stage: planning
- Raised by: researcher

## Decision needed

Choose how rows with missing `sex` or `body_mass_g` are handled. This is locked
before any values are viewed. Method family and metrics are a separate later
checkpoint (CP-planning-4).

## Proposal

- Analysis set: rows where `body_mass_g` is non-missing and `sex` is exactly
  `male` or `female`. No other exclusions: no outlier removal, no filtering by
  island or year, no imputation.
- Report, in the Modeling package, the number of rows dropped per species and the
  reason (missing sex, missing mass, both), plus n per species x sex in the
  analysis set, so the exclusion is visible rather than silent.
- Rows with missing `sex` are not recoverable by inference (no guessing sex from
  other measurements).
- Recalled, not verified in this session: the public file has a small number of
  NA values in these two columns (a handful of rows). Actual counts will be
  reported at Modeling; the rule does not depend on them.

## Evidence

- `notes/prior-work-scan.md`: header and row count only; no values inspected.
- `inbox/answered/CP-planning-2.md` (D-3): acquisition success rule.
- `docs/plan-stage.md`: exclusions must be locked before results are visible.

## Alternatives

- Keep missing-sex rows in an "unknown" group: not needed for a male vs female
  question and adds a third group with little meaning.
- Impute sex or mass: goes beyond "descriptive and small"; rejected.
- Also trim outliers: a post-hoc-style choice that can change the description;
  not proposed.

## Open objections

None raised yet (reviewer pass has not run). Uncertainty: dropping missing-sex
rows slightly changes the sample versus the full file; this is disclosed by the
dropped-row report, but the user may prefer a different treatment.

## Reversibility

Easy to change now; no data have been downloaded or viewed. After results are
visible, any change is a new decision that must say results were already seen.

## Options

1. Approve as proposed: complete-case on sex and body mass, no other exclusions, dropped-row report (recommended)
2. Keep missing-sex rows as a separate "unknown" group in the report
3. Ask for more checks before deciding

## Decision



Approve as proposed: complete-case on sex and body mass, no other exclusions, dropped-row report (recommended)
synthetic: recommended option taken

_Recorded 2026-10-10 by orchestrator (synthetic gate)._

