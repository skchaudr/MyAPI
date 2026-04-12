import asyncio
from fastapi import APIRouter, HTTPException
from api.schemas import EnrichRequest, EnrichResponse, BatchEnrichRequest, BatchEnrichResponse, EnrichResult
from context_refinery.services import GeminiService

router = APIRouter()

@router.post("/enrich", response_model=EnrichResponse)
async def enrich_content(request: EnrichRequest):
    try:
        service = GeminiService()
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(None, service.enrich, request.content)
        return EnrichResponse(**result)
    except Exception as e:
        if "GEMINI_API_KEY" in str(e):
            raise HTTPException(status_code=503, detail="GEMINI_API_KEY not configured on this server")
        raise HTTPException(status_code=500, detail=str(e))


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
            if "GEMINI_API_KEY" in str(e):
                raise HTTPException(status_code=503, detail="GEMINI_API_KEY not configured on this server")
            results.append(EnrichResult(index=i, status="error", error=str(e)))
            failed += 1

        if i < len(request.documents) - 1:
            await asyncio.sleep(0.2)

    return BatchEnrichResponse(
        results=results,
        total=len(request.documents),
        succeeded=succeeded,
        failed=failed
    )
