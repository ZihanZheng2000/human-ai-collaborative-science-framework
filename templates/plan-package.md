# Planning Package

This package becomes the **Approved Planning Package** only after the user
approves the Planning Gate.

## Planning Workflow Identity

- package status: draft for Planning Review / revised after Planning Review / approved
- Planning Researcher: researcher agent name or runtime
- Planning Reviewer: reviewer agent name or runtime / skipped
- reviewer file: `docs/reviewer-agents/planning-reviewer-agent.md`
- reviewer mode: critique-only / edits explicitly authorized by user / skipped
- review mode: standard / blind
- reviewer rights: advisory + escalation (default) / other per Decision-Rights Map
- decision log: `decision-log.md`
- Planning Review status: pending / completed / skipped
- researcher-agent response status: pending / completed / not applicable
- user Planning Gate status: pending / approved / revise / backtrack / terminate

## User-Need Profile

Complete this section by proposing answers first, then recording only user
corrections or additions. Do not use it as a broad interview transcript.

| User-need field | Proposed answer | Common choices | User correction or addition |
|---|---|---|---|
| research area |  |  |  |
| intended output |  | paper / report / demo / skill / dataset / tool / manuscript package / proposal / policy note / internal decision brief |  |
| workflow mode |  | auto-until-needed / step-by-step discussion |  |
| intended research product |  | empirical finding / method / dataset / benchmark / skill / workflow demo / manuscript package |  |
| research purpose |  | discover pattern / build method or tool / validate intervention / revise existing artifact / compare alternatives / workflow test |  |
| practical success criterion |  | evidence for a claim / reusable workflow / validated dataset / decision support / publishable package / proof of feasibility |  |
| target audience or venue |  | academic readers / internal decision-makers / course / policy users / engineering users / public readers / domain experts |  |
| data/source direction |  | provided data / public data / literature only / corpus construction / API data / no empirical data |  |
| available data |  | none known / user-provided / public source known / to be found |  |
| constraints |  | time / tooling / runtime / API-token / privacy / licensing / language / method complexity |  |
| novelty expectation |  | publication novelty / useful replication / demo / internal evidence / no novelty claim |  |
| avoid-list |  | no known exclusions / avoid specific data / methods / domains / paid APIs / private data / black-box methods |  |
| gate mode |  | real user gates / synthetic gates / mixed |  |
| reviewer strategy |  | use reviewer / skip reviewer |  |

## Domain Onboarding

Complete this section when user-supplied domain materials were provided before
Planning began. Leave blank and mark "skipped — no user materials" if none.

### Material Inventory

| File or folder | Material type | Domain covered | Date or version |
|---|---|---|---|
| | paper / report / data documentation / policy doc / field notes / other | | |

### Domain Knowledge Summary

Compact record of what was learned from user-supplied materials that is not
obvious from general AI knowledge. This should govern field-specific decisions
throughout Planning, Modeling, and Reporting.

**Key domain concepts and terminology:**

**Field norms or conventions relevant to this project:**

**Domain-specific constraints (data access, measurement, ethics, reporting):**

**Conflicts or uncertainties found in the materials:**

**User resolution for any conflicts:**

### Potential Skill Patterns from User Materials

List possible reusable patterns noticed in user-supplied materials. Do not
convert these into formal research-skill cards until the research route is
selected or narrowed in step 11.

| Pattern ID | Source material | Pattern noticed | Status |
|---|---|---|---|
| | | | candidate / selected for step 11 / rejected |

### Domain Onboarding Status

- status: completed / skipped — no user materials / skipped — user declined / deferred
- materials read: [count] files
- potential skill patterns noted: [count]
- downstream implications flagged: yes / no

## Resolved Decision-Changing Unknowns

Record only unresolved items that materially changed or could have changed the
research design. Do not use this section for low-value preference questions.

| Unknown or ambiguity | Provisional answer | User correction or resolution | Effect on plan |
|---|---|---|---|
|  |  |  |  |

## Prior Work Scan

This section records the focused literature and prior-work scan. It should be compact, but it should be completed before the full plan is written.

| Cluster or source | What has been done | Method or evidence pattern | Relevance to this project |
|---|---|---|---|
|  |  |  |  |

## Research Opportunities and Routes Considered

| Opportunity or route | Prior-work basis | Gap or value | Initial feasibility | Decision |
|---|---|---|---|---|
|  |  |  |  | selected / rejected / backup / future work |

## Planning Depth Decision

Complete this section after the focused prior-work scan, so idea maturity and
planning depth are calibrated by literature evidence rather than guessed before
the scan.

| Item | Decision | Reason | Downstream implication |
|---|---|---|---|
| idea maturity | exploratory / partly formed / mature / revision |  |  |
| literature/prior-work scan depth | full / light / skipped / deferred |  |  |
| novelty assessment depth | full / light / skipped / deferred |  |  |
| venue/output calibration depth | full / light / skipped / deferred |  |  |
| revisit trigger |  | before scale-up / before Reporting / before Review / before submission / other |  |

## Candidate Research Plans Considered

Use this section only if more than one plausible route was considered.

| Plan | RQ | Data | Method | Venue/output fit | Decision |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## Feasibility and Cost Check

| Item | Assessment | Evidence or test | Fallback |
|---|---|---|---|
| data access | feasible / uncertain / blocked |  |  |
| text/table/image/API extractability | feasible / uncertain / blocked |  |  |
| candidate sources vs usable acquired data |  |  |  |
| demo scale |  |  |  |
| full-study scale |  |  |  |
| runtime/storage burden |  |  |  |
| API/token cost |  |  |  |
| external tool or skill feasibility |  |  |  |
| licensing/privacy/ethics |  |  |  |

## Data Source Identity

Use this section whenever data will be downloaded, scraped, queried, or extracted. Distinguish exact raw data from documentation and citation sources.

| Role | Source name or URL | Version/date/access date | License/access status | Notes |
|---|---|---|---|---|
| raw data host |  |  |  |  |
| official data source |  |  |  |  |
| documentation source |  |  |  |  |
| citation source |  |  |  |  |

## Venue or Output Calibration

| Candidate venue/output | Why it fits | Tradeoffs | Decision |
|---|---|---|---|
|  |  |  | selected / rejected / backup / deferred |

If no venue is selected, state the provisional route and when it should be revisited.

### Official Venue Requirements

| Requirement | Official rule or constraint | Effect on plan |
|---|---|---|
| article type and scope |  |  |
| manuscript structure |  |  |
| word/page limit |  |  |
| abstract format |  |  |
| reference style |  |  |
| figure/table rules |  |  |
| data/code availability |  |  |
| ethics/funding/COI/AI disclosure |  |  |
| reporting checklist or supplement rules |  |  |

### Venue Exemplar Scan

Inspect 2-5 recent structurally similar articles from the selected or candidate venue when the intended output is a formal manuscript.

| Exemplar | Why similar | Structure pattern | Evidence/validation pattern | Figure/table pattern | Citation pattern | Implication for this plan |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

### Venue-Derived Plan Constraints

| Constraint from venue or exemplars | Required plan response | Status |
|---|---|---|
|  | data scale / validation / robustness / citation depth / article type / visual plan / disclosure | satisfied / needs Model / needs Reporting / infeasible / deferred |

## Selected or Confirmed Research Route

Complete this section after literature, candidate-route discussion,
feasibility, and venue/output calibration.

| Route element | Selected value | Evidence or reason | User confirmation status | Decision ID |
|---|---|---|---|---|
| working research question |  |  | confirmed / provisional / needs decision |  |
| intended output and claim level |  |  | confirmed / provisional / needs decision |  |
| data/source strategy |  |  | confirmed / provisional / needs decision |  |
| method family |  |  | confirmed / provisional / needs decision |  |
| feasibility status and fallback |  |  | confirmed / provisional / needs decision |  |
| target venue/audience/output mode |  |  | confirmed / provisional / needs decision |  |
| future-work boundary |  |  | confirmed / provisional / needs decision |  |

## Decision-Rights Map

Copy the default map from `docs/decision-rights.md` and adjust it. This map is
a Tier 1 decision; changes after approval are reconfigurations recorded in the
decision log.

| Decision class | Performed by | Authority | Tier | Domain judgment supplied by | Notes |
|---|---|---|---|---|---|
| research purpose, question, claim level | researcher proposes | user | 1 (2 at gate) |  |  |
| prior-work / novelty depth, skip or defer | researcher proposes | user | 1 |  |  |
| data source and acquisition success rule | researcher proposes | user | 1 |  |  |
| labels, event definitions, inclusion/exclusion rules | researcher proposes | user | 1 |  | lock before results |
| method family, model search space, metrics, validation split | researcher proposes | user | 1 |  | lock before results |
| analysis execution and repair within locked contract | researcher | researcher | 0 |  |  |
| interpretation, causal or domain claims | researcher proposes | user | 1 |  |  |
| response to blocker/major findings (defer or reject) | researcher proposes | user | 1 |  |  |
| output route, venue, audience | researcher proposes | user | 1 |  |  |
| stage transition, backtrack, release, terminate | researcher proposes | user | 2 |  |  |
| workflow mode, reviewer strategy, this map | anyone proposes | user | 1 |  |  |

- reviewer rights: advisory + escalation / other:
- stages using blind review: Reviewing / other:
- domain expert involvement: none / named expert for decision classes:
- decision ID confirming this map:

## External Tool and Skill Scan

Complete this section after the route is selected or narrowed. Record mature
external tools, packages, templates, databases, or existing skills that could be
reused before creating new project-specific skills.

| Candidate tool, package, template, or skill | Workflow task | Maturity or reason to trust | Output to bring back | Cost/access/limits | Decision |
|---|---|---|---|---|---|
|  | literature / data / model / writing / citation / formatting / review / other |  |  |  | reuse / wrap / adapt / reject / create new skill |

## Skill Construction Decision

Complete this section only after external alternatives have been checked.

| Skill need | External alternative checked | Why external option is sufficient or insufficient | Decision | Promotion status |
|---|---|---|---|---|
|  |  |  | no skill needed / use existing skill / create project-specific skill / promote to core later | none / project-specific / candidate core |

## Research-Skill Cards or Skill Candidates

Convert only selected-route-relevant prior work into formal skill cards or skill
candidates. Do not create cards for every screened source.

| Card or candidate ID | Source basis | Pattern captured | Used in route? | Status |
|---|---|---|---|---|
|  |  | research design / data acquisition / measurement / baseline / modeling / validation / figure-table / reviewer risk | yes / no | selected / provisional / rejected |

## Planning Reviewer Critique

Use this section before the user Planning Gate. The reviewer agent should be separate from the researcher agent when available and approved by the user. The reviewer critiques only unless the user explicitly authorizes edits.

| Finding ID | Severity | Concern | Evidence or reasoning | Route | Blocks gate? | Recommended action |
|---|---|---|---|---|---|---|
| PR-1 | blocker / major / minor / suggestion / accepted limitation |  |  | Planning / Modeling / Reporting / Reviewing / Terminate / user decision | yes / no |  |

If external Planning Review was skipped, record why:

- skipped reason:
- risk accepted:
- revisit trigger:

## Researcher-Agent Response to Planning Review

The researcher agent must respond to reviewer findings before the user Planning Gate.

Blocker and major findings that are deferred or rejected are escalated: add
them to the decision log's Open Escalations and quote them at the gate. Only the
user can uphold the response.

| Finding ID | Response status | Change made or planned | Blocks gate? | Escalated to user? | User ruling | Notes |
|---|---|---|---|---|---|---|
| PR-1 | accepted and fixed / accepted but deferred / rejected with reason / needs user decision |  | yes / no | yes / no | upheld / overturned / pending / n.a. |  |

## Approved Research Question

`<one clear question>`

## Working Title

`<title>`

## Hypotheses or Expected Claims

- `<hypothesis or expected claim>`

## Data Plan

- primary data source:
- backup data source:
- exact raw data host:
- official data source:
- documentation source:
- data version or access date:
- license/access status:
- acquisition success rule:
- minimum viable data scale:
- full-study data scale:
- key variables:
- unit of analysis:
- time/spatial coverage:
- access or licensing concerns:

## Method Blueprint

1. `<analysis step>`
2. `<analysis step>`
3. `<analysis step>`

## Expected Manuscript Package

- figures:
- tables:
- likely method/conceptual visuals:
- claim-evidence map:
- limitations to acknowledge:
- reproducibility artifacts:

## Risks and Gate Notes

| Risk | Severity | Mitigation |
|---|---|---|
|  |  |  |

## Planning Gate Decision

- decision: approve for Modeling / revise Planning / request another Planning Review / backtrack / terminate
- gate mode: real user gate / synthetic gate / mixed
- decision maker:
- decision-log ID:
- approval quality: substantive / nominal (what was missing) / synthetic
- escalated findings ruled on: finding ID -> upheld / overturned
- open objections carried forward:
- date:
- required changes before Modeling:
- accepted limitations:
- unresolved user decisions:

## Acceptance Rubric for Model Stage

The Model stage can begin only if:

- the research purpose and final product are clear
- the planning depth decision is explicit
- the prior-work scan supports the proposed gap or opportunity, or its skip/defer decision is recorded with a revisit trigger
- useful prior-work patterns or skill candidates have been captured
- the required data can be accessed or a fallback data source is approved
- candidate sources have been distinguished from actually usable data
- the selected method is feasible under the user's constraints
- expected runtime and API/token cost are acceptable or capped
- the core assumptions are explicit
- the Decision-Rights Map is confirmed and the analysis choices to lock before results are listed
- expected figures or tables are defined
- unresolved risks are either mitigated or accepted by the user
- Planning Reviewer findings are fixed, deferred with triggers, rejected with reasons, or escalated for user decision, and the user has ruled on every escalated blocker or major
- the user has approved the Planning Gate after the researcher-agent response to Planning Review
