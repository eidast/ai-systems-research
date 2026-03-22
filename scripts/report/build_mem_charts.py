#!/usr/bin/env python3
import json
import sys
from pathlib import Path

if len(sys.argv) != 3:
    print("usage: build_mem_charts.py <summary-json> <output-dir>", file=sys.stderr)
    sys.exit(1)

summary_path = Path(sys.argv[1])
out_dir = Path(sys.argv[2])
out_dir.mkdir(parents=True, exist_ok=True)

data = json.loads(summary_path.read_text())
rows = [r for r in data if r["group"]["benchmark_id"] == "mem-large-json-transform"]
rows = sorted(rows, key=lambda r: r["metrics"]["wall_time_ms"]["mean"])
langs = [r["group"]["language"] for r in rows]
wall = [r["metrics"]["wall_time_ms"]["mean"] for r in rows]
mem = [r["metrics"]["mem_peak_mb"]["mean"] for r in rows]

WIDTH = 900
HEIGHT = 420
MARGIN = 60

def save(path: Path, content: str):
    path.write_text(content)

def bar_chart(title, labels, values, y_label, out_name, color="#2563eb"):
    maxv = max(values) if values else 1
    inner_w = WIDTH - 2 * MARGIN
    inner_h = HEIGHT - 2 * MARGIN
    bar_w = inner_w / max(len(values), 1)
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}">']
    parts.append(f'<text x="{WIDTH/2}" y="30" text-anchor="middle" font-size="20">{title}</text>')
    parts.append(f'<line x1="{MARGIN}" y1="{HEIGHT-MARGIN}" x2="{WIDTH-MARGIN}" y2="{HEIGHT-MARGIN}" stroke="black"/>')
    parts.append(f'<line x1="{MARGIN}" y1="{MARGIN}" x2="{MARGIN}" y2="{HEIGHT-MARGIN}" stroke="black"/>')
    parts.append(f'<text x="20" y="{HEIGHT/2}" transform="rotate(-90 20,{HEIGHT/2})" text-anchor="middle" font-size="14">{y_label}</text>')
    for i, (lab, val) in enumerate(zip(labels, values)):
        h = 0 if maxv == 0 else (val / maxv) * (inner_h - 20)
        x = MARGIN + i * bar_w + 20
        y = HEIGHT - MARGIN - h
        parts.append(f'<rect x="{x}" y="{y}" width="{bar_w-40}" height="{h}" fill="{color}"/>')
        parts.append(f'<text x="{x + (bar_w-40)/2}" y="{HEIGHT-MARGIN+18}" text-anchor="middle" font-size="12">{lab}</text>')
        parts.append(f'<text x="{x + (bar_w-40)/2}" y="{y-5}" text-anchor="middle" font-size="11">{round(val,2)}</text>')
    parts.append('</svg>')
    save(out_dir / out_name, ''.join(parts))

bar_chart("mem-large-json-transform — mean wall time", langs, wall, "Milliseconds", "mem-large-json-transform-wall-time.svg")
bar_chart("mem-large-json-transform — mean peak memory", langs, mem, "MB", "mem-large-json-transform-memory.svg", color="#059669")
print(out_dir)
