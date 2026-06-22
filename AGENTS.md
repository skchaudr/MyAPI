# AGENTS.md — MyAPI-rebuild

Personal context engine rebuild. A vault of durable handoffs surfaced as
context briefs via MCP — not v0's single RAG pool.

Read [`project-documents/REBUILD-CONTEXT-ANCHOR.md`](project-documents/REBUILD-CONTEXT-ANCHOR.md)
first in any cold session — it locks the paradigm, glossary, and direction
so origin/naming don't get re-litigated. Build plan:
[`project-documents/ARCHITECTURE.md`](project-documents/ARCHITECTURE.md).
Project brief: [`PROJECT-BRIEF.md`](PROJECT-BRIEF.md).

## Phase

Planning / docs only. No implementation code yet. Branch `rebuild` (no
commits yet). Do not invent run/test/lint commands — they don't exist.
Work order is traces → golden briefs → reader → MCP, in that sequence.

## Project snapshot

- **Target stack:** Python (`context_refinery/` — adapters, triage CLI,
  FastAPI `/query`), Markdown/Obsidian (corpus + brief output,
  FSRS-migratable frontmatter), JSON/YAML (graph + schemas)
- **Existing tooling:** `graphify extract .` refreshes
  `graphify-out/.graphify_analysis.json` (no LLM cold-start needed)
- **Substrates:** [`../MyAPI/Corpus v1.0/`](../MyAPI/) (22 PARA buckets),
  `../MyAPI/graphify-out/graph.json` (862 nodes, 2186 links)
- **MCP surface (target):** `get_project_context`, `get_person_context` —
  the anchor locks these two names; do not fork into `get_user_context` /
  "operator context"
- **No install / test / lint / run yet** — implementation is the next chapter
- **Key dirs:** `project-documents/`, `handoffs/`, `graphify-out/`, `evals/`,
  `ingest/`, `rag-pipeline/` (sub-agent contracts)
