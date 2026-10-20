#!/usr/bin/env python3
"""Conservative CSV exporter from evidence-backed JSON; stdlib only."""
from pathlib import Path
import csv, json, re
from datetime import datetime, timezone
ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/'data/research_records.json'
OUT=ROOT/'outputs'
COLUMNS=['prospect_id','breaker_brand','seller_type','tiktok_handle','tiktok_shop','instagram','youtube','audience_size','business_email','email_source_url','website_linktree','sms_program','recent_activity','priority_score','priority_tier','score_coverage','country','live_verified','live_evidence_url','live_evidence_date','live_frequency','linkedin','fanatics_ebay_other','business_contact_form','email_verification_status','sms_evidence_url','source_access_status','research_date','confidence','activity_source_url','audience_source_url','seed_url','review_reason']
EVIDENCE_FIELDS=['prospect_id','claim','url','source_type','observed_at','note']
def write_csv(path,fields,rows):
    with path.open('w',newline='',encoding='utf-8-sig') as f:
        w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(rows)
def compile_data(records):
    prospective=[];evidence=[];reviews=[]
    ids=set()
    for row in records:
        r=dict(row)
        pid=str(r.get('prospect_id','')).strip()
        if not pid or pid in ids: raise ValueError('Every prospect needs unique nonempty prospect_id')
        ids.add(pid)
        ev=r.get('evidence',[])
        if not isinstance(ev,list): raise ValueError(f'{pid}: evidence must be list')
        email=str(r.get('business_email') or '').strip()
        source=str(r.get('email_source_url') or '').strip()
        email_matches=[x for x in ev if x.get('claim')=='email' and x.get('url')==source and source.startswith('https://')]
        reasons=[]
        if email:
            if not re.fullmatch(r'[^@\s]+@[^@\s]+\.[^@\s]+',email) or not email_matches:
                reasons.append('Business email invalid or lacks exact evidence source; email omitted')
                r['business_email']='';r['email_source_url']='';r['email_verification_status']='unverified'
            elif r.get('email_verification_status') not in ('publicly_listed','deliverability_checked'):
                r['email_verification_status']='publicly_listed'
        else:
            r['email_verification_status']=r.get('email_verification_status') or 'not_found'
        if r.get('sms_program') not in ('yes','no','unknown'):
            r['sms_program']='unknown';reasons.append('Unknown SMS program state')
        if r.get('sms_program')=='yes' and not any(x.get('claim')=='sms' for x in ev):
            r['sms_program']='unknown';reasons.append('SMS yes without evidence; changed to unknown')
        if not r.get('live_verified') or not r.get('live_evidence_url'):
            reasons.append('LIVE activity not yet verified')
            r['live_verified']=False;r['priority_tier']='review'
        else:
            if not any(x.get('claim')=='live_activity' and x.get('url')==r['live_evidence_url'] for x in ev):
                reasons.append('LIVE verification lacks matching evidence');r['live_verified']=False;r['priority_tier']='review'
        try: score=int(r.get('priority_score',0))
        except (ValueError,TypeError): score=0;reasons.append('Invalid score')
        r['priority_score']=max(0,min(100,score))
        try: coverage=float(r.get('score_coverage',0))
        except (ValueError,TypeError):coverage=0
        r['score_coverage']=max(0,min(1,coverage))
        if r['live_verified'] and not reasons:
            r['priority_tier']='high' if score>=70 and coverage>=.6 else ('medium' if score>=45 else 'review')
        r['review_reason']='; '.join(filter(None,[str(r.get('review_reason') or ''),*reasons]))
        for x in ev:
            if x.get('url'):
                evidence.append({'prospect_id':pid,**{k:x.get(k,'') for k in EVIDENCE_FIELDS if k!='prospect_id'}})
        prospective.append({c:r.get(c,'') for c in COLUMNS})
        if r['review_reason'] or not r['live_verified']:
            reviews.append({c:r.get(c,'') for c in COLUMNS})
    return prospective,evidence,reviews

def main():
    OUT.mkdir(exist_ok=True)
    if not SRC.exists():
        print(f'No {SRC}. No leads are prepopulated. Create it from researched evidence and rerun.')
        return 1
    records=json.loads(SRC.read_text(encoding='utf-8'))
    if not isinstance(records,list):raise ValueError('JSON must contain an array')
    prospect,evid,review=compile_data(records)
    write_csv(OUT/'prospects.csv',COLUMNS,prospect)
    write_csv(OUT/'evidence.csv',EVIDENCE_FIELDS,evid)
    write_csv(OUT/'review_queue.csv',COLUMNS,review)
    verified=sum(str(x['live_verified']).lower()=='true' for x in prospect)
    emails=sum(bool(x['business_email']) for x in prospect)
    high=sum(x['priority_tier']=='high' for x in prospect)
    summary = (
        f"# Research run summary\n\nGenerated UTC: {datetime.now(timezone.utc).isoformat()}\n\n"
        f"- Total research records: {len(prospect)}\n- LIVE verified: {verified}\n"
        f"- Public business emails with source: {emails}\n- High priority: {high}\n"
        f"- Review queue: {len(review)}\n- Evidence rows: {len(evid)}\n\n"
        "Read research notes and blocked-source limitations from Claude Code's run narrative.\n"
    )
    (OUT/'run_summary.md').write_text(summary,encoding='utf-8')
    print(f'Exported {len(prospect)} prospects; {verified} LIVE verified; {emails} emails; {len(review)} review')
    return 0
if __name__=='__main__':raise SystemExit(main())
