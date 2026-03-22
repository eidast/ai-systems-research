# MEM Large JSON Transform — Results Log

## Latest summary

| Language | Mean ms | Median ms | Max RSS MB | CPU avg % | Trials |
|---|---:|---:|---:|---:|---:|
| typescript | 51.333 | 50.181 | 81.31 | 66.667 | 6 |
| python | 75.861 | 76.075 | 42.771 | 88.889 | 6 |
| go | 92.058 | 91.578 | 24.208 | 271.429 | 3 |
| rust | 287.486 | 286.013 | 11.188 | 0 | 3 |
| java | 376.965 | 377.46 | 117.359 | 200.196 | 3 |
| csharp | 779.471 | 776.248 | 220.297 | 122.026 | 3 |

## Interpretation notes

- Results are based on the generated medium dataset and current host/toolchain versions.
- This benchmark is more representative of transform-heavy component workloads than the CPU microbenchmark.
- All current language implementations passed smoke correctness before measured execution.
- Raw evidence is preserved under `results/raw/` and curated summary under `results/curated/latest/`.