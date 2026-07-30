#!/usr/bin/env bash
# Daily: allowlist build → deliver to Khoj (soft-skip if down).
# Canon: config/daily_corpus_allowlist.yaml (handful of paths — not whole SSD).
# Logs: ~/Library/Logs/myapi-daily-hot-corpus.{log,err.log}
set -euo pipefail

export PATH="/usr/local/bin:/usr/bin:/bin:/opt/homebrew/bin:${HOME}/.local/bin:${PATH}"
export HOME="${HOME:-/Users/sab-mini}"

REPO="${MYAPI_REPO:-/Users/sab-mini/repos/MyAPI}"
cd "$REPO"

echo "=== $(date -u +%Y-%m-%dT%H:%M:%SZ) daily hot corpus START host=$(hostname -s) ==="
echo "allowlist=${MYAPI_DAILY_ALLOWLIST:-$REPO/config/daily_corpus_allowlist.yaml}"
python3 scripts/daily_corpus_allowlist.py
python3 scripts/build_daily_active_corpus.py
python3 scripts/deliver_daily_active_corpus.py
echo "=== $(date -u +%Y-%m-%dT%H:%M:%SZ) daily hot corpus END ==="
