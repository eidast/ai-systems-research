# Producer Consumer Pipeline — Results Log

## Latest summary

| Language | Mean ms | Median ms | Max RSS MB | CPU avg % | Trials |
|---|---:|---:|---:|---:|---:|
| typescript | 45.267 | 45.355 | 52.74 | 100.0 | 6 |
| go | 61.998 | 62.611 | 22.125 | 400.0 | 3 |
| python | 121.931 | 121.384 | 12.412 | 100.0 | 9 |
| rust | 178.457 | 173.773 | 1.781 | 71.64 | 3 |
| java | 302.279 | 301.274 | 102.854 | 238.095 | 3 |
| csharp | 663.093 | 664.167 | 220.042 | 141.145 | 3 |

## Interpretation notes

- Concurrency benchmark now covers the full main language set.
- Uses deterministic transform and bounded in-process coordination with shared benchmark semantics.
- Raw evidence is preserved under `results/raw/` and curated summary under `results/curated/latest/`.