# Checkpoint: Data source and acquisition success rule

- Type: tier-1 checkpoint
- Stage: planning
- Raised by: researcher

## Decision needed

Confirm which copy of the Palmer penguins data is used, how it is pinned, and
what counts as successful acquisition. This is locked before any values are
viewed. Handling of missing sex/mass rows and the metrics are separate later
checkpoints (CP-planning-3, CP-planning-4).

## Proposal

- Source: the `palmerpenguins` package CSV `inst/extdata/penguins.csv`, raw URL
  `https://raw.githubusercontent.com/allisonhorst/palmerpenguins/main/inst/extdata/penguins.csv`.
  Original data: Gorman, Williams & Fraser (2014), PLoS ONE 9(3):e90081.
  Licence: CC0 (per package DESCRIPTION v0.1.1; to be re-confirmed at acquisition).
- Pinning: the `main` branch can change, and I could not resolve a commit SHA in
  this session (GitHub API access was not enabled). Instead, at acquisition in
  Modeling, record the access date and the SHA-256 of the downloaded file, and
  store the raw file unmodified in `artifacts/input/` (raw kept separate from cleaned data).
- Acquisition success rule (all must hold, else stop and report, no silent substitution):
  1. HTTP 200 and a parseable CSV;
  2. header is exactly `species,island,bill_length_mm,bill_depth_mm,flipper_length_mm,body_mass_g,sex,year`;
  3. 344 data rows (matches the row count seen in the feasibility check);
  4. `species` has exactly Adelie, Chinstrap, Gentoo.
  Candidate links alone do not count as data.

## Evidence

- `notes/prior-work-scan.md`: data reachability check (HTTP 200, header, 344 rows; no values inspected).
- `packages/planning-package.md`: Feasibility and route sections.

## Alternatives

- Install the R/Python `palmerpenguins` package version-pinned: stronger pin, but adds tooling beyond "small".
- Use a seaborn/other mirror copy: copies may differ in cleaning; not preferred.

## Open objections

None raised yet (reviewer pass has not run). Uncertainty: the file is pinned by hash at download time rather than by commit, so a later change on `main` would be detected only by hash mismatch, not prevented.

## Reversibility

Easy to change now; no data values have been viewed or downloaded.

## Options

1. Approve as proposed: raw CSV pinned by access date and SHA-256, with the four-part success rule (recommended)
2. Use a version-pinned package install instead
3. Ask for more checks before deciding

## Decision


Approve as proposed: raw CSV pinned by access date and SHA-256, with the four-part success rule (recommended)
synthetic: recommended option taken

_Recorded 2026-10-10 by orchestrator (synthetic gate)._

