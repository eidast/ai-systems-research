# Parallel Reduction — Results Log

## Latest summary

| Language | Mean ms | Median ms | Max RSS MB | CPU avg % | Trials |
|---|---:|---:|---:|---:|---:|
| typescript | 36.205 | 35.972 | 46.932 | 66.667 | 3 |
| go | 80.616 | 67.495 | 22.172 | 318.519 | 3 |
| python | 98.075 | 97.198 | 19.995 | 266.071 | 6 |
| rust | 173.422 | 161.967 | 1.797 | 9.295 | 3 |
| java | 314.956 | 281.248 | 103.578 | 209.971 | 3 |
| csharp | 628.191 | 623.37 | 216.042 | 123.082 | 3 |

## Interpretation notes

- Parallelism benchmark now covers the full main language set.
- Uses deterministic partition + reduction with consistent aggregate semantics.
- Raw evidence is preserved under `results/raw/` and curated summary under `results/curated/latest/`.