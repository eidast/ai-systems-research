# Benchmark Report — Large File Streaming

## Summary Table

| Language | Mean ms | Median ms | Peak memory MB | CPU avg % | Trials |
|---|---:|---:|---:|---:|---:|
| typescript | 98.378 | 98.317 | 61.719 | 100.0 | 3 |
| python | 135.846 | 135.846 | 11.576 | 92.803 | 6 |

## Charts

![Wall time](../charts/latest/io-large-file-streaming-wall-time.svg)

![Peak memory](../charts/latest/io-large-file-streaming-memory.svg)

## Notes

- Component benchmark for line-oriented file streaming.
- CPU is derived from host-side `/usr/bin/time -l` as `(user + sys) / real * 100`.