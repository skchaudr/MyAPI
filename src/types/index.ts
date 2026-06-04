export interface CanonicalDocument {
  id: string;
  content: string;
  title?: string;
  doc_type?: string;
  tags?: string[];
  [key: string]: any;
}

export interface EnrichmentResult {
  summary?: string;
  doc_type?: string;
  tags?: string[];
}
