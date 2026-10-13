# Scientific Accountability: Inquiry-Cycle Contract (Proposal)

**Status:** design proposal v0.1, 2026-10-13; **not implemented as a new engine**. Grounded in the current [companion paper, Coordination section](https://github.com/ZihanZheng2000/human-ai-collaborative-science/blob/main/sections/04_coordination.tex). See also [Organization Contract](organization-contract.md) and [Shared Research State Contract](shared-research-state-contract.md).

## 1. What changed from the earlier reading

The theoretical **Scientific Accountability Loop** is broader than a review-and-approval pipeline. It explains how inquiry proceeds from an existing research state, through proposals, scientific execution, examination of results, revision or resolution, and the recording of outcomes and unresolved issues back into shared state. Critique and authorization are important functions **within** this process but do not define every scientific step.

The earlier operational sequence `propose → critique → respond → authorize → act → record` is a **decision-review subprotocol for consequential choices**, not the universal scientific inquiry cycle. It remains useful at stage gates or high-stakes decisions and must not be deleted from currently running projects without migration.

## 2. Conceptual cycle (not a mandatory state machine)

```text
Current research state
      ↓
Identify question / propose approach
      ↓
Develop / execute / investigate
      ↓
Examine evidence / critique / verify
      ↓
Revise / extend / accept provisionally / defer / reject / stop
      ↓
Update research state, including open questions and next actions
      ↺
```

Phases can overlap, recur, branch, or return to earlier activities. Execution can surface a new question immediately. Critique can occur before, during, or after execution; independent review is required only where the chosen design or risk contract calls for it. Scientific acceptance is *provisional and evidence-bounded*; it is not identical to administrative approval.

**Authorization overlay:** before an action exceeding the actor's authorized scope, invoke the applicable decision-rights tier and record the outcome. Authorization is not a universal phase placed between examination and execution.

## 3. Minimum inspectable transitions

| Transition | Evidence to preserve when scientifically consequential | What not to assume |
| --- | --- | --- |
| From state to proposal | driving question, target claim/activity ID, assumptions, relevant evidence, alternatives | that a proposal is authorized |
| To execution | method and version, data/tool source, scope, planned validity checks, permissions required | that an executed analysis is valid |
| To examination | outputs, quality checks, reviewer/human objections, counterevidence, unresolved uncertainty | that reviewer agreement proves correctness |
| To revision or resolution | accepted/deferred/rejected changes, reasons, before/after scientific object pointers, affected contribution IDs | that every revision improves quality |
| To updated state | bounded claim status, evidence refs, objections, next activity, active authorization | that a summary supersedes source records |

Record consequential change paths using Activity IDs, Contribution IDs, Decision IDs (when applicable), and evidence links from the companion contracts. Avoid turning routine iteration into a gate or a verbose transcript.

## 4. Two separate loops and their relationship

**Inquiry cycle (scientific process):** propose, execute, examine, revise/resolve, update and iterate. It can be lightweight and is not necessarily sequential.

**Decision review (governance):** proposal, critique appropriate to the risk, response, authorization, execution, recording. It applies when a consequential action requires the designated decision authority. Reviewer gates in the existing orchestrator are one implementation of this subprotocol.

They can overlap: a human critique may prompt new analysis, and that analysis can be completed within an existing authorization scope. Conversely, changing a preregistered validation split after seeing results requires a new disclosed and authorized decision. **Critique is not equivalent to authorization**, and **authorization is not scientific validation**.

## 5. Reconfiguration only when warranted

Ordinary failed experiments, alternate hypotheses, and disagreements are normal inquiry events. They should trigger further investigation or scoped review when appropriate, **not automatically a redesign of who performs or authorizes work**.

Propose reconfiguration when evidence suggests a *persistent organizational mismatch* (e.g., repeated expertise gaps, systematic missed objections, recurring unresolved escalations, newly consequential safety or resource constraints, or changed objectives). Thresholds such as “twice” are **operational heuristics**, not theoretical laws. Record the basis, costs, alternative mitigations, and authority for changes. A single major high-risk event can justify immediate reconfiguration; a recurring but harmless difference need not.

## 6. How to evaluate this mechanism

Measure more than gate completion or number of critique findings:

- scientific work completed and validity of resulting evidence;
- whether objections were addressed by examination, revision, bounded acceptance, or properly disclosed deferral;
- whether transitions and unresolved issues are reconstructable after restart;
- unnecessary interruption and human review burden;
- whether the cycle improves correctness or error detection compared with a simpler process when iterations and resources are matched or priced.

A successful trace demonstrates **feasibility and accountability**, not necessarily *system-design gain*. Empirical improvement claims require controlled or otherwise credible comparisons and assurance.

## 7. Compatibility and implementation order

**Current runtime remains unchanged.** The orchestrator's four-stage maker-checker/gate path is a valid, more prescriptive *workflow profile* on top of the broader scientific cycle. The existing Tier 0/1/2 permissions and decision log remain authoritative.

Suggested next engineering iteration:
1. Add optional links from stage packages to activity, contribution, evidence, and scientific-resolution records.
2. Add a bounded, decision-relevant current-state view that updates after significant scientific changes.
3. Distinguish routine scientific iteration from consequential authorization; do not add human gates for every examine/revise cycle.
4. Use small seeded-error and domain evaluation tasks before changing the engine or declaring improvement.

This contract should not be read as a claim that the present orchestrator supports arbitrary graph-shaped scientific workflows.
