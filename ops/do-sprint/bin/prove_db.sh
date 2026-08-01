#!/usr/bin/env bash
# Prove TLS + auth to managed Postgres without echoing secrets.
set -euo pipefail

if [[ -z "${DATABASE_URL:-}" ]]; then
  echo "error: DATABASE_URL not set" >&2
  exit 2
fi

# Never print DATABASE_URL
psql "$DATABASE_URL" -v ON_ERROR_STOP=1 -c \
  "SELECT current_database() AS current_database,
          current_user      AS current_user,
          inet_server_addr() AS server_addr,
          left(version(), 60) AS version;"

echo "OK: database connectivity proved"
