import os
import json
import re
from typing import Dict, Any, Optional

# Doc types must match CanonicalDoc.doc_type values
_VALID_DOC_TYPES = {"conversation", "note", "spec", "log", "article", "other"}

_DEFAULT_VERTEX_PROJECT = "sb-info-notes-2026"
_DEFAULT_VERTEX_LOCATION = "us-central1"
_DEFAULT_MODEL = "gemini-2.5-flash"

_PROMPT_TEMPLATE = """\
You are a document classification and summarization assistant for a personal knowledge RAG pipeline.

Analyze the following document content and return a JSON object with exactly these three fields:
- "summary": A 2-3 sentence summary of the document's core content, optimized for RAG embedding. Be dense and precise.
- "doc_type": One of these exact strings — "conversation", "note", "spec", "log", "article", "other".
- "tags": A list of 3-8 lowercase keyword tags (strings) capturing the main topics.

Respond with only valid JSON. No markdown fences, no explanation.

DOCUMENT:
{content}
"""


class GeminiService:
    """Gemini enrich client: GEMINI_API_KEY if set, else Vertex + ADC."""

    def __init__(self, model_name: Optional[str] = None):
        self.api_key = os.environ.get("GEMINI_API_KEY")
        self.project = (
            os.environ.get("GOOGLE_CLOUD_PROJECT")
            or os.environ.get("GCLOUD_PROJECT")
            or _DEFAULT_VERTEX_PROJECT
        )
        self.location = (
            os.environ.get("GOOGLE_CLOUD_LOCATION")
            or os.environ.get("VERTEX_LOCATION")
            or _DEFAULT_VERTEX_LOCATION
        )
        self.model_name = (
            model_name
            or os.environ.get("GEMINI_MODEL")
            or _DEFAULT_MODEL
        )
        # Back-compat flag used by older callers/tests
        self.has_api_key = bool(self.api_key)
        self.auth_mode = "none"
        self._client = None
        self._init_error: Optional[str] = None

        try:
            from google import genai

            if self.api_key:
                self._client = genai.Client(api_key=self.api_key)
                self.auth_mode = "api_key"
            else:
                # Application Default Credentials (user ADC or GCE SA)
                self._client = genai.Client(
                    vertexai=True,
                    project=self.project,
                    location=self.location,
                )
                self.auth_mode = "vertex_adc"
        except Exception as e:
            self._init_error = str(e)
            self._client = None
            self.auth_mode = "none"

    @property
    def is_configured(self) -> bool:
        return self._client is not None

    def enrich(self, content: str) -> Dict[str, Any]:
        """
        Calls Gemini to produce a summary, doc_type classification, and tags
        for the given document content.

        Returns a dict with keys: summary, doc_type, tags.
        Raises Exception if neither GEMINI_API_KEY nor Vertex/ADC is usable.
        """
        if not self._client:
            detail = self._init_error or "no client"
            raise Exception(
                "Gemini not configured. Set GEMINI_API_KEY, or configure "
                f"Vertex ADC (project={self.project}, location={self.location}). "
                f"Init error: {detail}"
            )

        # Truncate very large documents to avoid blowing token limits.
        # 8000 chars ≈ ~2000 tokens — well within flash limits.
        truncated = content[:8000] if content else ""

        prompt = _PROMPT_TEMPLATE.format(content=truncated)

        response = self._client.models.generate_content(
            model=self.model_name,
            contents=prompt,
        )
        raw = response.text.strip()

        # Strip markdown fences if the model wraps its output anyway
        raw = re.sub(r"^```(?:json)?\s*", "", raw, flags=re.IGNORECASE)
        raw = re.sub(r"\s*```$", "", raw)

        parsed = json.loads(raw)

        # Validate and sanitize fields
        summary = str(parsed.get("summary", "")).strip() or None
        doc_type = parsed.get("doc_type", "other")
        if doc_type not in _VALID_DOC_TYPES:
            doc_type = "other"
        tags = parsed.get("tags", [])
        if not isinstance(tags, list):
            tags = []
        tags = [str(t).lower().strip() for t in tags if t]

        return {
            "summary": summary,
            "doc_type": doc_type,
            "tags": tags,
        }
