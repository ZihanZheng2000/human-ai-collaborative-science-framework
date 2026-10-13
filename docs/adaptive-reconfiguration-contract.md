# Adaptive Reconfiguration: Organization-Change Contract (Proposal)

**Status:** design proposal v0.1 (2026-10-13); not an orchestrator feature change. Grounded in the companion paper's current [Coordination section](https://github.com/ZihanZheng2000/human-ai-collaborative-science/blob/main/sections/04_coordination.tex). Related: [Organization Contract](organization-contract.md), [Accountability Contract](accountability-contract.md), [Shared Research State Contract](shared-research-state-contract.md).

## Purpose

**Adaptability** is the capacity to revise the activity–actor–authority arrangement when it no longer serves an inquiry. Reconfiguration is **not** a response to every scientific failure or critique; many issues belong to normal inquiry iteration. A scientific experiment that fails, an unresolved hypothesis, or a reviewer challenge may call for new evidence without any role or authority change.

**Reconfiguration** changes a future assignment of scientific activities, actors, or consequential decision rights. **Escalation** changes who addresses one issue; **backtracking** revisits prior scientific work; **mitigation** repairs a local problem without changing the organizational arrangement. A single escalation can motivate later reconfiguration but is not itself reconfiguration.

## 1. Diagnose before changing organization

| Observation | Usually first response | Consider reconfiguration when |
| --- | --- | --- |
| A hypothesis fails or analysis yields a null result | revise hypothesis or investigate evidence within approved scope | the assigned actor persistently cannot execute or interpret required activities |
| Reviewer questions a method or claim | examine evidence and address objection | repeated or consequential blind spots indicate inappropriate actor assignment or review authority |
| Missing domain knowledge | consult materials, request specific expertise | the missing competency affects an ongoing class of decisions requiring a new specialist or revised assignment |
| New high-risk or irreversible action | stop at applicable authority checkpoint | responsibility or authorization rules need to change for subsequent actions |
| Same type of consequential conflict recurs | examine decisions, causes, and costs | existing decision boundaries systematically block or distort scientific progress |
| Research goal or technical capability changes | reconsider task decomposition and resources | the old distribution of work and decisions no longer fits the new objectives |
| User wants different interaction pace | adjust interface or checkpoints within current rights | a lasting change to delegated activity or authorization is actually required |

**Do not equate counts with proof.** Existing rules like “twice in the same area” are screening signals, not sufficient or necessary scientific criteria. One severe event can require immediate intervention; many minor events might need none.

## 2. A minimal reconfiguration proposal

A proposal should document:

1. **Observed mismatch:** what activity or decision class is inadequately assigned; link evidence, events, relevant contribution/activity/decision IDs.
2. **Why ordinary iteration or local mitigation is insufficient:** distinguish scientific uncertainty from organizational failure.
3. **Current and proposed mapping:** which activity, actor, or authority changes (before → after), including scope and duration.
4. **Alternatives and costs:** do nothing, add a targeted check, obtain expertise, redesign rights; human time, latency, computation and disruption.
5. **Authorization:** which human or otherwise authorized actor can approve this mapping change under the *existing* Decision-Rights Map. No self-authorized rights escalation.
6. **Impact:** which prior decisions, open reviews, evidence access or planned tasks must be revisited; what remains unresolved.
7. **Revisit and rollback:** observable success/failure signals, time or task boundary for reassessment, and how to restore the earlier mapping.

Change request IDs should reference the authoritative decision-log ID when authorized. No separate “approval” stored in an AI-authored note may override the orchestrator-owned human decision record.

## 3. Operational path (design, not an automatic trigger)

```text
Observe change / persistent mismatch / serious risk
                    ↓
Diagnose: scientific iteration, mitigation, escalation, or organizational mismatch?
             ↙                                  ↘
Normal inquiry or local fix            Propose mapping change
(no reconfiguration)                   (evidence + alternatives)
                                                  ↓
                                        Authorize under current rights
                                            ↙             ↘
                                         Reject         Approve
                                            ↓              ↓
                                    Keep current map   Version new map;
                                                       notify affected actors
                                                            ↓
                                                      Evaluate and revisit
```

The framework should encourage **small, reversible adjustments** when feasible. Emergency pauses protecting safety, privacy, or costly irreversible actions may be required under existing policies; an emergency pause is not permission to transfer decision authority without authorization.

## 4. Example: reservoir rule inference

An AI researcher infers a drought-response rule using daily releases and storage. A domain scientist repeatedly identifies that the chosen drought event boundaries exclude relevant operational declarations. The researcher first corrects the event definitions and reruns the analysis: this is **scientific revision**, not reconfiguration.

If the same knowledge gap persists across multiple event-definition tasks, propose assigning drought-event labeling to the domain expert, requiring their review of future labels, and limiting AI authority to recommendations in this decision class. The authorized human approves the revised mapping; changes and unresolved earlier results are recorded. If the new arrangement adds substantial delay without reducing errors, revisit it.

This example is illustrative; no performance improvement is asserted.

## 5. Connection to evaluation

Evaluate a mapping change by comparing what matters **before and after** while recognizing that conditions may differ. Candidate measures: corrected consequential errors, missed expertise issues, reopened decisions, scientific-quality assessments, reconstruction accuracy, human review cost, execution latency, and adverse impacts. A before/after observation alone **does not establish causal benefit**; comparable tasks and resource-accounted baselines are needed for system-design gain.

Differentiate:
- **Diagnostic evidence:** reason to propose a change.
- **Authorization evidence:** proof of who approved the change.
- **Outcome evidence:** what happened after the change.
- **Attribution evidence:** whether the change, rather than other factors, caused improvement.

## 6. Compatibility and future validation

The current orchestrator maintains Tier 1 reconfiguration decisions and the existing decision-rights mapping. This contract **does not alter that behavior**. Its narrower change is conceptual: a fixed numerical signal prompts diagnosis, rather than mandating reconfiguration without assessing organizational mismatch. Existing “reviewer should flag” rules remain applicable for surfacing possible mismatch.

Proposed acceptance tests:
1. **No false redesign:** an ordinary failed hypothesis triggers scientific iteration, not actor/right reassignment.
2. **Correct escalation:** a serious missing competency produces an inspectable mapping-change proposal and appropriate authorization.
3. **No unauthorized self-promotion:** an agent cannot grant itself authority by editing a summary, proposal, or configuration suggestion.
4. **State continuity:** a new participant sees the active mapping, superseded version, affected decisions, and unresolved disputes.
5. **Right-sized intervention:** compare benefits and coordination costs against simple mitigation and a fixed arrangement.

Do not claim these tests have passed before implementing and executing them.
