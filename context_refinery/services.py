import os
import json
import re
from typing import Dict, Any

# Doc types must match CanonicalDoc.doc_type values
_VALID_DOC_TYPES = {"conversation", "note", "spec", "log", "article", "other"}

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
    def __init__(self, model_name: str = "gemini-1.5-flash"):
        self.api_key = os.environ.get("GEMINI_API_KEY")
        self.has_api_key = bool(self.api_key)
        self.model_name = model_name

        if self.has_api_key:
            from google import genai
            self._client = genai.Client(api_key=self.api_key)
        else:
            self._client = None

    def enrich(self, content: str) -> Dict[str, Any]:
        """
        Calls Gemini to produce a summary, doc_type classification, and tags
        for the given document content.

        Returns a dict with keys: summary, doc_type, tags.
        Raises Exception if GEMINI_API_KEY is not set.
        """
        if not self.has_api_key:
            raise Exception(
                "GEMINI_API_KEY is not set. Export it in your environment before running enrichment."
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
