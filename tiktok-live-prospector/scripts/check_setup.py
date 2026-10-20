from pathlib import Path
import csv
ROOT=Path(__file__).resolve().parents[1]
REQUIRED=['CLAUDE.md','README.md','RUN_PROMPT.md','.claude/skills/prospect-tiktok-live/SKILL.md','.claude/agents/discovery-researcher.md','.claude/agents/contact-verifier.md','.claude/agents/qualification-auditor.md','docs/research-playbook.md','docs/access-fallbacks.md','docs/scoring.md','schemas/fields.md','data/seed_links.csv','scripts/export.py']
def check():
    missing=[p for p in REQUIRED if not (ROOT/p).is_file()]
    with (ROOT/'data/seed_links.csv').open(newline='',encoding='utf-8') as f: rows=list(csv.DictReader(f))
    errors=[]
    if len(rows)!=16 or sum(r['seed_type']=='tiktok_shortlink' for r in rows)!=3 or sum(r['seed_type']=='linkedin_profile' for r in rows)!=13: errors.append('Expected exactly 3 TikTok and 13 LinkedIn independent seeds')
    if missing: errors.append('Missing files: '+', '.join(missing))
    return errors
if __name__=='__main__':
    errors=check()
    if errors:
        for e in errors: print('ERROR:',e)
        raise SystemExit(1)
    print('PASS: project files, Claude skill/agents, and 16 independent seed links present')
