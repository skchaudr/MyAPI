
from pydantic import BaseModel, Field, field_validator
from typing import Optional, Literal

# These types mirror src/types/schema.ts exactly.
# See docs/01-taxonomy.md for the meaning of each value.

MaturityStatus = Literal["mature", "incubating", "scratchpad", "deprecated", "reference"]
DocType = Literal["conversation", "note", "spec", "log", "article", "other"]
SourceSystem = Literal["chatgpt", "claude", "obsidian", "linkedin", "manual", "codex"]
SourceType = Literal["json", "html", "md", "csv"]


class EnrichRequest(BaseModel):
    content: str


class EnrichResponse(BaseModel):
    summary: Optional[str] = None
    doc_type: DocType
    tags: list[str]


class EnrichResult(BaseModel):
    index: int
    status: Literal["success", "error"]
    data: Optional[EnrichResponse] = None
    error: Optional[str] = None


class BatchEnrichRequest(BaseModel):
    documents: list[EnrichRequest] = Field(..., min_length=1, max_length=50)

    @field_validator('documents')
    @classmethod
    def check_content(cls, v):
        for d in v:
            if not d.content.strip():
                raise ValueError("content must be non-empty")
        return v


class BatchEnrichResponse(BaseModel):
    results: list[EnrichResult]
    total: int
    succeeded: int
    failed: int


class Source(BaseModel):
    system: SourceSystem
    type: SourceType
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
    status: MaturityStatus  # Always "scratchpad" on new imports per taxonomy rules
    doc_type: DocType
    tags: list[str]
    projects: list[str]
    content: ContentPayload
    quality: Quality


# ── Smart Retrieval Schemas ──────────────────────────────────────────────────

QueryIntent = Literal["temporal", "factual", "project_overview", "cross_source", "pattern"]
AnswerMode = Literal["lookup", "summary", "timeline", "dossier", "coach"]


class QueryRequest(BaseModel):
    q: str = Field(..., min_length=1, max_length=2000)
    n: int = Field(default=10, ge=1, le=50)
    sources: Optional[list[SourceSystem]] = None
    projects: Optional[list[str]] = None
    tags: Optional[list[str]] = None
    date_from: Optional[str] = None
    date_to: Optional[str] = None
    answer_mode: Optional[AnswerMode] = None


class RetrievedDocument(BaseModel):
    corpus_id: str
    snippet: str
    khoj_score: float
    final_score: float
    title: Optional[str] = None
    source: Optional[str] = None
    created_at: Optional[str] = None
    tags: list[str] = []
    projects: list[str] = []
    file: Optional[str] = None


class ResultGroup(BaseModel):
    key: str
    group_type: str
    documents: list[RetrievedDocument]
    count: int


class QueryClassification(BaseModel):
    intent: QueryIntent
    answer_mode: AnswerMode
    confidence: float
    temporal_hint: Optional[str] = None


class QueryResponse(BaseModel):
    query: str
    classification: QueryClassification
    results: list[RetrievedDocument]
    groups: list[ResultGroup]
    total_from_khoj: int
    total_after_filter: int
    answer_mode: AnswerMode
    timing_ms: float
