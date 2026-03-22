#!/usr/bin/env python3
import json
import queue
import sys
import threading

ITEM_COUNT = int(sys.argv[1]) if len(sys.argv) > 1 else 100000
WORKERS = 4
QSIZE = 256
q = queue.Queue(maxsize=QSIZE)
results = []
lock = threading.Lock()


def transform(x: int) -> int:
    return (x * 3 + 7) % 1000


def producer():
    for i in range(ITEM_COUNT):
        q.put(i)
    for _ in range(WORKERS):
        q.put(None)


def consumer():
    local_count = 0
    local_sum = 0
    while True:
        item = q.get()
        try:
            if item is None:
                break
            value = transform(item)
            local_count += 1
            local_sum += value
        finally:
            q.task_done()
    with lock:
        results.append((local_count, local_sum))

threads = [threading.Thread(target=consumer) for _ in range(WORKERS)]
for t in threads:
    t.start()
producer_thread = threading.Thread(target=producer)
producer_thread.start()
producer_thread.join()
q.join()
for t in threads:
    t.join()

count = sum(x[0] for x in results)
sumv = sum(x[1] for x in results)
print(json.dumps({"item_count": count, "value_sum": sumv, "workers": WORKERS, "queue_capacity": QSIZE}, sort_keys=True))
