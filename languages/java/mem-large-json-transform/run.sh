#!/usr/bin/env bash
set -euo pipefail
DIR="$(cd "$(dirname "$0")" && pwd)"
mkdir -p "$DIR/out"
javac -d "$DIR/out" "$DIR/MemLargeJsonTransform.java"
java -cp "$DIR/out" MemLargeJsonTransform "${1:?dataset path required}"
