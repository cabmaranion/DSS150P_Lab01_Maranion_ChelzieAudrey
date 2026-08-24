import json
from datetime import datetime, timezone
from pathlib import Path
import requests

API_URL = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(API_URL, timeout=20)

if response.status_code != 200:
    raise SystemExit(f"Request failed with status {response.status_code}")

print("status:", response.status_code)
print("content-type:", response.headers.get("Content-Type"))

payload = response.json()
print("top-level type:", type(payload).__name__)

if isinstance(payload, list):
    print("number of records:", len(payload))
    print("\nsample record:")
    print(json.dumps(payload[0], indent=2))
elif isinstance(payload, dict):
    print("top-level keys:", list(payload.keys()))
    print("\nsample record:")
    print(json.dumps(payload, indent=2)[:500])

out_path = Path("data/raw/api_snapshot.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(payload, f, indent=2, ensure_ascii=False)

print("\nsaved to:", out_path)
print("retrieved_at_utc:", datetime.now(timezone.utc).isoformat())