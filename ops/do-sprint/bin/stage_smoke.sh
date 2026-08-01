#!/usr/bin/env bash
# End-to-end stage proof: migrate → API CRUD → cleanup.
# Prerequisites: DATABASE_URL set; venv with deps; run from MyAPI root or any cwd.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"
cd "$ROOT"

if [[ -z "${DATABASE_URL:-}" ]]; then
  if [[ -f ops/do-sprint/secrets/stage.database_url ]]; then
    export DATABASE_URL="$(tr -d '\n' < ops/do-sprint/secrets/stage.database_url)"
  else
    echo "error: DATABASE_URL not set and no stage.database_url secret" >&2
    exit 2
  fi
fi

echo "== 1. prove DB =="
bash ops/do-sprint/bin/prove_db.sh

echo "== 2. migrate =="
python3 ops/do-sprint/bin/migrate.py

echo "== 3. tables =="
psql "$DATABASE_URL" -v ON_ERROR_STOP=1 -c \
  "SELECT tablename FROM pg_tables WHERE schemaname = 'public' ORDER BY 1;"

echo "== 4. start API =="
# Prefer venv if present
PY=python3
if [[ -x venv/bin/uvicorn ]]; then
  UV=venv/bin/uvicorn
  PY=venv/bin/python
elif [[ -x .venv/bin/uvicorn ]]; then
  UV=.venv/bin/uvicorn
  PY=.venv/bin/python
else
  UV="python3 -m uvicorn"
fi

PORT="${SMOKE_PORT:-8010}"
# shellcheck disable=SC2086
$UV api.main:app --host 127.0.0.1 --port "$PORT" >/tmp/myapi-stage-smoke.log 2>&1 &
PID=$!
cleanup() { kill "$PID" 2>/dev/null || true; }
trap cleanup EXIT

for i in $(seq 1 30); do
  if curl -sf "http://127.0.0.1:${PORT}/health" >/dev/null; then
    break
  fi
  sleep 0.3
done

echo "== 5. health =="
curl -sf "http://127.0.0.1:${PORT}/health" | $PY -m json.tool

echo "== 6. CRUD =="
CREATE=$(curl -sf -X POST "http://127.0.0.1:${PORT}/meta/sources" \
  -H 'content-type: application/json' \
  -d '{"system":"manual","title":"stage-smoke","external_id":"smoke-1","meta":{"sprint":"do"}}')
echo "$CREATE" | $PY -m json.tool
ID=$(echo "$CREATE" | $PY -c 'import sys,json; print(json.load(sys.stdin)["id"])')

curl -sf "http://127.0.0.1:${PORT}/meta/sources/${ID}" | $PY -m json.tool

curl -sf -X PATCH "http://127.0.0.1:${PORT}/meta/sources/${ID}" \
  -H 'content-type: application/json' \
  -d '{"system":"manual","title":"stage-smoke-updated","external_id":"smoke-1","meta":{"sprint":"do","ok":true}}' \
  | $PY -m json.tool

curl -sf -o /dev/null -w "DELETE HTTP %{http_code}\n" -X DELETE "http://127.0.0.1:${PORT}/meta/sources/${ID}"

echo "== 7. short request log insert =="
psql "$DATABASE_URL" -v ON_ERROR_STOP=1 -c \
  "INSERT INTO request_logs (endpoint, method, status_code, latency_ms, query_text)
   VALUES ('/meta/sources', 'POST', 201, 12.5, 'stage-smoke');
   SELECT count(*) AS request_logs FROM request_logs;"

echo "PASS: stage smoke complete"
