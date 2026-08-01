"""CRUD for sprint metadata tables (sources) — proves app ↔ Postgres path."""
from __future__ import annotations

from typing import Any, Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from api import db

router = APIRouter(prefix="/meta", tags=["meta"])


class SourceIn(BaseModel):
    system: str = Field(..., min_length=1, max_length=64)
    title: str = Field(default="", max_length=512)
    external_id: Optional[str] = None
    uri: Optional[str] = None
    meta: dict[str, Any] = Field(default_factory=dict)


class SourceOut(SourceIn):
    id: int
    created_at: str
    updated_at: str


def _require_db() -> None:
    if not db.available():
        raise HTTPException(status_code=503, detail="DATABASE_URL not configured")


@router.get("/db")
def meta_db_status():
    return db.health()


@router.post("/sources", status_code=201)
def create_source(body: SourceIn):
    _require_db()
    import json

    row = db.fetch_one(
        """
        INSERT INTO sources (system, title, external_id, uri, meta)
        VALUES (%s, %s, %s, %s, %s::jsonb)
        RETURNING id, system, title, external_id, uri, meta,
                  created_at::text, updated_at::text
        """,
        (body.system, body.title, body.external_id, body.uri, json.dumps(body.meta)),
    )
    return row


@router.get("/sources/{source_id}")
def get_source(source_id: int):
    _require_db()
    row = db.fetch_one(
        """
        SELECT id, system, title, external_id, uri, meta,
               created_at::text, updated_at::text
        FROM sources WHERE id = %s
        """,
        (source_id,),
    )
    if not row:
        raise HTTPException(status_code=404, detail="source not found")
    return row


@router.patch("/sources/{source_id}")
def update_source(source_id: int, body: SourceIn):
    _require_db()
    import json

    row = db.fetch_one(
        """
        UPDATE sources
        SET system = %s,
            title = %s,
            external_id = %s,
            uri = %s,
            meta = %s::jsonb,
            updated_at = now()
        WHERE id = %s
        RETURNING id, system, title, external_id, uri, meta,
                  created_at::text, updated_at::text
        """,
        (
            body.system,
            body.title,
            body.external_id,
            body.uri,
            json.dumps(body.meta),
            source_id,
        ),
    )
    if not row:
        raise HTTPException(status_code=404, detail="source not found")
    return row


@router.delete("/sources/{source_id}", status_code=204)
def delete_source(source_id: int):
    _require_db()
    row = db.fetch_one("DELETE FROM sources WHERE id = %s RETURNING id", (source_id,))
    if not row:
        raise HTTPException(status_code=404, detail="source not found")
    return None


@router.get("/sources")
def list_sources(limit: int = 50):
    _require_db()
    limit = max(1, min(limit, 200))
    return db.fetch_all(
        """
        SELECT id, system, title, external_id, uri, meta,
               created_at::text, updated_at::text
        FROM sources
        ORDER BY id DESC
        LIMIT %s
        """,
        (limit,),
    )
