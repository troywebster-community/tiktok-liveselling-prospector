# 100-point priority scoring rubric

Score only supported positive evidence; unknown inputs earn **unassessed**, not an assertion of poor performance. Publish `priority_score` as earned points and `score_coverage` as fraction of dimensions assessable. Ranking among incomplete accounts is provisional.

- **LIVE cadence / freshness (0–30):** >=weekly LIVE within 30d 30; at least 2 dated LIVEs within 30d 24; one dated LIVE within 30d 16; proof 31–90d 8; none proven 0 and mark not qualified.
- **Commercial operation (0–20):** multiple products recurring sales and explicit TikTok Shop LIVE 20; repeated promotional commerce 14; one verified shoppable LIVE 8; unknown 0.
- **Audience strength (0–15):** 100k+ verified followers/subscribers on identified account 15; 25k–99,999 11; 5k–24,999 7; <5k 3; unknown 0 and audience dimension unassessed. Counts must be platform-specified and dated; do not compare views and followers as same measure.
- **Community SMS opportunity (0–20):** repeatedly promotes live schedules across channels with no **visible** SMS proof 14; has verified opt-in SMS program (possible competitor) 12; public stated need for notifications/list ownership 20; otherwise unknown 0. Never turn missing evidence into `sms_program=no`.
- **Contact actionability (0–15):** public business email verified from directly attributed site 15; official business contact form 9; active public business social contact 5; no contact 0.

Qualification: direct LIVE evidence + known seller/host account + geographical fit. `priority_tier` high (>=70 and coverage >=0.6 and LIVE verified), medium (45–69 or insufficient coverage), review (not verified/identity uncertain). Assign a separate `email_verification_status`: `publicly_listed`, `deliverability_checked`, `not_found`, `blocked`, `unverified`.
