## Destination

**Semantic Graphify for agent cold-start.** In the first 30–90 seconds of an agent session, agents hit MyAPI/MCP the way they hit Graphify — and get structured, leveled, grounded orientation: *where we are, what’s true, what’s open, what’s dangerous* — without file archaeology or confident bogus answers. Substrate is the real work surface (agent sessions, project notes outside `docs/`, chats, project docs, and the semantic meaning behind code), not an AST-only graph.

One-line form: Agent cold-start that returns structured, leveled, grounded orientation over work + life knowledge — including semantic meaning of project code — via an API/MCP agents can hammer like Graphify.

## Notes

- **Domain:** personal + project knowledge retrieval; agent cold-start; MCP surface; episodic memory levels; honest retrieval.
- **Skills every session should consult:** `/grilling`, `/domain-modeling`; `/research` for AFK tickets; `/prototype` only if a ticket needs a throwaway shape.
- **Path constraint (non-negotiable):** realistic and near. Reuse Context Refinery, adapters, Khoj, corpus work, anchors, query bank, any MCP/golden-brief work already on other hosts. Map clears into a *thin* build plan — not a multi-month platform rewrite.
- **Tracker:** local markdown under `.scratch/semantic-graphify-cold-start/` (no `setup-matt-pocock-skills` wiring in this clone yet).
- **Plan, don’t do:** tickets resolve *decisions*. Implementation waits for map clear → `/to-spec` (or a tiny direct implement if the effort collapses).
- **Principles fixed at chart time:** cold-start first; semantic graph over life/work corpus (not AST); honest no-evidence/weak-evidence; agent Graphify-class questions as product signal; episodic levels (raw → summary → decision → status).
- **Clone note:** this host’s `/home/saboor/MyAPI` is on `feat/corpus-v1-normalization`. GitHub `main` holds rebuild MCP/briefs/plans; local feat trees hold live `/query` engine — inventory in research/01.
- **Wayfinder → GDDP (execution handoff):** Wayfinder decides; human authors a **new** MyAPI graph in `gddp-config` from locked decisions; `gddp-runtime` dispatches and stops at receipts. Open decision tickets never become nodes. Old six-node `graphs/myapi` is reference/loot only. Full rule: [WAYFINDER-TO-GDDP.md](WAYFINDER-TO-GDDP.md).
- **GDDP target:** new graph under `/home/sab-mini/gddp-config/graphs/` (path/name TBD at authoring; default `myapi` replace or `myapi-cold-start` — pick at put time).
- **Thread capture (tickets ↔ nodes):** [THREAD-CAPTURE-MAP.md](THREAD-CAPTURE-MAP.md) — full side-by-side of tickets and executor nodes.
- **Canonical intent for mission planning → GDDP:** [CANONICAL-INTENT-FOR-MISSION-PLANNING.md](CANONICAL-INTENT-FOR-MISSION-PLANNING.md) — what Wayfinder captured that GDDP must preserve; node order for a *usable* end state; agenda for Factory Droid mission planning.
## Decisions so far

- [Inventory existing machinery](issues/01-inventory-existing-machinery.md) — Live `/query`+refinery on feat trees; MCP/briefs/plans on GitHub `main`. Research: [research/01](research/01-inventory-existing-machinery.md)
- [Cold-start question bank](issues/02-cold-start-question-bank.md) — Eight must-questions for v1. Research: [research/02](research/02-cold-start-question-bank.md)
- [Don’t fake confidence](issues/03-honest-answer-contract.md) — Already in north star: grounded or say weak/missing; no Graphify-bogus invention. Field names = build detail.
- [Thinnest v1 loop](issues/04-thinnest-v1-loop.md) — Khoj → MyAPI → 2 MCP tools + `/query` (args/examples); prove MyAPI first; MCP brief + query hits; new GDDP graph later.
- [Episodic levels](issues/05-episodic-levels-v1.md) — Status/open/danger + decisions in brief; summaries support; raw as links.
- [Source priority](issues/06-source-priority-v1.md) — Sessions, project notes, chats, docs, anchors/handoffs via existing Khoj path; prefer high-signal over bulk chat spam.
- [Code-meaning boundary](issues/07-code-meaning-boundary-v1.md) — MyAPI owns meaning; Graphify/repo owns structure; knowledge-primary.
- [MyAPI vs MCP ownership](issues/08-myapi-vs-mcp-ownership.md) — MyAPI/Khoj = engine; MCP = thin two-tool doorway; `/query` stays first-class.

## Not yet specified

- Full entity/edge ontology for a long-lived “life graph” (beyond what v1 cold-start needs).
- Live join from Graphify AST nodes → narrative meaning nodes (symbol-level linking product).
- Multi-project portfolio scale (beyond proving one project cold-start well).
- Exact post-04 reconcile table for the six existing myapi GDDP nodes (keep / rewrite / defer / split) — procedure is in WAYFINDER-TO-GDDP.md; content waits on 03+04.
- Active-corpus window policy vs full Corpus v1.0 cold substrate as the default index for cold-start.
- Production MCP packaging / install UX across Claude Code, Codex, Cursor, Grok CLI.
- Human-facing UI (Obsidian browsing) as a product surface — vault is substrate means, not this map’s destination.

## Out of scope

- Replacing Graphify for pure code-structure queries (imports, call graphs, “where is X defined?” as AST).
- Multi-tenant SaaS / external customers in this effort.
- Perfect total recall of all historical chats forever as a v1 bar.
- Greenfield rewrite of Context Refinery or Khoj.
- Automating graph truth writes without human trust gates.
- Finishing every Phase-2 bank query as the definition of done for this map.
