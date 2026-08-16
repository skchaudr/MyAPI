# Expected Fixture: get_person_context("Sab")

Tool target: `get_person_context`
Intent: `project_overview`
Context type: `person`

## Short Answer

Sab is the person the context engine is built to support: a builder/operator whose continuity depends on durable project handoffs, live Obsidian anchors, session traces, decisions, preferences, and portfolio-shaped evidence. `get_person_context` should not wait on LinkedIn or WhatsApp exports; those belong to the friend-refinery origin thread. A useful Sab brief should be Obsidian-primary, evidence-backed, and honest about which personal facts are grounded versus still missing from normalized corpus v2.0.

## Why This Matters

The person tool is part of the canonical two-tool target. This fixture locks the distinction between "Sab as person/context owner" and "friend platform export product origin," so future agents do not reduce person context to operator jargon or defer it behind unrelated LinkedIn/WhatsApp ingestion.

## Key Relationships

- Sab -> needs -> durable handoffs and context briefs for agent continuity (evidence-backed, conf 0.9)
- `get_person_context` -> answers -> "Who is Sab?" (evidence-backed, conf 0.95)
- Person brief -> source_emphasis -> Obsidian-primary projects, decisions, preferences, portfolio shape (evidence-backed, conf 0.95)
- LinkedIn / WhatsApp exports -> belong_to -> friend-refinery origin, not required person-context blocker (evidence-backed, conf 0.9)
- Live Obsidian SSD -> best_source_for -> current person/project truth and `get_person_context` (evidence-backed, conf 0.9)

## Evidence

- The rebuild is surfaced through MCP tools including `get_person_context` - `/Users/sab-mini/repos/MyAPI-rebuild/project-documents/REBUILD-CONTEXT-ANCHOR.md:L13` (confidence 0.95)
- "`get_person_context` | Who is Sab?" - `/Users/sab-mini/repos/MyAPI-rebuild/project-documents/REBUILD-CONTEXT-ANCHOR.md:L94-L99` (confidence 0.95)
- "Person brief: Obsidian-primary (projects, decisions, preferences, portfolio shape)" - `/Users/sab-mini/repos/MyAPI-rebuild/project-documents/REBUILD-CONTEXT-ANCHOR.md:L101-L105` (confidence 0.95)
- "Person context does not wait on those exports" - `/Users/sab-mini/repos/MyAPI-rebuild/project-documents/REBUILD-CONTEXT-ANCHOR.md:L105` (confidence 0.95)
- The canonical direction is to aggregate data so `get_project_context` and `get_person_context` can be made - `/Users/sab-mini/repos/MyAPI-rebuild/IMPLEMENTATION-PLAN.md:L12-L21` (confidence 0.9)
- The implementation plan explicitly confirms `get_person_context` as a Phase 5 MCP tool - `/Users/sab-mini/repos/MyAPI-rebuild/IMPLEMENTATION-PLAN.md:L100-L107` (confidence 0.9)
- Live vault is "Current person/project truth, preferences, decisions, active project anchors. Best source for `get_person_context`." - `/Users/sab-mini/repos/MyAPI-rebuild/project-documents/corpus-freshness-audit-2026-07-01.md:L31` (confidence 0.9)

## Open Risks / Unknowns

- This fixture can define the desired shape, but it cannot provide a rich personal profile until the live Obsidian SSD notes are normalized and cited directly.
- Architecture text still says to defer `get_person_context`, but the context anchor and implementation plan supersede that for the current two-tool target.
- Sab-specific facts such as current priorities, preferences, and portfolio story must come from live vault anchors and traces, not from generic inference about the rebuild.
- The first generated person brief should distinguish durable facts from session-current facts, with freshness/provenance visible in evidence metadata.

## Useful Next Questions

- `get_person_context("Sab")`: What are Sab's current active projects and highest-priority responsibilities?
- `get_person_context("Sab")`: Which decisions and preferences should future agents honor by default?
- `get_project_context("MyAPI-rebuild")`: Which live Obsidian anchors should seed the first person-context graph nodes?
