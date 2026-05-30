#!/usr/bin/env bash
set -euo pipefail
REPO="$(cd "$(dirname "$0")" && pwd)"
cd "$REPO"

echo "=== setup: MyAPI ==="

# 1. Python
python3 --version 2>&1 || { echo "✗ python3 not found"; exit 1; }
echo "✓ python3 $(python3 --version 2>&1 | awk '{print $2}')"

# 2. Install deps (pip only — no heavy ML frameworks)
pip install -q -r requirements.txt 2>/dev/null && echo "✓ pip deps installed" || echo "⚠ pip install failed"

# 3. Verify key imports (no Khoj server needed for import check)
python3 -c "import yaml, rich; from context_refinery import triage" 2>/dev/null && echo "✓ core imports OK" || echo "⚠ import check failed"

# 4. Run tests
if [ -f "tests" ]; then
  pytest -q --tb=short 2>/dev/null && echo "✓ tests pass" || echo "⚠ tests failed or no tests"
fi

# 5. Snapshot
echo "--- snapshot ---"
echo "  branch:  $(git branch --show-current 2>/dev/null || echo 'not a git repo')"
echo "  python:  $(python3 --version 2>&1)"
echo "  setup:   $(date -u +%Y-%m-%dT%H:%M:%SZ)"
