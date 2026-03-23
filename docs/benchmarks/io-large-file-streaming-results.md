# Large File Streaming — Results Log

## Latest summary

| Language | Mean ms | Median ms | Max RSS MB | CPU avg % | Trials |
|---|---:|---:|---:|---:|---:|
| go | 77.88 | 77.942 | 22.323 | 283.333 | 3 |
| typescript | 99.648 | 98.641 | 61.63 | 100.0 | 6 |
| python | 135.907 | 135.582 | 11.556 | 94.276 | 9 |
| rust | 334.507 | 335.875 | 1.943 | 56.99 | 3 |
| java | 418.019 | 434.841 | 121.922 | 211.034 | 3 |
| csharp | 758.015 | 757.538 | 219.641 | 116.741 | 3 |

## Interpretation notes

- I/O benchmark now covers the full main language set.
- Processing is line-oriented and intended to avoid full-file materialization as the benchmark story.
- Raw evidence is preserved under `results/raw/` and curated summary under `results/curated/latest/`.