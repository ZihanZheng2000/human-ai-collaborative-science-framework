# Run Log — smoke-v02-co2-2026-10-10

Chronological execution events and Tier 0 decisions. Tier 1/2 decisions are in `../../decision-log.md`.

- 2026-10-10 Setup: example folder created under `examples/` (smoke test). Python venv with pandas/matplotlib created in the session scratchpad (Tier 0).
- 2026-10-10 Acquisition: gml.noaa.gov blocked by egress proxy (HTTP CONNECT 403). Downloaded annual and monthly files from GitHub mirror `datasets/co2-ppm`. Checksums: annual b1548ededea6f9b7eecac370753de8d8da6e0afafe1041f749a11db78c2e33c4, monthly 5d4c2a520d0c6180bb7dd830bf093c9be4716775ddd03d90c04434d423d81b74.
- 2026-10-10 Acquisition check: monthly CSV header has 6 columns, rows have 7 values (misaligned). Annual file header Year,Mean,Uncertainty; 1959-2025. Raw tail values seen; no growth rates computed.
- 2026-10-10 Planning Review (standard) run via headless Claude Code; critique `reviewer-critique-planning.md` (10 findings). Tier 0: stdout moved to `agent/`.
- 2026-10-10 Modeling: `artifacts/code/analyze_growth.py` written; run twice; outputs identical (`artifacts/validation/rerun_check.md`). Tier 0: venv package versions pinned in `artifacts/code/requirements.txt`.
- 2026-10-10 Modeling Review (standard): 9 findings. Tier 0 repairs after review: script creates output dirs, legend, numeric raw/clean check, hand check; rerun hashes recorded.
- 2026-10-10 Reporting Review (standard): 8 findings; report revised; reconfiguration D-14 adopted.
- 2026-10-10 Reviewing Review (blind, partly blind): 13 findings; Review Package revised; seeded faults disclosed (D-16); archived (D-17). run-notes.md written.
