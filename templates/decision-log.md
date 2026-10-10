# Decision Log

Project: `<research-name>`

This is the shared research state for decisions. Record every Tier 1 decision
checkpoint, Tier 2 stage gate, escalation, reconfiguration, and informal review.
Tier 0 routine decisions go in the run log, not here. Append rows; never delete
them. When a decision is replaced, set its status to `superseded by D-<n>`.

See `docs/decision-rights.md` for tiers and `docs/coordination.md` for the loop.

## Current Decision-Rights Map

Link to the authoritative map (normally the Planning Package) and list any
reconfigurations since it was approved.

- map location: `packages/planning-package.md#decision-rights-map`
- reconfigurations since approval: none / D-<n>, D-<n>

## Decisions

| ID | Date | Stage | Type | Decision | Proposed by | Evidence / artifacts | Alternatives considered | Open objections at decision time | Authorized by | Approval quality | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| D-1 |  | Planning | tier-1 checkpoint / tier-2 gate / escalation / reconfiguration / informal review / skip-defer |  | researcher / reviewer / user / expert |  |  | none / finding IDs and summary | user / expert / researcher (Tier 0 only) / synthetic | substantive / nominal: what was missing / synthetic | active / reopened / superseded by D-n / deferred until <trigger> |

## Open Escalations

Findings or decisions waiting for user judgment. Remove a row only by adding the
resolving decision to the table above.

| Escalation | Source | Since | Blocking? | Resolving decision |
|---|---|---|---|---|
|  | reviewer finding ID / researcher / user |  | yes / no |  |

## Deferred Items

| Item | Deferred by decision | Revisit trigger | Status |
|---|---|---|---|
|  | D-<n> | before scale-up / before Reporting / before release / other | open / revisited in D-<n> |
