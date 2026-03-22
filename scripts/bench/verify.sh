#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

required_paths=(
  "$ROOT_DIR/configs/benchmark-matrix.yaml"
  "$ROOT_DIR/schemas/benchmark-definition.schema.json"
  "$ROOT_DIR/schemas/benchmark-run.schema.json"
  "$ROOT_DIR/benchmarks/definitions/cpu/cpu-prime-count.yaml"
)

for p in "${required_paths[@]}"; do
  if [[ ! -f "$p" ]]; then
    echo "missing required file: $p" >&2
    exit 1
  fi
done

for tool in python3 git; do
  if ! command -v "$tool" >/dev/null 2>&1; then
    echo "missing required tool: $tool" >&2
    exit 1
  fi
done

echo "verification ok"
