import os
import secrets

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import APIKeyHeader
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


api_key_header = APIKeyHeader(name="X-API-Key")

def verify_admin_api_key(api_key: str = Depends(api_key_header)):
    expected_api_key = os.environ.get("ADMIN_API_KEY")
    if not expected_api_key:
        raise HTTPException(status_code=500, detail="Internal Server Error")
    if not secrets.compare_digest(api_key, expected_api_key):
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return api_key

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/admin/info", dependencies=[Depends(verify_admin_api_key)])
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
    @app.get("/debug/sentry-test")
    def sentry_test():
        raise RuntimeError("MyAPI Sentry smoke test")
