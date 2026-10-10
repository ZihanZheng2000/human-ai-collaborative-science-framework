# Public Release Checklist

Use this before publishing the repository on GitHub.

## Repository

- [ ] Confirm repository name, recommended: `human-gated-ai-research-framework`
- [ ] Ensure `.env` is ignored and not committed
- [ ] Replace placeholder URL in `CITATION.cff`
- [ ] Check license and contributor names
- [ ] Confirm README links work
- [ ] Add screenshots or workflow figures if desired

## Examples

- [ ] Keep public examples lightweight unless data, artifacts, and permissions have been reviewed
- [ ] Confirm each published example follows `docs/example-organization.md`
- [ ] Review any case study for private notes, API keys, copyrighted material, and large generated artifacts

## Paper

- [ ] The companion paper is maintained in a separate repository; confirm the README citation and title match its current version
- [ ] Replace placeholder contributor names if needed
- [ ] Decide whether the paper targets arXiv, preprint, or internal technical note first
- [ ] Add repository URL after GitHub publication

## Security and Privacy

- [ ] Search for API keys, tokens, private paths, and personal notes
- [ ] Remove or anonymize sensitive data
- [ ] Confirm all included datasets can be redistributed or are small derived artifacts
