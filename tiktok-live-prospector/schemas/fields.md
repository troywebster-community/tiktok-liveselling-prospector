# Data contract

Use `data/research_records.json` as a JSON array of prospect objects. You may start from `schemas/sample_record.json`. All fields optional in source except `prospect_id`, `breaker_brand`, `seller_type`, `live_verified`, `evidence`. Exporter fills absent values as blank/unknown where appropriate. **No sample record counts as a lead.**

**Required requested business fields:** `breaker_brand` (seller / brand), `tiktok_shop` (where sells), `instagram`, `youtube`, `audience_size` (formatted platform + count), `business_email`, `email_source_url`, `website_linktree`, `sms_program` (`yes|no|unknown`), `recent_activity`, `priority_score`.

**Added TikTok-specific and QA fields:** `prospect_id`, `tiktok_handle`, `seller_type`, `linkedin`, `fanatics_ebay_other` (optional channel), `country`, `live_verified` (boolean), `live_evidence_url`, `live_evidence_date` (YYYY-MM-DD), `live_frequency`, `email_verification_status`, `business_contact_form`, `sms_evidence_url`, `priority_tier`, `score_coverage` (0..1), `source_access_status`, `research_date` (YYYY-MM-DD), `confidence`, `review_reason`, `seed_url`, `activity_source_url`, `audience_source_url`.

`evidence` is an array: `{ "claim": "live_activity|email|seller_identity|social|audience|sms|other", "url": "https://...", "source_type": "direct|official_crosslink|third_party|indexed_snippet", "observed_at": "YYYY-MM-DD", "note": "text" }`. No business email without a matching `email` claim and exact URL. For indexed snippets, mark evidence lower confidence.

Exported evidence file has prospect ID, claim, source URL/type, observation date and notes. Review queue includes unknown LIVE/identity, unsourced business email and conflicting evidence. The exporter enforces email-source rule and produces conservative status labels.
