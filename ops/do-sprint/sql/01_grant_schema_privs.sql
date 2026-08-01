-- Run once per logical database as doadmin, connected TO that database.
-- Example:
--   psql "$ADMIN_URL_STAGE" -f ops/do-sprint/sql/01_grant_schema_privs.sql \
--     -v app_user=myapi_stage_user
--
-- Variables:
--   app_user  — role that owns application objects (e.g. myapi_stage_user)

\set ON_ERROR_STOP on

GRANT USAGE, CREATE ON SCHEMA public TO :"app_user";
ALTER DEFAULT PRIVILEGES IN SCHEMA public
  GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO :"app_user";
ALTER DEFAULT PRIVILEGES IN SCHEMA public
  GRANT USAGE, SELECT ON SEQUENCES TO :"app_user";

-- Existing objects (if re-run after partial setup)
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO :"app_user";
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO :"app_user";
