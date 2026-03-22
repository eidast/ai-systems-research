# Benchmark Report — MEM Large JSON Transform

## Configuration

- benchmark: `mem-large-json-transform`
- dataset: `benchmarks/datasets/generated/mem-large-json-transform-medium.json`
- trials: `3` per language
- warmups: `1`

## Summary Table

| Language | Mean ms | Median ms | Peak memory MB | CPU avg % | Trials |
|---|---:|---:|---:|---:|---:|
| typescript | 51.333 | 50.181 | 81.31 | 66.667 | 6 |
| python | 75.861 | 76.075 | 42.771 | 88.889 | 6 |
| go | 92.058 | 91.578 | 24.208 | 271.429 | 3 |
| rust | 287.486 | 286.013 | 11.188 | 0 | 3 |
| java | 376.965 | 377.46 | 117.359 | 200.196 | 3 |
| csharp | 779.471 | 776.248 | 220.297 | 122.026 | 3 |

## Charts

![Wall time](../charts/latest/mem-large-json-transform-wall-time.svg)

![Peak memory](../charts/latest/mem-large-json-transform-memory.svg)

## Notes

- Component benchmark for transform-heavy JSON processing.
- CPU is derived from host-side `/usr/bin/time -l` as `(user + sys) / real * 100`.