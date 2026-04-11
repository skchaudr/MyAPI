import asyncio
from fastapi import APIRouter, HTTPException
from api.schemas import EnrichRequest, EnrichResponse
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
