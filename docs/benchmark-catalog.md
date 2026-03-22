# Benchmark Catalog v1

This catalog defines the initial benchmark families that will be implemented in the repository.

## Catalog design principles

- Every benchmark must answer an architectural question, not only a technical one.
- Every benchmark must declare its technical stressor and architectural analog.
- Every benchmark must support structured measurement and reproducible execution.

## Family 1 — CPU-bound

### CPU-01 — Pi Precision Computation
- **Tier:** micro / component
- **Technical class:** CPU-bound
- **Architectural analog:** numerical compute stage / deterministic calculation worker
- **Question answered:** how do runtimes behave under sustained deterministic arithmetic workloads?
- **Planned implementations:** Python, Go, Rust, TypeScript/Node.js, Java, C#, Assembly (selected)
- **Notes:** compare serious algorithm vs naive variant in separate tracks

### CPU-02 — Prime Counting
- **Tier:** micro
- **Technical class:** CPU-bound
- **Architectural analog:** pure compute service / validation engine
- **Question answered:** what is the raw compute cost profile across runtimes with strict algorithm parity?

### CPU-03 — Matrix Multiplication
- **Tier:** component
- **Technical class:** CPU-bound + parallelism
- **Architectural analog:** analytics compute stage / batch numeric engine
- **Question answered:** how do runtimes scale in compute-heavy workloads, including multicore execution?

## Family 2 — Memory-bound

### MEM-01 — Large JSON Transform
- **Tier:** component
- **Technical class:** memory-bound + I/O
- **Architectural analog:** ETL transform stage / ingestion service
- **Question answered:** how do runtimes trade memory pressure, throughput, and implementation complexity during large structured transformations?

### MEM-02 — In-Memory Aggregation
- **Tier:** component
- **Technical class:** memory-bound
- **Architectural analog:** analytics worker / reporting service
- **Question answered:** how efficiently can each runtime aggregate and group large in-memory datasets?

### MEM-03 — Text Buffer Processing
- **Tier:** component
- **Technical class:** memory-bound
- **Architectural analog:** log pipeline / parser stage
- **Question answered:** how do allocation behavior and buffer handling affect throughput and memory footprint?

## Family 3 — Parallelism

### PAR-01 — Parallel Worker Pool on Compute Tasks
- **Tier:** component
- **Technical class:** parallelism + CPU-bound
- **Architectural analog:** distributed worker shard running local parallel jobs
- **Question answered:** how well does each runtime exploit multiple cores under controlled parallel execution?

### PAR-02 — Parallel Reduction
- **Tier:** component
- **Technical class:** parallelism
- **Architectural analog:** analytics reduction stage
- **Question answered:** what speedup and coordination costs appear as workers increase?

## Family 4 — Concurrency

### CON-01 — Producer / Consumer Pipeline
- **Tier:** component
- **Technical class:** concurrency
- **Architectural analog:** event processor / bounded internal pipeline
- **Question answered:** how do runtimes behave in coordinated multi-stage flows with bounded queues?

### CON-02 — Fan-out / Fan-in Task Orchestration
- **Tier:** component
- **Technical class:** concurrency
- **Architectural analog:** orchestration service / control plane
- **Question answered:** what is the coordination and scheduling overhead for many short-lived tasks?

## Family 5 — I/O-bound

### IO-01 — Large File Streaming
- **Tier:** component
- **Technical class:** I/O-bound
- **Architectural analog:** file ingestion service / streaming transform stage
- **Question answered:** which runtimes sustain throughput while controlling memory growth and backpressure?

### IO-02 — Log Processing Pipeline
- **Tier:** component
- **Technical class:** I/O-bound + memory-bound
- **Architectural analog:** observability ingestion pipeline
- **Question answered:** how do runtimes behave under sequential read-transform-write workloads?

### IO-03 — Simulated HTTP Burst
- **Tier:** reference-workload
- **Technical class:** concurrency + I/O-bound
- **Architectural analog:** request/response service under bursty load
- **Question answered:** what do throughput, p95, p99, and degradation behavior look like under service-style pressure?

## Reference workload direction

After foundational and component benchmarks stabilize, add reference workloads:

- request/response API service
- asynchronous event consumer
- batch ETL job
- control-plane scheduler

## Cross-references

- [Research Design v1](./research-design.md)
- [Methodology](./methodology.md)
- [Execution Protocol](./execution-protocol.md)
- [Decision Framework](./decision-framework.md)
