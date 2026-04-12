# Jules Task: Add Batch Gemini Enrichment Endpoint

## Summary
Add a `POST /enrich/batch` endpoint that enriches multiple documents in a single request, with rate limiting and progress tracking. The single-doc `/enrich` endpoint already works — this extends it.

## Current Architecture

### Existing endpoint: `POST /enrich`
- File: `api/routers/enrich.py`
- Accepts: `{ "content": "..." }` (single string)
- Returns: `{ "summary": "...", "doc_type": "note", "tags": ["a", "b"] }`
- Calls `GeminiService.enrich()` via `asyncio` executor

### GeminiService (`context_refinery/services.py`)
- Model: `gemini-1.5-flash`
- Truncates input to 8,000 characters
- Returns JSON: `{ summary, doc_type, tags }`
- Validates doc_type against taxonomy, sanitizes tags to lowercase

### EnrichmentService (`context_refinery/enrichment.py`)
- Wraps GeminiService with `enrich_document(doc, options)`
- Accepts `CanonicalDoc` dataclass + optional `EnrichmentOptions`
- Deep copies doc before modifying
- Merges enriched tags with existing tags, deduplicates
- Graceful fallback: returns original doc if enrichment fails

### Schemas (`api/schemas.py`)
- `EnrichRequest(content: str)`
- `EnrichResponse(summary, doc_type, tags)`
- `CanonicalDocumentResponse` — full document schema

## Requirements

### 1. New endpoint: `POST /enrich/batch`

**Request body:**
```python
class BatchEnrichRequest(BaseModel):
    documents: list[EnrichRequest]  # max 50 items
```

**Response body:**
```python
class BatchEnrichResponse(BaseModel):
    results: list[EnrichResult]
    total: int
    succeeded: int
    failed: int

class EnrichResult(BaseModel):
    index: int
    status: Literal["success", "error"]
    data: Optional[EnrichResponse] = None
    error: Optional[str] = None
```

### 2. Rate limiting
- Process documents sequentially (not concurrently) to respect Gemini API rate limits
- Add a 200ms delay between each Gemini call (`asyncio.sleep(0.2)`)
- If a single document fails, log the error and continue to the next — don't abort the batch

### 3. Input validation
- Reject batches larger than 50 documents (return 422)
- Each document's content must be non-empty

### 4. Register the endpoint
Add the new endpoint in `api/routers/enrich.py` and ensure it's included in the existing router.

## Key Files to Modify
- `api/routers/enrich.py` — add new endpoint
- `api/schemas.py` — add `BatchEnrichRequest`, `BatchEnrichResponse`, `EnrichResult`

## Key Files to Read (don't modify)
- `context_refinery/services.py` — understand GeminiService
- `context_refinery/enrichment.py` — understand EnrichmentService
- `docs/01-taxonomy.md` — valid doc_type and status values

## Tests to Add
Add tests in `tests/test_api_enrich.py`:
1. `test_batch_enrich_success` — 3 docs, all succeed
2. `test_batch_enrich_partial_failure` — 3 docs, one fails, others succeed
3. `test_batch_enrich_empty_list` — empty list returns 422
4. `test_batch_enrich_over_limit` — 51 docs returns 422
5. `test_batch_enrich_no_api_key` — returns 503

Use the existing `MockGeminiService` from `tests/conftest.py` — it already patches globally.

## Do NOT
- Modify the existing single `/enrich` endpoint
- Change GeminiService or EnrichmentService internals
- Add concurrent/parallel Gemini calls (rate limit risk)
- Add new dependencies
