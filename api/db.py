"""Minimal Postgres access for the DO sprint persistence slice.

Uses DATABASE_URL. Never logs the DSN.
"""
from __future__ import annotations

import os
from contextlib import contextmanager
from typing import Any, Iterator, Optional

_pool = None


def database_url() -> Optional[str]:
    return os.environ.get("DATABASE_URL")


def available() -> bool:
    return bool(database_url())


def _connect():
    try:
        import psycopg
        from psycopg.rows import dict_row
    except ImportError as e:
        raise RuntimeError("psycopg not installed") from e
    dsn = database_url()
    if not dsn:
        raise RuntimeError("DATABASE_URL is not set")
    return psycopg.connect(dsn, connect_timeout=10, row_factory=dict_row)


@contextmanager
def connection() -> Iterator[Any]:
    conn = _connect()
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def fetch_one(sql: str, params: tuple = ()) -> Optional[dict]:
    with connection() as conn:
        return conn.execute(sql, params).fetchone()


def fetch_all(sql: str, params: tuple = ()) -> list[dict]:
    with connection() as conn:
        return list(conn.execute(sql, params).fetchall())


def execute(sql: str, params: tuple = ()) -> None:
    with connection() as conn:
        conn.execute(sql, params)


def health() -> dict:
    if not available():
        return {"database": "unconfigured"}
    try:
        row = fetch_one(
            "SELECT current_database() AS db, current_user AS usr, "
            "NOW() AS ts"
        )
        return {
            "database": "ok",
            "current_database": row["db"] if row else None,
            "current_user": row["usr"] if row else None,
        }
    except Exception as e:
        return {"database": "error", "detail": type(e).__name__}
