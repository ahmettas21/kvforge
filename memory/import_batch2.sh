#!/bin/bash
# Import remaining Ham Rehber contacts
TOKEN=$(membrane token --expiresIn 720h 2>&1 | head -1)

# Generate JSONL with Python, save to file
python3 -c "
import json
with open('/tmp/raw_contacts.json') as f:
    raw = json.load(f)
remaining = raw[3700:]
for c in remaining:
    print(json.dumps({'name': c['name'][:100], 'phone': c['phone'][:30]}, ensure_ascii=False))
" > /tmp/batch2.jsonl

OK=0
FAIL=0
TOTAL=$(wc -l < /tmp/batch2.jsonl)
echo "Total to import: $TOTAL"

while IFS= read -r line; do
  NAME=$(echo "$line" | python3 -c "import sys,json; print(json.loads(sys.stdin.read()).get('name',''))" 2>/dev/null)
  PHONE=$(echo "$line" | python3 -c "import sys,json; print(json.loads(sys.stdin.read()).get('phone',''))" 2>/dev/null)
  
  if [ -z "$NAME" ]; then
    ((FAIL++))
    continue
  fi
  
  PAYLOAD='{"connectionKey":"notion","api":{"method":"POST","path":"/v1/pages","body":{"parent":{"database_id":"35e7f54b-79e1-81f3-9118-dd13c9f7812f"},"properties":{"İsim":{"title":[{"type":"text","text":{"content":"'"$NAME"'"}}]},"Telefon":{"rich_text":[{"type":"text","text":{"content":"'"$PHONE"'"}}]}}}}'
  
  STATUS=$(curl -s -m 30 "https://api.getmembrane.com/act" \
    -H "Authorization: Bearer $TOKEN" \
    -H "Content-Type: application/json" \
    -d "$PAYLOAD" 2>/dev/null | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('output',{}).get('status','?'))" 2>/dev/null)
  
  if [ "$STATUS" = "200" ]; then
    ((OK++))
  else
    ((FAIL++))
  fi
  
  if (( OK % 50 == 0 )); then
    echo "OK=$OK FAIL=$FAIL"
  fi
  
  sleep 0.02
done < /tmp/batch2.jsonl

echo "FINAL: OK=$OK FAIL=$FAIL"
