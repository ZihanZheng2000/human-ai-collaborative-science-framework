# Decision Rights and Authority

This document specifies **decision authority within the organization layer**.
The four workflow stages are management boundaries, not the definition of scientific
activities. This document distinguishes who performs work from who may authorize
consequential decisions. See [Organization Data Contract](organization-contract.md)
for a proposed stage-independent activity/actor/contribution representation; it
is not yet implemented by the orchestrator.

Three things are kept separate:

| Dimension | Question | Example |
|---|---|---|
| Activity | What scientific work has to be done? | choose a dataset, define an event label, critique a claim |
| Actor | Who performs it? | researcher agent, reviewer agent, user, domain expert, tool |
| Authority | Who may turn the result into a decision that changes the project? | user approves, researcher may proceed, reviewer may escalate |

Performing an activity does not confer authority over it. The researcher agent
may find, compare, and recommend datasets; that does not authorize it to commit
the project to one.

## Actors

| Actor | Default activities | Default authority |
|---|---|---|
| User (human owner) | sets purpose, supplies domain judgment and materials, makes gate and checkpoint decisions | approves, redirects, stops, reassigns, changes decision rights |
| Domain expert (optional) | supplies tacit, local, or disciplinary judgment the user or agents lack | advisory unless the user delegates a specific decision class to them |
| Researcher agent | proposes, searches, executes, drafts packages, triages critique | executes Tier 0 decisions; proposes everything else |
| Reviewer agent | critiques packages and artifacts independently | advisory and escalation rights (see below); never approves, never edits by default |
| Tools (code, APIs, models) | retrieve, compute, fit, render | none; outputs are evidence, not decisions |

Role labels such as "researcher" or "reviewer" describe a default bundle of
activities. The project's Decision-Rights Map records what each actor actually
does and may decide.

## Action Types

Authority is action-specific. The framework uses these action types:

| Action | Meaning |
|---|---|
| propose | put a candidate decision forward with evidence and alternatives |
| execute | carry out work within an already-authorized scope |
| critique | challenge a proposal, artifact, or claim |
| escalate | force a decision to a higher authority instead of letting it be settled locally |
| approve | authorize a proposal so it changes the project |
| redirect / stop | change or halt the inquiry |
| reconfigure | change who performs or authorizes a class of decisions |

## Decision Tiers

Not every decision deserves a gate. Decisions are classified by consequence and
reversibility, and the accountability loop is scaled to match
(see [coordination.md](coordination.md)).

| Tier | What it covers | Who decides | Record |
|---|---|---|---|
| **Tier 0 — routine** | reversible, low-cost, within an already-approved scope: file layout, script structure, retries, plot styling, parameter choices explicitly delegated by the contract | researcher agent | run log; decision log only if it affects a package |
| **Tier 1 — decision checkpoint** | consequential or hard-to-reverse decisions inside a stage: research question wording, claim level, dataset or source choice, event/label definitions, exclusion rules, method family, model search space and metrics, skipping or deferring a planned check, changing workflow mode | user, after the researcher proposes with evidence and alternatives | decision log entry, required |
| **Tier 2 — stage gate** | moving between stages, backtracking, finalizing, releasing, terminating | user, after the full maker-checker loop | decision log entry + gate section of the stage package |

Rules:

- When in doubt between two tiers, use the higher one.
- A Tier 1 decision does not need a reviewer pass, but it does need the
  researcher's proposal, the evidence, the alternatives considered, and the
  user's decision recorded together.
- Tier 1 decisions that fix analysis choices (labels, exclusions, metrics,
  model search space, validation split) must be made **before** the researcher
  sees the results they would affect. Changing them afterward is a new Tier 1
  decision and must say that results were already visible.
- In **Auto-until-needed** mode, the researcher may batch several Tier 1
  proposals into one checkpoint, but it still may not decide them alone.
- In **Step-by-step discussion** mode, each Tier 1 decision is its own
  checkpoint.

## Default Decision-Rights Map

Every real project copies this map into its Planning Package and adjusts it.
Later changes to the map are reconfigurations (see
[coordination.md](coordination.md#adaptive-reconfiguration)).

| Decision class | Performed by | Authority | Tier |
|---|---|---|---|
| research purpose, research question, claim level | researcher proposes | user | 1 (2 at gate) |
| prior-work / novelty scan depth, skip or defer | researcher proposes | user | 1 |
| data source and acquisition success rule | researcher proposes | user | 1 |
| labels, event definitions, inclusion/exclusion rules | researcher proposes | user (domain expert if assigned) | 1 |
| method family, model search space, evaluation metrics | researcher proposes | user | 1 |
| analysis execution within the locked contract | researcher | researcher | 0 |
| repair, cleaning, retries within the locked contract | researcher | researcher; escalate if it changes a Tier 1 choice | 0 |
| critique of a package | reviewer | advisory; may escalate | — |
| response to critique (fix / defer / reject) | researcher | researcher for minor and suggestion; user for rejected or deferred blocker and major | 1 |
| interpretation of results, causal or domain claims | researcher proposes | user (domain expert if assigned) | 1 |
| output route, venue, audience | researcher proposes | user | 1 |
| stage transition, backtrack, finalize, release, terminate | researcher proposes | user | 2 |
| workflow mode, reviewer strategy, reviewer assignment | researcher or user proposes | user | 1 |
| changes to this map | anyone proposes | user | 1 |

## Reviewer Rights

The reviewer agent's rights are explicit:

- **Advisory**: every finding is input to the researcher's response.
- **Escalation**: a finding the reviewer marks `blocker` or `major` cannot be
  closed by the researcher alone unless it is accepted and fixed. If the
  researcher rejects it or defers it, the finding is escalated to the user at
  the next checkpoint or gate, with the reviewer's original wording. The
  reviewer may also set `Route: user decision` on any finding to force escalation.
- **No approval, no veto**: the reviewer cannot approve a gate or stop the
  project. A blocker is a strong recommendation, not a veto; only the user can
  pass a gate with an open blocker, and doing so must be recorded as an
  accepted risk.
- **No edits by default**: the reviewer edits files only when the user
  explicitly authorizes a specific edit.

A project may strengthen these rights (for example, giving a domain-expert
reviewer blocking rights on label definitions). That is a change to the
Decision-Rights Map.

## Who Records Human Decisions

In orchestrated runs ([orchestration.md](orchestration.md)) the orchestrator
writes every decision-log row whose authority is a person, and computes its
approval quality from the request the person saw. Agents propose and record
their own proposals, mitigations, disclosures, and escalations, but never a
human approval. In manual runs the researcher records the user's decision and
the reviewer checks it.

## What the Researcher Agent May Not Do Alone

- approve its own checkpoint or gate
- close a reviewer blocker or major by rejecting or deferring it
- change a Tier 1 choice after seeing results without saying so
- change the research question, data source, method, sample frame, or claim
  level
- change the Decision-Rights Map, workflow mode, or reviewer strategy
- present a decision as user-approved when the user only agreed with a topic or
  direction

## Substantive versus Nominal Approval

A human approval counts as substantive only when the user could actually
exercise judgment. A checkpoint or gate is **substantive** when the user was
shown:

1. the proposal and what it changes;
2. the evidence and the artifact paths to inspect it;
3. the alternatives considered and why they were not chosen;
4. open objections, including escalated reviewer findings, in their original
   wording;
5. what approval will cause, and how it could be reversed;
6. the explicit option to ask for more checks, override, or escalate further.

If any of these were missing, the decision log must mark the approval as
**nominal** and say what was missing. A nominal approval is still a decision,
but the downstream packages and reviewers should treat it as weaker evidence of
human oversight.

Synthetic gates (framework tests) are always labeled `synthetic` and are never
substantive human approval.
