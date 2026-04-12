// src/types/schema.ts
// This is the single source of truth for the CanonicalDocument data contract.
// All adapters, services, and UI components MUST use these types.
// See docs/01-taxonomy.md for the meaning of each value.

export type MaturityStatus =
  | "mature"
  | "incubating"
  | "scratchpad"
  | "deprecated"
  | "reference";

export type DocType =
  | "conversation"
  | "note"
  | "spec"
  | "log"
  | "article"
  | "other";

export type SourceSystem =
  | "chatgpt"
  | "claude"
  | "obsidian"
  | "linkedin"
  | "manual";

export type SourceType = "json" | "html" | "md" | "csv";

export interface CanonicalDocument {
  // 1. Identity
  id: string; // UUID

  title: string;

  // 2. Provenance
  source: {
    system: SourceSystem;
    type: SourceType;
    original_file_name?: string;
    url?: string;
  };

  // 3. Temporal Data
  timestamps: {
    created_at?: string;
    updated_at?: string;
    ingested_at: string;
  };

  // 4. Taxonomy & RAG Metadata
  author: string;
  status: MaturityStatus; // Defaults to "scratchpad" on all new imports
  doc_type: DocType;
  tags: string[];
  projects: string[];

  // 5. The Payload
  content: {
    raw_text?: string;
    cleaned_markdown: string;
    summary?: string;
  };

  // 6. Metrics & Validation
  quality: {
    is_noisy: boolean;
    warnings: string[];
  };
}
