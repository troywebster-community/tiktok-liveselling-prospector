---
name: prospect-tiktok-live
description: Run the TikTok Shop LIVE prospecting workflow. Research the 16 seed links, discover verified active US TikTok Shop LIVE sellers, creator affiliates and brand hosts, record evidence in data/research_records.json, export CSVs and run tests. Use when asked to run, refresh or extend the prospect list.
---

# Prospect TikTok Shop LIVE sellers

Follow `CLAUDE.md` truth standards at every step. They override anything below.

## 1. Setup
1. Read `docs/research-playbook.md`, `docs/scoring.md`, `docs/access-fallbacks.md`, `schemas/fields.md`, `data/seed_links.csv`.
2. Run `python3 scripts/check_setup.py`. Fix missing local files before research.
3. List which tools work right now (web search, page fetch, curl). Test LinkedIn, TikTok, Instagram. Write down what is blocked. Never claim access you don't have.

## 2. Seeds (all 16, before discovery)
- TikTok shortlinks: `curl -sS -o /dev/null -w "%{redirect_url}" URL` shows the app deep link with a `sellerId`. The public store page is `https://shop.tiktok.com/us/store/x/<sellerId>`; its HTML carries `"shop_name"`. That identifies the shop, it does not prove LIVE.
- LinkedIn seeds: LinkedIn blocks logged-out fetches (HTTP 999). Research the person through web search, company bios, interviews, event pages. Do not tie a LinkedIn seed to a TikTok seed without public evidence.
- Every seed gets a record, even if it does not qualify. Set `seed_url` to the original link exactly.

## 3. Discovery
Use the `discovery-researcher` agent, split by category (beauty, fashion, collectibles and trading cards, jewelry and crystals, home and kitchen, wellness and supplements, pets, food, thrift and resale). Use queries from the playbook.

## 4. Evidence tools
- `python3 scripts/tiktok_public.py profile HANDLE` gives public follower count, bio, bio link, commerce flag and `room_id_live_now` (non-empty means LIVE at time of check: direct `live_activity` evidence dated today).
- `python3 scripts/tiktok_public.py video-date URL` decodes a TikTok video ID into its UTC post date. A dated video that shows or announces a specific LIVE broadcast counts; a plain shoppable video does not.
- Other LIVE proof: YouTube or Instagram LIVE replays with dates, brand pages announcing a dated TikTok LIVE, news or event listings.

## 5. Contacts and SMS
Use the `contact-verifier` agent. Business emails only, from a page the account controls or cross-links, exact URL recorded. SMS `yes` only with an observed opt-in prompt (keyword text-to-join, SMS signup form, "text me" link to a texting platform).

## 6. Scoring, audit, export
1. Score with `docs/scoring.md`. Record `priority_score` and `score_coverage`.
2. Run the `qualification-auditor` agent over all records.
3. `python3 scripts/export.py`, then `python3 -m unittest discover -s tests -v`.
4. Report exact counts: LIVE verified, public business emails, high tier. Explain limits. Do not pad to 50.
