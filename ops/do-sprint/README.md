# DigitalOcean sprint ops (Day 1+)

Run on **sab-dev-2** (staging) first, then mirror on **sab-dev** (production).

## Hard prerequisites

1. **Trusted sources** on `myapi-db` include both Droplets (prefer VPC private IPs).
2. **Admin DSN** as `ADMIN_DATABASE_URL` (doadmin → `defaultdb`, `sslmode=require`).
3. Tools: `psql`, `python3`, `openssl`, `doctl` (optional but useful).

Secrets live in `ops/do-sprint/secrets/` (gitignored, mode 700/600).

## Step 3 — connect staging

```bash
# After doadmin URL is available:
export ADMIN_DATABASE_URL='postgresql://doadmin:***@HOST:25060/defaultdb?sslmode=require'

bash ops/do-sprint/bin/bootstrap_roles.sh

export DATABASE_URL="$(tr -d '\n' < ops/do-sprint/secrets/stage.database_url)"
bash ops/do-sprint/bin/prove_db.sh
```

Expected: `current_database = myapi_stage`, `current_user = myapi_stage_user`.

## Step 4 — schema + MyAPI CRUD

```bash
# once per host
python3 -m venv venv && venv/bin/pip install -r requirements.txt

export DATABASE_URL="$(tr -d '\n' < ops/do-sprint/secrets/stage.database_url)"
bash ops/do-sprint/bin/stage_smoke.sh
```

Pass: migrate + health shows DB ok + create/read/update/delete source via `/meta/sources`.

## Production mirror (sab-dev)

Same flow with `prod.database_url` / `myapi_prod` / `myapi_prod_user`.

## Notes

- MyAPI had **no** Alembic/Django/Prisma migrations; this sprint adds versioned SQL under `sql/migrations/` and `bin/migrate.py`.
- Retrieval still uses Khoj; Postgres holds **metadata / jobs / logs / evals / benchmarks**.
