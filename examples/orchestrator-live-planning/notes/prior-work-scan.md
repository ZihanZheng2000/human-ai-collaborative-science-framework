# Prior-work scan (light) — live-penguins

Status: light scan, written from researcher background knowledge in an
orchestrated run with no literature-retrieval step. Citations below were NOT
re-verified against the sources in this session; verify before any citation is
used in a deliverable.

| Source (recalled) | What it did | Relevance |
|---|---|---|
| Gorman, Williams & Fraser (2014), PLoS ONE 9(3):e90081 | Original field study that produced the data: sexual size dimorphism and niche divergence in Pygoscelis penguins near Palmer Station | The question "do sexes differ in mass within species" is the kind of question the data were collected for; not novel |
| Horst, Hill & Gorman, `palmerpenguins` R package (v0.1.1, CC0 per DESCRIPTION, recalled and not re-verified) | Packages the data as a teaching/example dataset | Dataset is widely used for exactly this sort of demo |
| General penguin biology literature on sexual size dimorphism | Males are generally reported as larger in these genera | Gives a directional prior; do not use it to pre-judge results |

Implication: no novelty claim is possible or sought. The project is a workflow
trial / descriptive demonstration (matches user's "framework trial").

Data reachability check (feasibility only, no analysis, no values inspected):
`https://raw.githubusercontent.com/allisonhorst/palmerpenguins/main/inst/extdata/penguins.csv`
returned HTTP 200; header `species,island,bill_length_mm,bill_depth_mm,flipper_length_mm,body_mass_g,sex,year`; 344 data rows.
