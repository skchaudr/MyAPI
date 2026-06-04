import { CanonicalDocument, EnrichmentResult } from '../types';
import { GeminiService } from '../services/geminiService';

export interface EnrichmentOptions {
  enableSummary?: boolean;
  enableDocType?: boolean;
  enableTags?: boolean;
}

export class EnrichmentService {
  private geminiService: GeminiService;

  constructor(geminiService?: GeminiService) {
    this.geminiService = geminiService || new GeminiService();
  }

  async enrichDocument(
    doc: CanonicalDocument,
    options: EnrichmentOptions = { enableSummary: true, enableDocType: true, enableTags: true }
  ): Promise<CanonicalDocument> {
    try {
      const enrichment = await this.geminiService.enrich(doc.content);

      const result: CanonicalDocument = { ...doc };

      if (options.enableSummary && enrichment.summary) {
        result.summary = enrichment.summary;
      }

      if (options.enableDocType && enrichment.doc_type) {
        result.doc_type = enrichment.doc_type;
      }

      if (options.enableTags && enrichment.tags) {
        result.tags = [...(doc.tags || []), ...enrichment.tags];
        // Deduplicate tags
        result.tags = Array.from(new Set(result.tags));
      }

      return result;
    } catch (error) {
      console.warn("Enrichment failed or skipped:", (error as Error).message);
      // Fallback behavior: return the original document unmodified
      return doc;
    }
  }
}
