# Decision Log

Project: `live-penguins`

This is the shared research state for decisions. Record every Tier 1 decision
checkpoint, Tier 2 stage gate, escalation, reconfiguration, and informal review.
Tier 0 routine decisions go in the run log, not here. When the user's own words
are the authority for a decision, quote them and state what they authorized.
Record one decision per row; do not bundle several Tier 1 choices. Append rows; never delete
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
| D-1 | 2026-10-10 | Pre-Planning | tier-1 checkpoint | Setup from workflow.config.json: mode=step-by-step, reviewer=use, gates=synthetic | orchestrator | workflow.config.json |  |  | synthetic | synthetic | active |
| D-2 | 2026-10-10 | Planning | tier-1 checkpoint | Checkpoint: Research question and claim level: Approve as proposed: descriptive question and claim level (recommended). synthetic: recommended option taken | researcher | research/live-penguins/inbox/answered/CP-planning-1.md |  | None raised yet (reviewer pass has not run). Uncertainty: "differ" in the request could be read as asking for inference; the proposal reads it as descriptive per the user's explicit instruction. | synthetic | synthetic | active |
| D-3 | 2026-10-10 | Planning | tier-1 checkpoint | Checkpoint: Data source and acquisition success rule: Approve as proposed: raw CSV pinned by access date and SHA-256, with the four-part success rule (recommended). synthetic: recommended option taken | researcher | research/live-penguins/inbox/answered/CP-planning-2.md |  | None raised yet (reviewer pass has not run). Uncertainty: the file is pinned by hash at download time rather than by commit, so a later change on `main` would be detected only by hash mismatch, not prevented. | synthetic | synthetic | active |
| D-4 | 2026-10-10 | Planning | tier-1 checkpoint | Checkpoint: Inclusion/exclusion rule for missing sex or body mass: Approve as proposed: complete-case on sex and body mass, no other exclusions, dropped-row report (recommended). synthetic: recommended option taken | researcher | research/live-penguins/inbox/answered/CP-planning-3.md |  | None raised yet (reviewer pass has not run). Uncertainty: dropping missing-sex rows slightly changes the sample versus the full file; this is disclosed by the dropped-row report, but the user may prefer a different treatment. | synthetic | synthetic | active |
| D-5 | 2026-10-10 | Planning | tier-1 checkpoint | Checkpoint: Method family and metrics: Approve as proposed: descriptive table (n, mean, median, SD, range, differences) plus one by-sex plot per species, no inferential statistics (recommended). synthetic: recommended option taken | researcher | research/live-penguins/inbox/answered/CP-planning-4.md |  | None raised yet (reviewer pass has not run). Uncertainty: "differ" in the request could be read as wanting a test; the proposal follows the user's "descriptive and small" instruction and D-2. Minimum-per-cell n is unknown until data are viewed; if a cell is very small, Modeling reports it as such an | synthetic | synthetic | active |
| D-6 | 2026-10-10 | Planning | tier-1 checkpoint | Checkpoint: Decision-Rights Map: Approve the map as proposed (recommended). synthetic: recommended option taken | researcher | research/live-penguins/inbox/answered/CP-planning-5.md |  | None raised yet (reviewer has not run). Disclosures for your attention: (1) `workflow.config.json` assigns `codex` as researcher, but this run's researcher is Claude Code, and no override is logged; (2) the config says gates `real` while D-1 records `synthetic`. Neither is changed by this proposal. | synthetic | synthetic | active |
| D-7 | 2026-10-10 | Planning | tier-2 gate | Planning Gate: Approve for Modeling (recommended), stating your rulings on PR-1 and PR-2. synthetic: recommended option taken | researcher | research/live-penguins/inbox/answered/GATE-planning-r1.md |  | PR-1 (major): "Role and gate-mode assignment diverge from `workflow.config.json` with no user authorization. (a) Researcher is claude-code, config says codex. (b) D-1 records `gates=synthetic` \"from workflow.config.json\", but the config says `\"gates\": \"real\"`." Recommended: "User states whether the claude-code researcher and the synthetic gate mode are intended, and logs it as an override decision."; PR-2 (major): "Several consequential Planning choices have no decision-log entry or authorizer." Items: prior-work depth, venue calibration skipped, tool scan skipped, output route/venue/audience, future-work boundary, avoid-list, idea maturity. Recommended: "have the user confirm the User-Need Profile and Planning Depth table at the gate and log that." | synthetic | synthetic | active |

## Open Escalations

Findings or decisions waiting for user judgment. Remove a row only by adding the
resolving decision to the table above.

| Escalation | Source | Since | Blocking? | Resolving decision |
|---|---|---|---|---|
| PR-1 (major): "Role and gate-mode assignment diverge from `workflow.config.json` with no user authorization. (a) Researcher is claude-code, config says codex. (b) D-1 records `gates=synthetic` \"from workflow.config.json\", but the config says `\"gates\": \"real\"`." Recommended: "User states whether the claude-code researcher and the synthetic gate mode are intended, and logs it as an override decision." | reviewer PR-1 | 2026-10-10 | yes | pending Planning Gate ruling |
| PR-2 (major): "Several consequential Planning choices have no decision-log entry or authorizer." Items: prior-work depth, venue calibration skipped, tool scan skipped, output route/venue/audience, future-work boundary, avoid-list, idea maturity. Recommended: "have the user confirm the User-Need Profile and Planning Depth table at the gate and log that." | reviewer PR-2 | 2026-10-10 | yes | pending Planning Gate ruling |

## Deferred Items

| Item | Deferred by decision | Revisit trigger | Status |
|---|---|---|---|
| Venue calibration skipped (internal demo) | pending PR-2 ruling | before any external sharing | open |
| External tool scan skipped | pending PR-2 ruling | before any new tooling is proposed | open |
| Prior-work citations and CC0 licence recalled, not verified | pending PR-2 ruling | before any external sharing; licence re-recorded at acquisition (D-3) | open |
| Per-cell n and NA counts unknown | D-4/D-5 | at Modeling, after data acquisition | open |
| Reporting must state descriptive reading of "differ" in first paragraph (PR-8) | researcher (accepted suggestion) | before Reporting | open |
