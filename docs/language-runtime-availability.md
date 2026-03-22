# Language Runtime Availability

This document records which language runtimes/toolchains are currently available on the host used for benchmark execution.

## Objective

Scientific benchmarking requires explicit disclosure of execution constraints. A benchmark matrix is only valid when the repository states which language implementations are executable on the current host.

## Host snapshot

Observed available runtimes/tools during bootstrap:

- Python: available
- Node.js / npm: available
- Go: not currently available
- Rust / Cargo: not currently available
- Java / javac: not currently available
- .NET / C#: not currently available

## Methodological rule

A language may appear in the research scope before it is executable on the host, but:

- it must not be included in comparative result claims until the runtime/toolchain is available,
- missing runtime availability must be documented,
- results must clearly distinguish between planned languages and executed languages.

## Current implication

The repository can currently execute and compare:

- Python
- TypeScript/Node.js

The remaining languages stay in the design scope, but not yet in the executed result set on this host.

## Cross-references

- [Methodology](./methodology.md)
- [Active Observability](./active-observability.md)
- [Benchmark Catalog v1](./benchmark-catalog.md)
