# Skill Strategy

## Purpose

This workflow should not assume that every research operation must be implemented as an internal skill. Some capabilities are already mature outside the repository, such as literature search, citation management, document formatting, journal template handling, systematic-review checklists, and statistical or visualization tooling.

The skill strategy defines when to reuse external mature tools, when to orchestrate them through workflow-native skills, and when to create new project-specific skills.

## Core Principle

Use mature external tools for commodity research operations. Use workflow-native skills for orchestration, evidence control, handoffs, and human gates. Create new domain or method skills only when a recurring research operation is not already covered well enough by existing tools.

Internal skills should make the workflow more inspectable, not hide external work behind another black box.

## Skill Categories

This repository uses a simple ownership distinction:

- **Internal skills** are skills written and maintained in this repository under `skills/`.
- **External tools or skills** are installable or downloadable tools, packages, services, databases, templates, or skills maintained outside this repository.

All seven skills in `skills/` are internal workflow-native skills. Keeping a skill internal does not mean the framework should reimplement every operation itself. Several internal skills are intentionally designed to wrap, orchestrate, or verify external tools while preserving the framework's stage packages, evidence records, and gates.

### 1. External Mature Tools or Skills

These are tools, services, plugins, templates, databases, or established packages that already solve a common research task.

Examples:

- literature search and deep research tools
- academic databases and APIs
- citation managers and DOI metadata services
- systematic-review checklists
- publisher or journal templates
- document, spreadsheet, presentation, or bibliography tools
- statistical, visualization, or experiment-tracking packages
- mature domain-specific analysis packages

Use these when the task is already standardized, externally maintained, and more reliable than a quick internal skill.

### Recommended External Research Skills

The following external skills are useful companions for this workflow. They should be treated as optional, inspectable tools rather than workflow-native control modules. Their outputs must be brought back into the appropriate stage package under the external handoff rules below.

| External skill | Best stage(s) | Use for | Do not use for | Required handoff back into this workflow |
|---|---|---|---|---|
| [Academic Research Skills for Codex](https://github.com/Imbad0202/academic-research-skills-codex) | Planning, Reporting, Reviewing | Literature review support, paper-structure planning, drafting assistance, simulated review, and end-to-end academic workflow suggestions | Replacing this repository's stage gates, package templates, claim-evidence checks, or route-aware review | Record invoked workflow, input prompt/files, generated notes or draft sections, citation/source status, unresolved claims, and which stage owns verification |
| [Deep-Research-skills](https://github.com/Weizhena/Deep-Research-skills) | Planning, Reporting | Focused prior-work scan, structured deep investigation, outline-first research, and targeted literature addenda | Treating web-search summaries as verified evidence or skipping citation/source-support checks | Record research outline, search queries, sources screened, included/excluded items, summary outputs, citation metadata, and verification gaps |
| [Research-Paper-Writing-Skills](https://github.com/Master-cai/Research-Paper-Writing-Skills) | Reporting | ML/CV/NLP manuscript drafting, abstract/introduction/related-work refinement, and claim-evidence-aware writing suggestions for manuscript output mode | Creating unsupported claims, finalizing citations, or bypassing the claim-evidence mapper | Record manuscript section input, generated or revised prose, claim changes, citation requirements, unsupported claims, and Reporting-stage verification status |
| [CCF-Figure](https://github.com/Deepshare-Official/CCF-Figure) | Reporting | AI/CS method figures, conceptual diagrams, workflow diagrams, graphical-abstract prompts, and non-empirical visual structure selection | Creating new empirical figures, robustness plots, data-derived charts, or final publication graphics without review | Record selected diagram type, assembled prompt, source claims used, whether the visual is conceptual or empirical, and caption/evidence limits |

These four skills cover common external needs without changing the framework's core control logic: deep research, Codex-native academic workflow support, manuscript-output assistance inside Reporting, and research-figure prompting. They should normally be referenced in the Plan Package as external tool candidates, then invoked only when a stage has a clear input and a clear verification path.

### Claude Code as Researcher: Built-in Capability Coverage (Config B)

When Claude Code is the researcher agent (Config B), the four Codex-specific
external skills above are not directly available. Claude Code's built-in
capabilities cover the same functional needs without additional installation.

| Codex external skill | CC built-in replacement | Assessment |
|---|---|---|
| Academic Research Skills for Codex | WebSearch + WebFetch + native literature synthesis | Sufficient — CC can retrieve, summarize, and position prior work; apply the same external-handoff recording rules |
| Deep-Research-skills | WebSearch + WebFetch with outline-first prompting | Sufficient — instruct CC to follow an outline-first research plan and record queries, sources screened, and verification gaps as required by the external handoff rules |
| Research-Paper-Writing-Skills | Native writing capability | Sufficient for most manuscript modes — CC can draft ML/CV/NLP and non-CS manuscripts; apply the claim-evidence mapper skill to verify support before finalizing |
| CCF-Figure | Native diagram description + Mermaid / draw.io prompting | Partial — CC can specify figure structure, assembly notes, and caption logic; for precise CCF-style outputs, provide venue exemplars as user-supplied materials so CC can match the style |

When Claude Code is the researcher, record the same external handoff information
required for Codex external skills: what capability was used, what inputs were
given, what was produced, and what verification gaps remain.

### Workflow-Native Skills: Claude Code Slash Commands

The seven workflow-native skills in `skills/` are available to Claude Code as
slash commands via `.claude/commands/`. Invoke them by name during the relevant
stage:

| Slash command | Stage | Purpose |
|---|---|---|
| `/venue-calibration` | Planning, Reporting | Calibrate target outlet and extract plan constraints |
| `/research-skill-card-distiller` | Planning | Convert retrieved or user-supplied papers into skill cards |
| `/model-contract-runner` | Modeling | Execute the approved modeling contract end to end |
| `/figure-table-narrative` | Reporting | Plan visual evidence and tie figures/tables to claims; use external tools such as CCF-Figure for visual generation |
| `/claim-evidence-mapper` | Reporting, Reviewing | Map every claim to evidence or flag it as unsupported |
| `/route-aware-reviewer` | Reviewing | Stress-test the evidence package and route findings |
| `/gate-manager` | All stages | Record gate decisions and advance to the next stage |

Codex accesses the same skills by reading the corresponding `skills/<name>/SKILL.md`
directly. Both agents follow the same underlying procedures.

### 2. Workflow-Native Skills

These are the reusable skills maintained in this repository. Their job is not to replace external tools. Their job is to control the research workflow:

- clarify purpose and venue fit
- distill prior work into reusable research patterns
- enforce modeling contracts and data acquisition rules
- map claims to evidence
- design figure and table narratives
- route review findings to the right stage
- manage gates and backtracking

Workflow-native skills should declare where external tools can be used and what evidence must be brought back into the stage package.

Current internal skills fall into two practical groups:

| Internal skill | Relationship to external tools |
|---|---|
| `venue-calibration` | Wraps external venue pages, author guidelines, templates, and exemplar papers; keeps the venue constraints inside Planning and Reporting packages |
| `research-skill-card-distiller` | May use external literature-search or deep-research outputs; keeps the reusable skill-card format internal |
| `model-contract-runner` | Uses external execution tools such as Python, R, Jupyter, containers, APIs, or domain packages; keeps success rules, run logs, repair decisions, and gate readiness internal |
| `figure-table-narrative` | Does not generate figures itself; hands method/conceptual visuals to CCF-Figure or diagram tools and empirical visuals to Model/plotting tools; keeps claim-visual alignment, evidence status, placement, and caption limits internal |
| `claim-evidence-mapper` | May use external citation or retrieval tools for support; keeps the final claim-evidence map and unsupported-claim flags internal |
| `route-aware-reviewer` | May use external reviewer simulation or checklists; keeps severity labels and route decisions internal |
| `gate-manager` | Mostly framework-native; records human gates, synthetic gates, transitions, and backtracking |

### 3. Project-Specific Skills

These are narrow skills created for one project or domain, such as a water-science manuscript-revision skill.

Project-specific skills should usually live inside the project folder or a run-specific agent artifact folder, such as `<run_dir>/agent/` (see `docs/stage-handoffs.md`), until they have been reused across more than one project. A project-specific skill can be promoted to `skills/` only when it is general enough, documented, and useful beyond the original case.

## Decision Rules

Before creating a new skill, ask:

- Is there a mature external tool, package, checklist, template, or database that already solves this operation?
- Is the task a workflow-control problem or a domain/content problem?
- Does the operation need to be reused across projects?
- Does the skill make the process more inspectable, or does it hide important decisions?
- What inputs, outputs, evidence, and failure modes must the skill expose?
- Can the result be verified by the user or another stage?

Preferred order:

1. Reuse an external mature tool when the task is standard and the output can be inspected.
2. Use a workflow-native skill to orchestrate, check, and package the result.
3. Create a project-specific skill when no mature tool captures the domain operation.
4. Promote a project-specific skill to a core workflow skill only after repeated use and review.

## External Handoff Rules

When a stage uses an external tool, the result must be brought back into the workflow as inspectable evidence.

Record:

- tool or source name
- version, access date, API endpoint, model, package version, or template version when relevant
- input query, prompt, file, dataset, or manuscript section
- output artifact path or citation
- verification status
- limitations or known failure modes
- whether the output is evidence, a suggestion, formatting support, or a convenience artifact

External outputs should not be treated as automatically correct. They should pass through the same stage checks as internal outputs.

## Stage-Level Use

### Plan

Plan should scan for existing skills, tools, papers, packages, and prior workflows before writing a new plan. If mature external approaches exist, the plan should reuse or adapt them instead of inventing a new method from scratch.

Plan should produce:

- external tool candidates
- prior-work skill patterns
- project-specific skill needs
- feasibility and cost implications of using each tool
- decision on reuse, adaptation, or new skill construction

### Model

Model may use external packages, APIs, datasets, compute tools, or experiment frameworks, but it must still obey the modeling contract. External tools do not remove the need for acquisition success counts, preflight checks, run logs, validation, preliminary finding briefs, and evidence-deepening decisions.

### Reporting

Reporting may use external tools for evidence packaging, dashboards, tables, summaries, papers, slides, web pages, software documentation, citation/reference management, document formatting, and non-empirical explanatory visuals. It must still preserve provenance, distinguish supported from preliminary findings, map claims to evidence, and route missing empirical evidence back to Model.

Reporting should not use a language-polishing or formatting tool to create unsupported claims or hide weak evidence.

### Review

Review may use external citation checkers, plagiarism/similarity tools, reporting checklists, venue checklists, and reviewer-simulation tools. Their outputs should be treated as review evidence and routed into the Review Package with severity labels and revision actions.

## Promotion Criteria

A project-specific skill can be promoted to a core skill when:

- it has been useful in at least two projects or clearly applies across many projects
- its inputs and outputs are stable
- it includes examples and failure modes
- it exposes evidence rather than only final prose
- it integrates with stage packages and gate rules
- it does not duplicate a mature external tool without adding workflow value

## Anti-Patterns

Avoid:

- writing an internal skill only because a task appeared once
- replacing mature tools with fragile prompt-only instructions
- using external tools without recording what they did
- treating external deep-research output as verified evidence without citation checks
- turning a project-specific prompt into a core skill before it has been tested
- creating a skill that produces polished text but no traceable evidence

## Minimal Skill Card

When a new skill is proposed, record:

- skill name
- stage used
- problem solved
- why external tools are insufficient
- inputs
- outputs
- evidence or logs produced
- failure modes
- verification method
- promotion status: project-specific, candidate core skill, or core skill
