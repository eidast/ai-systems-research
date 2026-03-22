# CPU Prime Count — Results Log

## Latest summary for input_size=300000

| Language | Mean ms | Median ms | Max RSS MB | CPU avg % | Trials |
|---|---:|---:|---:|---:|---:|
| python | 31.862 | 31.783 | 12.172 | 50.0 | 6 |
| typescript | 37.363 | 37.358 | 47.495 | 25.0 | 6 |
| go | 67.115 | 57.688 | 21.891 | 142.13 | 6 |
| rust | 161.505 | 152.151 | 1.774 | 5.808 | 6 |
| java | 352.916 | 338.626 | 82.323 | 67.742 | 6 |
| csharp | 614.987 | 605.028 | 216.245 | 59.142 | 6 |

## Interpretation notes

- Results are based on the current host and toolchain versions documented in `docs/toolchain-versions.md`.
- CPU utilization is derived from host-side `/usr/bin/time -l` using `(user + sys) / real * 100` as a common cross-language baseline.
- This is a microbenchmark and should not be overgeneralized into full architecture conclusions.
- Raw evidence is preserved under `results/raw/` and curated summary under `results/curated/latest/`.