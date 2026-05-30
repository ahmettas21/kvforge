#!/usr/bin/env python3
"""Final Ham Rehber import - no shell escaping, just Python requests."""
import json, subprocess, time, os, sys

HAM_DB = "35e7f54b-79e1-81f3-9118-dd13c9f7812f"

def create(c, token):
    payload = json.dumps({
        "connectionKey": "notion",
        "api": {
            "method": "POST",
            "path": "/v1/pages",
            "body": {
                "parent": {"database_id": HAM_DB},
                "properties": {
                    "İsim": {"title": [{"type": "text", "text": {"content": c['name'][:100]}}]},
                    "Telefon": {"rich_text": [{"type": "text", "text": {"content": c['phone'][:30]}}]}
                }
            }
        }
    }, ensure_ascii=False)
    
    cmd = ['curl', '-s', '-m', '30',
        'https://api.getmembrane.com/act',
        '-H', f'Authorization: Bearer {token}',
        '-H', 'Content-Type: application/json',
        '-d', payload]
    
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=35)
    try:
        d = json.loads(r.stdout)
        return d.get('output',{}).get('status') == 200
    except:
        return False

# Load remaining
with open('/tmp/raw_contacts.json') as f:
    raw = json.load(f)

remaining = raw[3700:]
total = len(remaining)
print(f"Remaining: {total}")

# Get token
r = subprocess.run(['membrane','token','--expiresIn','720h'], capture_output=True, text=True, timeout=10)
token = [l.strip() for l in r.stdout.split('\n') if l.strip()][0]

ok = fail = 0
for i, c in enumerate(remaining):
    if create(c, token):
        ok += 1
    else:
        fail += 1
        # Refresh token on fail
        r = subprocess.run(['membrane','token','--expiresIn','720h'], capture_output=True, text=True, timeout=10)
        token = [l.strip() for l in r.stdout.split('\n') if l.strip()][0]
    
    if (i+1) % 50 == 0:
        print(f"  {i+1}/{total} OK={ok} FAIL={fail}")
        sys.stdout.flush()
    
    time.sleep(0.03)

print(f"\nDONE: OK={ok} FAIL={fail}")
print(f"Grand total Kişiler DB: 688")
print(f"Grand total Ham Rehber DB: ~3560+{ok} (API'deki sayıyı kontrol et)")
