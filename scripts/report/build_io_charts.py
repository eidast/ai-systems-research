#!/usr/bin/env python3
import json, sys
from pathlib import Path

if len(sys.argv) != 3:
    print('usage: build_io_charts.py <summary-json> <output-dir>', file=sys.stderr)
    sys.exit(1)
summary = json.loads(Path(sys.argv[1]).read_text())
out_dir = Path(sys.argv[2]); out_dir.mkdir(parents=True, exist_ok=True)
rows = [r for r in summary if r['group']['benchmark_id'] == 'io-large-file-streaming']
rows = sorted(rows, key=lambda r: r['metrics']['wall_time_ms']['mean'])
langs = [r['group']['language'] for r in rows]
wall = [r['metrics']['wall_time_ms']['mean'] for r in rows]
mem = [r['metrics']['mem_peak_mb']['mean'] for r in rows]
W,H,M=900,420,60

def bar(title, vals, labels, ylabel, name, color):
    maxv=max(vals) if vals else 1; iw=W-2*M; ih=H-2*M; bw=iw/max(len(vals),1)
    p=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}">',f'<text x="{W/2}" y="30" text-anchor="middle" font-size="20">{title}</text>',f'<line x1="{M}" y1="{H-M}" x2="{W-M}" y2="{H-M}" stroke="black"/>',f'<line x1="{M}" y1="{M}" x2="{M}" y2="{H-M}" stroke="black"/>',f'<text x="20" y="{H/2}" transform="rotate(-90 20,{H/2})" text-anchor="middle" font-size="14">{ylabel}</text>']
    for i,(lab,val) in enumerate(zip(labels,vals)):
        h=0 if maxv==0 else (val/maxv)*(ih-20); x=M+i*bw+20; y=H-M-h
        p.append(f'<rect x="{x}" y="{y}" width="{bw-40}" height="{h}" fill="{color}"/>')
        p.append(f'<text x="{x+(bw-40)/2}" y="{H-M+18}" text-anchor="middle" font-size="12">{lab}</text>')
        p.append(f'<text x="{x+(bw-40)/2}" y="{y-5}" text-anchor="middle" font-size="11">{round(val,2)}</text>')
    p.append('</svg>'); (out_dir/name).write_text(''.join(p))

bar('io-large-file-streaming — mean wall time', wall, langs, 'Milliseconds', 'io-large-file-streaming-wall-time.svg', '#2563eb')
bar('io-large-file-streaming — mean peak memory', mem, langs, 'MB', 'io-large-file-streaming-memory.svg', '#059669')
print(out_dir)
