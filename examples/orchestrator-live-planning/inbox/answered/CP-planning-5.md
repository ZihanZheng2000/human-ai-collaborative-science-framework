# Checkpoint: Decision-Rights Map

- Type: tier-1 checkpoint
- Stage: planning
- Raised by: researcher

## Decision needed

Confirm who proposes, executes, and authorizes each class of decision in this
project, and which analysis choices are locked before results are visible.
`docs/plan-stage.md` requires the user to confirm this map before the Planning
package goes to the reviewer.

## Proposal

Use the default map from `docs/decision-rights.md` unchanged in structure, with
these project adjustments (full table in `packages/planning-package.md#decision-rights-map`):

- Researcher proposes and executes; the user authorizes every Tier 1 class and Tier 2 gate.
- Analysis execution and repair inside the locked contract are Tier 0 (researcher); a repair that would change a Tier 1 choice is escalated.
- Locked before results: data source and success rule (D-3), exclusion rule (D-4), metrics and plot (D-5). There is no model or validation split.
- Reviewer rights: advisory + escalation (default). Blind review for the Reviewing stage only (per config).
- No domain expert assigned. Interpretation beyond the descriptive claim level (biological or causal reading) is out of scope and would need a Tier 1 decision.
- No tier is raised: nothing here has privacy, safety, or public-release cost; output is an internal demo.

## Evidence

- `docs/decision-rights.md`: default map this copies.
- `packages/planning-package.md`: proposed map, locked-choice list, and the disclosed risks below.
- `decision-log.md`: D-2..D-5, the locked choices.

## Alternatives

- Give the researcher Tier 0 authority over plot styling only and nothing more: already covered by Tier 0 "analysis execution".
- Assign a domain expert for interpretation: not proposed; interpretation is not part of the claim level.
- Raise exclusion or metric changes to Tier 2: unnecessary for a small internal trial.

## Open objections

None raised yet (reviewer has not run). Disclosures for your attention:
(1) `workflow.config.json` assigns `codex` as researcher, but this run's researcher is Claude Code, and no override is logged; (2) the config says gates `real` while D-1 records `synthetic`. Neither is changed by this proposal. Either could be confirmed or corrected as a separate Tier 1 decision about reviewer/role assignment.

## Reversibility

Easy. Later changes to the map are reconfigurations recorded in the decision log. No results are visible.

## Options

1. Approve the map as proposed (recommended)
2. Approve with changes (state them in the notes)
3. Ask for more checks before deciding

## Decision


Approve the map as proposed (recommended)
synthetic: recommended option taken

_Recorded 2026-10-10 by orchestrator (synthetic gate)._

