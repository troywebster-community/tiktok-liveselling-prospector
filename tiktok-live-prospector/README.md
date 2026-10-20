# TikTok Shop LIVE Prospector for Claude Code

A research-first Claude Code project for sourcing TikTok Shop LIVE sellers/hosts and verifying public **business** emails for Community prospecting. Uses the user's 3 TikTok short links plus 13 LinkedIn profiles as **independent seeds**, not assumed matches.

## GitHub upload — keep hidden `.claude` files
**Recommended: GitHub Desktop or git**, which preserves dotfolders. Unzip, open the *project folder*, create a new **private** GitHub repository, commit and push. Do not upload the ZIP as a single repo file. If using GitHub's browser uploader, inspect the resulting repository and confirm `.claude/skills/prospect-tiktok-live/SKILL.md` and `.claude/agents/*.md` are present; browser drag-and-drop may skip dotfolders. Do not commit `outputs/`, `data/research_records.json`, API keys or `__pycache__`.

Commands from local shell:
```bash
git init
git add .
git commit -m "Initial TikTok LIVE prospecting project"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/tiktok-live-prospector.git
git push -u origin main
```
(Create the empty private GitHub repo first; if it already contains commits, use normal GitHub Desktop setup instead of blindly pushing.)

## In Claude Code
1. Open / clone this repository as the working directory.
2. Run `python3 scripts/check_setup.py`.
3. Invoke `/prospect-tiktok-live` or paste `RUN_PROMPT.md` into Claude Code if the skill isn't registered.
4. Claude uses its available web research/browser integrations; **code does not magically grant TikTok access**.
5. Claude fills `data/research_records.json` using `schemas/fields.md` and provided example.
6. Run `python3 scripts/export.py` then `python3 -m unittest discover -s tests -v`.
7. Read CSVs in `outputs/` and the review queue.

## Research limitations
Public TikTok profiles, LIVE rooms, Instagram and LinkedIn often restrict access. Use the source fallback ladder in `docs/access-fallbacks.md`. Inaccessible never means inactive. The included three short TikTok URLs could not be resolved by the original project builder: they are **unverified seeds** until Claude resolves them. The 13 LinkedIn links are potential people to research; no verified relationship to the 3 TikTok URLs is asserted.

## Files
- `CLAUDE.md`: persistent constraints and QA
- `.claude/skills/prospect-tiktok-live/SKILL.md`: reusable slash skill
- `.claude/agents/`: independent discovery, evidence and contact research agents
- `data/seed_links.csv`: all 16 user-provided input links
- `docs/`: methods, scoring and site fallbacks
- `schemas/`: output field guide and sample record
- `scripts/`: setup validator and CSV exporter
- `tests/`: basic validation tests

Use Python 3.10+ standard library only. No credentials required to export data. Existing seeds are **not** valid prospects until researched.
