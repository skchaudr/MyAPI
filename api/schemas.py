from pydantic import BaseModel
from typing import Optional


class EnrichRequest(BaseModel):
    content: str


class EnrichResponse(BaseModel):
    summary: Optional[str] = None
    doc_type: str
    tags: list[str]


class Source(BaseModel):
    system: str
    type: str
    original_file_name: Optional[str] = None
    url: Optional[str] = None


class Timestamps(BaseModel):
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    ingested_at: str


class ContentPayload(BaseModel):
    raw_text: Optional[str] = None
    cleaned_markdown: str
    summary: Optional[str] = None


class Quality(BaseModel):
    is_noisy: bool
    warnings: list[str]


class CanonicalDocumentResponse(BaseModel):
    id: str
    title: str
    source: Source
    timestamps: Timestamps
    author: str
    status: str
    doc_type: str
    tags: list[str]
    projects: list[str]
    content: ContentPayload
    quality: Quality
