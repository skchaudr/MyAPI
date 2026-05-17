## 2024-05-24 - Exception Details Leak in API Routers
**Vulnerability:** Fast API routes in `api/routers/enrich.py`, `api/routers/export.py`, `api/routers/imports.py`, and `api/routers/query.py` returned raw exception strings directly to the client inside HTTP 500 error messages via `detail=str(e)`.
**Learning:** This widespread pattern could leak sensitive paths, configurations (like `GEMINI_API_KEY` paths or error states), and stack traces. It existed because the generic exception handlers naively passed the full error object back for debugging rather than isolating it.
**Prevention:** Use `logger.error("Error context", exc_info=True)` to safely store the exception context server-side, and return a sanitized, generic error message string in the HTTP response body to the client.
