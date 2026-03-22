#!/usr/bin/env python3
import json
from pathlib import Path

out = Path('benchmarks/datasets/generated/mem-large-json-transform-medium.json')
out.parent.mkdir(parents=True, exist_ok=True)
records = []
for i in range(50000):
    records.append({
        "id": i,
        "category": f"cat-{i % 20}",
        "value": (i * 7) % 1000,
        "weight": (i * 13) % 97,
        "active": i % 3 == 0,
        "name": f"record-{i}",
    })
out.write_text(json.dumps(records))
print(out)
