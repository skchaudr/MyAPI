import asyncio
import logging

from fastapi import APIRouter, HTTPException
from api.schemas import EnrichRequest, EnrichResponse, BatchEnrichRequest, BatchEnrichResponse, EnrichResult
from context_refinery.services import GeminiService

router = APIRouter()
logger = logging.getLogger(__name__)


def _is_gemini_unconfigured(exc: Exception) -> bool:
    msg = str(exc).lower()
    return "not configured" in msg or "gemini_api_key" in msg


@router.post("/enrich", response_model=EnrichResponse)
async def enrich_content(request: EnrichRequest):
    try:
        service = GeminiService()
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(None, service.enrich, request.content)
        return EnrichResponse(**result)
    except Exception as e:
        if _is_gemini_unconfigured(e):
            raise HTTPException(
                status_code=503,
                detail="Gemini not configured (set GEMINI_API_KEY or Vertex ADC)",
            )
        logger.error("Enrichment error", exc_info=True)
        # SECURITY: Do not expose raw exception strings to the client to prevent internal information leakage.
        raise HTTPException(status_code=500, detail="An internal server error occurred")


@router.post("/enrich/batch", response_model=BatchEnrichResponse)
async def enrich_batch(request: BatchEnrichRequest):
    service = GeminiService()
    loop = asyncio.get_event_loop()

    results = []
    succeeded = 0
    failed = 0

    for i, doc in enumerate(request.documents):
        try:
            result = await loop.run_in_executor(None, service.enrich, doc.content)
            enrich_response = EnrichResponse(**result)
            results.append(EnrichResult(index=i, status="success", data=enrich_response))
            succeeded += 1
        except Exception as e:
            if _is_gemini_unconfigured(e):
                raise HTTPException(
                    status_code=503,
                    detail="Gemini not configured (set GEMINI_API_KEY or Vertex ADC)",
                )
            logger.error("Batch enrichment error at index %s", i, exc_info=True)
            # SECURITY: Do not expose raw exception strings to the client to prevent internal information leakage.
            results.append(
                EnrichResult(index=i, status="error", error="An internal server error occurred")
            )
            failed += 1

        if i < len(request.documents) - 1:
            await asyncio.sleep(0.2)

    return BatchEnrichResponse(
        results=results,
        total=len(request.documents),
        succeeded=succeeded,
        failed=failed
    )
