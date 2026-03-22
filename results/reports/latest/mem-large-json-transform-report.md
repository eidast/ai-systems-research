# Benchmark Report — MEM Large JSON Transform

## Configuration

- benchmark: `mem-large-json-transform`
- dataset: `benchmarks/datasets/generated/mem-large-json-transform-medium.json`
- trials: `3` per language
- warmups: `1`

## Summary Table

| Language | Mean ms | Median ms | Peak memory MB | CPU avg % | Trials |
|---|---:|---:|---:|---:|---:|
| typescript | 50.067 | 50.073 | 81.391 | 66.667 | 3 |
| python | 75.569 | 75.455 | 42.823 | 94.444 | 3 |

## Charts

![Wall time](../charts/latest/mem-large-json-transform-wall-time.svg)

![Peak memory](../charts/latest/mem-large-json-transform-memory.svg)

## Notes

- Component benchmark for transform-heavy JSON processing.
- CPU is derived from host-side `/usr/bin/time -l` as `(user + sys) / real * 100`.