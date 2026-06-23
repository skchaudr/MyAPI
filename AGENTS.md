# AGENTS.md — MyAPI / MyAPI-rebuild

Personal context engine rebuild. A vault of durable handoffs surfaced as
context briefs via MCP — not v0's single RAG pool.

Read [`project-documents/REBUILD-CONTEXT-ANCHOR.md`](project-documents/REBUILD-CONTEXT-ANCHOR.md)
first in any cold session — it locks the paradigm, glossary, and direction
so origin/naming don't get re-litigated. Build plan:
[`project-documents/ARCHITECTURE.md`](project-documents/ARCHITECTURE.md).
Project brief: [`PROJECT-BRIEF.md`](PROJECT-BRIEF.md).

## Phase

Planning / docs-first rebuild work is now merged toward `main`. Do not invent
run/test/lint commands for new rebuild surfaces until the repo adds them.
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
- **Key dirs:** `project-documents/`, `handoffs/`, `graphify-out/`, `evals/`,
  `ingest/`, `rag-pipeline/` (sub-agent contracts)

## Command location rules

This repository has historically used both local Mac and remote VM surfaces.
When giving a command, always state where it should be run.

Required labels:

- `Run on Mac:` — local workstation where the user is typing
- `Run on VM:` — command executed from the remote Google Cloud VM target
- `Run in VM shell:` — command run after SSHing into the VM
- `Run in Cloud Shell:` — command run in Google Cloud Shell

If a command depends on `localhost`, `127.0.0.1`, a service port, or a local
file path, the target machine must be explicit. If the command only makes sense
after an SSH hop or inside a specific shell session, say that too.

Prefer one long command line over wrapped multi-line commands when possible. If
a command must be multi-line, keep each line self-contained and clearly
delimited. Any command being instructed to run must be placed on its own
separate line, not inline with surrounding prose.
