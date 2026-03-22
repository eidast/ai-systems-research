# Benchmark Suite v1

This document defines the benchmark categories that will be implemented across the selected language set.

## Design Rules

1. Each benchmark must represent a realistic workload class.
2. Implementations should be equivalent in intent.
3. Avoid pathological or misleading microbenchmarks unless clearly labeled.
4. Capture both performance and implementation complexity context.

## 1. CPU-Bound Benchmarks

### Candidate Workloads
- Pi computation to a fixed precision
- Prime number generation / counting
- Matrix multiplication
- Hashing / compression throughput
- Selected recursive computation for pedagogical comparison

### Questions Answered
- Which runtimes deliver the best raw compute efficiency?
- How much does compiler/JIT optimization matter?
- How much does algorithm quality dominate language choice?

## 2. Memory-Bound Benchmarks

### Candidate Workloads
- Large JSON parsing and transformation
- Massive aggregation over in-memory datasets
- Deduplication using hash-based structures
- Text processing over large buffers
- Graph/tree construction and traversal

### Questions Answered
- Which runtimes are more memory-efficient under pressure?
- How does allocation behavior affect throughput?
- What is the impact of garbage collection and heap strategy?

## 3. Parallelism Benchmarks

### Candidate Workloads
- Parallel matrix operations
- Data partitioning and parallel reduction
- Worker pool over CPU-intensive tasks
- Multi-core block processing

### Questions Answered
- How well does each runtime scale with additional cores?
- What is the overhead of coordination and synchronization?
- How close to ideal speedup can each implementation get?

## 4. Concurrency Benchmarks

### Candidate Workloads
- Producer-consumer pipelines
- Fan-out / fan-in task orchestration
- Task queue processing
- Bounded concurrency execution
- Coordinated multi-stage workflows

### Questions Answered
- Which concurrency models are easiest to reason about?
- What is the coordination cost per runtime?
- Where do async and threaded models differ meaningfully?

## 5. I/O-Bound Benchmarks

### Candidate Workloads
- Large file streaming and parsing
- Log processing pipelines
- Simulated HTTP request bursts
- Streaming transforms
- Batch ETL-style ingestion and output

### Questions Answered
- Which runtimes sustain the best throughput under I/O pressure?
- How well does each model handle backpressure?
- What is the memory cost of streaming versus buffering?

## Assembly Inclusion Rule

Assembly is included only where one of these conditions is true:

1. The benchmark materially benefits from low-level control.
2. The comparison teaches something meaningful about abstraction cost.
3. The implementation remains feasible and reproducible.

## Related Docs

- [Research Design v1](./research-design.md)
- [Methodology](./methodology.md)
- [Benchmark Pipeline Diagram](./diagrams/benchmark-pipeline.md)
