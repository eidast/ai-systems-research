#!/usr/bin/env bash
set -euo pipefail
DIR="$(cd "$(dirname "$0")" && pwd)"
mkdir -p "$DIR/out"
javac -d "$DIR/out" "$DIR/PrimeCount.java"
java -cp "$DIR/out" PrimeCount "${1:-100000}"
