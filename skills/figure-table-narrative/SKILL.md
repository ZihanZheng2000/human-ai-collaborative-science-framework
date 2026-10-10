---
name: figure-table-narrative
description: Use during Reporting as a visual-evidence planning and handoff controller. This skill does not replace CCF-Figure, plotting libraries, diagram tools, or design software; it decides visual purpose, claim alignment, evidence status, caption limits, and Reporting-package handoff.
---

# Figure and Table Narrative Skill

## Boundary

This is an internal control skill, not a figure-generation skill.

Use external tools to design or generate visuals:

- CCF-Figure for AI/CS method figures, framework diagrams, workflow figures, conceptual diagrams, and graphical-abstract prompts
- Python, R, ggplot, matplotlib, seaborn, plotly, or Observable for empirical figures and tables
- Mermaid, draw.io, Figma, Illustrator, LaTeX, or document tools for diagrams and final layout

Use this skill to decide which visuals are needed, what evidence they support, where they appear, what captions may claim, and how external visual outputs are recorded in the Reporting Package.

## Use When

- Reporting begins from a Modeling Package
- the method or workflow needs a schematic
- figures and tables exist but are not yet tied to claims
- Review finds missing or confusing visuals
- CCF-Figure or another external visual tool should be invoked and its output needs a clear handoff back into Reporting

## Inputs

- Modeling Package figures and tables
- claim-evidence map
- reporting package or manuscript architecture
- target venue rules, if any
- external visual tool outputs or prompts, if already produced

## Procedure

1. List each major claim that needs visual support.
2. Assign empirical figures/tables from Model outputs.
3. Decide whether Reporting needs conceptual, method, workflow, or graphical-abstract visuals.
4. Select the appropriate external visual tool when a new visual is needed.
5. Record the external tool, prompt/input, output path, evidence basis, and limitations.
6. Place each visual in the report or manuscript where it is interpreted.
7. Check numbering, captions, in-text references, and claim strength.
8. Send any new empirical visual request back to Model.

## Outputs

- figure/table narrative table
- method schematic or conceptual diagram requests for external tools such as CCF-Figure
- visual placement plan
- external visual handoff notes

## Guardrails

- Conceptual and workflow diagrams may be planned in Reporting and generated with external visual tools.
- CCF-Figure or similar tools may propose visual structure, but this skill must still verify claim alignment, evidence status, caption scope, and handoff records.
- Data-derived figures and tables must come from Model or a documented Model addendum.
- Captions should state what the reader should learn, not only name the file.
- Captions must not imply empirical support that is absent from the Modeling Package or claim-evidence map.
