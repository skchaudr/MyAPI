# Expected Fixture: get_project_context("Pi / Needle")

Tool target: `get_project_context`
Intent: `project_overview`
Context type: `project`

## Short Answer

Pi / Needle should be treated as an important live source family for agent/runtime continuity, not as a generic directory to ingest wholesale. The current MyAPI-rebuild docs identify scoped Pi paths, especially Needle, agent sessions, harness sessions, and handoffs, as fresh enough for a raw audit pass but not yet supported by an adapter/default path. A good project brief should surface that Pi / Needle context is valuable, current, and ingestion-risky unless scoped.

## Why This Matters

This fixture tests whether `get_project_context` can produce a project brief for a related operational system that is outside the rebuild repo but central to the intended corpus. It should show the engine can distinguish "fresh evidence source" from "implemented ingestion path" and recommend bounded next steps instead of pulling all of `.pi`.

## Key Relationships

- Pi / Needle traces -> evidences -> cross-agent continuity and runtime provenance (evidence-backed, conf 0.9)
- Pi / Needle traces -> missing_adapter_in -> MyAPI-rebuild ingestion defaults (evidence-backed, conf 0.9)
- Scoped roots -> safer_than -> naive `.pi` ingestion (evidence-backed, conf 0.9)
- Corpus v2.0 raw audit -> should_include -> scoped Pi/Needle traces (evidence-backed, conf 0.85)
- `get_project_context("Pi / Needle")` -> should_return -> source status, risks, and next ingestion questions (inferred from brief contract, conf 0.8)

## Evidence

- "Pi / Needle traces" are listed among intended live sources for durable handoffs - `/Users/sab-mini/repos/MyAPI-rebuild/project-documents/corpus-freshness-audit-2026-07-01.md:L5-L7` (confidence 0.9)
- Scoped Pi paths include `/Users/sab-mini/.pi/needle`, `/Users/sab-mini/.pi/agent/sessions`, `/Users/sab-mini/.pi/harness/sessions`, `/Users/sab-mini/.pi/.handoffs`, and `/Users/sab-mini/.pi/agent/handoffs` - `/Users/sab-mini/repos/MyAPI-rebuild/project-documents/corpus-freshness-audit-2026-07-01.md:L42` (confidence 0.9)
- Pi / Needle traces are "Important for cross-agent continuity and runtime provenance" - `/Users/sab-mini/repos/MyAPI-rebuild/project-documents/corpus-freshness-audit-2026-07-01.md:L42` (confidence 0.9)
- "No current MyAPI-rebuild adapter/default for this family" - `/Users/sab-mini/repos/MyAPI-rebuild/project-documents/corpus-freshness-audit-2026-07-01.md:L42` (confidence 0.9)
- Freshness judgment includes "scoped `/Users/sab-mini/.pi` traces" - `/Users/sab-mini/repos/MyAPI-rebuild/project-documents/corpus-freshness-audit-2026-07-01.md:L44-L51` (confidence 0.85)
- Recommended sab-air defaults include Pi/Needle scoped roots - `/Users/sab-mini/repos/MyAPI-rebuild/project-documents/corpus-freshness-audit-2026-07-01.md:L67-L72` (confidence 0.85)

## Open Risks / Unknowns

- `.pi` is large; a naive ingestion pass would likely pull cache, code, generated artifacts, and unrelated local state.
- The docs establish freshness and likely role, but they do not yet define a Pi/Needle parser contract or fixture schema.
- The specific project names and entities inside Needle traces still need a raw manifest/sample parse before this brief can cite individual event traces.
- Current MyAPI-rebuild adapter defaults do not include Pi/Needle, so this context may remain invisible until a dedicated adapter or raw extractor exists.

## Useful Next Questions

- `get_project_context("Pi / Needle")`: Which scoped roots are freshest and parser-ready?
- `get_project_context("Pi / Needle")`: Which traces should become first durable handoffs?
- `get_project_context("MyAPI-rebuild")`: What adapter contract is needed before Pi / Needle can enter corpus v2.0?
