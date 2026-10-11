"""Prompts the engine sends to agents.

Every agent session starts fresh. Continuity comes from the shared research
state on disk (README status block, decision log, packages, inbox), which each
prompt tells the agent to read first.
"""

from pathlib import Path

STAGE_DOCS = {
    "planning": ("docs/plan-stage.md", "templates/plan-package.md", "planning-package.md"),
    "modeling": ("docs/model-stage.md", "templates/model-package.md", "modeling-package.md"),
    "reporting": ("docs/reporting-stage.md", "templates/reporting-package.md", "reporting-package.md"),
    "reviewing": ("docs/review-stage.md", "templates/review-package.md", "reviewing-package.md"),
}

CHECKPOINT_PROTOCOL = """\
## How to ask the user (Tier 1 decision checkpoints)

You cannot talk to the user directly. Every Tier 1 decision class in
{fw}/docs/decision-rights.md that you settle needs the user, including choices to
skip, defer, or lighten a planned check (prior-work depth, venue calibration,
tool scan) and the output route. Write one file per decision (closely related
minor choices may share one file) to
`{inbox}/pending/CP-{stage}-<n>.md` using `{fw}/templates/checkpoint-request.md`
(sections: Decision needed, Proposal, Evidence, Alternatives, Open objections,
Reversibility, Options with the recommended option first, and an empty
Decision section). Then stop. The orchestrator will collect the answer, record
it in the decision log, and start you again with the answer.

{mode_rule}

Do not write decision-log rows that record a user approval; the orchestrator
writes those. You maintain the Open Escalations and Deferred Items tables.
"""

MODE_RULES = {
    "step-by-step": "Workflow mode is step-by-step: stop after each Tier 1 checkpoint file you write.",
    "auto-until-needed": (
        "Workflow mode is auto-until-needed: continue working where you can, batch the Tier 1 "
        "checkpoints you need into the inbox, and stop when you cannot proceed without answers."
    ),
}


def files_for(stage: str, revision: int) -> dict:
    suffix = "" if revision == 1 else f"-r{revision}"
    return {
        "request": f"review-request-{stage}{suffix}.md",
        "framing": f"review-framing-{stage}{suffix}.md",
        "critique": f"reviewer-critique-{stage}{suffix}.md",
        "gate": f"gate-request-{stage}{suffix}.md",
    }


def researcher_work(ctx: dict) -> str:
    stage = ctx["stage"]
    spec, template, package = STAGE_DOCS[stage]
    f = files_for(stage, ctx["revision"])
    handoff = (
        f"When the package is ready for review, write `{ctx['run_dir']}/{f['request']}` and "
        f"`{ctx['run_dir']}/{f['framing']}` (format: {ctx['fw']}/docs/reviewer-agents/cross-agent-handoff.md), "
        "update the README status block, and stop."
        if ctx["reviewer"] == "use"
        else f"The reviewer pass is skipped for this run. When the package is ready, record the skip "
        f"(reason, accepted risk, revisit trigger) in the package, write the gate request "
        f"`{ctx['run_dir']}/{f['gate']}` using `{ctx['fw']}/templates/gate-request.md`, and stop."
    )
    notes = ctx.get("notes") or "none"
    return f"""You are the RESEARCHER agent in the Human-AI Collaborative Science Framework.
You were started by the workflow orchestrator. Follow {ctx['fw']}/docs/agent-roles/researcher-role.md.

Working directory: the project folder ({ctx['project_abs']}). Paths without a
leading / are relative to it. Framework rules and templates (read-only): {ctx['fw']}
Project folder: .
Run directory: {ctx['run_dir']}
Current stage: {stage} (revision {ctx['revision']})
Stage specification: {ctx['fw']}/{spec}
Package template: {ctx['fw']}/{template}
Package to create or revise: packages/{package}
Gate mode: {ctx['gates']} gates
Agent assignment for this run: {ctx.get('config', 'workflow.config.json')} (this
snapshot, not the repository's workflow.config.json, is what this run uses)

The user's research request (verbatim):
{ctx.get('topic') or '(see the project README)'}

Start by reading the project's README.md status block, decision-log.md, the
inbox/answered/ folder, and any earlier stage packages. These are the shared
research state; you have no memory of earlier sessions.

Messages from the user or orchestrator for this session:
{notes}

{CHECKPOINT_PROTOCOL.format(inbox='inbox', fw=ctx['fw'], stage=stage, mode_rule=MODE_RULES[ctx['mode']])}
## Your task now

Do the {stage} stage work. Before any review request, check every sentence of
the package and any deliverable against the claim-evidence map and the
authorized claim level. {handoff}
"""


def researcher_triage(ctx: dict) -> str:
    stage = ctx["stage"]
    _, _, package = STAGE_DOCS[stage]
    f = files_for(stage, ctx["revision"])
    return f"""You are the RESEARCHER agent in the Human-AI Collaborative Science Framework.
You were started by the workflow orchestrator. Follow {ctx['fw']}/docs/agent-roles/researcher-role.md.

Working directory: the project folder ({ctx['project_abs']}). Paths without a
leading / are relative to it. Framework rules and templates (read-only): {ctx['fw']}
Project folder: .
Run directory: {ctx['run_dir']}
Current stage: {stage} (revision {ctx['revision']}), step: respond to review

Read the README status block, decision-log.md, and the reviewer critique
`{ctx['run_dir']}/{f['critique']}`.

1. Triage every finding (accepted and fixed / accepted but deferred / rejected
   with reason / needs user decision) in the package's response section of
   `packages/{package}`. Fix what you accept.
2. Add every deferred or rejected blocker or major finding to the decision
   log's Open Escalations table, quoting the reviewer's wording.
3. Write the gate request `{ctx['run_dir']}/{f['gate']}` using
   `{ctx['fw']}/templates/gate-request.md`: decision needed and recommendation, what was
   done, evidence to inspect, open objections (escalated findings verbatim),
   alternatives, consequence of approval, and options with the recommended
   option first. Leave the Decision section empty.
4. Update the README status block and stop.

If a fix needs a Tier 1 decision first, use the checkpoint protocol below and
stop instead of writing the gate request.

{CHECKPOINT_PROTOCOL.format(inbox='inbox', fw=ctx['fw'], stage=stage, mode_rule=MODE_RULES[ctx['mode']])}"""


def reviewer_cli(ctx: dict, blind_pass: str) -> str:
    stage = ctx["stage"]
    f = files_for(stage, ctx["revision"])
    reviewer_file = f"{ctx['fw']}/docs/reviewer-agents/{stage}-reviewer-agent.md"
    if blind_pass == "independent":
        framing_rule = (
            "This is a BLIND review, independent pass. The researcher's framing file is withheld. "
            "Write the critique with your independent findings, and leave the Follow-Up Findings "
            "section saying 'pending second pass'."
        )
    elif blind_pass == "follow-up":
        framing_rule = (
            f"This is the BLIND review follow-up pass. Your independent findings are already in "
            f"`{ctx['run_dir']}/{f['critique']}`. Now read `{ctx['run_dir']}/{f['framing']}` and replace "
            "the Follow-Up Findings section with findings that respond to the researcher's framing. "
            "Do not change the independent findings."
        )
    else:
        framing_rule = f"Standard review: read `{ctx['run_dir']}/{f['framing']}` before critiquing."
    output_rule = (
        f"Write the critique to `{ctx['run_dir']}/{f['critique']}`."
        if ctx["reviewer_output"] == "file"
        else "Print the complete critique markdown to standard output; the orchestrator saves it."
    )
    return f"""You are the REVIEWER agent in the Human-AI Collaborative Science Framework.
You were started by the workflow orchestrator. Follow {ctx['fw']}/docs/agent-roles/reviewer-role.md.

Working directory: the project folder ({ctx['project_abs']}). Paths without a
leading / are relative to it. Framework rules and templates (read-only): {ctx['fw']}

Stage: {stage} (revision {ctx['revision']})
Agent assignment for this run: {ctx.get('config', 'workflow.config.json')}
Review request: {ctx['run_dir']}/{f['request']}
Stage reviewer file: {reviewer_file}
Decision log: decision-log.md

{framing_rule}

Read {ctx['fw']}/docs/decision-rights.md, {ctx['fw']}/docs/coordination.md, and
{ctx['fw']}/docs/reviewer-agents/cross-agent-handoff.md, then the request, the stage
package, the decision log, and the listed artifacts. {output_rule}
Do not modify any other file.
"""


def reviewer_api_system(repo_root: Path, stage: str) -> str:
    parts = []
    for rel in [
        "docs/agent-roles/reviewer-role.md",
        f"docs/reviewer-agents/{stage}-reviewer-agent.md",
        "docs/reviewer-agents/cross-agent-handoff.md",
        "docs/decision-rights.md",
    ]:
        parts.append(f"<document path=\"{rel}\">\n{(repo_root / rel).read_text(encoding='utf-8')}\n</document>")
    return (
        "You are the REVIEWER agent in the Human-AI Collaborative Science Framework. You cannot "
        "open files: the orchestrator has included the files you need below and in the user "
        "message, and it will save your reply as the critique file. Reply with the complete "
        "critique markdown and nothing else.\n\n" + "\n\n".join(parts)
    )


def reviewer_api_user(stage: str, request_text: str, artifacts: list, blind_pass: str,
                      framing_text: str = "", independent_text: str = "") -> str:
    docs = "\n\n".join(
        f"<document path=\"{p}\">\n{t}\n</document>" for p, t in artifacts
    )
    if blind_pass == "independent":
        task = ("This is a BLIND review, independent pass: the researcher's framing is withheld. "
                "Write the full critique; in Follow-Up Findings write 'pending second pass'.")
    elif blind_pass == "follow-up":
        task = ("This is the BLIND review follow-up pass. Below are your independent critique and the "
                "researcher's framing. Reply with ONLY the replacement '## Follow-Up Findings' "
                "section (heading included).\n\n<independent_critique>\n" + independent_text +
                "\n</independent_critique>\n\n<researcher_framing>\n" + framing_text + "\n</researcher_framing>")
    else:
        task = ("Standard review. The researcher's framing:\n\n<researcher_framing>\n" + framing_text +
                "\n</researcher_framing>\n\nWrite the full critique.")
    return f"""Stage under review: {stage}

<review_request>
{request_text}
</review_request>

{docs}

{task}"""
