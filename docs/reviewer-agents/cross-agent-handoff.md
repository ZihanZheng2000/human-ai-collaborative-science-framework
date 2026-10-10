# Cross-Agent Handoff Protocol

This document defines how the researcher agent and reviewer agent exchange work
inside each stage's maker-checker loop. It implements the Tier 2 accountability
loop described in [../coordination.md](../coordination.md); the reviewer's
rights are defined in [../decision-rights.md](../decision-rights.md#reviewer-rights).

Which agent is researcher and which is reviewer (per stage, if desired) is set
in `roles` in `workflow.config.json`. Any agent can hold either role: a CLI
agent, a model API (reviewer only), or a person. The protocol is the same for
all of them. In orchestrated runs ([../orchestration.md](../orchestration.md))
the orchestrator starts the reviewer, enforces blind mode, and records the
user's gate decision; in manual runs the user hands the files between agents.

## Run Directory

`<run_dir>` below means:

- real research project: `research/<research-name>/artifacts/<run_id>/`
- framework smoke test or legacy run: `artifacts/<run_id>/`

`<run_id>` is a descriptive slug that stays the same for every file in the run,
for example `water-env-plan-v1` or `smoke-test-2026-06-28`.

---

## The Loop

Files are named per stage, because all four stages of a run share one run
directory: `<stage>` is `planning`, `modeling`, `reporting`, or `reviewing`.

```
[researcher] drafts or revises the stage package
  -> [researcher] writes <run_dir>/review-request-<stage>.md
                  and <run_dir>/review-framing-<stage>.md
  -> [reviewer]  reads the request and the package
                 (blind mode: opens the framing file only after its independent findings)
  -> [reviewer]  writes <run_dir>/reviewer-critique-<stage>.md
  -> [researcher] triages each finding, updates the package, logs escalations
  -> [researcher] presents a substantive gate to the user
  -> user approves, revises, backtracks, or terminates
```

---

## Step 1: Researcher Writes the Review Request

**Files**: `<run_dir>/review-request-<stage>.md` (header and artifact list) and
`<run_dir>/review-framing-<stage>.md` (the researcher's summary, known risks,
and questions). They are separate so that blind review can actually be blind:
a reviewer cannot read a header without also seeing framing that sits in the
same file.

The request is the authoritative assignment for this pass. If its reviewer
assignment differs from `roles` in `workflow.config.json`, it must cite the decision-log entry
in which the user approved the override.

```markdown
# Review Request

## Header

- Stage: [Planning / Modeling / Reporting / Reviewing]
- Run ID: <run_id>
- Run directory: <run_dir>
- Gate mode: [real user gate / synthetic gate / mixed]
- Review mode: [standard / blind]
- Stage package path: <path>
- Decision log path: <path or "smoke test: none">
- Researcher agent: <agent name from workflow.config.json>
- Reviewer agent: <agent name from workflow.config.json>
- Assignment source: [workflow.config.json / user override D-<n>]
- Reviewer rights: advisory + escalation (default) / other per Decision-Rights Map
- Framing file: <run_dir>/review-framing-<stage>.md
- Date: <date>

## Artifacts to Inspect

<paths to the package, data, figures, run logs, scripts, and deliverables the
reviewer should open; no researcher commentary here>
```

```markdown
# Review Framing (<stage>)

<!-- Blind mode: the reviewer opens this file only after writing its
independent findings. -->

## Summary of Work Done

## Known Risks or Open Questions

## Specific Questions for the Reviewer
```

Keep the request file free of interpretation so blind review stays blind. Do
not list the framing file under Artifacts to Inspect.

---

## Step 2: Reviewer Reads and Critiques

The reviewer reads:

1. the request file (header and artifact list);
2. the stage package and listed artifacts;
3. the stage reviewer file:
   - Planning → `planning-reviewer-agent.md`
   - Modeling → `modeling-reviewer-agent.md`
   - Reporting → `reporting-reviewer-agent.md`
   - Reviewing → `reviewing-reviewer-agent.md`
4. the decision log, to check that consequential choices in the package were
   authorized;
5. in **standard** mode, the framing file before critiquing; in **blind** mode,
   only after writing the independent findings. A blind reviewer that opens the
   framing early must say so at the top of the critique.

**File**: `<run_dir>/reviewer-critique-<stage>.md`

```markdown
# Reviewer Critique

- Stage: [Planning / Modeling / Reporting / Reviewing]
- Reviewer agent: <agent name>
- Assignment confirmed: [yes / mismatch: details]
- Gate mode acknowledged: [real / synthetic / mixed]
- Review mode: [standard / blind]
- Date: <date>

## Findings

| Finding ID | Severity | Concern | Evidence or reasoning | Route | Blocks gate? | Recommended action |
|---|---|---|---|---|---|---|
| PR-1 | blocker / major / minor / suggestion / accepted limitation | | | Planning / Modeling / Reporting / Reviewing / Terminate / user decision | yes / no | |

## Follow-Up Findings (blind mode only)

Findings added after reading the researcher's framing. Same table format;
continue the ID sequence.

## Reconfiguration Signals

Optional. Patterns that suggest the Decision-Rights Map no longer fits (see
`docs/coordination.md#adaptive-reconfiguration`).

## Overall Assessment

<one short paragraph: ready for the gate as-is, ready after minor fixes, or
needs substantial revision>
```

### Finding IDs and table format

All stages use the same seven-column table. Only the ID prefix changes:

| Stage | Prefix |
|---|---|
| Planning | `PR-` |
| Modeling | `MR-` |
| Reporting | `RR-` |
| Reviewing | `RVR-` |

### Assignment mismatch

If the request names a different reviewer than `workflow.config.json` and does not
cite a user override, the reviewer still writes the critique but records the
mismatch as the first finding (severity `major`, route `user decision`). The
user decides whether the pass counts.

---

## Step 3: Researcher Responds

The researcher adds a **Response to Reviewer** section to the stage package.
Each finding gets one response:

- **Accepted and fixed**: what changed
- **Accepted but deferred**: why, and the revisit trigger
- **Rejected with reason**: why the finding is wrong or out of scope
- **Needs user decision**: escalated directly

**Escalation rule.** A `blocker` or `major` finding that is deferred or rejected
is escalated to the user. The researcher adds it to the decision log's Open
Escalations table and quotes the reviewer's original wording at the gate. Only
the user can uphold the researcher's response.

The researcher then presents the gate using the substantive gate presentation
in [../coordination.md](../coordination.md#substantive-gate-presentation).

---

## Skipped Reviewer Pass

If the reviewer pass is skipped, the researcher records in the stage package and
the decision log:

- why the pass was skipped and who decided
- the accepted risk
- the revisit trigger

A skipped pass does not block the gate, but the gate presentation must say so.

---

## File Conventions

- Keep review requests and critiques after the stage completes.
- For revision passes, append `-r2`, `-r3`, etc.:
  `<run_dir>/review-request-<stage>-r2.md`, `<run_dir>/reviewer-critique-<stage>-r2.md`.
- Reviewer process logs (for example headless stdout) go in `<run_dir>/agent/`,
  not next to the critique.
- Informal early-look reviews use `<run_dir>/early-look-<n>.md` and are recorded
  in the decision log as `informal review`; they do not replace the formal pass.
- Critiques are input to the researcher's response. They are not stage packages
  and never count as gate approval.
