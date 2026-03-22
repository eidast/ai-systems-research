#!/usr/bin/env python3
import json
import sys
from pathlib import Path

if len(sys.argv) != 4:
    print("usage: render_report.py <summary-json> <charts-dir> <output-md>", file=sys.stderr)
    sys.exit(1)

summary_path = Path(sys.argv[1])
charts_dir = Path(sys.argv[2])
out_path = Path(sys.argv[3])
out_path.parent.mkdir(parents=True, exist_ok=True)

data = json.loads(summary_path.read_text())
rows = [r for r in data if r["group"]["benchmark_id"] == "cpu-prime-count" and r["group"]["input_size"] == 300000]
rows = sorted(rows, key=lambda r: r["metrics"]["wall_time_ms"]["mean"])

lines = [
    "# Benchmark Report — CPU Prime Count",
    "",
    "## Configuration",
    "",
    "- benchmark: `cpu-prime-count`",
    "- input_size: `300000`",
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
    f"![Wall time](../charts/latest/cpu-prime-count-wall-time.svg)",
    "",
    f"![Peak memory](../charts/latest/cpu-prime-count-memory.svg)",
    "",
    f"![Memory vs time](../charts/latest/cpu-prime-count-memory-vs-time.svg)",
    "",
    f"![CPU](../charts/latest/cpu-prime-count-cpu.svg)",
    "",
    "## Notes",
    "",
    "- CPU is derived from host-side `/usr/bin/time -l` as `(user + sys) / real * 100`.",
    "- This remains a microbenchmark and is not sufficient alone for full architectural conclusions.",
]
out_path.write_text("\n".join(lines))
print(out_path)
