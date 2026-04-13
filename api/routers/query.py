import asyncio
import logging
from fastapi import APIRouter, HTTPException
from api.schemas import QueryRequest, QueryResponse
from context_refinery.retrieval import RetrievalPipeline, KhojUnavailableError

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/query", response_model=QueryResponse)
async def query(request: QueryRequest):
    pipeline = RetrievalPipeline()
    try:
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(
            None,
            lambda: pipeline.execute(
                q=request.q,
                n=request.n,
                sources=request.sources,
                projects=request.projects,
                tags=request.tags,
                date_from=request.date_from,
                date_to=request.date_to,
                answer_mode=request.answer_mode,
            ),
        )
        return QueryResponse(**result)
    except KhojUnavailableError:
        raise HTTPException(status_code=502, detail="Khoj search backend is unavailable")
    except Exception as e:
        logger.error(f"Query pipeline error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
