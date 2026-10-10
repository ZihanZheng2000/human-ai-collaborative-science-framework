# Public Release Checklist

Use this before publishing the repository on GitHub.

## Repository

- [ ] Confirm repository name, recommended: `human-ai-collaborative-science-framework`
- [ ] Ensure `.env` is ignored and not committed
- [ ] Confirm the `repository-code` URL in `CITATION.cff` after renaming the GitHub repository
- [ ] Check license and contributor names
- [ ] Confirm README links work
- [ ] Add screenshots or workflow figures if desired
- [ ] `python -m unittest discover -s tests` passes
- [ ] `python scripts/build_agent_instructions.py` leaves `CLAUDE.md`, `AGENTS.md`, `GEMINI.md` unchanged (they match `docs/agent-roles/`)
- [ ] `workflow.config.json` and `workflow.config.example.json` contain no API keys or private paths

## Examples

- [ ] Keep public examples lightweight unless data, artifacts, and permissions have been reviewed
- [ ] Confirm each published example follows `docs/example-organization.md`
- [ ] Review any case study for private notes, API keys, copyrighted material, and large generated artifacts

## Paper

- [ ] The companion paper is maintained in a separate repository; confirm the README citation and title match its current version
- [ ] Add the repository URL to the paper once it is public

## Security and Privacy

- [ ] Search for API keys, tokens, private paths, and personal notes (including agent prompt logs under `examples/*/artifacts/*/agent/`)
- [ ] Remove or anonymize sensitive data
- [ ] Confirm all included datasets can be redistributed or are small derived artifacts
