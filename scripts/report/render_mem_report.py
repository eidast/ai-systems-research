#!/usr/bin/env python3
import json
import sys
from pathlib import Path

if len(sys.argv) != 4:
    print("usage: render_mem_report.py <summary-json> <charts-dir> <output-md>", file=sys.stderr)
    sys.exit(1)

summary_path = Path(sys.argv[1])
out_path = Path(sys.argv[3])
out_path.parent.mkdir(parents=True, exist_ok=True)

data = json.loads(summary_path.read_text())
rows = [r for r in data if r["group"]["benchmark_id"] == "mem-large-json-transform"]
rows = sorted(rows, key=lambda r: r["metrics"]["wall_time_ms"]["mean"])

lines = [
    "# Benchmark Report — MEM Large JSON Transform",
    "",
    "## Configuration",
    "",
    "- benchmark: `mem-large-json-transform`",
    "- dataset: `benchmarks/datasets/generated/mem-large-json-transform-medium.json`",
    "- trials: `3` per language",
    "- warmups: `1`",
    "",
    "## Summary Table",
    "",
    "| Language | Mean ms | Median ms | Peak memory MB | CPU avg % | Trials |",
    "|---|---:|---:|---:|---:|---:|",
]
for r in rows:
    lines.append(f"| {r['group']['language']} | {r['metrics']['wall_time_ms']['mean']} | {r['metrics']['wall_time_ms']['median']} | {r['metrics']['mem_peak_mb']['mean']} | {r['metrics']['cpu_percent_avg']['mean']} | {r['trials']} |")
lines += [
    "",
    "## Charts",
    "",
    "![Wall time](../charts/latest/mem-large-json-transform-wall-time.svg)",
    "",
    "![Peak memory](../charts/latest/mem-large-json-transform-memory.svg)",
    "",
    "## Notes",
    "",
    "- Component benchmark for transform-heavy JSON processing.",
    "- CPU is derived from host-side `/usr/bin/time -l` as `(user + sys) / real * 100`.",
]
out_path.write_text("\n".join(lines))
print(out_path)
