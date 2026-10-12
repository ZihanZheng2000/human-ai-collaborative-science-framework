# Design Rationale: From the 9A Framework to a Reference Implementation

**Status:** Design baseline for review (2026-10-12). This document records intended design principles, not empirical validation or a claim that all described capabilities are already implemented.

**Theory source:** [Human–AI Collaborative Science](https://github.com/ZihanZheng2000/human-ai-collaborative-science) (companion conceptual paper, especially Organization, Coordination, and Evaluation).

## 1. Purpose and scope

The **9A Framework** is a conceptual account of how to **describe, design, and evaluate** human–AI collaborative scientific inquiry. Its layers are:

- **Organization:** Activity, Actor, Authority.
- **Coordination:** Awareness, Accountability, Adaptability.
- **Evaluation:** Achievement, Attribution, Assurance.

This repository is **one reference implementation** of selected design implications of that theory, organized as an executable research workflow. It is neither the definition of the 9A Framework nor a claim that its four stages, tool choices, skills, roles, and gate counts are necessary for all human–AI collaborative science.

**Separation of claims:**

1. **Conceptual claim:** the 9A vocabulary distinguishes important design and evaluation questions.
2. **Design hypothesis:** particular mechanisms (e.g., explicit decision rights, shared state, critical review) may improve inquiry under stated conditions.
3. **Implementation claim:** the code implements some mechanisms with specific engineering choices; this must be checked against tests and traces.
4. **Empirical claim:** a mechanism improves quality, reliability, or efficiency relative to a credible baseline; this requires comparative evidence, not just a successful demonstration.

Do not infer (4) from (1)–(3). A smoke test demonstrates a bounded execution path, not scientific benefit or generality.

## 2. What counts as collaboration

In the companion paper, **AI assistance** delegates bounded tasks under human direction; **AI autonomy** directs substantial parts of inquiry with limited substantive human engagement; **human–AI collaborative science** requires reciprocal engagement in which contributions from human and AI **substantively influence scientific reasoning, judgment, or research direction**.

A human gate or approval alone is **not evidence** of substantive collaboration. A workflow may be human-gated yet remain primarily supervised automation. Conversely, a human correction that changes a hypothesis, method, evidence interpretation, or research direction can be a meaningful contribution.

To characterize a run, distinguish:
- **Opportunity to intervene:** was a human offered a real choice?
- **Actual engagement:** what did the human and AI each propose, challenge, revise, or reject?
- **Consequential effect:** what changed in the inquiry, with an evidence-linked before/after record?
- **Authorization:** who was permitted to accept the change? Approval is not the same as epistemic contribution.

These are **proposed observables**, not a validated score or binary classifier. Do not label a run “collaborative” merely because gates were approved. If an intervention did not change direction, it might still contribute substantive reasoning (e.g., evidence-backed defense of a hypothesis); document the reasoning rather than assuming no contribution.

## 3. Theory → requirement → mechanism → implementation → test

The middle column describes **functional requirements**, not mandatory software components. Status is deliberately conservative.

| 9A concept | Functional design requirement | Mechanism used or proposed here | Evidence or discriminating test |
| --- | --- | --- | --- |
| **Activity** | Represent meaningful scientific work at task-relevant granularity, independent of project phases | Research activities in stage packages; **proposed:** explicit activity records decoupled from stages | Can review, hypothesis revision, and evidence search recur across stages without incorrect classification? |
| **Actor** | Record who actually performed and co-performed activities | Configurable researcher, reviewer, human, and expert assignments; **proposed:** contribution records | Can a task be jointly performed and can responsibilities be reconstructed? |
| **Authority** | Distinguish performance, recommendation, approval, escalation, and effective influence | Decision-Rights Map and Tier 0/1/2 decisions; **proposed:** record option selection/framing and alternatives visible to authorizer | Can the record show who shaped options versus who approved them? |
| **Awareness** | Preserve **decision-relevant**, reconstructable state including claims, evidence, uncertainty, and open disputes | Status block, decision log, stage packages, inbox; **proposed:** concise state-reconstruction views | Can a new participant recover current claims, uncertainties, and next decision accurately and promptly? |
| **Accountability** | Make consequential contributions challengeable, responsive, and authorized; separate scientific validity from permission | Propose → critique → respond → authorize → act → record, review and escalation | Do objections materially change claims/actions? Are unresolved objections visible and tested? |
| **Adaptability** | Allow revision of activity–actor–authority mapping when the arrangement is inadequate | Reconfiguration decisions and triggers; **proposed:** connect observed evaluation failures to reconfiguration proposals | Does adaptation help versus a fixed design with comparable time and resources? |
| **Achievement** | Measure scientific quality, process, reliability, and human effort rather than only artifact completion | Workflow evaluation and run notes | Domain/expert assessment, supported-claim audit, reproducibility, human repair costs |
| **Attribution** | Separate improvement from added model computation, tools, human attention, or task variance | **Proposed experimental use:** matched baselines and ablations | Same actors and task: alter a design mechanism, price or match resources |
| **Assurance** | State why outcome and attribution measurements deserve confidence | Known outcomes, seeded faults, reruns, expert adjudication, delayed validation | What validation type supports each conclusion, and what uncertainty remains? |

There is **no one-to-one correspondence** between the nine concepts and nine code modules.

## 4. Architectural boundaries

### Activity is not Stage

An **activity** is a meaningful scientific operation (e.g., formulate a hypothesis, retrieve counterevidence, estimate a model, critique a causal claim). A **stage** is a workflow management boundary. The default **Planning → Modeling → Reporting → Reviewing** pipeline is a pragmatic template, **not a theory of the necessary sequence of scientific discovery**. Critique and revision can occur within any stage; backtracking is normal. Exploration may require flexible iteration; confirmatory choices need more disciplined preregistration or explicitly disclosed post-result changes.

**Near-term rule:** retain the current four-stage workflow for compatibility, but avoid saying it exhausts or defines Activity. Stage-level packages can reference work performed across stage boundaries. More flexible activity scheduling is a *future design change*, not current behavior.

### Authority is not competence

An actor with formal approval power may lack expertise to assess a technical claim. Track epistemic assessment separately from authorization. Reviewers can challenge; authorized actors decide whether a project may proceed. Approval cannot turn an invalid scientific claim into a valid one. Stronger validation, a domain expert, or a decision to stop may be necessary where evidence is inadequate.

Formal authority also differs from **effective influence**: the actor filtering the alternatives, framing a summary, or controlling evidence access can shape the outcome without approving it. Decision records should show significant alternatives, objections, and their provenance.

### Shared state is not an information dump

The state must help participants reconstruct **what is currently believed, why, what remains contested, and what decision follows**. Full raw logs support audit but should not replace a selective, current, decision-relevant summary. Selective reviewer access can preserve independent critique without deleting provenance.

### Accountability is not a correctness guarantee

The scientific accountability loop makes judgments inspectable and contestable, not automatically true. **Traceability**, **evidential validity**, and **decision responsibility** require separate tests. Review can itself be wrong or correlated across models.

### Evaluation must feed design

Evaluation is not only end-of-run documentation. Findings should inform whether a reviewer is useful, which decisions merit escalation, which human expertise is needed, and whether the cost of added gates is justified. This feedback pathway is a **design objective**; empirical superiority is unproven.

## 5. Core functions, configurable mechanisms, and engineering choices

| Category | What belongs here | Policy |
| --- | --- | --- |
| **Theory-linked core functions** | Explicit activity–actor–authority mapping, reconstructable shared research state, contestability/accountability, authorized reconfiguration, evaluation | Preserve the **function**; implementations may vary |
| **Configurable design mechanisms** | Human checkpoint placement and frequency, review strategy and independence, stage ordering/backtracking rules, expert involvement, gate strictness | Choose according to scientific risk, reversibility, competence, and available resources; compare alternatives |
| **Replaceable engineering choices** | Markdown files, folder names, CLI agent vendors, seven bundled skills, handoff filenames, orchestrator internals | Never present as 9A theoretical necessities |

The present Tier 0/1/2 tiers and four gates are **one way** of implementing decision rights, not universal requirements. The seven skills implement workflow tasks; they are not nine theoretical dimensions.

## 6. Implementation and validation roadmap

This initial revision is **documentation-only** and does not alter orchestrator behavior.

1. **Current documentation alignment:** clarify theory vs implementation in README; keep the runnable workflow and existing examples intact.
2. **Architecture specifications:** introduce stage-independent activity and contribution records, decision-relevant state summaries, and explicit records of human/AI scientific influence; update templates and invariants before changing the engine.
3. **Controlled implementation changes:** preserve backward compatibility or provide migration rules; exercise role permissions, review isolation, resume/retry, logging consistency, and untrusted-input boundaries.
4. **Empirical evaluation:** compare at least a simple AI-assisted workflow, the current human-gated workflow, and a revised collaborative arrangement on bounded domain-relevant tasks. Match or price model calls, compute, elapsed time, and human effort. Report negative results, missed errors, and unsuccessful interventions.
5. **Feedback to the theory paper:** revise conceptual wording only where operationalization exposes an actual conceptual ambiguity; do not redefine theoretical constructs to accommodate accidental software constraints.

## 7. Minimum evidence for future claims

- **“Runnable”:** reproducible execution with artifacts and tests under a stated environment.
- **“Traceable”:** an independent reader can reconstruct consequential choices and unresolved disputes.
- **“Human-gated”:** actual decision authority was available and exercised or explicitly declined, rather than synthetic approval.
- **“Collaborative”:** documented reciprocal scientific engagement; gate counts alone are insufficient.
- **“More reliable/better”:** credible comparative evidence under controlled or priced resources, with stated validation and uncertainty.
- **“Generalizable”:** evaluation across multiple tasks, actors, and domains; a single case is insufficient.

## 8. Open design questions

1. What is the smallest useful unit of scientific activity and contribution for reconstruction without excessive logging?
2. How do we identify substantive reciprocal engagement without requiring every intervention to change the result?
3. Which checkpoints require domain expertise rather than a generic human approval?
4. How can state summaries preserve live disagreements without propagating the researcher agent's framing into independent review?
5. When does adaptive coordination outperform a simpler fixed workflow after accounting for human attention and computation?

**Non-goal for this batch:** no assertion that the current software already supports fully dynamic activity scheduling, causal attribution, or validated collaboration classification.
