#!/usr/bin/env bash
set -euo pipefail
DIR="$(cd "$(dirname "$0")" && pwd)"
mkdir -p "$DIR/out"
javac -d "$DIR/out" "$DIR/LargeFileStreaming.java"
java -cp "$DIR/out" LargeFileStreaming "${1:?dataset path required}"
