# Expected Fixture: get_project_context("MyAPI-rebuild")

Tool target: `get_project_context`
Intent: `project_overview`
Context type: `project`

## Short Answer

MyAPI-rebuild is a personal context engine rebuilt around durable handoffs and ContextBriefs, not a larger single RAG pool. The target product surface is two MCP calls, `get_project_context` and `get_person_context`, backed by a bottom-up stack: corpus, graph, context packs, MCP, then study/export. The next useful slice is to establish golden briefs as the quality bar before implementing the MCP tools.

## Why This Matters

This fixture defines what a good project brief should return before the system can generate it. It should let an agent understand the project direction, current phase, source hierarchy, and open gaps without re-litigating the old MyAPI origin or mistaking raw dumps for the product.

## Key Relationships

- MyAPI-rebuild -> implements -> durable handoff vault and MCP ContextBriefs (evidence-backed, conf 0.95)
- ContextBrief -> returned_by -> `get_project_context` and `get_person_context` (evidence-backed, conf 0.95)
- Corpus v2.0 -> feeds -> graph traversal and retrieval -> brief assembly (evidence-backed, conf 0.9)
- Golden briefs -> define_quality_bar_for -> future ContextBrief model and MCP integration tests (evidence-backed, conf 0.9)
- Live sources -> include -> Obsidian SSD, Codex sessions, Claude projects, scoped Pi/Needle traces, rebuild handoffs (evidence-backed, conf 0.85)

## Evidence

- "Rebuild MyAPI as a vault of durable handoffs... surfaced as context briefs via MCP" - `/Users/sab-mini/repos/MyAPI-rebuild/project-documents/REBUILD-CONTEXT-ANCHOR.md:L13` (confidence 0.95)
- "The fix is shape, not more data: sanitize -> normalize -> presentable narrative with evidence pointers" - `/Users/sab-mini/repos/MyAPI-rebuild/project-documents/REBUILD-CONTEXT-ANCHOR.md:L76` (confidence 0.95)
- "`get_project_context` | What's going on with this project?" - `/Users/sab-mini/repos/MyAPI-rebuild/project-documents/REBUILD-CONTEXT-ANCHOR.md:L94-L97` (confidence 0.95)
- "Everything returns one of these" for ContextBrief - `/Users/sab-mini/repos/MyAPI-rebuild/project-documents/ARCHITECTURE.md:L132-L145` (confidence 0.95)
- "The portfolio vertical slice is L0 -> L1 -> L2 -> L3" - `/Users/sab-mini/repos/MyAPI-rebuild/IMPLEMENTATION-PLAN.md:L35-L38` (confidence 0.9)
- "Phase 4... golden briefs (expected output for known inputs)" - `/Users/sab-mini/repos/MyAPI-rebuild/IMPLEMENTATION-PLAN.md:L91-L98` (confidence 0.9)
- "live sources exist and are mostly fresh enough for a raw audit pass" - `/Users/sab-mini/repos/MyAPI-rebuild/project-documents/corpus-freshness-audit-2026-07-01.md:L5-L7` (confidence 0.85)

## Open Risks / Unknowns

- The current code defaults are not aligned with intended live sources, so generated briefs may miss live Obsidian, current Codex sessions, and Pi/Needle traces until ingestion defaults are patched.
- `get_person_context` is canonically required by the plan, but older architecture text still contains a conflicting deferral note; the anchor and implementation plan should win for this rebuild.
- Event traces for MyAPI v0 and rebuild night are part of the integrated plan, but this fixture is based only on the requested grounding docs, not the eventual trace corpus.
- No MCP implementation exists yet in this task; this is an expected fixture for future structural evaluation.

## Useful Next Questions

- `get_project_context("MyAPI-rebuild")`: What is the next implementation slice after golden briefs?
- `get_project_context("MyAPI-rebuild")`: Which source families should be ingested first for corpus v2.0?
- `get_project_context("MyAPI-rebuild")`: Which risks would make a generated brief fail the golden quality bar?
