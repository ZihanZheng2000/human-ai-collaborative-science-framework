---
name: research-skill-card-distiller
description: Use during Plan to convert retrieved papers OR user-supplied domain materials into reusable research-skill cards that capture field norms, data requirements, method patterns, assumptions, failure modes, and manuscript obligations.
---

# Research Skill-Card Distiller

## Use When

- similar research papers have been retrieved via literature scan
- the user has supplied domain materials (papers, reports, field notes, data
  documentation) during Domain Onboarding
- the user needs field-calibrated planning rather than ungrounded idea generation
- a paper's or document's reusable research pattern should be separated from
  its specific findings

## Inputs

**From retrieved literature (step 6 of Planning):**
- retrieved papers or paper notes
- target research area
- intended output route

**From user-supplied domain materials (step 0 Domain Onboarding):**
- papers, institutional reports, policy documents, field notes, data
  dictionaries, codebooks, or prior project materials provided by the user
- folder path: `research/<research-name>/artifacts/input/domain-materials/` by convention (`artifacts/<run_id>/domain-materials/` for smoke tests)
- domain area and research intent stated by the user

## Procedure

### For retrieved papers

1. Cluster papers by research pattern, not only topic.
2. For each pattern, identify when it is useful.
3. Extract required data, method template, assumptions, failure modes, and
   manuscript obligations.
4. Tie every card to source papers.
5. Mark concerns that require user approval or later Model validation.

### For user-supplied domain materials

1. Read each file. Note the material type, domain covered, and purpose.
2. Identify reusable patterns relevant to the planned research:
   - field measurement or indicator conventions
   - data collection or acquisition norms
   - standard analysis or modeling approaches for this domain
   - common validation or evaluation criteria
   - reporting conventions or required disclosures
   - known limitations or common failure modes in the field
3. Cluster materials by the research pattern they illustrate, not only by topic.
4. For each pattern, extract:
   - what data or materials it requires
   - method or analysis template
   - domain-specific assumptions
   - failure modes or known caveats
   - manuscript or reporting obligations
5. Tie each card to the specific source document, section, or file.
6. Flag any domain claims that conflict with retrieved literature or general
   knowledge and surface them for user resolution.
7. Mark concerns that require user approval or later Model validation.

### For mixed inputs (user materials + retrieved papers)

Run both procedures above, then cross-check:
- Do user-supplied patterns align with the retrieved literature?
- Do retrieved papers reveal gaps in the user-supplied materials?
- Are there contradictions between user materials and published work? If yes,
  flag for user decision before incorporating either as a plan constraint.

## Outputs

- research-skill cards using `templates/research-skill-card.md`
- source attribution for each card (retrieved paper or user-supplied file)
- selected/provisional cards for the Plan Package
- conflict flags if user materials and retrieved literature disagree

## Guardrails

- Do not copy a paper's or document's exact project as the user's plan.
- Do not treat weakly related papers or materials as field norms.
- Do not treat user-supplied materials as automatically authoritative; note
  conflicts with published work and surface them for user resolution.
- Do not produce skill cards from a single source when multiple sources could
  cross-check the pattern.
- Preserve room for AI-generated novelty after field calibration.
- Label each card's source type: retrieved-paper, user-supplied, or mixed.
