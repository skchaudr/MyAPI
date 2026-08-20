# Graphify layer inventory — what graphify-out/ knows

Built 2026-08-19 from live measurement of `graphify-out/` on main @ 0fbcb09.
Graph built_at_commit: `d82a5eaefaa76ed8a9f815660052c8637a50e1b9` (matches the
evidence contract pin; report header dates the build 2026-08-08).

## 1. Capabilities inventories (exact counts from graph.json)

- **Nodes: 53,573** — by file_type: `document` 41,068 · `code` 12,337 ·
  `rationale` 163 · `concept` 5. Origin: 53,562 AST-extracted, 11 unknown.
- **Links: 73,117** — by relation: `contains` 46,811 · `calls` 20,747 ·
  `indirect_call` 4,326 · `references` 580 · `imports` 173 ·
  `rationale_for` 163 · `method` 133 · `imports_from` 103 · `uses` 48 ·
  `inherits` 20 · `re_exports` 10 · `defines` 2 · `conceptually_related_to` 1.
  Extraction split per GRAPH_REPORT.md: 94% extracted / 6% inferred
  (4,389 inferred edges, avg confidence 0.55).
- **Communities: 3,733** (2,701 carry a name; report shows 3,306, omits 427 thin).
- **Coverage by source root (nodes):** `Corpus v1.0` 51,391 · `scratch` 608 ·
  `project-docs` 447 · `context_refinery` 371 · `tests` 199 · `.handoffs` 164 ·
  `scripts` 143 · others < 55 · 31 nodes have no source_file.
- **Experimental fact:** this is primarily a *corpus* graph (96% of nodes under
  Corpus v1.0), secondarily a code graph. Code-structure questions (calls,
  imports, inheritance) are served by the 12,337 code nodes; document
  relationships dominate `contains`.

### Known data-quality points (recorded, not papered over)
- Community names are noisy: many are quoted sentence fragments or error
  strings (e.g. names beginning `'"I cried tears of joy…'`). Treat
  community_name as low-authority text; use community id for joins.
- 31 nodes lack source_file; 11 nodes lack a known origin.
- GRAPH_REPORT.md hub list includes non-code artifacts (e.g. "Sab") as hubs —
  degree centrality here reflects corpus mentions, not code importance.

## 2. Dual representation (both preserved)

**Deterministic structural data** — referenced in place (67 MB; not copied):
| Artifact | Bytes | SHA-256 |
|---|---|---|
| `graphify-out/graph.json` | 67,111,631 | `847d2e851d3389c50742101f90f54eb0445a297d47e78f22fafbe34202879b8e` |
| `graphify-out/GRAPH_REPORT.md` | 821,201 | `be90f45c35e8e2a000eae833a7cf08574cba8adced4fd3ac5d74a1002894973c` |
| `graphify-out/manifest.json` | 762,140 | `f2676917c5c3ea56d6e5a6fbcfe2eb02f203aca835310962f5972d7cc1f6e039` |

Reproducibility: `graphify-out/graph.json` is tracked in git; the sha256
above pins the exact bytes consumed by this inventory at @0fbcb09.

**Retrieval-friendly textual representation** — `GRAPH_REPORT.md` itself
(corpus check, community hubs, per-community summaries) plus this inventory.
These are what a retrieval system should index; graph.json is what a program
should query.

## 3. Distinction: which representation serves which question

| Question class | Served by | Why |
|---|---|---|
| "What does module X call/import?" | graph.json (deterministic) | exact relation edges with source_location; retrieval text loses precision |
| "Which files relate to concept Y?" | graph.json communities + GRAPH_REPORT | community ids are joins; names too noisy to query directly |
| "Give me an orientation summary of the repo/corpus" | GRAPH_REPORT.md (retrieval-friendly) | prose, hubs, corpus verdict |
| "How stale is structural knowledge?" | built_at_commit vs HEAD | deterministic comparison, no LLM |
| "Why was decision/rationale Z recorded?" | graph.json `rationale_for` edges (163) | sparse; retrieval over corpus text likely better coverage |
| Treatment/corpus experiments | graph.json only | counts, hashes, and edges must be exact and re-checkable |

Rule of thumb: **anything a scorer or evaluator must re-verify comes from
graph.json; anything a reader needs for orientation comes from the report.**
