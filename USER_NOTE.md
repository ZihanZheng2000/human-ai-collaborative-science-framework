# User Note: Working with the AI Research Agents

This guide is for researchers who are not familiar with AI coding tools.
It explains what to expect at each stage, what to say to the AI, and how to
stay in control of your research.

---

## What This Workflow Does

You provide the research question, domain knowledge, and judgment. The AI agent
helps you plan, analyze, write, and review — but nothing moves forward without
your approval. Every stage ends with a gate where you decide what happens next.

---

## Before You Start: What to Prepare

The researcher agent should lead the workflow. You should not need to remind it
what step comes next. When it pauses, it should tell you the current stage, what
it just completed, the next concrete action, and the specific decision or input
it needs from you.

At the start of Planning, the researcher agent should not begin by asking a long
list of questions. It should first tell you what it thinks you want to do, how
it proposes to run the workflow, what package it will create, and what it will
do next. Your job is to confirm that understanding or correct the part that is
wrong. Once the goal is clear enough, the agent should start Planning rather
than keep asking low-value preference questions.

For a real research project, Planning should normally include a focused
literature/prior-work and novelty check before the Planning Package is treated
as ready. This can be light, but it should answer whether the idea has already
been studied, what adjacent work did, and whether the project is better framed
as a paper, demo, replication, tool, dataset, or internal report. If you only
confirm that the topic is interesting, that is not approval to start Modeling.

You do not need to write code. You do need to have ready:

- **A research question or topic**, even a rough one. The Planning stage will
  help you sharpen it.
- **Any domain materials you already have**: papers, reports, data files,
  policy documents, field notes. Put them in a folder you can point the AI to.
- **A rough idea of your output goal**: journal article, policy report, thesis
  chapter, slide deck, or something else. If you are not sure, the AI will ask.

For each new real research project, the researcher agent should create a
separate project folder under:

```text
research/<research-name>/
```

Inside that folder, stage packages, discussion notes, run artifacts, data,
code, figures, tables, deliverables, and archived files should be kept in their
own subfolders. This keeps one research project from getting mixed with another
and supports step-by-step discussion.

If your prompt is already clear enough, the AI should make a reasonable proposed
route and ask whether that is what you mean. It should not require you to design
the workflow before it begins.

---

## Starting a Session

There are two ways to run the workflow.

### Automatic (recommended)

The orchestrator passes work between the agents for you. You only answer when a
decision is yours to make.

1. Choose your agents in `workflow.config.json` (any mix of command-line agents
   such as Claude Code, Codex, or Gemini CLI, model APIs for the reviewer, or a
   person). `workflow.config.example.json` shows the options.
2. Start a project, describing the topic in your own words:

```text
python -m orchestrator init ~/papers/my-study --topic "describe your question, problem, or research idea in plain language"
python -m orchestrator run ~/papers/my-study
```

Run these from the framework folder. The project folder (`~/papers/my-study`
here) can be anywhere, including a folder that already has your data; the
agents work inside it.

3. You are asked three setup questions (workflow mode, reviewer strategy, gate
   mode). After that the agents work on their own. The run stops and asks you
   only at decision checkpoints, stage gates, and if something gets stuck.
4. If you would rather not wait at the terminal, type `later`, or run with
   `--inbox-only`. Open the file the orchestrator names in
   `research/my-project/inbox/pending/`, write your choice under **Decision**
   (a number, or your own words, plus any notes), and run the same command
   again. `python -m orchestrator status research/my-project` shows where
   things stand.

Every decision you make is written to the project's `decision-log.md` by the
orchestrator itself, so the agents cannot record an approval you did not give.

### Manual (talking to an agent directly)

You can also open Claude Code (or any agent) in your project folder and work
with it in conversation. When a stage package is ready for review, hand just
the review to the configured reviewer:

```text
python -m orchestrator review ~/papers/my-study --stage planning --run-id <run_id>
```


Open a new session with any AI agent and say only two things: what you want to
do, and what the topic is.

```text
You are the researcher agent. Read your instruction file (CLAUDE.md, AGENTS.md, or GEMINI.md) and workflow.config.json, then follow this repository's workflow starting with Pre-Planning Session Setup.
The topic is: [describe your question, problem, or research idea in plain language].
```

That is enough. The researcher agent should read the workflow instructions,
confirm its role, ask you to choose the workflow mode and reviewer strategy,
then propose a user-need profile for you to confirm or correct. You can add
domain materials, output goals, constraints, or target venue later when the
agent asks or when they become relevant.

If you just want to try the framework with a small test question first, use:

```text
python -m orchestrator init research/test-run --topic "[short test topic]"
python -m orchestrator run research/test-run
```

and choose "synthetic gates" at setup. Or, in a manual session:

```text
You are the researcher agent. Read your instruction file and workflow.config.json, then run a small framework smoke test with synthetic gates.
The topic is: [short test topic, or "choose one for me"].
```

---

## How Each Stage Works

The workflow has four stages. The AI runs each one and then stops to ask for
your decision before moving on.

| Stage | What the AI does | What you decide at the gate |
|---|---|---|
| **Planning** | Clarifies your question, scans prior work, checks feasibility, recommends a venue or output route, drafts a research plan | Is this the right direction? Can we proceed? |
| **Modeling** | Acquires data, runs analysis, produces figures and tables | Are the results correct and sufficient? |
| **Reporting** | Packages evidence, drafts the paper, report, or other deliverable | Is this ready for review? |
| **Reviewing** | Critiques the work and flags what needs fixing | What should be revised, accepted, or stopped? |

For real projects, the AI should begin with Planning only. Modeling, Reporting,
and Reviewing should not be treated as active work until the previous gate is
approved.

`<run_dir>` in this guide means `research/<research-name>/artifacts/<run_id>/`
(or `artifacts/<run_id>/` for a smoke test).

---

## Decisions Inside a Stage: Checkpoints

Gates are not the only time you decide. Inside each stage the AI will stop and
ask you about consequential choices — the research question wording, which
dataset to use, how an event or label is defined, which cases to exclude, which
metrics a model is judged by, how to interpret a result. These are **decision
checkpoints** (Tier 1 in `docs/decision-rights.md`).

At a checkpoint the AI should show you:

- what it proposes and what that changes
- the evidence and where to look at it
- the alternatives it considered
- any objections it knows about
- whether the choice is easy or hard to reverse

Routine choices (file names, code structure, retries) the AI makes on its own.
If you think a choice the AI made alone should have come to you, say so — that
is useful feedback and gets recorded.

Choices that shape the analysis (labels, exclusions, metrics, model search
space) are fixed **before** the AI sees results. If they change afterward, the
AI must tell you that results were already visible.

Every checkpoint and gate decision is written to the project's
`decision-log.md`. The top of the project's `README.md` shows the current
status: stage, last decision, open escalations, and the next action.

```text
Show me the decision log entries for this stage.
```

---

## At the Gates: What to Say

At the end of each stage, the AI will present a **gate decision**. It should
include:

- what decision is needed and what the AI recommends
- what was done and where the stage package is
- three to five files worth opening to check the evidence
- **open objections**: any reviewer finding the AI did not fully fix, in the
  reviewer's own words, and the AI's reason
- the alternatives and what approval will cause

If the AI rejected or postponed a serious reviewer finding (blocker or major),
you decide whether that response stands:

```text
On PR-3, I do not accept your reason. Fix it before the gate.
```

If something is missing from the gate summary, you can ask for more checks
before deciding:

```text
Before I decide, show me the reviewer's original findings and the evidence for
the main result.
```

Then choose one:

When the chat interface supports structured choices, the AI should show
clickable options for the gate, such as approve, revise, or backtrack. You can
still type a condition or correction instead of choosing one of the buttons.

**Approve and continue**
```text
Approved. Please proceed to [Modeling / Reporting / Reviewing].
```

**Approve with a condition**
```text
Approved, but before you start Modeling, please change the data source to [X]
and narrow the scope to [Y].
```

**Ask for a revision first**
```text
Not ready yet. Please revise the research question — it is too broad.
Focus on [specific aspect] and come back to the gate.
```

**Backtrack to an earlier stage**
```text
Let's go back to Planning. The data source identified in Modeling does not
exist in the format we assumed. We need to change the method.
```

**Stop the project**
```text
Please terminate. The data required for this question is not publicly
available and we cannot proceed.
```

---

## Providing Your Own Domain Materials

The AI's knowledge of non-CS domains has gaps. You can fill these gaps by
providing your own materials: papers you trust, domain reports, field notes,
data dictionaries, or background documents.

At the start of Planning, the AI will ask whether you have domain materials.
This is called **Domain Onboarding** — the AI reads your materials first,
extracts field norms and method patterns into skill cards, and then uses that
knowledge to calibrate everything that follows: the literature scan, the
research plan, the method choice, and the output format.

**Standard folder for domain materials:**

```
research/<research-name>/artifacts/input/domain-materials/
```

For example: `research/water-quality-2026/artifacts/input/domain-materials/`

**What to put there:**

- domain papers or preprints (especially ones not easily found by web search)
- government or institutional reports and technical standards
- data dictionaries, codebooks, or data documentation
- field notes, interview summaries, or expert briefings
- prior project materials or draft manuscripts

**How to tell the AI about your materials:**

```text
I have domain background materials in research/<research-name>/artifacts/input/domain-materials/.
Please read them before writing the research plan and tell me what you
extracted from them.
```

**What the AI will give back:**

- a Domain Knowledge Summary: what it learned from your materials that
  changes or constrains the plan
- skill cards: reusable patterns extracted from your materials
- any conflicts between your materials and published literature, flagged
  for your decision

**Adding materials mid-project:**

You can provide materials at any stage, not only at the beginning.

```text
I am adding a report to research/<research-name>/artifacts/input/domain-materials/.
Please read [filename] and tell me if it changes any assumptions
in the current plan.
```

**Correcting the AI when it is wrong about your domain:**

```text
That assumption is incorrect for this field. See the document at [path].
Please re-read section [X] and revise.
```

---

## Giving Feedback and Redirecting the AI

You are in control at all times. You do not need to wait for a gate to give
feedback. Useful things to say mid-stage:

**Correct a wrong assumption**
```text
That is not how this works in [your domain]. In practice, [explain the real
situation]. Please revise the plan with this in mind.
```

**Narrow or expand the scope**
```text
The scope is too broad. Focus only on [specific population / time period /
geographic area].
```

**Flag a data problem**
```text
The dataset you identified is behind a paywall and I do not have access.
Please find an alternative or adjust the method.
```

**Ask for a simpler output**
```text
For now, I only need a short summary report, not a full journal manuscript.
Please target that output instead.
```

**Ask for an explanation**
```text
I do not understand the analysis method you chose. Please explain it in plain
language and tell me why it suits my research question.
```

---

## When Something Goes Wrong

**The AI makes a confident claim about your domain that is wrong.**
Correct it directly and ask the AI to revise. Provide a source or your own
expertise as evidence. The AI should not override your domain judgment.

**The AI skips a step or moves too fast.**
```text
Please stop. We have not finished [Planning / Modeling]. Go back and
complete [specific missing item] before continuing.
```

For example:
```text
Please stop. We have not finished Planning. Before writing the final Planning
Package or moving to Modeling, do a focused literature/prior-work scan and tell
me whether this idea has already been done, what gap remains, and whether it is
worth pursuing.
```

**The AI waits for you to manage the workflow.**
```text
Please lead the workflow according to your instruction file. Tell me the current stage,
the current package path, the next action you will take, and the decision you
need from me before proceeding.
```

**The AI produces output that looks like a report summary, not a real paper.**
```text
This reads like a summary, not a manuscript. The [Introduction / Discussion /
Conclusion] needs a proper argument, not bullet points. Please revise using
the structure expected for [target venue].
```

**The AI cannot find usable data.**
```text
We need to revise the data strategy. Return to Planning and propose three
alternative data sources with their access conditions.
```

**You are not sure what just happened.**
```text
Please summarize what stage we are in, what has been completed, what the
current package contains, and what the next step is.
```

---

## Changing Who Does What

Sometimes the problem is not the research but how the work is divided. Signs:
you keep correcting the AI on the same domain point; the same kind of decision
keeps coming back; the reviewer keeps flagging the same area; or the project's
real focus has changed. You can ask for a change in how the collaboration is
organized (a **reconfiguration**):

```text
I keep correcting the label definitions. From now on, propose options only and
let me (or [domain expert]) decide labels. Record this in the decision log.
```

```text
Switch to step-by-step discussion for the rest of Modeling.
```

The AI should also propose such a change on its own when it sees these signs.

---

## What You Should NOT Delegate to the AI

- **Final judgment on your research question**: the AI can sharpen it, but the
  question must reflect your domain expertise and goals.
- **Verification that cited papers exist and say what the AI claims**: always
  spot-check citations in the final deliverable.
- **Approval of results you do not understand**: if you cannot explain why a
  result makes sense, ask the AI to explain it before approving the gate.
- **Ethics and compliance decisions**: the AI will flag risks, but institutional
  approval, data access rights, and authorship decisions are yours.

---

## Talking to the Researcher Agent

The researcher agent owns the stage packages and runs the workflow. It does
most of the work. You direct it, correct it, and approve or reject its output.

### Starting or Handing Off to the Researcher

At the beginning of a session, or after the reviewer has finished its critique:

```text
You are the researcher agent. Read your instruction file (CLAUDE.md,
AGENTS.md, or GEMINI.md).

We are currently in [Planning / Modeling / Reporting / Reviewing].
The current stage package is at [path].
```

If continuing after a reviewer critique:

```text
The reviewer critique is at <run_dir>/reviewer-critique-<stage>.md.
Please read it, triage each finding, update the stage package, and then
present the gate to me.
```

### Directing the Work

**Set a clear goal before the stage begins:**
```text
Before you start Modeling, confirm the Modeling Goal in one sentence.
Do not proceed until I have approved it.
```

**Keep the AI on track mid-stage:**
```text
Pause and tell me: what have you completed, what is still pending, and
what is the next concrete step?
```

**Stop an action before it happens:**
```text
Stop before [running the analysis / writing the draft / moving to the next
stage]. I need to review [specific item] first.
```

### Correcting Domain Errors

**When the AI gets domain knowledge wrong:**
```text
This is incorrect for [your field]. In [your domain], [correct explanation].
Please revise [specific section / assumption / method] using this information.
```

**When the AI uses the wrong method:**
```text
The method you selected is not standard in this field. The conventional
approach is [method name]. Please revise the modeling contract to use it.
If you are unsure how to apply it, I will explain.
```

**When a result looks suspicious:**
```text
I am not confident this finding is correct. Please show me:
1. the exact source data or artifact it comes from
2. the calculation or analysis step that produced it
3. any validation you have run on it
Do not move forward until this is verified.
```

### Providing Materials Mid-Stage

```text
I am adding domain materials to research/<research-name>/artifacts/input/domain-materials/.
Before continuing, please read [specific file or folder] and tell me
what you extracted from it that is relevant to our research plan.
```

```text
I have a paper that directly addresses our research gap. It is at [path].
Please read it and tell me: does it change our novelty claim?
If yes, revise the plan accordingly. If no, explain why.
```

### Adjusting Scope or Direction

**Narrow the scope:**
```text
The current scope is too broad. Please revise the research question to focus
only on [specific population / time period / geography / variable].
Update the Plan Package and come back to me before continuing.
```

**Change the output type:**
```text
We no longer need a journal manuscript. Change the target output to
[policy report / slide deck / technical appendix]. Revise the venue
calibration and reporting plan accordingly.
```

**Change the data source:**
```text
The dataset you identified is not accessible. Please find an alternative
that meets the acquisition success rule. Propose two options with their
access conditions and wait for my decision before proceeding.
```

---

## Talking to the Reviewer Agent

The reviewer agent critiques only. It does not change the research direction
and does not approve gates. You engage with it to get a sharper, more focused
critique — and to decide which findings the researcher should act on.

### Starting a Reviewer Session

Open a new session with the reviewer agent and say:

```text
You are the reviewer agent. Read your instruction file (CLAUDE.md,
AGENTS.md, or GEMINI.md).

Please review the [Planning / Modeling / Reporting / Reviewing] package.
The review request is at <run_dir>/review-request-<stage>.md.
Read the stage package and supporting artifacts listed there.
Write your critique to <run_dir>/reviewer-critique-<stage>.md.
Critique only — do not modify any files.
```

The review request says whether this is a **standard** or **blind** review. In
blind mode the reviewer forms its own findings before reading the researcher's
summary and questions, which makes it harder for the researcher's framing to
hide a problem. Reviewing uses blind mode by default; you can ask for it at any
stage.

If you want to focus the review:

```text
Pay particular attention to: [data provenance / claim strength /
method validity / citation support / a specific section].
```

### Getting Sharper Findings

**If a finding is too vague:**
```text
Finding PR-[N] is not specific enough. What exactly is wrong, and
where in the package does the problem appear? Please restate it with
a concrete example and a clearer recommended action.
```

**If you want the reviewer to prioritize:**
```text
We have limited time. Which two or three findings do you consider
blockers that would prevent us from moving forward? Focus on those.
```

**If the reviewer missed something:**
```text
Please also review [specific section / claim / data source].
I am concerned that [specific issue] has not been checked.
Add any findings on this to your critique file.
```

### Disagreeing with a Finding

```text
I disagree with finding PR-[N]. In this domain, [explanation of why
the finding does not apply or is already addressed]. Please mark this
as an accepted limitation or withdraw the finding, and explain your
revised assessment.
```

```text
Finding PR-[N] is correct but not fixable within the current scope.
Please mark it as an accepted limitation with the reason:
[explanation]. We will disclose it in the Reporting stage.
```

### Authorizing the Reviewer to Edit

By default the reviewer agent does not modify files. If you want it to
fix something directly:

```text
I authorize you to fix finding PR-[N] directly. Please make only
that change to [specific file], record what you changed, and then
stop. Do not make any other edits.
```

### Closing the Reviewer Session

Once the reviewer has written its critique:

```text
Your critique is complete. Please summarize in two or three sentences:
overall, is this stage package ready for the gate, and what is the
single most important issue the researcher needs to address?
```

---

## Switching Between Agents: Session Script (manual runs only)

In automatic runs the orchestrator does this for you. In manual runs the
researcher and reviewer are separate sessions (they can be different products),
so you hand off context explicitly. Use these scripts each time you switch.

**Researcher → Reviewer** (after researcher finishes a stage):

```text
You are the reviewer agent. Read your instruction file (CLAUDE.md, AGENTS.md, or GEMINI.md).
The researcher has completed the [stage] package.
The review request is at <run_dir>/review-request-<stage>.md.
Please critique and write findings to <run_dir>/reviewer-critique-<stage>.md.
Critique only — do not modify any files.
```

**Reviewer → Researcher** (after reviewer writes critique):

```text
You are the researcher agent. Read your instruction file (CLAUDE.md, AGENTS.md, or GEMINI.md).
The reviewer has finished. Read <run_dir>/reviewer-critique-<stage>.md.
Triage each finding, update the [stage] package with the response-to-reviewer
section, and then present the gate to me.
```

**If you want to tell the researcher your position on specific findings before it triages:**

```text
Before you update the package, here is my position on the reviewer findings:
- PR-1: Accept and fix. [Any guidance on how.]
- PR-2: Accept as limitation. Disclose in the Reporting stage.
- PR-3: Reject. [Reason.]
- PR-4: I need your recommendation before deciding.
Now triage the rest and update the package.
```

---

## Quick Reference: Useful Phrases

| Situation | What to say |
|---|---|
| Start a session | See "Starting a Session" above |
| Approve a gate | `Approved. Proceed to [next stage].` |
| Reject a gate | `Not ready. Please revise [specific item].` |
| Provide materials | `Read the files in [folder path] before continuing.` |
| Correct the AI | `That is wrong for this domain. [Explanation]. Please revise.` |
| Pause the workflow | `Stop here. I need to check [X] before we continue.` |
| Ask for status | `Where are we? Summarize the current stage and what is next.` |
| Change the output type | `Change the target output to [report / slides / preprint].` |
| Backtrack | `Go back to [Planning / Modeling]. The reason is [X].` |
| Hand off to reviewer | See "Switching Between Agents" above |
| Hand off to researcher | See "Switching Between Agents" above |
| Tell researcher your view on findings | See "Switching Between Agents" above |
