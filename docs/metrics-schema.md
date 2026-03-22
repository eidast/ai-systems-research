# Metrics Schema v1

This document defines the measurement model for the repository.

## Metric groups

## 1. Core metrics
Required for all benchmarks.

- `correctness_passed`
- `elapsed_ms`
- `trial_count`
- `mean`
- `median`
- `stddev`
- `min`
- `max`
- `optimization_stage`
- `environment_profile`

## 2. Latency metrics
Required for latency-sensitive and service-style benchmarks.

- `p50_ms`
- `p95_ms`
- `p99_ms`
- `max_latency_ms`

## 3. Throughput metrics
Required where throughput is meaningful.

- `throughput_ops_sec`
- `throughput_mb_sec`
- `requests_sec`

## 4. Resource metrics

- `cpu_avg_pct`
- `cpu_peak_pct`
- `mem_avg_mb`
- `mem_peak_mb`
- `startup_ms`

## 5. Quality and stability metrics

- `error_rate`
- `timeout_count`
- `retry_count`
- `queue_depth_max`
- `degradation_notes`

## 6. Engineering effort metrics

- `build_time_sec`
- `time_to_first_correct_min`
- `time_to_benchmarkable_min`
- `optimization_passes`
- `human_interventions`

## 7. AI trace metadata

- `ai_used`
- `ai_mode`
- `prompt_cycles`
- `ai_trace_ref`

## Canonical grouping keys

Every result group should be keyed at minimum by:

- `benchmark_id`
- `benchmark_tier`
- `technical_class`
- `architectural_analog`
- `language`
- `runtime_version`
- `mode`
- `optimization_stage`
- `environment_profile`
- `input_size`
- `concurrency_level`

## Interpretation rules

- Means are not sufficient for service-style benchmarks.
- Tail metrics must be separated from average metrics.
- Cold-start and warm-state data must not be mixed.
- Engineering effort must be tracked separately from runtime results.

## Cross-references

- [Methodology](./methodology.md)
- [Execution Protocol](./execution-protocol.md)
- [Charting Strategy](./charting-strategy.md)
