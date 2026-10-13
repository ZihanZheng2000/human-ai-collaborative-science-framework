# Shared Research State: Decision-Relevant State Contract (Proposal)

**Status:** design proposal v0.1; not implemented by the orchestrator. Complements [Organization Contract](organization-contract.md), [Coordination](coordination.md), and [Design Rationale](design-rationale.md).

## Purpose

Shared research state is a **reconstructable representation of the inquiry**, not a transcript, a large memory dump, or a guarantee that recorded claims are correct. It allows a returning scientist, incoming agent, or authorized reviewer to recover the current scientific position, open uncertainty, consequential choices, and next action with links to inspectable evidence. It must also preserve disagreement and the possibility of selective, blind access.

## Two complementary views, not competing sources of truth

1. **Current State View** — a compact, revisable index answering what is believed *now*, on what evidence, with which uncertainties and responsibilities.
2. **Historical Evidence Trail** — append-only/superseded decision records, contributions, claims, versioned artifacts, review findings, and execution traces answering how the state emerged.

The current view is a **derived navigation layer**, not an authority that can override the decision log, source artifacts, or original critique. A summary–source conflict must be flagged and resolved; never silently rewrite the underlying record.

## Minimum Current State View

| Section | Minimum content | Linkage and guardrail |
| --- | --- | --- |
| Research question and scope | current question, claim level, scope exclusions | authoritative approved plan/decision ID; distinguish proposed vs approved |
| Current claims and findings | claim ID, short statement, support level: proposed / preliminary / supported within scope / contested / superseded | evidence/artifact references; validation and uncertainty; avoid automatic truth claims |
| Key assumptions and methods | active methodological commitments, datasets, unresolved limitations | versioned evidence and decisions, especially post-result method changes |
| Open disagreements | objection ID, original objection or precise reference, competing interpretations, owner, next check, revisit trigger | do not erase dismissed/deferred objections; preserve reviewer's own words in source |
| Activity and contribution map | active activity IDs, actor IDs and substantive contribution references | see Organization Contract; no false attribution of human decisions |
| Authority and decisions | decision IDs, active authorized scope, pending approvals, explicit reconfigurations | human approval only from authoritative decision record |
| Next scientific actions | proposed next step, why, responsible actor, prerequisite, authorization needed | never treat recommendation as authorization |
| Freshness and coverage | update date/order, responsible updater, missing files or unverified links | mark incomplete/stale summary; no claim of full reconstruction without checking |

The view should privilege **three to five decision-relevant items per section when possible**, while linking to full records. Do not omit critical blockers to meet a length target.

### Claim support labels are workflow status, not epistemic proof

“Supported within scope” means the cited evidence and checks documented so far support a bounded claim. It is not an assertion of universal scientific correctness. A reviewer or new evidence may reopen it.

## Update triggers and precedence

Update the current view on: approved or superseded consequential decisions; material new evidence; substantive claim revision; new or resolved blocker; reconfiguration; stage pause/handoff; changed next action. Routine command logs do not automatically need a summary change.

Precedence when records conflict:
1. **Primary evidence, reproducible outputs, and original critique** determine what source material actually says.
2. **Orchestrator-owned human authorization log** determines who authorized an action (without asserting scientific truth).
3. **Versioned scientific claims and stage packages** communicate currently maintained interpretations.
4. **Current State View** indexes and summarizes these sources, and must disclose detected conflict.

These are **different kinds of authority**, not a universal linear ranking: evidence does not authorize an action; approval does not establish validity.

A state update should record: what changed, which source IDs justify the change, whether approval was required, unresolved objections, and the new next action. Never convert a proposal into an approved state without an authorized decision.

## Selective access and blind review

A shared reconstructable state **does not mean identical visibility for everyone at all times**. Design access profiles:
- **Researcher/owner:** complete authorized state for active work.
- **Standard reviewer:** claims, evidence, relevant methodological context, objections as permitted by review protocol.
- **Blind reviewer (first pass):** review object and allowed raw evidence **without researcher framing, private recommendations, decision rationales, or summary fields likely to contaminate independence**.
- **Post-blind reviewer:** receives additional framing after first independent findings are sealed.

A “blind-safe summary” must be generated or checked from explicitly allowed source fields; merely hiding a filename is insufficient. Test side channels through packages, README, log paths, and artifact names. This document specifies intended policy, not present access-control guarantees.

## Small example: drought-event analysis

- **Research question:** Do operating rules differ in drought periods?
- **Current finding F-2 (preliminary):** release–storage relationship appears different in selected drought windows; observational association only.
- **Evidence:** artifact E-5 (event windows), E-6 (regression diagnostics); missing robustness across alternative event definitions.
- **Open objection O-3:** reviewer disputes whether seasonality explains the difference; unresolved, owner researcher, revisit before claims are strengthened.
- **Contribution:** C-8 (human requests seasonality control), C-9 (AI proposes matched-season analysis).
- **Decision:** D-4 authorizes the bounded follow-up analysis, not a causal drought-effect claim.
- **Next action:** A-7 run matched-season comparison; requires no new gate if within D-4 scope.

This example is illustrative, not an actual study result.

## Compatibility and staged adoption

The existing `README.md` status block, `decision-log.md`, stage packages, inbox, and run logs remain authoritative for their respective functions. **Do not add mandatory machine-readable fields or create new persistent project files in existing runs yet.**

**Proposed pilot:** a manually maintained `notes/current-research-state.md` (or equivalent summary) as an **optional** view linked from the existing README status block. Only after usability tests should it be written automatically or made required.

## Acceptance tests before implementation

1. **Cold restart:** a new actor reconstructs current claim, supporting evidence, open dispute, authority, and next action without reading entire logs.
2. **No evidence laundering:** an unsupported or contested claim does not become “confirmed” through repeated summaries.
3. **State-change consistency:** a superseded decision and its dependent claims are updated or flagged, without deleting history.
4. **Blind-review isolation:** reviewer first-pass context excludes researcher framing even when current-state summaries exist.
5. **Cost and focus:** compare reconstruction correctness/time and missed blockers against reading unstructured history; count human summary maintenance effort.
6. **False approvals:** no synthetic or model-authored entry appears as a real human authorization.

These are proposed tests; no execution or effectiveness result is claimed.
