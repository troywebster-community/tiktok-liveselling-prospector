import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from check_setup import check
from export import compile_data
class TestProject(unittest.TestCase):
    def test_files_and_seeds(self): self.assertEqual(check(),[])
    def test_unsourced_email_removed(self):
        p,e,r=compile_data([{'prospect_id':'1','breaker_brand':'Test','business_email':'fake@example.com','email_source_url':'https://example.com','live_verified':False,'sms_program':'unknown','evidence':[]}])
        self.assertFalse(p[0]['business_email']);self.assertEqual(len(r),1)
    def test_sourced_email_stays(self):
        p,e,r=compile_data([{'prospect_id':'1','breaker_brand':'Test','business_email':'hello@example.com','email_source_url':'https://example.com/contact','live_verified':True,'live_evidence_url':'https://example.com/live','country':'US','score_coverage':1,'priority_score':80,'sms_program':'unknown','evidence':[{'claim':'email','url':'https://example.com/contact'},{'claim':'live_activity','url':'https://example.com/live'}]}])
        self.assertEqual(p[0]['business_email'],'hello@example.com');self.assertEqual(p[0]['priority_tier'],'high')
    def test_sms_without_evidence_unknown(self):
        p,_,_=compile_data([{'prospect_id':'1','sms_program':'yes','evidence':[]}]);self.assertEqual(p[0]['sms_program'],'unknown')
    def test_non_us_live_not_qualified(self):
        p,_,r=compile_data([{'prospect_id':'1','live_verified':True,'live_evidence_url':'https://example.com/live','country':'unknown','score_coverage':1,'priority_score':90,'sms_program':'unknown','evidence':[{'claim':'live_activity','url':'https://example.com/live'}]}])
        self.assertEqual(p[0]['priority_tier'],'review');self.assertEqual(len(r),1)
if __name__=='__main__':unittest.main()
