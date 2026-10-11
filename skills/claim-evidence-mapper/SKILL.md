---
name: claim-evidence-mapper
description: Use during Reporting or Reviewing to ensure every important finding, deliverable claim, manuscript claim, and substantive literature or model-supported sentence when present is tied to verified literature, model outputs, user-approved domain knowledge, interpretation, or an explicit limitation.
---

# Claim-Evidence Mapper

## Use When

- packaging evidence into findings
- drafting or revising a Reporting deliverable, including a manuscript or paper
- checking whether claims are supported
- preparing Review-stage evidence audit

## Inputs

- Reporting Package, manuscript draft, or outline
- Planning Package
- Modeling Package
- literature map
- source list or bibliography
- figures and tables

## Procedure

1. Identify the accepted citation threshold: internal/smoke test, demo/proof-of-concept, preliminary manuscript/preprint, or submission-ready manuscript.
2. Extract major findings or claims from each section/package.
3. Extract sentence-level or clause-level substantive literature, method, gap, comparison, and model-supported claims.
4. Classify each claim as literature-supported, model-supported, user-supplied, interpretation, limitation, or unsupported.
5. Attach source IDs, citation keys, citation numbers, DOI/URL when available, figure/table IDs, or artifact paths.
6. Check whether each citation supports the sentence or clause where it is placed.
7. Flag citation deserts: paragraphs with multiple substantive literature claims and no mapped citation.
8. Downgrade, remove, or mark unsupported claims for targeted literature retrieval, Model addendum, or user clarification.
9. Produce a citation-grounded claim map and source-support gap list.

## Outputs

- claim-evidence map
- citation-grounded claim map
- section evidence bundles
- unsupported-claim list
- citation and model-evidence gaps
- targeted literature addendum requests
- accepted citation threshold and unresolved items by output type

## Guardrails

- Do not map any claim at a higher claim level than the one authorized in the decision log; raising it is a Tier 1 checkpoint.

- Do not use citations as decoration.
- Do not cite a source unless it supports the sentence or clause being cited.
- Do not leave "previous studies show," "little work has examined," or similar gap claims without mapped evidence.
- Do not let interpretation claims read like empirical findings.
- Do not turn association into causation unless the method supports it.
- Do not ask the user to verify all citations from scratch; unresolved citation-existence or source-support issues should be listed explicitly.
- Do not label an internal/demo citation check as submission-ready.
- Do not let a lower citation threshold support stronger manuscript claims.
