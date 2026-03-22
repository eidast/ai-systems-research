# Active Observability for Benchmark Runs

This document defines the minimum observability requirements for experimental runs in this repository.

## Objective

Every benchmark execution must produce verifiable timing and resource evidence that can later support publication-grade documentation.

## Required observability dimensions

For every measured run, capture at minimum:

- start timestamp
- end timestamp
- total elapsed wall-clock time
- average CPU utilization
- peak CPU utilization (or best available approximation when tool limits apply)
- peak memory consumption
- exit code
- correctness status

## Scientific-method alignment

Observability is not optional instrumentation. It is part of the method.

A benchmark result is only scientifically useful when:
- the measurement process is explicit,
- the environment is disclosed,
- the collection method is repeatable,
- the result can be independently rechecked.

## Timing rules

### Start time
The measurement start must be recorded immediately before the benchmarked workload begins.

### End time
The measurement end must be recorded immediately after workload completion.

### Total time
Elapsed wall-clock time must be computed from start to end and stored in milliseconds.

## CPU and memory rules

Because each language/runtime may expose different internal metrics, repository-wide comparisons must use a common outer measurement method first.

### Current bootstrap rule
At bootstrap stage, cross-language comparability is based on an **external measurement layer**:
- `/usr/bin/time -l` on the host
- structured metadata and logs stored with each run

### Later-stage rule
If language-specific profilers are added, they must be treated as **supplemental evidence**, not as replacements for the common external baseline.

## Verification rule
No result should be considered decision-grade unless the raw measurement artifacts are preserved in `results/raw/` and can be inspected later.

## Cross-references

- [Methodology](./methodology.md)
- [Execution Protocol](./execution-protocol.md)
- [Metrics Schema](./metrics-schema.md)
