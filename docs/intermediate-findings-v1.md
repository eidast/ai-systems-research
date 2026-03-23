# Intermediate Findings v1

> Cross-benchmark synthesis of the current benchmark program. This document is intentionally provisional: it captures patterns that are already visible, but avoids turning early benchmark evidence into universal claims.

## 1. Scope of this synthesis

This synthesis uses the currently available benchmark families implemented in the repository:

- `cpu-prime-count`
- `mem-large-json-transform`
- `con-producer-consumer-pipeline`
- `io-large-file-streaming`

The goal is not to declare a winner. The goal is to identify:

- early runtime patterns,
- architecture-relevant tradeoffs,
- suspicious anomalies,
- and the kinds of decisions this benchmark evidence can already support.

## 2. Important interpretation limits

Before reading any comparative table, these limits matter:

1. Some curated groups still include multiple runs accumulated over time.
2. A few earlier runs were collected before some measurement fixes, especially around CPU derivation.
3. Not every benchmark family has identical historical run counts per language.
4. These are still **component-level and microbenchmark-level workloads**, not full production systems.
5. Some implementations are intentionally simple and baseline-oriented, not heavily optimized.

This means the current results are best interpreted as **directional engineering evidence**, not final published truth.

## 3. Representative benchmark snapshot

The following values are selected from the current `results/curated/latest/result-summary.json` and reflect the current comparative picture.

## 3.1 CPU — `cpu-prime-count` @ input_size=300000

| Language | Mean wall ms | Mean peak memory MB | Notes |
|---|---:|---:|---|
| Python | 31.862 | 12.172 | Surprisingly strong on this benchmark; likely benefits from compact implementation and workload shape. |
| TypeScript | 37.363 | 47.495 | Competitive wall time, much larger memory footprint. |
| Go | 67.115 | 21.891 | Reasonable middle ground; more variance than expected. |
| Rust | 161.505 | 1.774 | Very low memory footprint, but slower than expected in current baseline implementation. |
| Java | 352.916 | 82.323 | High startup/runtime overhead visible in this microbenchmark. |
| C# | 614.987 | 216.245 | Largest memory cost and slowest current baseline on this workload. |

### CPU family interpretation

Early conclusion:
- for this specific deterministic microbenchmark, **Python and TypeScript currently dominate wall time**,
- **Rust dominates memory efficiency**,
- and **Java/C# appear penalized by runtime/startup/implementation overhead** in the current baseline shape.

Architectural interpretation:
- This benchmark is too small and too synthetic to say “Python is the best compute language.”
- What it does suggest is that **small deterministic CPU tasks do not always reward more complex runtime/toolchain choices** unless memory or other constraints dominate.

## 3.2 Memory — `mem-large-json-transform`

| Language | Mean wall ms | Mean peak memory MB | Notes |
|---|---:|---:|---|
| TypeScript | 51.333 | 81.310 | Fastest current baseline, but memory-heavy. |
| Python | 75.861 | 42.771 | Strong balance of speed and moderate memory. |
| Go | 92.058 | 24.208 | Good memory profile; slower than Python/TypeScript in current baseline. |
| Rust | 287.486 | 11.188 | Extremely memory-efficient; wall time much higher in this current baseline. |
| Java | 376.965 | 117.359 | Heavy runtime/memory cost in this current implementation. |
| C# | 779.471 | 220.297 | Slowest and most memory-intensive current baseline. |

### Memory family interpretation

Early conclusion:
- **TypeScript and Python are currently strongest on elapsed time**,
- **Go looks like a strong middle-ground option**,
- **Rust looks very attractive where memory is the primary constraint**,
- and **Java/C# currently underperform in both elapsed time and memory footprint** for this workload.

Architectural interpretation:
- For transform-heavy workloads where memory budget matters but absolute minimal memory is not mandatory, **Python and Go look especially interesting**.
- If memory is severely constrained, **Rust shows a compelling footprint story even with slower current baseline runtime**.
- TypeScript appears attractive for developer speed and throughput, but it is carrying significant memory cost.

## 3.3 Concurrency — `con-producer-consumer-pipeline`

| Language | Mean wall ms | Mean peak memory MB | Notes |
|---|---:|---:|---|
| TypeScript | 45.267 | 52.740 | Strong elapsed time in current bounded-queue simulation. |
| Go | 61.998 | 22.125 | Very strong concurrency profile with excellent multicore CPU usage. |
| Python | 121.931 | 12.412 | Correct and simple, but limited by runtime model. |
| Rust | 178.457 | 1.781 | Excellent memory profile, slower current baseline implementation. |
| Java | 302.279 | 102.854 | Considerable overhead in current design. |
| C# | 663.093 | 220.042 | Weak current baseline on both time and memory. |

### Concurrency family interpretation

Early conclusion:
- **TypeScript and Go are currently the most compelling performers** in this benchmark family.
- **Go looks particularly architecture-relevant** because it combines:
  - strong elapsed time,
  - far lower memory cost than TypeScript,
  - and clearly high CPU utilization.
- **Python works but does not look like the strongest option** when bounded in-process coordination becomes central.
- **Rust again shows an excellent memory story but slower elapsed time in the current baseline.**

Architectural interpretation:
- If the decision is about **concurrency coordination under bounded queues**, Go already looks like one of the strongest practical candidates.
- TypeScript looks good for local coordination performance, but memory cost remains materially higher.

## 3.4 I/O — `io-large-file-streaming`

| Language | Mean wall ms | Mean peak memory MB | Notes |
|---|---:|---:|---|
| Go | 77.880 | 22.323 | Best current elapsed time and low memory. |
| TypeScript | 99.648 | 61.630 | Strong elapsed time but memory-heavy. |
| Python | 135.907 | 11.556 | Slower than Go/TypeScript but very memory-efficient. |
| Rust | 334.507 | 1.943 | Extremely memory-efficient, but slow in current baseline. |
| Java | 418.019 | 121.922 | Heavy runtime/memory cost in current implementation. |
| C# | 758.015 | 219.641 | Slowest and heaviest current baseline. |

### I/O family interpretation

Early conclusion:
- **Go currently looks like the strongest overall I/O streaming option** in the benchmark suite.
- **TypeScript remains fast but memory-expensive**.
- **Python is slower than Go/TypeScript but has an excellent memory profile relative to implementation simplicity**.
- **Rust remains the most memory-frugal current option, but not the fastest in elapsed time**.

Architectural interpretation:
- For practical line-oriented ingestion, **Go appears especially attractive** because it combines speed, low memory, and strong runtime behavior.
- TypeScript could still make sense when platform alignment matters and memory pressure is acceptable.
- Python remains viable where simplicity and implementation speed matter more than peak throughput.

## 4. Cross-family patterns already visible

## 4.1 Go is emerging as the strongest all-around systems candidate

Across memory, concurrency, and I/O, Go repeatedly appears as a strong balance point:

- not always the fastest,
- rarely the most memory-efficient,
- but often one of the strongest practical combinations of speed + memory + operational simplicity.

This makes Go look architecturally attractive for:

- worker services,
- ingestion pipelines,
- queue-oriented services,
- and systems where predictable operational behavior matters.

## 4.2 TypeScript is consistently strong on elapsed time, but expensive on memory

TypeScript/Node is repeatedly competitive in wall-clock performance in the current suite.

However, that performance often comes with materially higher memory cost than Python, Go, and especially Rust.

Architectural implication:
- TypeScript can be highly attractive where team/product velocity and ecosystem alignment matter,
- but memory-heavy workloads may expose runtime cost tradeoffs earlier than in some alternatives.

## 4.3 Python is stronger than many naive assumptions would predict

Python remains surprisingly competitive in this benchmark suite.

Patterns so far:
- excellent or near-leading wall time in CPU microbenchmark,
- good memory profile in memory and I/O transforms,
- weaker relative position in concurrency-heavy workloads.

Architectural implication:
- Python still looks very credible for:
  - ETL,
  - file processing,
  - transform-heavy workloads,
  - and fast implementation loops,
- but less compelling where in-process concurrency coordination is a first-order design need.

## 4.4 Rust is telling a clear memory-efficiency story, but not yet an elapsed-time story

Rust is repeatedly the most memory-efficient or among the most memory-efficient implementations.

At the same time, in the current baseline implementations it is not winning elapsed time.

Important interpretation note:
- This does **not** mean Rust is “slow.”
- It means the **current baseline implementations and benchmark setup** are not yet showing Rust’s full optimization potential.

Architectural implication:
- Rust already looks relevant for highly memory-constrained systems,
- but the repository needs a later optimization pass before drawing stronger claims about its full performance envelope.

## 4.5 Java and C# currently look penalized by baseline simplicity and runtime overhead

Both Java and C# underperform in the current suite on elapsed time and memory usage.

However, the right interpretation is careful:

- the benchmarks are relatively small/component-oriented,
- the implementations are intentionally simple,
- and runtime/JIT/warmup effects may not be represented in the most favorable way.

Architectural implication:
- current evidence does **not** support these runtimes as the strongest choices for the benchmark suite as currently implemented,
- but it would be premature to generalize this into a universal conclusion against JVM/.NET systems.

## 5. Provisional architecture guidance

## If the problem is CPU micro work
Current evidence suggests:
- Python and TypeScript are surprisingly competitive on elapsed time,
- Rust is best on footprint,
- Java/C# are currently unattractive in this benchmark form.

## If the problem is memory-sensitive structured transformation
Current evidence suggests:
- Python, Go, and Rust form the most interesting decision set,
- TypeScript is fast but memory-heavy,
- Go looks like a practical systems middle ground.

## If the problem is bounded in-process concurrency
Current evidence suggests:
- Go is one of the strongest practical candidates,
- TypeScript performs well but with higher memory cost,
- Python is functionally viable but less attractive when concurrency becomes central.

## If the problem is file ingestion / line streaming
Current evidence suggests:
- Go is currently the strongest overall profile,
- Python is attractive for simplicity with modest memory,
- TypeScript is strong if memory headroom exists,
- Rust is interesting when footprint matters more than elapsed time in the current baseline.

## 6. What the AI angle is already suggesting

The benchmark suite is not only comparing languages. It is already demonstrating a deeper point:

AI makes it much easier to:
- draft equivalent implementations,
- port patterns across runtimes,
- iterate on comparative experiments,
- and build evidence faster than a human working language-by-language from scratch.

That means the cost of **multi-language architectural exploration** is dropping.

This may be one of the most important conclusions of the whole project.

The new bottleneck is not writing code. The new bottleneck is:
- methodology,
- correctness,
- equivalence,
- and interpretation discipline.

## 7. Immediate next recommendations

1. Clean the historical summary layer so “latest” comparisons are easier to interpret without mixed run counts.
2. Add an intermediate comparative dashboard/table purpose-built for architecture decisions.
3. Open the **parallelism** family next.
4. Revisit Rust, Java, and C# implementations later with a dedicated optimization pass before stronger external publication claims.
5. Add richer visuals:
   - heatmaps,
   - normalized comparisons,
   - workload-fit matrix,
   - performance vs memory vs complexity charts.

## 8. Bottom line

The current evidence already supports a meaningful provisional story:

- **Go is emerging as the strongest overall systems generalist** in the benchmark suite.
- **TypeScript is repeatedly fast, but memory-expensive.**
- **Python remains highly competitive where simplicity and transform-heavy work matter.**
- **Rust is already winning the memory story, but not yet the elapsed-time story in current baselines.**
- **Java and C# need more favorable or more realistic treatment before strong external conclusions are justified.**

This is already enough to start writing serious architecture-facing commentary, as long as the claims remain scoped and disciplined.

## Cross-references

- [Architecture Overview](./architecture-overview.md)
- [Decision Framework](./decision-framework.md)
- [Research Narrative](./research-narrative.md)
- [CPU Prime Count Results](./benchmarks/cpu-prime-count-results.md)
- [MEM Large JSON Transform Results](./benchmarks/mem-large-json-transform-results.md)
- [Producer Consumer Pipeline Results](./benchmarks/con-producer-consumer-pipeline-results.md)
- [Large File Streaming Results](./benchmarks/io-large-file-streaming-results.md)
