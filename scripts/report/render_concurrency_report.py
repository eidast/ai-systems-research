#!/usr/bin/env python3
import json
import sys
from pathlib import Path

if len(sys.argv) != 4:
    print('usage: render_concurrency_report.py <summary-json> <charts-dir> <output-md>', file=sys.stderr)
    sys.exit(1)
summary = json.loads(Path(sys.argv[1]).read_text())
out_path = Path(sys.argv[3])
out_path.parent.mkdir(parents=True, exist_ok=True)
rows = [r for r in summary if r['group']['benchmark_id'] == 'con-producer-consumer-pipeline']
rows = sorted(rows, key=lambda r: r['metrics']['wall_time_ms']['mean'])
lines = ['# Benchmark Report — Producer Consumer Pipeline','','## Summary Table','','| Language | Mean ms | Median ms | Peak memory MB | CPU avg % | Trials |','|---|---:|---:|---:|---:|---:|']
for r in rows:
    lines.append(f"| {r['group']['language']} | {r['metrics']['wall_time_ms']['mean']} | {r['metrics']['wall_time_ms']['median']} | {r['metrics']['mem_peak_mb']['mean']} | {r['metrics']['cpu_percent_avg']['mean']} | {r['trials']} |")
lines += ['', '## Charts', '', '![Wall time](../charts/latest/con-producer-consumer-pipeline-wall-time.svg)', '', '![Peak memory](../charts/latest/con-producer-consumer-pipeline-memory.svg)', '', '## Notes', '', '- Component benchmark for bounded in-process concurrency coordination.', '- CPU is derived from host-side `/usr/bin/time -l` as `(user + sys) / real * 100`.']
out_path.write_text('\n'.join(lines))
print(out_path)
