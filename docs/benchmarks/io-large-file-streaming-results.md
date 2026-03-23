# Large File Streaming — Results Log

## Latest summary

| Language | Mean ms | Median ms | Max RSS MB | CPU avg % | Trials |
|---|---:|---:|---:|---:|---:|
| typescript | 98.378 | 98.317 | 61.719 | 100.0 | 3 |
| python | 135.846 | 135.846 | 11.576 | 92.803 | 6 |

## Interpretation notes

- Initial I/O benchmark bootstrap across Python and TypeScript.
- Streaming line-oriented processing without full-file materialization.
- Raw evidence is preserved under `results/raw/` and curated summary under `results/curated/latest/`.