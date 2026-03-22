# CPU Prime Count — Implementation Notes

## Objective

Track the current implementation status of the `cpu-prime-count` benchmark by language.

## Status

### Executable now
- Python
- TypeScript / Node.js

### Planned but blocked by missing local runtime/toolchain
- Go
- Rust
- Java
- C#

## Rule

A benchmark may only be included in comparative charts and architecture conclusions for languages that have:

1. a checked-in implementation,
2. a runnable local toolchain,
3. measured raw results preserved in `results/raw/`.

## Current algorithmic intent

Both current implementations use a sieve-based deterministic prime counting approach with equivalent intent.

## Cross-references

- [Benchmark Definition](../../benchmarks/definitions/cpu/cpu-prime-count.yaml)
- [Language Runtime Availability](../language-runtime-availability.md)
- [Execution Protocol](../execution-protocol.md)
