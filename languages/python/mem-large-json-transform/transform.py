#!/usr/bin/env python3
import json
import sys
from collections import defaultdict

path = sys.argv[1]
with open(path, 'r') as f:
    data = json.load(f)

agg = defaultdict(lambda: {"count": 0, "value_sum": 0, "weight_sum": 0, "active_count": 0})
for item in data:
    bucket = agg[item['category']]
    bucket['count'] += 1
    bucket['value_sum'] += item['value']
    bucket['weight_sum'] += item['weight']
    bucket['active_count'] += 1 if item['active'] else 0

summary = {
    "total_records": len(data),
    "categories": dict(agg),
}
print(json.dumps(summary, sort_keys=True))
