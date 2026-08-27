import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.observability import init_sentry
from api.routers import enrich, imports, query, meta
from api import db

init_sentry()

app = FastAPI(title="Context Refinery API", version="1.0.0")

allowed_origins_env = os.environ.get("ALLOWED_ORIGINS", "")
allow_origins = [origin.strip() for origin in allowed_origins_env.split(",") if origin.strip()]
if not allow_origins:
    allow_origins = [
        "http://localhost:3000",   # Vite dev
        "http://localhost:4173",   # Vite preview
    ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,
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
