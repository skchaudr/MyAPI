import os

from fastapi import FastAPI
import secrets
from fastapi import Depends, HTTPException, status
from fastapi.security import APIKeyHeader
from fastapi.middleware.cors import CORSMiddleware
from api.observability import init_sentry
from api.routers import enrich, imports, query, meta
from api import db

init_sentry()

app = FastAPI(title="Context Refinery API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",   # Vite dev
        "http://localhost:4173",   # Vite preview
        "http://0.0.0.0:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(enrich.router)
app.include_router(imports.router, prefix="/import")
app.include_router(query.router)
app.include_router(meta.router)
# export.py is retired — export is now client-side via exportService.ts



api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)

def verify_health_api_key(api_key: str = Depends(api_key_header)):
    expected_key = os.environ.get("HEALTH_API_KEY")
    if not expected_key:
        import logging
        logger = logging.getLogger(__name__)
        logger.error("HEALTH_API_KEY is not configured on the server")
        raise HTTPException(status_code=500, detail="An internal server error occurred")
    if not api_key or not secrets.compare_digest(api_key, expected_key):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API Key",
        )

@app.get("/health", dependencies=[Depends(verify_health_api_key)])
def health():
    from context_refinery.services import GeminiService

    svc = GeminiService()
    payload = {
        "status": "ok",
        "model": svc.model_name,
        "auth_mode": svc.auth_mode,
        "project": None if svc.auth_mode == "api_key" else svc.project,
        "location": None if svc.auth_mode == "api_key" else svc.location,
        "gemini_configured": svc.is_configured,
        "khoj_url": os.environ.get("KHOJ_URL"),
    }
    payload.update(db.health())
    return payload


if os.getenv("ENABLE_SENTRY_TEST_ENDPOINT") == "1":
    @app.get("/debug/sentry-test")
    def sentry_test():
        raise RuntimeError("MyAPI Sentry smoke test")
