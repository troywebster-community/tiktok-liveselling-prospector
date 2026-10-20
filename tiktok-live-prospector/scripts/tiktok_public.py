#!/usr/bin/env python3
"""Read public, logged-out TikTok profile fields and decode video post dates; stdlib only.

Usage:
  python3 scripts/tiktok_public.py profile HANDLE [HANDLE ...]
  python3 scripts/tiktok_public.py live HANDLE [HANDLE ...]
  python3 scripts/tiktok_public.py video-date VIDEO_URL_OR_ID [...]

Only reads what TikTok serves to any logged-out visitor. No login, no captcha bypass.
`live` reads the public /@HANDLE/live page, which lists the account's most recent LIVE room:
room_status 2 means broadcasting at check time, 4 means ended; start_utc dates that LIVE.
The profile page's roomId is often empty even while live, so use `live` for LIVE evidence.
"""
import json, re, sys, urllib.request
from datetime import datetime, timezone

UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36'

def fetch(url):
    req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept-Language': 'en-US,en;q=0.9'})
    with urllib.request.urlopen(req, timeout=25) as r:
        return r.read().decode('utf-8', 'replace')

def profile(handle):
    handle = handle.lstrip('@')
    url = f'https://www.tiktok.com/@{handle}'
    out = {'handle': handle, 'url': url, 'observed_at': datetime.now(timezone.utc).strftime('%Y-%m-%d')}
    try:
        html = fetch(url)
    except Exception as e:
        out['access_status'] = f'blocked ({e.__class__.__name__})'
        return out
    m = re.search(r'<script id="__UNIVERSAL_DATA_FOR_REHYDRATION__"[^>]*>(.*?)</script>', html, re.S)
    if not m:
        out['access_status'] = 'unresolved'
        return out
    data = json.loads(m.group(1))
    info = data.get('__DEFAULT_SCOPE__', {}).get('webapp.user-detail', {}).get('userInfo')
    if not info or not info.get('user', {}).get('uniqueId'):
        out['access_status'] = 'not_found'
        return out
    u, s = info['user'], info.get('stats', {})
    out.update({
        'access_status': 'accessible',
        'unique_id': u.get('uniqueId'),
        'nickname': u.get('nickname'),
        'verified': u.get('verified'),
        'bio': u.get('signature'),
        'bio_link': (u.get('bioLink') or {}).get('link'),
        'commerce_user': (u.get('commerceUserInfo') or {}).get('commerceUser'),
        'followers': s.get('followerCount'),
        'likes': s.get('heartCount'),
        'videos': s.get('videoCount'),
    })
    return out

def live(handle):
    handle = handle.lstrip('@')
    url = f'https://www.tiktok.com/@{handle}/live'
    out = {'handle': handle, 'url': url, 'checked_utc': datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M')}
    try:
        html = fetch(url)
    except Exception as e:
        out['access_status'] = f'blocked ({e.__class__.__name__})'
        return out
    m = re.search(r'<script id="SIGI_STATE"[^>]*>(.*?)</script>', html, re.S)
    if not m:
        out['access_status'] = 'unresolved'
        return out
    info = json.loads(m.group(1)).get('LiveRoom', {}).get('liveRoomUserInfo') or {}
    room = info.get('liveRoom') or {}
    start = room.get('startTime')
    out.update({
        'access_status': 'accessible' if info else 'not_found',
        'room_id': (info.get('user') or {}).get('roomId') or '',
        'room_status': room.get('status'),
        'title': room.get('title'),
        'start_utc': datetime.fromtimestamp(start, timezone.utc).strftime('%Y-%m-%d %H:%M') if start else None,
        'viewers': (room.get('liveRoomStats') or {}).get('userCount'),
    })
    return out

def video_date(v):
    m = re.search(r'(\d{15,20})', v)
    if not m:
        return {'input': v, 'error': 'no video id'}
    ts = int(m.group(1)) >> 32
    return {'input': v, 'posted_utc': datetime.fromtimestamp(ts, timezone.utc).strftime('%Y-%m-%d %H:%M')}

if __name__ == '__main__':
    cmds = {'profile': profile, 'live': live, 'video-date': video_date}
    if len(sys.argv) < 3 or sys.argv[1] not in cmds:
        print(__doc__); raise SystemExit(2)
    fn = cmds[sys.argv[1]]
    for arg in sys.argv[2:]:
        print(json.dumps(fn(arg), ensure_ascii=False))
