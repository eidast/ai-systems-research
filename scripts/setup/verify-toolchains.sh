#!/usr/bin/env bash
set -euo pipefail

for cmd in python3 node npm go rustc cargo java javac dotnet clang as; do
  if ! command -v "$cmd" >/dev/null 2>&1; then
    echo "MISSING: $cmd" >&2
    exit 1
  fi
done

echo "python3: $(python3 --version 2>&1)"
echo "node: $(node --version 2>&1)"
echo "npm: $(npm --version 2>&1)"
echo "go: $(go version 2>&1)"
echo "rustc: $(rustc --version 2>&1)"
echo "cargo: $(cargo --version 2>&1)"
echo "java: $(java -version 2>&1 | head -n1)"
echo "javac: $(javac -version 2>&1 | head -n1)"
echo "dotnet: $(dotnet --version 2>&1)"
echo "clang: $(clang --version 2>&1 | head -n1)"
echo "as: $(as --version 2>&1 | head -n1)"

echo "toolchain verification ok"
