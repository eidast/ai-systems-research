#!/usr/bin/env python3
import json
import sys
from collections import defaultdict

path = sys.argv[1]
agg = defaultdict(lambda: {"count": 0, "value_sum": 0, "weight_sum": 0, "active_count": 0})
total = 0
with open(path, 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        _, category, value, weight, active = line.split(',')
        bucket = agg[category]
        bucket['count'] += 1
        bucket['value_sum'] += int(value)
        bucket['weight_sum'] += int(weight)
        bucket['active_count'] += int(active)
        total += 1
print(json.dumps({"total_records": total, "categories": dict(agg)}, sort_keys=True))
