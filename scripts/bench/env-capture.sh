#!/usr/bin/env bash
set -euo pipefail

OUT_FILE="${1:-}"
if [[ -z "$OUT_FILE" ]]; then
  echo "usage: env-capture.sh <output-file>" >&2
  exit 1
fi

mkdir -p "$(dirname "$OUT_FILE")"

HOSTNAME_VALUE="$(hostname || echo unknown)"
OS_NAME="$(uname -s || echo unknown)"
ARCH_NAME="$(uname -m || echo unknown)"
OS_VERSION="$(sw_vers -productVersion 2>/dev/null || uname -r || echo unknown)"
CPU_BRAND="$(sysctl -n machdep.cpu.brand_string 2>/dev/null || sysctl -n machdep.cpu.brand_string 2>/dev/null || echo Apple-Silicon-or-unknown)"
PHYSICAL_CORES="$(sysctl -n hw.physicalcpu 2>/dev/null || echo unknown)"
LOGICAL_CORES="$(sysctl -n hw.logicalcpu 2>/dev/null || echo unknown)"
MEM_BYTES="$(sysctl -n hw.memsize 2>/dev/null || echo 0)"
MEM_GB=$(python3 - <<PY
mem_bytes = int("$MEM_BYTES" or 0)
print(round(mem_bytes / (1024**3), 2) if mem_bytes else "unknown")
PY
)
GIT_COMMIT="$(git rev-parse HEAD 2>/dev/null || echo unknown)"
GIT_BRANCH="$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo unknown)"
GIT_DIRTY="$(if git diff --quiet 2>/dev/null; then echo false; else echo true; fi)"
PY_VER="$(python3 --version 2>/dev/null | awk '{print $2}' || echo unknown)"
NODE_VER="$(node --version 2>/dev/null || echo unknown)"
GO_VER="$(go version 2>/dev/null | awk '{print $3}' || echo unknown)"
RUST_VER="$(rustc --version 2>/dev/null | awk '{print $2}' || echo unknown)"
JAVA_VER="$(java -version 2>&1 | head -n1 | awk -F '"' '{print $2}' || echo unknown)"
DOTNET_VER="$(dotnet --version 2>/dev/null || echo unknown)"
CAPTURED_AT="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"

cat > "$OUT_FILE" <<EOF
{
  "captured_at": "$CAPTURED_AT",
  "host": {
    "hostname": "$HOSTNAME_VALUE",
    "os": "$OS_NAME",
    "os_version": "$OS_VERSION",
    "arch": "$ARCH_NAME",
    "cpu_model": "$CPU_BRAND",
    "physical_cores": "$PHYSICAL_CORES",
    "logical_cores": "$LOGICAL_CORES",
    "memory_gb": "$MEM_GB"
  },
  "toolchain": {
    "python": "$PY_VER",
    "node": "$NODE_VER",
    "go": "$GO_VER",
    "rust": "$RUST_VER",
    "java": "$JAVA_VER",
    "dotnet": "$DOTNET_VER"
  },
  "git": {
    "commit": "$GIT_COMMIT",
    "branch": "$GIT_BRANCH",
    "dirty": $GIT_DIRTY
  }
}
EOF

echo "$OUT_FILE"
