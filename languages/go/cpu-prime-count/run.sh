#!/usr/bin/env bash
set -euo pipefail
DIR="$(cd "$(dirname "$0")" && pwd)"
BIN="$DIR/prime_count_go"
go build -o "$BIN" "$DIR/prime_count.go"
"$BIN" "${1:-100000}"
