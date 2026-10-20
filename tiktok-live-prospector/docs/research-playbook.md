# TikTok Shop LIVE research playbook

## Identify the market correctly
TikTok Shop has distinct participants: `SELLER` (runs a shop), `CREATOR_AFFILIATE` (sells other brands' products), `BRAND_HOST` (staff/host selling for a brand), `AGENCY` (manages hosts), `UNKNOWN`. A shopper video or store product is not itself proof of LIVE selling. A multi-brand creator can be a strong prospect, but decide the **buyer/contact target** from evidence, not assumptions.

## Seed triage
- Shortlinks: save original exactly; if it redirects, save destination, visible shop/account, and timestamp. If redirects fail, mark `unresolved`, and search quoted URL code and related indexed snippets. Do not invent destination.
- LinkedIn: independently confirm named person's role, company, and business relation to TikTok Shop LIVE. Look for official websites, interviews, TikTok accounts and events. Do not assume every LinkedIn seed is a TikTok seller.
- Cross-platform identity requires brand self-links, official website links or credible third-party attribution. Similar names/handles are only candidates.

## Discovery queries (examples; customize by product/category)
- `site:tiktok.com/@ "LIVE" "TikTok Shop" "beauty"`
- `"TikTok Shop LIVE" "host" "business inquiries"`
- `"TikTok Shop" "live shopping" "email" "fashion"`
- `"TikTok LIVE" "shop" "join me live"`
- `"TikTok Shop LIVE" "stream schedule"`
- `"TikTok Shop creator" "LIVE" "linktree"`
- `"TikTok Shop LIVE" "host" "contact" site:linkedin.com/in`
- `"TikTok Shop" "live seller" "SMS"`
- Brand websites, creator press/interviews, YouTube archived live streams, Instagram caption snippets, news lists, event speaker/host pages.

## For every qualified prospect
1. Name/brand and `seller_type` with evidence; US location if supported.
2. LIVE evidence: direct replay, scheduled live, date-stamped clip referring to the broadcast, credible media/event listing; store evidence type, date, link. Recency: <=30 days strong, 31-90 days provisional, >90 days unverified/inactive pending research.
3. Selling/storefront links: official shop/seller URL, TikTok page, cross-platform sites; separate links for ambiguous brands.
4. Social profiles and public audience counts with observed date, platform and source. If inaccessible, `unknown`.
5. Official website/link-in-bio and direct business email on a named page. If not found after a reasonable search, leave blank and retain alternate contact route; explicitly mark `not_found` vs `blocked`.
6. SMS program: `yes` if opt-in marketing CTA observed, `unknown` without affirmative evidence; `no` only where directly supported. Record source and known provider only if explicitly named.
7. Score by `docs/scoring.md` and identify coverage gaps separately.

## Anti-hallucination checkpoints
- URL not loadable? You may cite indexed search result **as secondary**, with label `indexed_snippet` and capture date. Do not pretend it is a verified page visit.
- No public email? Do not synthesize or buy private contact information. Business form is sufficient as alternative.
- Counts change; write number, unit, platform and observation date or `unknown`.
- If source contradicts another, put the prospect in review queue.
- Deduplicate by confirmed canonical account/brand rather than similar personal names. Keep multiple business divisions if distinct.
