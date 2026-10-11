# Planning Stage Specification

## Purpose

The Planning stage converts a vague or concrete user research intent into one approved research plan package. It is designed for non-CS researchers and should avoid writing a polished plan before the system has understood the user's purpose, checked prior work, extracted useful research patterns, and tested feasibility.

There is only one Planning stage. The stage may contain early discovery work, but that discovery is not a separate plan. It is the evidence-gathering and clarification required before the final **Approved Planning Package** is written.

For framework validation, Plan may be run in **Smoke-Test Mode**. Smoke-Test Mode uses the same logic but deliberately selects a small, low-risk, low-cost project so the whole workflow can be exercised end to end. It should label gates as real user gates or synthetic gates, and it may use the compact `../templates/smoke-test-package.md` instead of the full Planning, Modeling, Reporting, and Reviewing packages.

## Core Principle

Plan is **purpose-first, literature-calibrated, skill-aware, feasibility-aware, and creativity-preserving**.

The system should not begin by generating candidate plans from general AI intuition. It should first clarify what the user actually wants to accomplish, then use prior work to understand whether the idea has been attempted, where the gap is, and which methods or validation patterns can be reused. Only after that should it generate a compact plan that fits the user's resources and intended output.

Clarification should start by reflecting the user's intent back as a proposed
user-need profile with selectable answers, not by asking a broad interview. The
researcher agent should say what it thinks the project is, propose likely
answers for output type, audience, purpose, success criterion, data/source
direction, and avoid-list, then ask the user to confirm, correct, or add only
what is missing. Once the goal is clear enough to plan, the agent should proceed
to the Planning package instead of asking low-value preference questions.

Planning begins only after the Pre-Planning Session Setup choices have been
confirmed or safely inferred from the user's explicit request. Those choices are
workflow mode and reviewer strategy. They determine whether Planning should be
auto-until-needed or step-by-step discussion, and whether a reviewer-agent
critique is required before the Planning Gate.

Prior work should not be treated only as background. When useful, it should be converted into research-skill cards or skill candidates: reusable patterns for data acquisition, measurement, modeling, validation, visualization, or manuscript framing.

The Planning stage should also check whether mature external tools, packages, templates, databases, or existing skills already solve part of the intended workflow. The goal is to reuse reliable external capabilities where possible and create new skills only for workflow-control gaps or project-specific operations that are not already covered well.

## Researcher / Reviewer / Gate Flow

Planning uses a maker-checker pattern before the user gate:

```text
Planning researcher agent
Planning reviewer agent
Researcher-agent response/fix
User Gate
```

The planning researcher agent clarifies the research purpose, runs the selected
prior-work, tool, feasibility, and venue checks, then drafts the Planning Package.

The planning reviewer agent is a separate agent from the planning researcher
agent when available and approved by the user. Use
`reviewer-agents/planning-reviewer-agent.md` for the reviewer task. The reviewer
critiques only by default. It should not modify files unless the user explicitly
authorizes that agent to edit. Its job is to identify planning risks,
unsupported novelty or gap claims, feasibility weaknesses, source-strategy
problems, venue/output mismatches, and missing Modeling-stage acceptance criteria.

After reviewer feedback, the researcher agent must triage the findings before
the user gate:

- accepted and fixed
- accepted but deferred with a revisit trigger
- rejected with reason
- needs user decision

Blocker and major findings that the researcher defers or rejects are escalated
to the user; only the user can uphold that response (see
`decision-rights.md#reviewer-rights`).

Only after the researcher agent has recorded this response should the Planning
Gate be shown to the user. If no separate reviewer agent is available or the
user declines it, the Planning Package must say that the Planning Review was
skipped and why.

## Internal Flow

Before Planning: run the Pre-Planning Session Setup from
`../docs/stage-handoffs.md`. Confirm active role configuration, workflow mode,
and reviewer strategy.

0. Domain Onboarding — if user-supplied materials exist, read them and produce a domain knowledge summary before the literature scan
1. Propose a user-need profile with selectable answers, then ask the user to confirm, correct, or add missing details
2. Ask only unresolved decision-changing questions before continuing
3. Run a focused literature and prior-work scan by default for real research,
   unless the user explicitly chooses skip/defer and the package records the
   accepted risk and revisit trigger
4. Extract gaps, opportunities, and possible research routes from the prior-work scan
5. Classify idea maturity and choose planning depth using the user need plus literature evidence
6. Generate candidate research plans, if more than one route remains
7. Run feasibility and cost checks on the plausible routes
8. Calibrate target venue, audience, or output format using official requirements and exemplar articles
9. Select or confirm the research route, research question, and claim level,
   and draft the project's Decision-Rights Map
10. Scan for mature external tools, packages, templates, and existing skills for the selected route
11. Distill useful selected prior work into research-skill cards or skill candidates
12. Write the Planning Researcher draft package
13. Run the Planning Reviewer critique, when available and approved
14. Triage reviewer findings and revise or annotate the package
15. Human gate
16. Output one approved plan package

The final output should be one **Approved Planning Package**. It combines user need, literature basis, selected skill cards, research opportunity, venue/output calibration, research question, data plan, method blueprint, risks, feasibility notes, and Modeling-stage acceptance criteria. The goal is compact traceability: enough information to support human review and downstream modeling, but not so many artifacts that the workflow becomes hard to use.

## Stepwise Planning Mode

Planning should normally be collaborative and incremental, especially for broad
or unfamiliar research topics. The Planning package is the compact handoff, not
the place to paste every detailed review or source note.

Use stepwise mode when the user selects **Step-by-step discussion** during
Pre-Planning Session Setup, when the project is broad or uncertain, or when
choices about research question, evidence, method, source strategy, claim level,
or output route would materially shape the project.

In stepwise mode, the researcher agent should:

1. Create or revise a short Planning package skeleton.
2. Work on one Planning unit at a time:
   - user-need profile
   - research question and boundaries
   - domain problem taxonomy
   - source/literature strategy
   - method route
   - data/source feasibility
   - risk rubric
   - target output or venue route
3. Present each unit as a discussion artifact or note before treating it as
   accepted in the Planning package.
4. Put long reviews, literature matrices, search logs, and source annotations
   in supporting artifacts, then summarize only their implications in the
   Planning package.
5. Ask the user for a concrete next decision when a unit would shape the
   research route.
6. Treat each accepted unit that shapes the research as a Tier 1 decision
   checkpoint: append it to `decision-log.md` with the proposal, evidence,
   alternatives, open objections, and the user's decision (see
   `decision-rights.md`).

Only after the user has discussed or accepted the major Planning units should
the researcher consolidate them into a complete Planning package for reviewer
critique.

Do not skip or collapse Planning units in stepwise mode unless the user
explicitly authorizes the skip, defer, or merge. When a unit is skipped or
deferred, record the reason, accepted risk, and revisit trigger in the Planning
package.

## Planning Project Folder Setup

Each real research project has its own project folder (layout:
`research-organization.md`; the orchestrator creates it, and in manual runs
the default is `research/<research-name>/`). The active Planning package is
`packages/planning-package.md`, long Planning notes go in `notes/`, and review
requests and critiques go in `artifacts/<run_id>/`.

## 0. Domain Onboarding

This step runs before everything else **only when the user provides domain
materials**. If no materials are provided, skip to step 1.

Non-CS domain researchers often have internal knowledge, field-specific reports,
literature, or data that the AI has never seen or has outdated information about.
Domain Onboarding reads those materials first so the rest of Planning is
calibrated to the user's actual field rather than the AI's generic assumptions.

### When to Run

Run Domain Onboarding if the user provides any of the following:

- domain papers or preprints not easily found by web search
- government or institutional reports, policy documents, or technical standards
- internal datasets, codebooks, or data dictionaries
- field notes, interview transcripts, or domain expert summaries
- prior project materials, draft manuscripts, or previous analyses
- any file the user says is background for the research

If no materials are provided, ask the user once:

```text
Do you have any domain background materials — papers, reports, data
documentation, or field notes — that you would like me to read before
I start planning? If yes, please share the folder path or file location.
If no, we will begin with a literature scan using web search.
```

If the user says no or does not respond, proceed to step 1 without waiting.

### Procedure

1. Identify the user-supplied material folder or file list.
   Convention: `artifacts/input/domain-materials/` inside the project folder.
2. Read each file. For each, note:
   - material type (paper, report, data documentation, policy doc, field notes, other)
   - domain covered
   - key concepts, terminology, or field-specific definitions introduced
   - methods or measurement approaches described
   - datasets or data sources mentioned
   - field norms or conventions implied
   - constraints or limitations specific to this domain
3. Produce a **Domain Knowledge Summary**: a compact note of what the AI has
   learned from the materials that is not obvious from general training.
   Flag any domain-specific terms, conventions, or constraints that should
   govern Planning, Modeling, and Reporting decisions downstream.
4. Note possible reusable method and field-norm patterns from the user-supplied
   materials. Convert them into formal research-skill cards only after the
   research route is selected or narrowed in step 11.
5. Record all materials read in the Domain Onboarding inventory so the Plan
   Package is traceable.

### Guardrails

- Do not treat user-supplied materials as automatically correct. Note any
  internal contradictions, outdated figures, or domain-specific claims that
  will need verification.
- Do not skip materials because they are long. Summarize rather than ignore.
- Do not over-index on one document. If materials conflict, flag the conflict
  and ask the user which source takes precedence.
- Do not use the domain summary to narrow the research question without the
  user's approval. Use it to inform, not to constrain.

## 1. Propose and Confirm the User-Need Profile

The system should first propose a concise user-need profile with selectable
answers. The default interaction is not to ask open-ended questions. The
researcher agent should infer the most likely answer from the user's request,
offer it as a proposed choice, and leave room for the user to correct or add
details.

Use this pattern at the start of Planning:

```text
I understand you want to do X.
I propose to run this as Y.
The active stage is Planning, and I will create Z package.
If this is right, I will proceed. If not, please correct the part that is wrong.
```

Then present a compact proposed profile:

| User-need field | Proposed answer | Other common choices | User correction or addition |
|---|---|---|---|
| intended output | paper / report / demo / skill / dataset / tool / manuscript package | proposal / thesis chapter / policy note / internal decision brief | |
| target audience | academic readers / internal decision-makers / course / policy users / engineering users | public-facing readers / domain experts / reviewers | |
| project purpose | discover a pattern / build a method or tool / validate an intervention / revise an artifact / compare alternatives | workflow test / benchmark / replication | |
| useful result | evidence for a claim / reusable workflow / validated dataset / decision support / publishable package | proof of feasibility / negative result / limitations map | |
| data/source direction | use provided data / find public data / use literature only / build a corpus / no empirical data | API data / scraped documents / benchmark data | |
| avoid-list | no known exclusions / avoid specific data / avoid specific methods / avoid specific domains | avoid paid APIs / avoid private data / avoid black-box methods | |

The user should be invited to confirm the proposed row values or edit only the
parts that are wrong or missing. If a safe default is clear, record it and move
on instead of asking for preferences.

Output should be a short user-need profile, not a long interview transcript.

The researcher agent should not make a project-shaping choice silently. If it
chooses a default domain, data source, output route, or implementation location,
it must present that choice as a proposal before drafting a full plan around it.

## 2. Resolve Only Decision-Changing Unknowns

Before continuing, the system should ask concise questions only when
the answer would materially change the research design, output package, data or
source strategy, method, implementation location, gate mode, or claim level.
The goal is not a long interview. The goal is to avoid producing a polished
plan for the wrong task while still moving forward once the user's intent is
clear enough.

Instead of asking the user a list of questions, first write provisional answers.
Ask only about fields that remain genuinely unresolved after the proposed
profile.

Examples of unresolved items that may require a user answer:

- two output routes would imply different evidence standards
- data access, API cost, runtime, privacy, or licensing constraints are unknown
- the user mentions a required or forbidden method, source, or domain but not enough detail to act
- the intended claim level is unclear and would change literature or feasibility work
- the project may be a real research project or only a smoke test/demo

Avoid low-value questions whose answers would not change the next Planning
action. For example, do not ask the user to choose every folder, naming detail,
validation style, or minor preference before Planning if a safe default can be
recorded and revised later.

If reasonable assumptions are safe, state them and proceed. If an assumption
would change the research design, ask for confirmation before drafting the full
Planning package. If the user corrects the route, update the understanding and
then proceed; do not restart the interview from scratch.

## 3. Run a Focused Literature and Prior-Work Scan

Before producing the full plan, the system should run a focused scan to determine whether the idea has already been studied and how adjacent work solved similar problems.

For real research, this scan is the default Planning action after user-need
confirmation. It may be full, light, or explicitly deferred according to the
setup choice, user request, and project risk. It should be skipped only for
smoke tests, clearly mature user-directed work, or an explicit user instruction.
When skipped or deferred, record the reason, accepted risk, who accepted it,
and the downstream trigger for revisiting it.

This scan is not a full systematic review. It should answer:

- Has this question, method, tool, or intervention already been attempted?
- Which fields have done something structurally similar?
- What datasets, baselines, metrics, and validation designs did prior work use?
- Where is the gap: topic, data, method, validation, scale, transparency, or application?
- Is there enough prior work to support a manuscript, or is the idea better framed as a demo, method note, replication, tool paper, or internal report?

Retrieval should prioritize structurally similar work, not only topically similar work.

Useful similarity dimensions:

- same or adjacent topic
- same data source
- same outcome variable
- same method family
- same unit of analysis
- same target domain
- similar manuscript type
- recent review or survey papers

The goal is to learn how comparable work became research, not to collect citations for decoration.

## 4. Extract Gaps, Opportunities, and Possible Routes

For each group of related work, identify:

- research pattern: the study design or manuscript structure that repeats across papers
- research gap: what prior work has not yet done
- research opportunity: what could be changed, updated, localized, replicated, simplified, extended, or validated

Opportunity types:

- new region or population
- newer data period
- alternative data source
- additional variable
- simpler replication
- robustness check
- cross-domain comparison
- updated method
- tool or skill construction
- validation benchmark
- contradiction or unresolved debate

Ideas that are interesting but infeasible should be marked as future work, not forced into the active plan.

## 5. Classify Idea Maturity and Choose Planning Depth

Planning should not force every project through the same amount of idea
generation, novelty assessment, or literature review. Classify idea maturity
after the initial user-need profile and focused prior-work scan, so the label is
calibrated by evidence rather than guessed before literature is inspected.

Suggested idea maturity labels:

- **Exploratory idea**: the user has a broad direction but not a stable question, output, data source, or claim.
- **Partly formed idea**: the user has a question or method but still needs novelty, feasibility, or output-route calibration.
- **Mature idea**: the user already understands the domain and wants execution planning more than idea discovery.
- **Revision or implementation task**: the user already has an artifact and needs structured improvement, not new idea generation.

Planning depth options:

| Option | Use when | Expected planning work |
|---|---|---|
| Full calibration | idea is new, risky, manuscript-oriented, or novelty-sensitive | idea refinement, focused literature scan, novelty/gap assessment, feasibility, venue/output calibration |
| Light calibration | idea is familiar but still needs grounding | brief prior-work check, feasibility, risks, source/tool scan |
| Skip or defer | user is confident, doing a demo, or wants speed | record the skip/defer decision, assumptions, and when literature/novelty must be revisited |

If the user chooses to skip or defer prior-work and novelty checks, the Plan
Package should label the project as demo, internal, preliminary, or
user-specified mature. It should not later claim strong novelty unless the
required prior-work basis has been added.

## 6. Generate Candidate Research Plans

Generate a small number of plans, usually 2-3, only when multiple plausible
routes remain after the prior-work scan. If the user has clearly approved one
direction, write that plan directly.

Each candidate should include:

- working title
- research question
- closest related work
- prior-work patterns that may become skill cards later
- data needed
- method
- expected figures and tables
- feasibility rating
- novelty rating
- target venue/output fit
- likely external tools or skills to check after route selection
- main risks
- minimum viable manuscript scope

## 7. Run Feasibility and Cost Checks

Before committing to an approved plan, the system should check whether the plausible route can actually be executed.

The check should include:

- whether required data can be accessed, downloaded, or extracted
- whether candidate links are enough or actual usable files must be obtained
- the identity of the raw data host, official data source, documentation source, citation source, version, access date, and license or access terms
- whether text, tables, images, metadata, or APIs are directly extractable
- likely runtime and storage needs
- likely API or token cost, if LLM calls are needed
- minimum demo scale and preferred full-study scale
- fallback data, methods, or scope if the preferred route fails
- ethical, legal, licensing, or privacy constraints
- figure/table feasibility
- feasibility of external tools or skills selected for the workflow

For data-collection projects, the Planning stage should distinguish candidate sources from usable acquired data. A planned corpus, dataset, or validation set should specify what counts as acquisition success.

When the raw data host differs from the official data source or documentation source, the Planning Package should record that mismatch explicitly. Documentation for a newer or different version should not silently stand in for the exact data used.

## 8. Calibrate Target Venue, Audience, or Output Format

Venue or output calibration should happen after the system understands the purpose, prior work, and feasibility. It does not need to lock the project into one journal, but it should identify the intended target enough to shape scope, evidence standards, methods, length, citation style, figures, and novelty expectations.

The system should ask for:

- target journal, conference, preprint server, thesis chapter, course paper, policy outlet, internal report, or public-facing note
- target field or audience if no venue is known
- preferred language and citation style, if relevant
- expected manuscript length or compactness
- whether the user wants the system to recommend possible venues

If the user has no target venue, the system should recommend 2-3 plausible venue or output routes and explain tradeoffs. A journal route may require stronger literature coverage, robustness, formatting, and novelty. A preprint or short empirical note may allow a more transparent workflow demonstration with narrower claims. A policy note may prioritize readable figures, practical interpretation, and concise methods.

Venue calibration should be provisional. The Planning Package should record whether the target is confirmed by the user, system-recommended and accepted, provisional or undecided, or deferred to Reporting.

If a specific journal or conference is selected, the system should retrieve official author instructions during Plan when venue requirements may affect data, methods, validation, article type, or feasibility. If only formatting details remain, they may be deferred to Reporting.

Planning-stage venue calibration has two parts:

### Official Venue Requirements

Official author instructions should be used for hard constraints:

- article types and scope
- manuscript structure
- word or page limits
- abstract format
- reference style
- figure and table rules
- data and code availability requirements
- ethics, funding, conflict-of-interest, and AI-use disclosure requirements
- reporting checklists, if any
- supplementary material rules

### Venue Exemplar Scan

Official instructions rarely reveal the actual writing and evidence conventions of a venue. When the intended output is a journal article, conference paper, thesis chapter, or similar formal manuscript, the Planning stage should inspect 2-5 recent structurally similar articles from the target venue or candidate venues.

The exemplar scan should extract:

- article type used by similar work
- section structure and heading conventions
- Introduction and Related Work depth
- typical Methods detail
- number and type of main figures and tables
- whether method schematics, conceptual diagrams, workflow diagrams, or graphical abstracts are common
- citation density and reference-list scale
- Results ordering and figure-caption style
- Discussion depth, limitation placement, and comparison with literature
- data/code availability statement style
- disclosure, ethics, funding, and supplementary material patterns

The exemplar scan should affect the plan. If exemplar articles suggest that the venue expects stronger validation, larger data scale, more robust baselines, more literature grounding, or a different article type, the Planning Package should record that requirement before Model begins. If the current project cannot meet those expectations, the Planning stage should recommend a different venue, a narrower claim level, or a demo/preprint route.

## 9. Select or Confirm the Research Route

After literature, route generation, feasibility, and output calibration, select
or confirm the route to carry into the Planning Researcher draft. In
step-by-step discussion mode, present the selected route to the user before
extracting formal skill cards or writing the full draft.

The selected route should lock:

- working research question
- intended output and claim level
- selected or provisional data/source strategy
- method family
- feasibility status and known fallback
- target venue, audience, or output mode
- what will be treated as future work rather than active scope

If the route remains uncertain, stop and ask the user to choose among the
candidate routes rather than drafting a full package around an unapproved route.

### Draft the Decision-Rights Map

Once the route is selected, copy the default map from `decision-rights.md` into
the Planning Package and adjust it to the project:

- mark decision classes where the researcher or the user lacks the needed
  domain judgment, and say who supplies it (user materials, a named domain
  expert, or a deferred check);
- raise the tier of any decision with irreversible cost, safety, privacy, or
  public-release consequences;
- state reviewer rights (default: advisory + escalation) and which stages use
  blind review;
- list which analysis choices must be locked at a Tier 1 checkpoint before
  results are visible (labels, exclusions, metrics, model search space,
  validation split).

The map is itself a Tier 1 decision and is confirmed by the user before the
Planning package goes to the reviewer.

## 10. Scan for Mature External Tools, Packages, Templates, and Existing Skills

Before creating a new project skill or custom method for the selected route,
check whether a mature external capability already exists.

Potential external capabilities include:

- literature search and deep research tools
- academic databases and citation metadata APIs
- citation managers and reference-formatting tools
- journal templates, author guidelines, and reporting checklists
- systematic-review protocols and checklists
- statistical, modeling, visualization, and experiment-tracking packages
- document, spreadsheet, presentation, or bibliography tools
- established domain-specific analysis packages
- existing public skills, prompts, workflows, or software repositories

For each candidate, record:

- what workflow task it could handle
- whether it is mature enough to reuse
- what inputs and outputs it produces
- whether outputs can be verified
- licensing, cost, API, data, privacy, or runtime constraints
- whether it should be reused directly, wrapped by a workflow-native skill, adapted, or rejected

The Planning Package should distinguish:

- external mature tools to reuse
- workflow-native skills to invoke
- project-specific skills to create
- prior-work patterns that remain as notes rather than formal skills

Use `../docs/skill-strategy.md` for the decision rules.

## 11. Distill Selected Prior Work Into Research-Skill Cards or Skill Candidates

After the research route is selected or narrowed, convert only relevant prior
work into reusable patterns. Do not create broad skill cards for every paper
screened during literature search.

For each useful paper or cluster, extract:

- research design pattern
- data acquisition pattern
- preprocessing or measurement pattern
- baseline or control-group pattern
- modeling or analysis pattern
- validation or evaluation pattern
- figure/table pattern
- limitation or reviewer-risk pattern

Each formal skill card should be traceable to source papers and short enough
for a researcher to inspect quickly. Use the template in
`../templates/research-skill-card.md`.

Not every useful pattern needs to become a formal skill card. Some may remain as
model steps, validation rubrics, figure ideas, or manuscript constraints.

## 12. Planning Researcher Draft

Before reviewer-agent critique or the user gate, the researcher agent should
produce a Planning Researcher draft. The draft should be complete enough for
critique, but it is not approved yet.

The draft should include:

- user-need profile
- planning depth decision
- prior-work, novelty, and gap basis, or explicit skip/defer rationale
- external tool and skill scan
- feasibility and cost check
- data source identity plan
- venue or output calibration
- candidate routes, when relevant
- selected research question and method blueprint
- Decision-Rights Map
- decision-log references for each Tier 1 decision made during Planning
- Modeling-stage acceptance rubric

The package status should be `draft for Planning Review`, not `approved`.

## 13. Planning Reviewer Critique

The Planning Reviewer should inspect the draft before the user gate.

Reviewer criteria:

- Is the research purpose clear enough to plan Modeling?
- Is the idea maturity label plausible?
- Is the planning depth appropriate for the intended output?
- Does the prior-work scan support the proposed gap, or is the skip/defer decision honest?
- Are novelty, contribution, and target-output claims too strong?
- Are data sources realistic and distinguished from candidate links?
- Is the method feasible under time, tooling, runtime, cost, and licensing constraints?
- Are mature external tools reused where appropriate?
- Are proposed project-specific skills justified?
- Does the venue or output route fit the evidence standard?
- Are Modeling-stage acceptance criteria specific enough to prevent drift?
- What would force backtracking before Modeling?

Reviewer findings should include severity, evidence or reasoning, and a route:
Planning fix, Modeling constraint, user decision, accepted limitation, or
terminate.

## 14. Researcher-Agent Response to Planning Review

The researcher agent must respond to Planning Reviewer findings before the user
gate.

For each finding, record:

- finding ID
- reviewer concern
- severity
- response status: accepted and fixed / accepted but deferred / rejected with reason / needs user decision
- change made or planned
- whether the item blocks the Planning Gate

Blocker or major findings that are deferred or rejected are escalated: add them
to the decision log's Open Escalations and quote them at the gate.

The researcher agent may fix local plan-package issues, clarify assumptions,
soften claims, add fallback sources, tighten acceptance criteria, or mark
limitations. The researcher agent should not silently change the user's research
question, target output, data source strategy, method, or claim level without
surfacing that change at the user gate.

## 15. Human Gate

The user should approve, edit, reject, or combine candidate plans.

Gate questions:

- Is this the problem the researcher actually wants to study?
- Is the idea maturity label correct?
- Is the selected planning depth acceptable: full, light, or skip/defer?
- Does the prior-work scan support the proposed gap?
- Do the selected skill cards or prior-work patterns fit the domain?
- Are mature external tools being reused where appropriate?
- Are any proposed new skills actually necessary?
- Is the data realistically obtainable?
- Is the method acceptable?
- Is the scope too large or too small?
- Is the novelty sufficient for the intended output?
- Does the target venue, audience, or output format fit this plan?
- Have Planning Reviewer findings been fixed, deferred, rejected with reason, or escalated for user decision?
- Is any skipped external Planning Review acceptable for this project?
- Do you uphold or overturn the researcher's response to each escalated finding?
- Does the Decision-Rights Map give the right people authority over the
  decisions that matter, including domain judgment the AI agents lack?
- What must be changed before modeling starts?

## 16. Approved Planning Package

The Planning stage outputs one compact approved plan package. It should combine the important artifacts rather than scatter them across many files.

Use the template in `../templates/plan-package.md`.
