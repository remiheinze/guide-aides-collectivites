#!/usr/bin/env python3
"""Synchronize public aid records from Aides-territoires."""
import json
import os
import time
from pathlib import Path
from urllib.request import Request, urlopen

TOKEN = os.environ.get("AIDES_TERRITOIRES_TOKEN", "").strip()
if not TOKEN:
    raise SystemExit(
        "Secret AIDES_TERRITOIRES_TOKEN absent. Demandez un jeton à aides-territoires@beta.gouv.fr "
        "puis ajoutez-le dans GitHub Settings > Secrets and variables > Actions."
    )

url = "https://aides-territoires.beta.gouv.fr/api/aids/?page=1"
items, seen = [], set()
while url:
    if url in seen:
        raise RuntimeError(f"Pagination loop detected: {url}")
    seen.add(url)
    req = Request(url, headers={
        "Accept": "application/json",
        "User-Agent": "GuideAidesCollectivites/1.0",
        "X-AUTH-TOKEN": TOKEN,
    })
    with urlopen(req, timeout=45) as response:
        payload = json.load(response)
    if not isinstance(payload, dict) or not isinstance(payload.get("results"), list):
        raise RuntimeError("Unexpected API response format")
    items.extend(payload["results"])
    url = payload.get("next")
    time.sleep(0.15)

out = Path("data/aids.json")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(items, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
print(f"Saved {len(items)} aid records to {out}")
