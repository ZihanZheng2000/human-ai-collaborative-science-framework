---
name: gate-manager
description: Use whenever Planning, Modeling, Reporting, or Reviewing reaches a Human Gate, or a Tier 1 decision checkpoint needs a user decision; presents the decision substantively, records it in the decision log, and advances to the next stage after approval unless blocked or explicitly paused.
---

# Gate Manager Skill

## Use When

- a stage package is ready for user approval (Tier 2 gate)
- a consequential in-stage decision needs the user (Tier 1 checkpoint)
- a Modeling package needs approval after an exploratory demo phase or full-scale execution
- the user says approve, revise, backtrack, pause, or terminate
- a reconfiguration of the Decision-Rights Map is proposed
- stage transition behavior must be recorded

## Inputs

- current stage package, or the Tier 1 proposal
- decision log and open escalations
- reviewer critique and researcher response, for Tier 2 gates
- demo-phase summary, if Modeling used an exploratory demo
- user decision and notes
- known blockers
- gate mode: real user gate, synthetic gate, or mixed

## Procedure

1. Confirm the tier (`docs/decision-rights.md`). When unsure, use the higher tier.
2. Build the substantive presentation (`docs/coordination.md#substantive-gate-presentation`):
   - decision needed and recommended choice
   - what was done and the package path
   - three to five evidence paths worth opening
   - open objections: escalated blocker/major findings in the reviewer's
     original wording with the researcher's response; deferred items and their
     triggers; skipped reviewer passes
   - alternatives and what each would cause
   - consequence of approval and how it could be reversed
3. Present the choices. When a structured user-choice tool such as
   `request_user_input` or `AskUserQuestion` is available, use clickable
   choices: 2-3 mutually exclusive options, recommended option first, plus a
   free-form path for conditions, corrections, or "ask for more checks". If the
   tool is unavailable, present the same choices as plain text.
4. Ask the user to uphold or overturn the researcher's response to each
   escalated finding.
5. Append the decision to `decision-log.md`: type, decision, proposer,
   evidence, alternatives, open objections, authorizer, approval quality
   (substantive / nominal with what was missing / synthetic), status.
6. Update the stage package gate section and the README status block.
7. If approved, mark the package status as approved and immediately begin the
   next stage unless the user pauses or the next stage is blocked.
8. If revised, route changes to the current stage.
9. If backtracked, route to the appropriate earlier stage.
10. If reconfigured, update the Decision-Rights Map and list decisions that must
    be re-checked.
11. If blocked, write the smallest next action needed.

## Structured Gate Choices

Use these defaults unless the stage package requires a more specific option:

| Gate | Choices |
|---|---|
| Planning Gate | Approve for Modeling / Revise Planning / Backtrack or terminate |
| Modeling Gate | Approve for Reporting / Revise Modeling / Backtrack to Planning |
| Reporting Gate | Approve for Reviewing / Revise Reporting / Request Modeling or Planning addendum |
| Reviewing Gate | Finalize or archive / Revise routed issues / Backtrack to earlier stage |
| Tier 1 checkpoint | Approve proposal / Choose alternative / Ask for more checks |

## Default Transitions

- Planning approval -> Modeling
- Modeling approval -> Reporting / Output Packaging
- Reporting approval -> Reviewing
- Reviewing approval -> finalization, sharing, submission, archive, another routed Modeling/Reporting cycle, or termination

## Guardrails

- Approval is an action, not only a label.
- Do not summarize away disagreement; if the gate summary and the critique file differ, the critique file wins.
- Do not record an approval as substantive if the user did not see the evidence paths and open objections.
- Do not treat agreement with a topic or direction as approval of a gate or checkpoint.
- Synthetic gates are acceptable for framework smoke tests, but must not be represented as real user, domain-owner, or expert approval.
- Do not continue if the user says pause, stop, or wait.
- Do not hide blockers; state them and the next action.
