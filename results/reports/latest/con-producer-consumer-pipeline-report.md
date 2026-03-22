# Benchmark Report — Producer Consumer Pipeline

## Summary Table

| Language | Mean ms | Median ms | Peak memory MB | CPU avg % | Trials |
|---|---:|---:|---:|---:|---:|
| typescript | 45.074 | 44.985 | 52.891 | 100.0 | 3 |
| python | 122.16 | 121.184 | 12.427 | 100.0 | 6 |

## Charts

![Wall time](../charts/latest/con-producer-consumer-pipeline-wall-time.svg)

![Peak memory](../charts/latest/con-producer-consumer-pipeline-memory.svg)

## Notes

- Component benchmark for bounded in-process concurrency coordination.
- CPU is derived from host-side `/usr/bin/time -l` as `(user + sys) / real * 100`.