# Execution Protocol v1

This document defines how benchmarks are executed, validated, and packaged.

## Execution phases

## 1. Definition validation
Before any run:
- benchmark definition exists
- benchmark metadata is complete
- implementation folders exist
- correctness fixtures are available

## 2. Environment capture
Capture at least:
- hardware profile
- OS and architecture
- runtime/compiler versions
- git commit SHA
- benchmark config reference

## 3. Correctness gate
No performance benchmark is valid unless correctness passes first.

Required checks:
- shared test vectors
- expected output validation
- equivalent semantics across implementations

## 4. Warmup phase
Warmup policy must be explicit and versioned.

- native/simple runtimes: 1–2 warmups as needed
- JIT runtimes: 3+ warmups or run-until-stable policy
- service benchmarks: warm service before opening measurement window

## 5. Measured runs
Default policy:
- microbenchmarks: 5 measured runs
- component/reference workloads: 3–5 measured runs

Each run must preserve:
- identical configuration
- identical dataset/input
- identical concurrency level
- consistent instrumentation

## 6. Stress and degradation phase
Required for concurrency and service-style benchmarks.

Test at multiple levels:
- low load
- expected load
- near saturation
- overload/degradation

Capture:
- p50/p95/p99
- throughput
- error rate
- queue/backpressure behavior
- recovery behavior

## 7. Outlier handling
- keep raw data
- exclude only with documented reason
- report exclusion count and rationale
- if anomaly rate is high, downgrade confidence

## 8. Result packaging
Each run should produce:
- raw per-trial JSON
- environment capture JSON
- logs
- curated summaries
- charts and markdown reports after aggregation

## Required result identifiers
- `run_id`
- `benchmark_id`
- `language`
- `mode`
- `trial`
- `environment_profile`

## Publishability gate
A result is publishable only if:
- correctness passed
- metadata is complete
- fairness rules are declared
- warmup policy is documented
- anomalies are transparent
- interpretation limits are stated

## Cross-references

- [Methodology](./methodology.md)
- [Benchmark Quality Plan](./benchmark-quality-plan-cesar.md)
- [Metrics Schema](./metrics-schema.md)
