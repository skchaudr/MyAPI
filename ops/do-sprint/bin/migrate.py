#!/usr/bin/env python3
"""Apply versioned SQL migrations under ops/do-sprint/sql/migrations/.

Requires DATABASE_URL (postgresql://… or postgres://…).
Never prints the connection string or password.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

try:
    import psycopg
except ImportError:
    print("error: psycopg not installed. Run: pip install 'psycopg[binary]'", file=sys.stderr)
    sys.exit(2)

MIGRATIONS_DIR = Path(__file__).resolve().parents[1] / "sql" / "migrations"


def main() -> int:
    dsn = os.environ.get("DATABASE_URL")
    if not dsn:
        print("error: DATABASE_URL is not set", file=sys.stderr)
        return 2

    files = sorted(MIGRATIONS_DIR.glob("*.sql"))
    if not files:
        print(f"error: no migrations in {MIGRATIONS_DIR}", file=sys.stderr)
        return 2

    applied: list[str] = []
    with psycopg.connect(dsn, connect_timeout=15) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS schema_migrations (
                version     TEXT PRIMARY KEY,
                applied_at  TIMESTAMPTZ NOT NULL DEFAULT now()
            )
            """
        )
        conn.commit()

        for path in files:
            version = path.name
            row = conn.execute(
                "SELECT 1 FROM schema_migrations WHERE version = %s",
                (version,),
            ).fetchone()
            if row:
                print(f"skip  {version}")
                continue
            sql = path.read_text(encoding="utf-8")
            with conn.transaction():
                conn.execute(sql)
                conn.execute(
                    "INSERT INTO schema_migrations (version) VALUES (%s) ON CONFLICT DO NOTHING",
                    (version,),
                )
            applied.append(version)
            print(f"apply {version}")

    print(f"done: applied {len(applied)} migration(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
