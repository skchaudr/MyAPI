-- MyAPI sprint persistence slice v001
-- Metadata, request logs, eval runs, benchmark runs — not the vector store.

CREATE TABLE IF NOT EXISTS schema_migrations (
    version     TEXT PRIMARY KEY,
    applied_at  TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS sources (
    id              BIGSERIAL PRIMARY KEY,
    external_id     TEXT,
    system          TEXT NOT NULL,
    title           TEXT NOT NULL DEFAULT '',
    uri             TEXT,
    meta            JSONB NOT NULL DEFAULT '{}'::jsonb,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_sources_system ON sources (system);
CREATE INDEX IF NOT EXISTS idx_sources_external_id ON sources (external_id);
CREATE INDEX IF NOT EXISTS idx_sources_meta_gin ON sources USING GIN (meta);

CREATE TABLE IF NOT EXISTS ingestion_jobs (
    id              BIGSERIAL PRIMARY KEY,
    source_id       BIGINT REFERENCES sources(id) ON DELETE SET NULL,
    status          TEXT NOT NULL DEFAULT 'pending',
    items_total     INT NOT NULL DEFAULT 0,
    items_done      INT NOT NULL DEFAULT 0,
    error           TEXT,
    started_at      TIMESTAMPTZ,
    finished_at     TIMESTAMPTZ,
    meta            JSONB NOT NULL DEFAULT '{}'::jsonb,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_ingestion_jobs_status ON ingestion_jobs (status);

CREATE TABLE IF NOT EXISTS request_logs (
    id              BIGSERIAL PRIMARY KEY,
    endpoint        TEXT NOT NULL,
    method          TEXT NOT NULL DEFAULT 'GET',
    status_code     INT,
    latency_ms      DOUBLE PRECISION,
    query_text      TEXT,
    client_id       TEXT,
    meta            JSONB NOT NULL DEFAULT '{}'::jsonb,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_request_logs_created_at ON request_logs (created_at DESC);
CREATE INDEX IF NOT EXISTS idx_request_logs_endpoint ON request_logs (endpoint);

CREATE TABLE IF NOT EXISTS evaluation_runs (
    id              BIGSERIAL PRIMARY KEY,
    name            TEXT NOT NULL,
    dataset_id      TEXT,
    score           DOUBLE PRECISION,
    metrics         JSONB NOT NULL DEFAULT '{}'::jsonb,
    notes           TEXT,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_evaluation_runs_name ON evaluation_runs (name);

CREATE TABLE IF NOT EXISTS benchmark_runs (
    id              BIGSERIAL PRIMARY KEY,
    label           TEXT NOT NULL,
    phase           TEXT NOT NULL DEFAULT 'baseline',
    rps             DOUBLE PRECISION,
    p50_ms          DOUBLE PRECISION,
    p95_ms          DOUBLE PRECISION,
    p99_ms          DOUBLE PRECISION,
    error_rate      DOUBLE PRECISION,
    concurrency     INT,
    duration_s      INT,
    notes           TEXT,
    raw             JSONB NOT NULL DEFAULT '{}'::jsonb,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_benchmark_runs_label ON benchmark_runs (label);
