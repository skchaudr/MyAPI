from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routers import enrich, imports, query

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
# export.py is retired — export is now client-side via exportService.ts

@app.get("/health")
def health():
    return {"status": "ok", "model": "gemini-1.5-flash"}
