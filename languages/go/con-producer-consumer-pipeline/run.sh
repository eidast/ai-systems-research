#!/usr/bin/env bash
set -euo pipefail
DIR="$(cd "$(dirname "$0")" && pwd)"
BIN="$DIR/con_producer_consumer_go"
go build -o "$BIN" "$DIR/pipeline.go"
"$BIN" "${1:-100000}"
