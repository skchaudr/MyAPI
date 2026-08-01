#!/usr/bin/env bash
# Create myapi_{stage,prod,bench} DBs and least-privilege users.
# Requires ADMIN_DATABASE_URL (doadmin connection to defaultdb).
# Generates passwords into ops/do-sprint/secrets/ (mode 600). Never prints them.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SECRETS="$ROOT/secrets"
mkdir -p "$SECRETS"
chmod 700 "$SECRETS"

if [[ -z "${ADMIN_DATABASE_URL:-}" ]]; then
  echo "error: ADMIN_DATABASE_URL not set (doadmin → defaultdb)" >&2
  exit 2
fi

gen_pass() {
  # URL-safe password without characters that break DSNs
  openssl rand -base64 32 | tr -d '/+=' | head -c 32
}

psql_admin() {
  psql "$ADMIN_DATABASE_URL" -v ON_ERROR_STOP=1 "$@"
}

echo "Bootstrapping roles and databases…"

for env_name in stage prod bench; do
  role="myapi_${env_name}_user"
  db="myapi_${env_name}"
  pass_file="$SECRETS/${env_name}.password"
  if [[ ! -f "$pass_file" ]]; then
    gen_pass >"$pass_file"
    chmod 600 "$pass_file"
    echo "  generated password file for $role"
  else
    echo "  reusing existing password file for $role"
  fi
  pass="$(tr -d '\n' <"$pass_file")"

  # Role
  exists="$(psql_admin -Atc "SELECT 1 FROM pg_roles WHERE rolname = '$role'")"
  if [[ "$exists" != "1" ]]; then
    psql_admin -c "CREATE ROLE ${role} LOGIN PASSWORD '${pass}'"
    echo "  created role $role"
  else
    psql_admin -c "ALTER ROLE ${role} PASSWORD '${pass}'"
    echo "  rotated password for $role"
  fi

  # Database
  db_exists="$(psql_admin -Atc "SELECT 1 FROM pg_database WHERE datname = '$db'")"
  if [[ "$db_exists" != "1" ]]; then
    psql_admin -c "CREATE DATABASE ${db} OWNER doadmin"
    echo "  created database $db"
  else
    echo "  database $db already exists"
  fi

  psql_admin -c "GRANT CONNECT ON DATABASE ${db} TO ${role}"
  psql_admin -c "REVOKE ALL ON DATABASE ${db} FROM PUBLIC"
  psql_admin -c "GRANT CONNECT ON DATABASE ${db} TO ${role}"

  # Schema privileges inside the DB (connect as doadmin to that DB)
  # Rewrite path: swap dbname in URL is fragile; use PGDATABASE override when possible.
  # Prefer explicit admin URL with /dbname — build from components if PG* vars set,
  # otherwise use psql connection service via -d.
  admin_host_url="${ADMIN_DATABASE_URL%%\?*}"
  # strip trailing /dbname
  base="${admin_host_url%/*}"
  db_admin_url="${base}/${db}"
  # preserve query string (sslmode etc.)
  if [[ "$ADMIN_DATABASE_URL" == *"?"* ]]; then
    qs="${ADMIN_DATABASE_URL#*\?}"
    db_admin_url="${db_admin_url}?${qs}"
  fi

  psql "$db_admin_url" -v ON_ERROR_STOP=1 \
    -c "GRANT USAGE, CREATE ON SCHEMA public TO ${role};" \
    -c "ALTER DEFAULT PRIVILEGES FOR ROLE doadmin IN SCHEMA public GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO ${role};" \
    -c "ALTER DEFAULT PRIVILEGES FOR ROLE doadmin IN SCHEMA public GRANT USAGE, SELECT ON SEQUENCES TO ${role};" \
    -c "GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO ${role};" \
    -c "GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO ${role};"

  # Write DSN template without printing password
  # Host/user/port extracted via psql once
  # shellcheck disable=SC2016
  hostport="$(psql_admin -Atc "SELECT format('%s:%s', inet_server_addr(), inet_server_port())")"
  # Prefer original host from ADMIN URL for DNS names (inet may be private IP — good for VPC)
  dsn_file="$SECRETS/${env_name}.database_url"
  # Build URL carefully: encode password for URL (only alnum from gen_pass)
  # Parse host/port/ssl from admin URL with python for correctness
  python3 - "$ADMIN_DATABASE_URL" "$role" "$pass" "$db" "$dsn_file" <<'PY'
import sys
from urllib.parse import urlparse, urlunparse, quote

admin, role, password, db, out = sys.argv[1:]
u = urlparse(admin)
# force user/password/db
netloc = f"{quote(role, safe='')}:{quote(password, safe='')}@{u.hostname}"
if u.port:
    netloc += f":{u.port}"
path = "/" + db
query = u.query or "sslmode=require"
new = urlunparse((u.scheme, netloc, path, "", query, ""))
open(out, "w", encoding="utf-8").write(new + "\n")
import os
os.chmod(out, 0o600)
print(f"  wrote {out} (mode 600)")
PY
done

echo "Bootstrap complete. Secrets under $SECRETS (not for git)."
echo "Next:"
echo "  export DATABASE_URL=\$(cat $SECRETS/stage.database_url)"
echo "  ops/do-sprint/bin/prove_db.sh"
echo "  python3 ops/do-sprint/bin/migrate.py"
