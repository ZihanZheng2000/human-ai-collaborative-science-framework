# Reviewer Agents

Reviewer-agent files define critique-only work for each stage. They are not
stage packages and they do not replace user gates. They tell a separate reviewer
agent what to inspect before the researcher agent responds and asks the user for
the stage gate decision.

Default rights (see `../decision-rights.md#reviewer-rights`):

```text
Reviewer agents critique and may escalate.
Reviewer blockers and majors cannot be rejected or deferred by the researcher alone;
they go to the user.
Reviewer agents never approve gates and do not modify files unless the user
explicitly authorizes a specific edit.
Researcher agents own the stage package and the response to review.
```

Stage reviewer files:

| Stage | Reviewer file | Reviewed package | Default review mode | ID prefix |
|---|---|---|---|---|
| Planning | `planning-reviewer-agent.md` | `templates/plan-package.md` | standard | `PR-` |
| Modeling | `modeling-reviewer-agent.md` | `templates/model-package.md` | standard | `MR-` |
| Reporting | `reporting-reviewer-agent.md` | `templates/reporting-package.md` | standard | `RR-` |
| Reviewing | `reviewing-reviewer-agent.md` | `templates/review-package.md` | blind | `RVR-` |

Every stage uses the same findings table:

| Finding ID | Severity | Concern | Evidence or reasoning | Route | Blocks gate? | Recommended action |
|---|---|---|---|---|---|---|

- severity: blocker / major / minor / suggestion / accepted limitation
- route: Planning / Modeling / Reporting / Reviewing / Terminate / user decision

See `cross-agent-handoff.md` for the request and critique file formats,
including blind review mode.
