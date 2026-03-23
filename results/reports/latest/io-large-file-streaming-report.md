# Benchmark Report — Large File Streaming

## Summary Table

| Language | Mean ms | Median ms | Peak memory MB | CPU avg % | Trials |
|---|---:|---:|---:|---:|---:|
| go | 77.88 | 77.942 | 22.323 | 283.333 | 3 |
| typescript | 99.648 | 98.641 | 61.63 | 100.0 | 6 |
| python | 135.907 | 135.582 | 11.556 | 94.276 | 9 |
| rust | 334.507 | 335.875 | 1.943 | 56.99 | 3 |
| java | 418.019 | 434.841 | 121.922 | 211.034 | 3 |
| csharp | 758.015 | 757.538 | 219.641 | 116.741 | 3 |

## Charts

![Wall time](../charts/latest/io-large-file-streaming-wall-time.svg)

![Peak memory](../charts/latest/io-large-file-streaming-memory.svg)

## Notes

- Component benchmark for line-oriented file streaming.
- CPU is derived from host-side `/usr/bin/time -l` as `(user + sys) / real * 100`.