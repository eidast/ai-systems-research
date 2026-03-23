# Research Narrative

> Living narrative log of the investigation: why this research exists, how it has evolved, what was built, what failed, what was corrected, and how the benchmark program is becoming a reusable architecture evidence engine.

## 1. Why this investigation exists

This research started from a core idea: modern AI changes software engineering not only by accelerating code generation, but by reducing the cost of exploring multiple implementation paths across languages, runtimes, and architectural styles.

The initial framing was a technical article about how AI enables developers to create more optimal and complex solutions, compare languages, reason about memory and CPU, and make stronger design choices. Very early, however, the scope became more ambitious.

The investigation shifted from a simple article or language comparison into a structured, evidence-driven research program intended to support senior engineering and architecture decisions.

## 2. The scope expansion

The early direction included comparing multiple languages on practical benchmark exercises. The language matrix was expanded to include:

- Python
- TypeScript / Node.js
- Go
- Rust
- Java
- C#
- Assembly as a special-case language for later, selected benchmarks only

At the same time, the benchmark scope expanded beyond raw compute into several classes of workloads:

- CPU-bound
- Memory-bound
- Parallelism
- Concurrency
- I/O-bound

This immediately changed the nature of the repository. It was no longer enough to collect code examples or isolated timing numbers. The project needed methodology, reproducibility, structured results, and interpretation.

## 3. The key reframing: from benchmark repo to architecture evidence engine

One of the most important conceptual shifts in the project was the realization that this should not become a language-war repository or a collection of leaderboard tables.

The more useful framing is that this repository is an **architecture evidence engine**:

- a place to implement equivalent workload classes across multiple languages,
- a place to capture reproducible evidence,
- a place to generate summaries, charts, and reports,
- and ultimately a place to support better architecture decisions in the AI era.

That shift influenced everything after it:

- the documentation structure,
- benchmark definitions,
- methodology,
- decision framework,
- charting strategy,
- testing rules,
- and the overall reporting style.

## 4. Repository setup and project conventions

The project was initially bootstrapped inside the OpenClaw workspace, but this was corrected after recalling the established convention that real projects and repositories belong under `~/Projects/`.

The repository was moved to:

- `~/Projects/ai-systems-research`

and linked from the workspace for operational convenience.

A public GitHub repository was then created and continuously updated as progress was made.

## 5. Early documentation foundation

Before implementing benchmarks, a substantial documentation base was created.

This included:

- top-level `README.md`
- documentation index
- research design
- methodology
- benchmark suite definition
- architecture overview
- decision framework
- metrics schema
- execution protocol
- charting strategy
- project operating rules
- visual diagrams in Mermaid
- a Markmap-compatible research map

This documentation-first phase was important because it made later benchmark work more disciplined and less ad hoc.

## 6. Toolchain discovery and versioning

The project initially started with only some runtimes available on the host. Early execution showed that only Python and Node.js were immediately available.

This forced an explicit distinction between:

- **planned research scope**, and
- **currently executable scope**.

Later, the missing runtimes were installed and verified. The repository then documented real, observed versions in `docs/toolchain-versions.md`.

The active host eventually had:

- Python 3.14.3
- Node.js 24.13.0
- npm 11.6.2
- Go 1.24.13
- Rust 1.87.0
- Cargo 1.87.0
- Java 21.0.10 LTS
- javac 21.0.10
- .NET SDK 10.0.201
- clang 17.0.0
- Apple `as`

This matters because reproducible benchmarking depends heavily on toolchain disclosure.

## 7. The first benchmark: CPU prime count

The first operational benchmark to be implemented was `cpu-prime-count`.

This benchmark was chosen as the first step because it is:

- deterministic,
- easy to reason about,
- algorithmically explicit,
- and relatively straightforward to port across languages.

It served as the first real test of the repository’s execution flow:

- benchmark definition
- language implementations
- host-side observability
- raw result preservation
- curated summary generation
- charts
- reports

### What was built

`cpu-prime-count` was implemented across:

- Python
- TypeScript / Node.js
- Go
- Rust
- Java
- C#

### What this benchmark proved

It established the first working end-to-end research loop:

1. define benchmark,
2. implement across languages,
3. run via a common runner,
4. capture timing and memory,
5. preserve raw data,
6. aggregate summaries,
7. generate charts,
8. write report artifacts.

This was the first moment the repository became operational research infrastructure rather than a documentation skeleton.

## 8. The observability baseline

A critical methodological choice was to measure benchmarks using a **common host-side external measurement layer** rather than relying first on language-specific profilers.

The repository adopted `/usr/bin/time -l` as the cross-language baseline for:

- wall-clock execution time,
- peak resident memory,
- and derived CPU utilization.

This choice was important because language-native profilers differ too much to be used as a shared first-layer comparison baseline.

### Important correction

An early bug caused CPU utilization to appear as `0` in result summaries. This was later corrected by deriving CPU percentage from:

- `real`
- `user`
- `sys`

using the formula:

`(user + sys) / real * 100`

This correction mattered because it prevented the project from silently normalizing invalid CPU metrics into the curated outputs.

## 9. The second benchmark: memory-bound JSON transformation

After the CPU benchmark, the next benchmark family added was `mem-large-json-transform`.

This was a more architecture-relevant step because it moved the investigation toward:

- parsing,
- structured data transformation,
- aggregation,
- memory pressure,
- and dataset-driven workload behavior.

### What was added

- benchmark definition in the memory family
- generated dataset under `benchmarks/datasets/generated/`
- dataset generation script
- implementations first in Python and TypeScript, then later across the full main language set
- charts and report artifacts
- cross-language equivalence testing

### Why it mattered

This benchmark moved the repository beyond microbenchmarking and into a component-style workload that maps more closely to ETL, ingestion, and transform-heavy services.

## 10. The third benchmark family: concurrency

Once CPU and memory benchmarks were operational, the next family opened was concurrency.

The initial benchmark chosen was:

- `con-producer-consumer-pipeline`

This benchmark models:

- bounded queue coordination,
- producer-consumer flows,
- deterministic per-item transform,
- aggregate correctness,
- and in-process coordination patterns.

### Initial rollout

The benchmark was first bootstrapped in:

- Python
- TypeScript

Once the pattern was stable, it was extended across the full language set:

- Go
- Rust
- Java
- C#

### Why this benchmark matters

This is a more architecture-facing workload than pure compute, because it begins to illuminate:

- coordination costs,
- queueing behavior,
- in-process concurrency models,
- and runtime ergonomics under bounded work distribution.

## 11. The fourth benchmark family begins: I/O-bound streaming

With CPU, memory, and concurrency in place, the next logical step was to begin the I/O-bound family.

The chosen starting point is:

- `io-large-file-streaming`

This benchmark is intended to model:

- line-oriented streaming,
- file ingestion,
- bounded memory growth,
- and deterministic aggregate processing over a large input.

The initial bootstrap is intentionally starting with Python and TypeScript, using a generated medium-size file, before later expansion to the rest of the language set.

This keeps the benchmark family aligned with the same build pattern used in previous families:

- definition first,
- dataset generation,
- initial implementations,
- equivalence tests,
- measured runs,
- charts and report,
- later expansion across the full matrix.

## 12. Testing and validation became mandatory

As soon as multiple benchmarks and multiple languages were in play, correctness became a bigger risk than raw performance.

The repository therefore added automated validation in several layers:

### Unit tests
Initial unit tests were created in Python to validate:

- `cpu-prime-count` logic,
- `mem-large-json-transform` output shape and counts.

### Cross-language consistency tests
Integration tests were added to check that multiple implementations produce equivalent outputs.

This now covers:

- CPU prime count across the main language set,
- memory transform equivalence across the main language set,
- concurrency pipeline equivalence where supported,
- and the first I/O bootstrap as it is introduced.

### Smoke tests
Smoke validation was added to ensure benchmark entrypoints still run after changes.

### Verify gate
A pre-run verification script was expanded to ensure:

- benchmark definitions exist,
- schemas exist,
- datasets exist,
- and required benchmark entrypoints are present.

This was an important evolution: the repo stopped being just runnable and started becoming defensible.

## 13. Specialist QA guidance from Cesar

The project also incorporated specialist QA feedback emphasizing that the biggest risk was not merely bad performance numbers, but reporting **semantically incorrect or weakly validated benchmark outputs**.

Key QA concerns raised and incorporated included:

- correctness gates that were too shallow,
- report fields that could drift from actual run data,
- and the need to validate equivalence rather than mere parseability.

This reinforced the decision to invest early in testing and post-change validation.

## 14. Reports, charts, and curated outputs

The repository now generates:

- raw result artifacts in `results/raw/`
- curated summaries in `results/curated/latest/`
- SVG charts in `results/charts/latest/`
- markdown reports in `results/reports/latest/`
- human-readable benchmark result logs in `docs/benchmarks/`

This multi-layer output structure matters because it supports different audiences:

- raw data for auditability,
- curated data for processing,
- charts for quick inspection,
- benchmark docs for interpretation,
- and later article material for external publication.

## 15. Build artifact discipline

As more language toolchains were introduced, generated build artifacts started leaking into the repository, especially from C#, Go, and Java workflows.

This led to a cleanup phase where:

- `.gitignore` was hardened,
- generated artifacts were removed from version control,
- and language layout expectations were documented.

This was an important hygiene step because benchmark repositories can become hard to trust when source, results, and toolchain junk are mixed together.

## 16. Manual execution as a first-class requirement

At a later stage, the root README was updated with explicit manual execution instructions so the project could be run by a human operator without relying on hidden assistant context.

The README now explains how to:

- verify toolchains,
- run tests,
- run smoke validation,
- execute each benchmark manually per language,
- execute measured runs through the common benchmark runner,
- and regenerate summaries, charts, and reports.

This is important for portability, collaboration, and future publication.

## 17. Where the research stands now

At this point, the investigation has moved from concept to working comparative system.

### Implemented benchmark families

#### CPU
- `cpu-prime-count`
- implemented across the main language set

#### Memory
- `mem-large-json-transform`
- implemented across the main language set

#### Concurrency
- `con-producer-consumer-pipeline`
- implemented across the main language set

#### I/O
- `io-large-file-streaming`
- implemented across the main language set

### Operational capabilities now present

- multi-language benchmark definitions
- language-local implementations
- raw measurement capture
- curated summary generation
- chart generation
- markdown report generation
- toolchain verification
- unit tests
- cross-language integration tests
- smoke tests
- project operating rules
- benchmark execution instructions
- living research narrative

## 18. A new phase: intermediate synthesis begins

Once CPU, memory, concurrency, and I/O were all operational across the main language set, the project reached an important transition point.

The research could no longer be described only as benchmark construction. It had enough evidence to justify a first synthesis pass.

That synthesis step produced an intermediate findings layer intended to answer questions like:

- what patterns are already visible across benchmark families?
- which language/runtime profiles are emerging?
- what can an architect provisionally conclude without overclaiming?
- what should be treated as signal vs what still needs optimization work?

This was important because the project needed to start turning data into architecture guidance, not just produce more raw result artifacts.

## 19. What still remains

The project is strong, but not complete.

Important next phases still include:

- parallelism-focused benchmark family
- stronger correctness gates inside the runner itself
- richer charts (heatmaps, normalized comparisons, decision matrices)
- hardening of report metadata to avoid drift between actual run counts and rendered narrative
- possible later introduction of Assembly as a special-case benchmark participant for carefully selected CPU tests
- deeper interpretation and publication-oriented writing from the current benchmark corpus

## 19. Narrative significance

The story so far is not just that benchmarks were written.

The more interesting story is that the repository gradually became:

- more rigorous,
- more reproducible,
- more architecture-aware,
- more testable,
- and more publication-ready.

This narrative matters because the eventual article or research report should not only present results, but also explain the methodological journey:

- how scope changed,
- why decisions were made,
- what failed,
- what had to be corrected,
- and why the resulting evidence can be trusted more than a naive language comparison.

## 20. Maintenance rule for this narrative

This file should be updated as the research evolves.

Every major phase should record:

- new benchmark families added,
- methodology changes,
- important implementation decisions,
- significant bugs or corrections,
- major findings,
- and interpretation shifts.

This ensures the project keeps not only its data, but also its memory.
