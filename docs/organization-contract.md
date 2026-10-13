# Organization Layer: Operational Data Contract (Proposal)

**Status:** proposed schema v0.1, not implemented by the orchestrator. Companion sources: [theory](https://github.com/ZihanZheng2000/human-ai-collaborative-science) Section 3, [design rationale](design-rationale.md), [decision rights](decision-rights.md).

## Objective and boundaries

Operationalize **Activity (what scientific work), Actor (who contributes), and Authority (who can authorize actions)** without equating activities with stages or inferring scientific collaboration from gate approvals. This is a **minimal conceptual record contract**, not a requirement to use JSON, create one file per action, or log every low-level tool call.

Four entities are sufficient for an initial design:

1. **Activity record** — meaningful scientific work and its research object.
2. **Contribution record** — an actor's substantive input to an activity or an existing scientific claim.
3. **Decision record** — a proposed consequential action and its actual authorization, already represented in the existing decision log.
4. **Evidence and change links** — pointers to inspectable artifacts and before/after changes, rather than copies of full execution logs.

An actor **registry** identifies humans, agents, groups, and tools, with role, version where relevant, and competencies or limitations **when known**. A role label (researcher, reviewer) is not the actor identity, and an execution tool is not automatically a decision authority.

## 1. Minimal records

| Record | Required fields | Useful optional fields |
| --- | --- | --- |
| Activity | `activity_id`, scientific objective, activity type, status, actor IDs, related artifact/claim IDs | parent activity, current workflow stage(s), input assumptions, outcome, predecessor activity IDs |
| Contribution | `contribution_id`, actor ID, related activity/claim ID, contribution type, content or artifact pointer, timestamp/order | response-to contribution ID, evidence, effect on inquiry, uncertainty, alternative considered |
| Decision | existing decision ID, proposal, proposer, evidence, alternatives, objections, authorizer, authorization status | related activity/contribution IDs, option framing or information access, competence/verification notes |
| Actor | `actor_id`, actor kind (human, agent, team, tool), specific identity label, role assignment | model/version, expertise scope, delegated permissions, limitations |
| Change link | affected claim/activity/plan ID, before pointer, after pointer, authoring contribution IDs, decision ID if authorization required | type of change, validation and dispute status |

Use stable IDs such as `A-12`, `C-19`, `D-7`; references must resolve within a run. Timestamps do not substitute for ordering where several actions occur simultaneously. Preserve rejected/deferred contributions and superseded versions rather than silently overwriting them.

**Activity types are illustrative and extensible:** problem-framing, hypothesis generation, literature/evidence retrieval, data curation, modeling, interpretation, critique, replication, communication. They may occur in **any stage**. Do not encode the four stages as the activity type taxonomy.

**Contribution types** (also extensible): propose, question, critique, counterevidence, correction, synthesis, justification, verification, interpretation, rejection or deferral rationale. A bare approval with no scientific input is a decision, not necessarily a contribution to scientific reasoning.

## 2. Relationships and invariants

- An Activity can have multiple Actors and multiple Contributions; the same Actor can contribute to many Activities.
- A Contribution points to an Actor and an Activity or scientific object. It is not equivalent to **authorization**.
- A Decision can reference many Contributions, but exactly who **authorized** a consequential action must remain explicit and must obey the active Decision-Rights Map.
- A Change links the scientific state before and after. Not every Contribution produces a change. A defended hypothesis may still reflect substantive scientific engagement if a specific evidence-based challenge and response can be reconstructed.
- Tier 0 routine execution stays lightweight in run logs. Preserve detailed contribution links for consequential scientific claims, disputes, methodological changes, and interventions, not every keystroke.
- After-the-fact modifications to analysis choices (labels, exclusions, validation split, metrics) must preserve the prior choice and disclosure that results were already observed.
- The authoritative log of human decisions remains the orchestrator-owned decision log; agents must **not** create fabricated human approvals in contribution records.
- Reviewer information barriers must be enforced by access controls, not merely by marking a contribution `blind`; retrospective linking cannot leak the researcher's framing into an independent review pass.
- A successful gate cannot be construed as a validation of scientific truth.

## 3. Detecting collaboration without circular definitions

The system should preserve **observables**, not produce an automatic unvalidated "collaborative=yes" score:

| Observable | Evidence to record | What cannot be concluded |
| --- | --- | --- |
| Human opportunity | request, alternatives, evidence, objections, override path | that the user engaged substantively |
| Human scientific input | specific question, correction, hypothesis, domain knowledge, counterargument | that the input was correct |
| AI scientific response | revision, evidence-backed defense, new experiment or changed interpretation | that the response improved quality |
| Reciprocal influence | contribution link(s), reasoning before/after, affected research object | that any observed gain was caused by the design |
| Authorization | who approved/rejected/redirected; effective scope and objections visible | that approval alone constitutes collaboration |

**Worked contrast:**

- **Case S (supervision):** agent proposes dataset X; human selects “Approve” without additional scientific reasoning; decision D-4 is valid as an approval but does not establish reciprocal scientific engagement.
- **Case C (collaboration):** agent proposes X; human points out that X excludes drought years (C-2); agent verifies coverage, proposes X+Y with a revised temporal scope (C-3), and human authorizes the change (D-4). Link C-2 → C-3 → D-4, preserve both proposals and coverage evidence.
- **Case D (substantive disagreement without plan change):** human challenges a model assumption with domain evidence; agent tests the challenge and provides a reproducible counteranalysis; human accepts the defended assumption. No plan change, but both scientific contributions remain inspectable. Do not classify this automatically as "non-collaborative."

## 4. Relationship to the existing repository

| Existing source | Keep authoritative for | Proposed addition (not implemented) |
| --- | --- | --- |
| `workflow.config.json` | runtime roles and assigned agents | optional stable actor IDs and expertise notes |
| `docs/decision-rights.md` | authorization policies and tiers | distinguish who shaped options from who authorized; reference relevant contributions |
| `decision-log.md` / `templates/decision-log.md` | consequential decisions and actual human authorization | cross-reference contribution IDs rather than duplicate or overwrite decisions |
| `packages/*.md` | compact stage-scoped summaries | activity/contribution references that can span stages |
| `run_log.md` | chronological execution trace | retain Tier 0 actions; link high-impact events as needed |
| `docs/coordination.md` | research state and accountability mechanisms | select a decision-relevant summary view over these links |

**Migration strategy:** introduce optional links/sections first. Existing examples and orchestrator logging remain valid with empty or absent contribution references. Do not require new fields in active machine-parsed files until adapters, migrations, and tests exist.

## 5. Five acceptance tests before implementation claims

1. **Cross-stage continuity:** the same hypothesis critique and refinement is representable across Planning, Modeling, and Reporting without inventing three distinct scientific activities.
2. **Joint activity:** two human and AI contributors can be represented with independently attributable scientific inputs.
3. **Authority vs influence:** an AI-produced short list, a human domain objection, and final human authorization are separately reconstructable.
4. **No false collaboration:** synthetic gates, bare approvals, and unexamined clicks cannot be counted as demonstrated substantive engagement.
5. **Safe restart/review:** a fresh session reconstructs the active claim and dispute; a blind reviewer sees only permitted evidence; no fabricated authorization appears after restart.

All tests above are **proposed acceptance criteria**, not passing test results.

## 6. Decisions to defer

- Whether to store the records in Markdown, JSON, SQLite, or a graph.
- Whether to enforce explicit activity IDs for every project or only evaluated research runs.
- Whether a quantitative rubric for substantive reciprocal engagement is reliable enough to publish.
- Whether actor capabilities should be measured, self-reported, or inferred from task outcomes.

Resolve these against actual reconstruction tasks and human-effort costs, rather than building a large ontology in advance.
