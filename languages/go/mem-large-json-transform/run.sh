#!/usr/bin/env bash
set -euo pipefail
DIR="$(cd "$(dirname "$0")" && pwd)"
BIN="$DIR/mem_large_json_transform_go"
go build -o "$BIN" "$DIR/transform.go"
"$BIN" "${1:?dataset path required}"
