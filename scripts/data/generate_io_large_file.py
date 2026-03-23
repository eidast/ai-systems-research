#!/usr/bin/env python3
from pathlib import Path

out = Path('benchmarks/datasets/generated/io-large-file-streaming-medium.txt')
out.parent.mkdir(parents=True, exist_ok=True)
with out.open('w') as f:
    for i in range(200000):
        category = f"cat-{i % 20}"
        value = (i * 7) % 1000
        weight = (i * 13) % 97
        active = 1 if i % 3 == 0 else 0
        f.write(f"{i},{category},{value},{weight},{active}\n")
print(out)
