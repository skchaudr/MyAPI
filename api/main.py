import os
import secrets
import logging

from fastapi import FastAPI, Depends, HTTPException, Security
from fastapi.security import APIKeyHeader
from fastapi.middleware.cors import CORSMiddleware
from api.observability import init_sentry
from api.routers import enrich, imports, query, meta
from api import db

logger = logging.getLogger(__name__)
init_sentry()

api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)

def verify_admin_key(api_key: str = Security(api_key_header)):
    expected_key = os.environ.get("ADMIN_API_KEY")
    if not expected_key:
        logger.error("ADMIN_API_KEY environment variable is not set. Failing securely.")
        raise HTTPException(status_code=500, detail="Internal server error")

    if not api_key or not secrets.compare_digest(api_key, expected_key):
        raise HTTPException(status_code=401, detail="Unauthorized")

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


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/admin/info", dependencies=[Depends(verify_admin_key)])
def admin_info():
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
    @app.get("/debug/sentry-test", dependencies=[Depends(verify_admin_key)])
    def sentry_test():
        raise RuntimeError("MyAPI Sentry smoke test")
