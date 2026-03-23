#!/usr/bin/env python3
import json, sys
from pathlib import Path

if len(sys.argv) != 4:
    print('usage: render_io_report.py <summary-json> <charts-dir> <output-md>', file=sys.stderr)
    sys.exit(1)
summary = json.loads(Path(sys.argv[1]).read_text())
out = Path(sys.argv[3]); out.parent.mkdir(parents=True, exist_ok=True)
rows = [r for r in summary if r['group']['benchmark_id'] == 'io-large-file-streaming']
rows = sorted(rows, key=lambda r: r['metrics']['wall_time_ms']['mean'])
lines=['# Benchmark Report — Large File Streaming','','## Summary Table','','| Language | Mean ms | Median ms | Peak memory MB | CPU avg % | Trials |','|---|---:|---:|---:|---:|---:|']
for r in rows:
    lines.append(f"| {r['group']['language']} | {r['metrics']['wall_time_ms']['mean']} | {r['metrics']['wall_time_ms']['median']} | {r['metrics']['mem_peak_mb']['mean']} | {r['metrics']['cpu_percent_avg']['mean']} | {r['trials']} |")
lines += ['', '## Charts', '', '![Wall time](../charts/latest/io-large-file-streaming-wall-time.svg)', '', '![Peak memory](../charts/latest/io-large-file-streaming-memory.svg)', '', '## Notes', '', '- Component benchmark for line-oriented file streaming.', '- CPU is derived from host-side `/usr/bin/time -l` as `(user + sys) / real * 100`.']
out.write_text('\n'.join(lines))
print(out)
