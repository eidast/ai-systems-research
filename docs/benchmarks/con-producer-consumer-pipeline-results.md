# Producer Consumer Pipeline — Results Log

## Latest summary

| Language | Mean ms | Median ms | Max RSS MB | CPU avg % | Trials |
|---|---:|---:|---:|---:|---:|
| typescript | 45.074 | 44.985 | 52.891 | 100.0 | 3 |
| python | 122.16 | 121.184 | 12.427 | 100.0 | 6 |

## Interpretation notes

- Initial concurrency benchmark bootstrap across Python and TypeScript.
- Uses deterministic transform and bounded in-process coordination.
- Raw evidence is preserved under `results/raw/` and curated summary under `results/curated/latest/`.