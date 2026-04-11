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

export interface CanonicalDocument {
  // 1. Identity
  id: string; // UUID or hash of content
  title: string; // Human-readable title

  // 2. Provenance (Where did this come from?)
  source: {
    system: "chatgpt" | "claude" | "obsidian" | "linkedin" | "manual";
    type: "json" | "html" | "md" | "csv";
    original_file_name?: string;
    url?: string;
  };

  // 3. Temporal Data
  timestamps: {
    created_at?: string; // ISO string of original creation
    updated_at?: string;
    ingested_at: string; // ISO string of when it hit the Refinery
  };

  // 4. Taxonomy & RAG Metadata
  author: string; // "Me", "ChatGPT", "Claude", "Friend's Name"
  status: MaturityStatus;
  doc_type: DocType;
  tags: string[];
  projects: string[]; // Highly relevant for your 20-30 projects

  // 5. The Payload
  content: {
    raw_text?: string; // Optional: Keep for debugging
    cleaned_markdown: string; // THE GOLD: Sanitized, header-formatted text
    summary?: string; // Optional: AI-generated 3-sentence summary
  };

  // 6. Metrics & Validation
  quality: {
    is_noisy: boolean; // Flagged by sanitization layer
    warnings: string[]; // E.g., "Missing H1 headers", "Very short"
  };
}
