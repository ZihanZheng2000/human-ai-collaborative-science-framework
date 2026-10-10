# Workflow Evaluation

This document is the **evaluation layer** of the framework. Stage reviews ask
whether one project's outputs are sound. Workflow evaluation asks whether the
*way the project was organized and coordinated* helped, and at what human cost.
Every substantial run should record these measures in its `run-notes.md`
(template: `templates/example-run-notes.md`). Most can be computed from the
decision log and stage packages without extra work.

## Unit of Evaluation

The unit is the whole human–AI research system and its trajectory, not one
model call or the final deliverable. A polished report can hide heavy human
repair, weak evidence, or decisions that cannot be reconstructed. A run that
correctly stopped a bad direction early may be a success even with no
deliverable.

## Four Dimensions

| Dimension | Question | Measures for this framework | Source |
|---|---|---|---|
| Scientific outcome | Is the resulting work sound at its claimed level? | claim-support audit (supported / limited / unsupported / removed per substantive claim); reproducibility rerun pass/fail; validation type used (see below) | claim-evidence map, Review Package |
| Collaboration process | Did interaction improve the inquiry? | reviewer findings that changed the route or a Tier 1 decision ("trajectory-changing findings"); user corrections that changed the route; blocker/major findings caught before vs after the gate they belonged to; duplicated or lost work | decision log, response-to-reviewer tables, run notes |
| Reliability and accountability | Can consequential decisions be reconstructed and governed? | share of Tier 1/2 decisions with proposer, evidence, objections, and authorizer recorded; nominal vs substantive approvals; escalations raised and how resolved; decisions reopened; reviewer-triage closure rate | decision log |
| Human effort | What human attention and repair did the system need? | number of checkpoints and gates; user corrections (hidden repair: re-runs, rewrites, domain corrections); approximate user time per gate; where effort went (judgment vs routine verification) | decision log, run notes |

Interpretation notes:

- More gates or more findings are not automatically better. High checkpoint
  counts with few trajectory changes suggest the tiers are set too low and the
  user's attention is being spent on routine verification.
- Many user domain corrections suggest an expertise mismatch and should trigger
  reconfiguration ([coordination.md](coordination.md#adaptive-reconfiguration)).
- A high share of nominal approvals means the human gate is at risk of being
  ceremonial.

## Comparing Workflow Designs

A single run shows feasibility, not that the design helps. To claim that some
part of the framework improves research, compare designs while holding the
actors and resources as fixed as possible:

| Design comparison | Hold fixed | Vary |
|---|---|---|
| reviewer value | same user, same researcher agent, same task | reviewer pass on vs off |
| reviewer independence | same reviewer agent | standard vs blind mode |
| checkpoint granularity | same task | Auto-until-needed vs Step-by-step discussion |
| authority placement | same intervention points | user approves vs user co-performs the decision |
| tiering | same task | all consequential decisions at stage gates vs Tier 1 checkpoints |

Price the resources: a design that uses more model calls, more wall-clock
time, or more user time is not better merely because its output is better.
Report the resource difference next to any quality difference.

Seeded-error tasks (deliberately planting a data leak, a mislabeled event, or
an unsupported causal claim) are the cheapest way to test whether critique and
gates actually catch problems.

### Seeded-fault protocol

1. Before any analysis, write a sealed seed record (what will be planted, at
   which stage, which reviewer check should catch it) outside the reviewer's
   reach, for example in the session scratchpad.
2. Do not label seeds anywhere a later reviewer can read (packages, responses,
   decision log) until every seeded stage has been reviewed. Respond to a caught
   seed as to any finding.
3. After the last seeded stage, commit the seed record, add a `disclosure`
   entry to the decision log, and mark decisions that responded to seeds.
4. In run notes, report seeds caught at their own stage, caught later, and
   missed, separately from unseeded findings. Reconfigurations triggered only by
   seeds demonstrate the mechanism; they are not evidence of a real recurring
   failure.

## Validation Without Ground Truth

Say which kind of validation backs each evaluation claim:

| Validation type | Example |
|---|---|
| known outcome | retrospective task where the answer is known |
| seeded error | planted defect: was it caught, at which stage, by whom |
| reproducibility | fresh rerun reproduces tables/figures/metrics within tolerance |
| expert adjudication | blinded domain expert rates findings or decisions; report disagreement |
| delayed validation | later evidence, replication, or publication review |

## Promoting Lessons

At the end of a run, each lesson in `run-notes.md` is marked: keep in example
for more evidence, promote to `docs/`/`templates/`/`skills/`, or reject as
noise. A lesson should normally be seen in two runs, or be backed by an
evaluation measure above, before it changes the core framework.
