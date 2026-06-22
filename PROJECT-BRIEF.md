# MyAPI-rebuild — Brief

Personal context engine. A vault of durable handoffs surfaced as context briefs via MCP — not v0's single RAG pool.

## Narrative

MyAPI-rebuild is the second attempt at a personal context engine, rebuilt
around one hard-won lesson: v0 dumped Obsidian, chat exports, and CLI
sessions into one retrieval pool and hoped ranking would sort it out. It
didn't — ChatGPT exports dominated by volume, ~579 CLI sessions were
ingested but never surfaced, and there were no presentable narratives, only
raw dumps. The rebuild inverts the premise: the product is not bigger
ingestion, it is **durable handoffs** — event traces and decisions boxed so
any agent can continue without re-litigating origin or direction. The
working theme is *Ascend* — if the product is "capture context in a box and
move it across sessions," the handoff is the tool. Two MCP tools
(`get_project_context`, `get_person_context`) return **context briefs**:
what matters, why, what the evidence is, what to think next. It is one of
three portfolio pieces (with .pi and GDDP) — together a triptych for
verify / control / continue in agent-era infrastructure.

## Ground state

Pulled from `graphify-out/.graphify_analysis.json` (2026-06-21).

- **Phase:** planning / docs only — 0 implementation code, branch `rebuild`
  (no commits yet). The graph reflects the *plan*, not the system.
- **Graph:** 31 nodes · 57 edges · 4 communities · 10 docs · cohesion 0.25–0.33
- **Target stack:** Python (`context_refinery/` — adapters, triage CLI,
  FastAPI `/query`), Markdown/Obsidian (corpus + brief output, FSRS-migratable
  frontmatter), JSON/YAML (graph + schemas), TypeScript (archived
  friend-refinery React UI — not rebuilt)
- **Top god nodes:** REBUILD-CONTEXT-ANCHOR.md (17), ARCHITECTURE.md (15),
  handoffs/001 (7), AGENTS.md root (6), MCP Tools (6), get_project_context (4)
- **Structure (4 communities):** handoff/AGENTS ecosystem (evals, ingest,
  rag-pipeline sub-agents); context-refinery core (event_trace, handoff
  vault, context_refinery, graphify); corpus + architecture (context brief,
  unified graph model, study/export layer); MCP surface
  (get_project/person_context, get_evidence_for_claim, get_review_queue)
- **Old MyAPI substrate:** `../MyAPI/Corpus v1.0/` (22 PARA buckets) +
  `../MyAPI/graphify-out/graph.json` (862 nodes, 2186 links) — the rebuild's L0/L1

## Current direction

Portfolio-ready as architecture + paradigm, with implementation as the
explicit next chapter. Done means: an honest README framing v0's failure
and the handoff inversion; `ARCHITECTURE.md` as the canonical build plan
(four layers L0–L4); two event traces (MyAPI v0 derail; rebuild-night Codex
derail) as the first durable handoffs in the vault; golden briefs proved by
a cold agent continuing without re-litigation.

## Known gaps / risks

- Root `AGENTS.md` is broken (voice-to-text derail mid-file) — needs full
  rewrite before any agent reads it cold
- Zero implementation code — README must not oversell; portfolio value is
  paradigm + architecture, with the build as stated next work
- "Context Refinery" naming collision: archived friend-refinery React UI vs
  the live `context_refinery/` Python package — drift risk for new readers
- `get_user_context` / `get_person_context` / "operator context" are the
  same tool — anchor locks the name to `get_person_context`; do not fork
- Friend-refinery origin (friends reclaiming ChatGPT/WhatsApp/LinkedIn
  dumps) must not be conflated with the person-context MCP tool — different
  threads

## Deeper docs

- Context anchor (read first): [`project-documents/REBUILD-CONTEXT-ANCHOR.md`](project-documents/REBUILD-CONTEXT-ANCHOR.md)
- Architecture (build plan): [`project-documents/ARCHITECTURE.md`](project-documents/ARCHITECTURE.md)
- Handoffs: [`handoffs/001-rebuild-narrative-recapture.md`](handoffs/001-rebuild-narrative-recapture.md)
- Old MyAPI + corpus: [`../MyAPI/`](../MyAPI/), `../MyAPI/Corpus v1.0/`
