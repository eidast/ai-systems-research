#!/usr/bin/env python3
import json
import math
import sys
from pathlib import Path

if len(sys.argv) != 3:
    print("usage: build_charts.py <summary-json> <output-dir>", file=sys.stderr)
    sys.exit(1)

summary_path = Path(sys.argv[1])
out_dir = Path(sys.argv[2])
out_dir.mkdir(parents=True, exist_ok=True)

data = json.loads(summary_path.read_text())
rows = [r for r in data if r["group"]["benchmark_id"] == "cpu-prime-count" and r["group"]["input_size"] == 300000]
rows = sorted(rows, key=lambda r: r["metrics"]["wall_time_ms"]["mean"])
langs = [r["group"]["language"] for r in rows]
wall = [r["metrics"]["wall_time_ms"]["mean"] for r in rows]
mem = [r["metrics"]["mem_peak_mb"]["mean"] for r in rows]
cpu = [r["metrics"]["cpu_percent_avg"]["mean"] for r in rows]

WIDTH = 900
HEIGHT = 420
MARGIN = 60


def save(path: Path, content: str):
    path.write_text(content)


def bar_chart(title, labels, values, y_label, out_name, color="#4f46e5"):
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
        x = MARGIN + i * bar_w + 10
        y = HEIGHT - MARGIN - h
        parts.append(f'<rect x="{x}" y="{y}" width="{bar_w-20}" height="{h}" fill="{color}"/>')
        parts.append(f'<text x="{x + (bar_w-20)/2}" y="{HEIGHT-MARGIN+18}" text-anchor="middle" font-size="12">{lab}</text>')
        parts.append(f'<text x="{x + (bar_w-20)/2}" y="{y-5}" text-anchor="middle" font-size="11">{round(val,2)}</text>')
    parts.append('</svg>')
    save(out_dir / out_name, ''.join(parts))


def scatter_chart(title, xs, ys, labels, x_label, y_label, out_name):
    maxx = max(xs) if xs else 1
    maxy = max(ys) if ys else 1
    inner_w = WIDTH - 2 * MARGIN
    inner_h = HEIGHT - 2 * MARGIN
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}">']
    parts.append(f'<text x="{WIDTH/2}" y="30" text-anchor="middle" font-size="20">{title}</text>')
    parts.append(f'<line x1="{MARGIN}" y1="{HEIGHT-MARGIN}" x2="{WIDTH-MARGIN}" y2="{HEIGHT-MARGIN}" stroke="black"/>')
    parts.append(f'<line x1="{MARGIN}" y1="{MARGIN}" x2="{MARGIN}" y2="{HEIGHT-MARGIN}" stroke="black"/>')
    parts.append(f'<text x="{WIDTH/2}" y="{HEIGHT-10}" text-anchor="middle" font-size="14">{x_label}</text>')
    parts.append(f'<text x="20" y="{HEIGHT/2}" transform="rotate(-90 20,{HEIGHT/2})" text-anchor="middle" font-size="14">{y_label}</text>')
    for x, y, label in zip(xs, ys, labels):
        px = MARGIN + (x / maxx) * (inner_w - 20) if maxx else MARGIN
        py = HEIGHT - MARGIN - (y / maxy) * (inner_h - 20) if maxy else HEIGHT-MARGIN
        parts.append(f'<circle cx="{px}" cy="{py}" r="5" fill="#dc2626"/>')
        parts.append(f'<text x="{px+8}" y="{py-8}" font-size="12">{label}</text>')
    parts.append('</svg>')
    save(out_dir / out_name, ''.join(parts))

bar_chart("cpu-prime-count @ input_size=300000 — mean wall time", langs, wall, "Milliseconds", "cpu-prime-count-wall-time.svg")
bar_chart("cpu-prime-count @ input_size=300000 — mean peak memory", langs, mem, "MB", "cpu-prime-count-memory.svg", color="#059669")
bar_chart("cpu-prime-count @ input_size=300000 — derived CPU utilization", langs, cpu, "CPU %", "cpu-prime-count-cpu.svg", color="#d97706")
scatter_chart("cpu-prime-count — memory vs wall time", mem, wall, langs, "Mean peak memory (MB)", "Mean wall time (ms)", "cpu-prime-count-memory-vs-time.svg")
print(out_dir)
