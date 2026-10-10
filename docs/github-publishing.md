# GitHub Publishing Guide

Recommended repository name:

`human-ai-collaborative-science-framework`

Recommended display title:

`Human–AI Collaborative Science Framework`

The repository was renamed from `human-gated-ai-research-framework` to match the
companion paper *Designing Human–AI Collaborative Science*. Rename it in GitHub
under Settings → General → Repository name; GitHub redirects the old URL, but
update local remotes with `git remote set-url origin <new-url>`.

## Before Creating the Repository

1. Review `docs/release-checklist.md`.
2. Make sure `.env` is not committed.
3. Decide whether generated example data and figures should be included.
4. Replace contributor names and citation metadata if desired.
5. Confirm the README's companion-paper reference matches the separately maintained paper.

## Suggested Repository Description

Human–AI collaborative research workflow: four gated stages, explicit decision rights, reviewer escalation, and an orchestrator that works with any agent (CLI, API, or human).

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
git commit -m "Prepare Human–AI Collaborative Science Framework v0.1"
```

Then create a GitHub repository named `human-ai-collaborative-science-framework` and follow GitHub's instructions to add the remote and push.

After the repository URL exists, update:

- `CITATION.cff`
- `docs/release-checklist.md`

## Suggested v0.1 Release Notes

Initial development release of Human–AI Collaborative Science Framework, including:

- four-stage Planning -> Modeling -> Reporting / Output Packaging -> Reviewing framework
- demo-before-scale-up control and run-log conventions
- human gate and synthetic gate semantics
- package templates
- workflow-native skills
- smoke-test mode
- lightweight examples folder and example organization rules
- organization, coordination, and evaluation layers (decision rights, decision log, escalation, workflow evaluation)
