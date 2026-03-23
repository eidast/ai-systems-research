#!/usr/bin/env bash
set -euo pipefail
DIR="$(cd "$(dirname "$0")" && pwd)"
BIN="$DIR/io_large_file_streaming_go"
go build -o "$BIN" "$DIR/stream.go"
"$BIN" "${1:?dataset path required}"
