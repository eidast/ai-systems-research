# Benchmark Report — CPU Prime Count

## Configuration

- benchmark: `cpu-prime-count`
- input_size: `300000`
- trials: `3` per language
- warmups: `1`

## Summary Table

| Language | Mean ms | Median ms | Peak memory MB | CPU avg % | Trials |
|---|---:|---:|---:|---:|---:|
| python | 31.862 | 31.783 | 12.172 | 50.0 | 6 |
| typescript | 37.363 | 37.358 | 47.495 | 25.0 | 6 |
| go | 67.115 | 57.688 | 21.891 | 142.13 | 6 |
| rust | 161.505 | 152.151 | 1.774 | 5.808 | 6 |
| java | 352.916 | 338.626 | 82.323 | 67.742 | 6 |
| csharp | 614.987 | 605.028 | 216.245 | 59.142 | 6 |

## Charts

![Wall time](../charts/latest/cpu-prime-count-wall-time.svg)

![Peak memory](../charts/latest/cpu-prime-count-memory.svg)

![Memory vs time](../charts/latest/cpu-prime-count-memory-vs-time.svg)

![CPU](../charts/latest/cpu-prime-count-cpu.svg)

## Notes

- CPU is derived from host-side `/usr/bin/time -l` as `(user + sys) / real * 100`.
- This remains a microbenchmark and is not sufficient alone for full architectural conclusions.