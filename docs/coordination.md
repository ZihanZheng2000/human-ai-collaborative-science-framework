# Coordination: Research State, Accountability Loop, and Reconfiguration

This document is the **coordination layer** of the framework. The Decision-Rights
Map ([decision-rights.md](decision-rights.md)) is a snapshot of who does what
and who decides. Coordination is how that arrangement is kept coherent, tested,
and changed as the project evolves. It relies on three mechanisms:

1. a **shared research state** that anyone can use to reconstruct where the
   project stands and why;
2. a **scientific accountability loop** that consequential contributions pass
   through before they change the project;
3. **adaptive reconfiguration** when the current arrangement stops fitting the
   work.

## Shared Research State

The [Shared Research State Contract](shared-research-state-contract.md) proposes a
**decision-relevant current view** over the existing historical evidence trail.
It is a design specification, **not an implemented orchestrator feature**.
The current summary must preserve open disagreements and link to original evidence;
a concise summary must never substitute for original critique or human authorization.


Every real project keeps its state in three places with distinct jobs:

| File | Job |
|---|---|
| `research/<name>/README.md` | **Status block**: current stage, active package, last decision, open escalations, next action. Updated whenever the researcher stops. |
| `research/<name>/decision-log.md` | **Decision log**: one row per Tier 1 or Tier 2 decision, reconfiguration, escalation, and informal review. Append-only; superseded decisions are marked, not deleted. Template: `templates/decision-log.md`. |
| `research/<name>/packages/*.md` | **Stage packages**: compact handoffs that cite decision IDs instead of repeating the history. |
| `research/<name>/inbox/` | **Pending and answered requests** for human decisions (checkpoints, gates, tasks). In orchestrated runs this is how agents reach the user ([orchestration.md](orchestration.md)). |

Run logs (`<run_dir>/run_log.md`) remain the chronological execution
record. The decision log is not an execution log: it records only decisions,
who proposed them, what evidence and objections existed, who authorized them,
and whether the authorization was substantive.

A new agent session, a reviewer, or a returning user should be able to answer
from these files alone:

- What does the project currently claim, and at what level?
- What has been authorized, by whom, and on what evidence?
- What is disputed or deferred, and what would reopen it?
- Who currently performs and authorizes each decision class?

**Selective independence.** Shared state does not mean every actor sees
everything at once. A reviewer may be given claims and evidence without the
researcher's rationale (see blind review below). The state is shared for
reconstruction and audit, not to force identical context on every critic.

## Scientific Accountability Loop

**Theory alignment (2026-10-13):** The companion paper now defines accountability
as the broader, iterative advancement of scientific work through proposal,
execution, examination, revision/resolution, and shared-state updates. See
[Accountability Contract](accountability-contract.md). The decision-review sequence
below is an **operational subprotocol for consequential decisions**, not a
mandatory scientific sequence for every activity. The current orchestrator
still implements its existing review and gate behavior.

Consequential decisions should not bypass appropriate review and authorization.
The existing decision-review subprotocol is:

```text
propose -> critique -> respond -> authorize -> act -> record
               ^          |
               |          v
               +-- deferred: collect evidence, re-critique
                          |
                          v
                     escalate (decision moves to a higher authority)
```

Critique and authorization are different functions. Critique asks whether a
contribution is epistemically adequate. Authorization decides whether it is
allowed to change the project. The actor best placed to judge a technical point
may not be the one authorized to act on it.

Scientific inquiry may iterate or branch without a new gate when it stays within
approved scope. Critique can occur before, during, or after an experiment;
scientific resolution and authorization remain distinct. A failed attempt or
ordinary disagreement is not by itself grounds for organizational reconfiguration.

### Scaling the decision-review subprotocol by tier

| Tier | Propose | Critique | Respond | Authorize | Record |
|---|---|---|---|---|---|
| 0 | implicit | researcher self-check | — | researcher | run log |
| 1 | researcher states proposal, evidence, alternatives | optional informal review; researcher states known objections | researcher | user | decision log |
| 2 | stage package | reviewer agent (or recorded skip) | response-to-reviewer section | user, at a substantive gate | decision log + package gate section |

### Response options

The researcher classifies each finding as:

| Response | Meaning | Who may close it |
|---|---|---|
| accepted and fixed | change made; cite what changed | researcher |
| accepted but deferred | real, but waits for evidence or a later stage; must name the revisit trigger | researcher for minor/suggestion; **user** for blocker/major |
| rejected with reason | finding judged wrong or out of scope | researcher for minor/suggestion; **user** for blocker/major |
| needs user decision | escalated directly | user |

Blocker and major findings that are rejected or deferred are **automatically
escalated**: the gate presentation must quote the reviewer's finding, the
researcher's reason, and ask the user to uphold or overturn the response.

A deferred finding is not resolved. Any later decision that depends on it must
re-check it before authorization.

### Reviewer information modes

The review request declares one of two modes:

| Mode | What the reviewer sees first | Use when |
|---|---|---|
| standard | review request (summary, known risks, specific questions), then the package | Planning, Modeling, Reporting by default |
| blind | the package and raw artifacts only; the researcher's summary, known risks, and questions are read **after** an independent findings pass | Reviewing stage by default; any gate where the researcher's framing could hide a problem (novelty claims, causal claims, contested interpretations) |

In blind mode, the critique file has two finding blocks: independent findings
(written before reading the researcher's framing) and follow-up findings
(written after). Comparing them shows whether the researcher's framing steered
the review.

### Informal early-look reviews

A reviewer may be asked to look at work in progress before the formal pass.
Early looks are useful for catching weak spots while the work is still cheap to
change. Record each one in the decision log as `informal review`, triage its
findings in a note, and do not count it as the formal reviewer pass for the
gate.

### Substantive gate presentation

Every Tier 2 gate, and every Tier 1 checkpoint where the user is asked to
decide, must include the six items in
[decision-rights.md](decision-rights.md#substantive-versus-nominal-approval).
In practice the gate message has these parts:

1. **Decision needed** and the recommended choice.
2. **What was done**: one paragraph and the package path.
3. **Evidence to inspect**: three to five artifact paths most worth opening.
4. **Open objections**: every escalated finding with the reviewer's original
   wording and the researcher's response; every deferred item and its trigger.
5. **Alternatives**: the other routes and what each would cause.
6. **Consequence of approval** and how it could be reversed.
7. **Choices**: approve / revise / backtrack or terminate, plus "ask for more
   checks" and free-form conditions.

The researcher controls what the user sees, so it must not summarize away
disagreement. If the gate summary and the critique file disagree, the critique
file wins.

## Adaptive Reconfiguration

See [Adaptive Reconfiguration Contract](adaptive-reconfiguration-contract.md) for the
proposed diagnostic procedure and validation criteria. The triggers below are
**screening signals for a possible organizational mismatch**, not automatic
proof that reassignment is necessary. Ordinary scientific disagreement or failure
is handled through inquiry iteration; the orchestrator's behavior is unchanged.

Backtracking and reconfiguration are different:

- **Backtracking** changes the *inquiry*: work returns to an earlier stage
  (see [stage-handoffs.md](stage-handoffs.md#backtracking-rules)).
- **Escalation** moves *one decision* to a higher authority.
- **Reconfiguration** changes the *organization*: who performs or authorizes a
  class of decisions from now on.

### Triggers

The researcher should diagnose possible organizational mismatch, and the reviewer
should flag it for consideration, when any of these occur. A proposal to
reconfigure is warranted when the current activity, actor, or authority
assignment is no longer suitable; a signal alone does not mandate redesign:

| Signal | Typical reconfiguration |
|---|---|
| the same decision class is escalated or reopened two or more times | raise its tier, or assign a domain expert to it |
| the user corrects the researcher's domain judgment on the same topic two or more times | require Domain Onboarding materials or a domain-expert reviewer for that decision class; downgrade researcher proposals there to "options only" |
| a reviewer raises blockers or majors in the same area across two passes | strengthen authority there: give the reviewer an explicit audit duty for that area, switch to blind review, add an expert, or have the user co-sign that decision class. A researcher self-check alone is a mitigation, not a reconfiguration. (Default already in place for claims: the Reporting reviewer audits every deliverable sentence against the claim map.) |
| the research object or claim level changes (for example, the case study becomes a test fixture for a workflow) | revise the Decision-Rights Map and re-check which stage packages need re-review |
| irreversible cost, safety, privacy, or public-release consequences appear | raise to Tier 1 or 2 and require substantive approval |
| a skipped check (reviewer, literature, validation) hits its revisit trigger | re-enable the check |
| the user's pace preference changes | switch workflow mode (Auto-until-needed / Step-by-step discussion) |

### Procedure

1. Propose the change as a Tier 1 decision: what moves, from whom, to whom,
   and why (cite the triggering decision IDs and say which "area" the findings
   share). A change that moves no activity or authority between actors is a
   mitigation; log it as such, not as a reconfiguration.
2. The user approves or rejects it.
3. Record it in the decision log with type `reconfiguration`.
4. Update the Decision-Rights Map in the Planning Package (or the current
   stage package if Planning is closed) and the README status block.
5. State which already-approved decisions, if any, must be re-checked under the
   new arrangement.

Because changing the organization is itself a consequential decision, it passes
through the same loop as any other Tier 1 decision.
