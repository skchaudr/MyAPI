-- Run as doadmin against the default `defaultdb` database.
-- Creates logical DBs and least-privilege app roles for the DO sprint.
--
-- Usage (passwords injected via psql variables, never committed):
--   psql "$ADMIN_DATABASE_URL" \
--     -v stage_pass="'…'" \
--     -v prod_pass="'…'" \
--     -v bench_pass="'…'" \
--     -f ops/do-sprint/sql/00_admin_bootstrap.sql

\set ON_ERROR_STOP on

-- Roles (idempotent)
SELECT format('CREATE ROLE %I LOGIN PASSWORD %L', 'myapi_stage_user', :'stage_pass')
WHERE NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'myapi_stage_user')\gexec
SELECT format('CREATE ROLE %I LOGIN PASSWORD %L', 'myapi_prod_user', :'prod_pass')
WHERE NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'myapi_prod_user')\gexec
SELECT format('CREATE ROLE %I LOGIN PASSWORD %L', 'myapi_bench_user', :'bench_pass')
WHERE NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'myapi_bench_user')\gexec

-- Rotate passwords even if roles already exist
ALTER ROLE myapi_stage_user PASSWORD :'stage_pass';
ALTER ROLE myapi_prod_user   PASSWORD :'prod_pass';
ALTER ROLE myapi_bench_user  PASSWORD :'bench_pass';

-- Databases (owned by doadmin; grants below)
SELECT 'CREATE DATABASE myapi_stage OWNER doadmin'
WHERE NOT EXISTS (SELECT 1 FROM pg_database WHERE datname = 'myapi_stage')\gexec
SELECT 'CREATE DATABASE myapi_prod OWNER doadmin'
WHERE NOT EXISTS (SELECT 1 FROM pg_database WHERE datname = 'myapi_prod')\gexec
SELECT 'CREATE DATABASE myapi_bench OWNER doadmin'
WHERE NOT EXISTS (SELECT 1 FROM pg_database WHERE datname = 'myapi_bench')\gexec

GRANT CONNECT ON DATABASE myapi_stage TO myapi_stage_user;
GRANT CONNECT ON DATABASE myapi_prod  TO myapi_prod_user;
GRANT CONNECT ON DATABASE myapi_bench TO myapi_bench_user;

-- Revoke public connect noise where possible
REVOKE ALL ON DATABASE myapi_stage FROM PUBLIC;
REVOKE ALL ON DATABASE myapi_prod  FROM PUBLIC;
REVOKE ALL ON DATABASE myapi_bench FROM PUBLIC;
GRANT CONNECT ON DATABASE myapi_stage TO myapi_stage_user;
GRANT CONNECT ON DATABASE myapi_prod  TO myapi_prod_user;
GRANT CONNECT ON DATABASE myapi_bench TO myapi_bench_user;
