#!/usr/bin/env python3
import json
import math
import multiprocessing as mp
import sys

ITEM_COUNT = int(sys.argv[1]) if len(sys.argv) > 1 else 200000
WORKERS = 4

def transform(x: int) -> int:
    return (x * 7 + 11) % 1000

def worker(bounds):
    start, end = bounds
    total = 0
    count = 0
    for i in range(start, end):
        total += transform(i)
        count += 1
    return count, total

def main():
    chunk = math.ceil(ITEM_COUNT / WORKERS)
    ranges = [(i, min(i + chunk, ITEM_COUNT)) for i in range(0, ITEM_COUNT, chunk)]
    with mp.Pool(WORKERS) as pool:
        results = pool.map(worker, ranges)
    count = sum(x[0] for x in results)
    value_sum = sum(x[1] for x in results)
    print(json.dumps({"item_count": count, "value_sum": value_sum, "workers": WORKERS}, sort_keys=True))

if __name__ == '__main__':
    main()
