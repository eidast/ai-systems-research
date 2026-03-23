#!/usr/bin/env bash
set -euo pipefail
DIR="$(cd "$(dirname "$0")" && pwd)"
BIN="$DIR/par_parallel_reduction_go"
go build -o "$BIN" "$DIR/parallel_reduction.go"
"$BIN" "${1:-200000}"
