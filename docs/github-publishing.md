# GitHub Publishing Guide

Recommended repository name:

`human-gated-ai-research-framework`

Recommended display title:

`A Human-Gated, Skill-Guided Framework for AI-Native Academic Research`

## Before Creating the Repository

1. Review `docs/release-checklist.md`.
2. Make sure `.env` is not committed.
3. Decide whether generated example data and figures should be included.
4. Replace contributor names and citation metadata if desired.
5. Confirm the README's companion-paper reference matches the separately maintained paper.

## Suggested Repository Description

Human-gated, skill-guided framework for evidence-grounded academic research by domain researchers.

## Suggested Topics

- ai-research
- academic-research
- research-workflow
- human-in-the-loop
- reproducible-research
- research-reporting
- research-agents
- llm-workflow

## First Commit Checklist

From the repository folder:

```powershell
git init
git add README.md LICENSE CONTRIBUTING.md CHANGELOG.md CITATION.cff .gitignore .env.example docs templates skills examples
git status
git commit -m "Prepare AI-Native Academic Research Framework v0.1"
```

Then create a GitHub repository named `human-gated-ai-research-framework` and follow GitHub's instructions to add the remote and push.

After the repository URL exists, update:

- `CITATION.cff`
- `docs/release-checklist.md`

## Suggested v0.1 Release Notes

Initial development release of AI-Native Academic Research Framework, including:

- four-stage Planning -> Modeling -> Reporting / Output Packaging -> Reviewing framework
- demo-before-scale-up control and run-log conventions
- human gate and synthetic gate semantics
- package templates
- workflow-native skills
- smoke-test mode
- lightweight examples folder and example organization rules
- organization, coordination, and evaluation layers (decision rights, decision log, escalation, workflow evaluation)
