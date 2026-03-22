#!/usr/bin/env python3
import json
import math
import statistics
import sys
from pathlib import Path

if len(sys.argv) != 3:
    print("usage: aggregate.py <raw-dir> <output-dir>", file=sys.stderr)
    sys.exit(1)

raw_dir = Path(sys.argv[1])
out_dir = Path(sys.argv[2])
out_dir.mkdir(parents=True, exist_ok=True)

runs = []
for path in raw_dir.glob("*/runs/*.json"):
    runs.append(json.loads(path.read_text()))

groups = {}
for r in runs:
    key = (
        r["benchmark"]["id"],
        r["implementation"]["language"],
        r["implementation"]["mode"],
        r["parameters"]["input_size"],
    )
    groups.setdefault(key, []).append(r)

summary = []
for key, items in groups.items():
    wall = [x["metrics"]["wall_time_ms"] for x in items]
    cpu = [x["metrics"]["cpu_percent_avg"] for x in items]
    mem = [x["metrics"]["mem_peak_mb"] for x in items]
    summary.append({
        "group": {
            "benchmark_id": key[0],
            "language": key[1],
            "mode": key[2],
            "input_size": key[3],
        },
        "trials": len(items),
        "metrics": {
            "wall_time_ms": {
                "mean": round(statistics.mean(wall), 3),
                "median": round(statistics.median(wall), 3),
                "min": round(min(wall), 3),
                "max": round(max(wall), 3),
                "stddev": round(statistics.pstdev(wall), 3) if len(wall) > 1 else 0.0,
            },
            "cpu_percent_avg": {
                "mean": round(statistics.mean(cpu), 3),
                "max": round(max(cpu), 3),
            },
            "mem_peak_mb": {
                "mean": round(statistics.mean(mem), 3),
                "max": round(max(mem), 3),
            },
        },
    })

(out_dir / "result-summary.json").write_text(json.dumps(summary, indent=2))
print(out_dir / "result-summary.json")
