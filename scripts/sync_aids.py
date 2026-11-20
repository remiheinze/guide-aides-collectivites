#!/usr/bin/env python3
"""Download all active aid records from the public Aides-territoires API."""
import json
import time
from pathlib import Path
from urllib.request import Request, urlopen

BASE = "https://aides-territoires.beta.gouv.fr/api/aids/?page=1"
OUT = Path("data/aids.json")
items = []
url = BASE
seen = set()

while url:
    if url in seen:
        raise RuntimeError(f"Pagination loop detected: {url}")
    seen.add(url)
    req = Request(url, headers={"Accept": "application/json", "User-Agent": "GuideAidesCollectivites/1.0"})
    with urlopen(req, timeout=45) as response:
        payload = json.load(response)
    page = payload.get("results", []) if isinstance(payload, dict) else payload
    if not isinstance(page, list):
        raise RuntimeError("Unexpected API response format")
    items.extend(page)
    url = payload.get("next") if isinstance(payload, dict) else None
    time.sleep(0.15)

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(items, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
print(f"Saved {len(items)} aid records to {OUT}")
