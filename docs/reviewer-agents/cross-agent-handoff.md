# Cross-Agent Handoff Protocol

This document defines how the researcher agent and reviewer agent exchange work
inside each stage's maker-checker loop. It implements the Tier 2 accountability
loop described in [../coordination.md](../coordination.md); the reviewer's
rights are defined in [../decision-rights.md](../decision-rights.md#reviewer-rights).

`WORKFLOW-CONFIG.md` sets the default assignment:

| Config | Researcher agent | Reviewer agent |
|---|---|---|
| A | Codex | Claude Code |
| B | Claude Code | Codex |

The protocol is the same for both configs.

## Run Directory

`<run_dir>` below means:

- real research project: `research/<research-name>/artifacts/<run_id>/`
- framework smoke test or legacy run: `artifacts/<run_id>/`

`<run_id>` is a descriptive slug that stays the same for every file in the run,
for example `water-env-plan-v1` or `smoke-test-2026-06-28`.

---

## The Loop

```
[researcher] drafts or revises the stage package
  -> [researcher] writes <run_dir>/review-request.md
  -> [reviewer]  reads the request (blind mode: only the header) and the package
  -> [reviewer]  writes <run_dir>/reviewer-critique.md
  -> [researcher] triages each finding, updates the package, logs escalations
  -> [researcher] presents a substantive gate to the user
  -> user approves, revises, backtracks, or terminates
```

---

## Step 1: Researcher Writes the Review Request

**File**: `<run_dir>/review-request.md`

The request is the authoritative assignment for this pass. If its reviewer
assignment differs from `WORKFLOW-CONFIG.md`, it must cite the decision-log entry
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
- Researcher agent: [Codex / Claude Code]
- Reviewer agent: [Codex / Claude Code]
- Assignment source: [WORKFLOW-CONFIG.md / user override D-<n>]
- Reviewer rights: advisory + escalation (default) / other per Decision-Rights Map
- Date: <date>

## Artifacts to Inspect

<paths to the package, data, figures, run logs, scripts, and deliverables the
reviewer should open; no researcher commentary here>

## Researcher Framing

<!-- In blind mode the reviewer reads this section only after writing
independent findings. -->

### Summary of Work Done

### Known Risks or Open Questions

### Specific Questions for the Reviewer
```

Keep **Artifacts to Inspect** free of interpretation so blind review stays blind.

---

## Step 2: Reviewer Reads and Critiques

The reviewer reads:

1. the request **Header** and **Artifacts to Inspect**;
2. the stage package and listed artifacts;
3. the stage reviewer file:
   - Planning → `planning-reviewer-agent.md`
   - Modeling → `modeling-reviewer-agent.md`
   - Reporting → `reporting-reviewer-agent.md`
   - Reviewing → `reviewing-reviewer-agent.md`
4. the decision log, to check that consequential choices in the package were
   authorized;
5. in **standard** mode, the Researcher Framing section before critiquing; in
   **blind** mode, only after writing the independent findings.

**File**: `<run_dir>/reviewer-critique.md`

```markdown
# Reviewer Critique

- Stage: [Planning / Modeling / Reporting / Reviewing]
- Reviewer agent: [Codex / Claude Code]
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

If the request names a different reviewer than `WORKFLOW-CONFIG.md` and does not
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
  `<run_dir>/review-request-r2.md`, `<run_dir>/reviewer-critique-r2.md`.
- Informal early-look reviews use `<run_dir>/early-look-<n>.md` and are recorded
  in the decision log as `informal review`; they do not replace the formal pass.
- Critiques are input to the researcher's response. They are not stage packages
  and never count as gate approval.
