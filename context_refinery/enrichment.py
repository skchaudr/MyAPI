from typing import Optional, Dict, Any, List
import copy
from .models import CanonicalDoc
from .services import GeminiService

class EnrichmentOptions:
    def __init__(self, enable_summary: bool = True, enable_doc_type: bool = True, enable_tags: bool = True):
        self.enable_summary = enable_summary
        self.enable_doc_type = enable_doc_type
        self.enable_tags = enable_tags

class EnrichmentService:
    def __init__(self, gemini_service: Optional[GeminiService] = None):
        self.gemini_service = gemini_service or GeminiService()

    def enrich_document(self, doc: CanonicalDoc, options: Optional[EnrichmentOptions] = None) -> CanonicalDoc:
        if options is None:
            options = EnrichmentOptions()

        try:
            enrichment = self.gemini_service.enrich(doc.content)

            # create a new instance to avoid modifying the original
            # we do a shallow copy of lists/dicts that we modify, but a simple way is
            # just to copy the whole object since Python assignment doesn't clone.
            result = copy.deepcopy(doc)

            if options.enable_summary and enrichment.get("summary"):
                result.summary = enrichment["summary"]

            if options.enable_doc_type and enrichment.get("doc_type"):
                result.doc_type = enrichment["doc_type"]

            if options.enable_tags and enrichment.get("tags"):
                if result.tags is None:
                    result.tags = []
                result.tags.extend(enrichment["tags"])
                # Deduplicate tags
                result.tags = list(dict.fromkeys(result.tags))

            return result
        except Exception as e:
            print(f"Enrichment failed or skipped: {e}")
            # Fallback behavior: return the original document unmodified
            return doc
