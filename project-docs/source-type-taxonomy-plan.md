---
title: source_type taxonomy plan
status: scratchpad
projects: [myapi, context-refinery]
tags: [design, retrieval, taxonomy, ingestion, source_type]
recall_type: meta
references_events:
  - handoffs/001-a7-anchor-variant-fix-episodic-axis.md
  - handoffs/002-f5-episodic-s1-schema-source-type-design.md
date: 2026-05-04
---

# source_type taxonomy — design plan

## Why this exists

MyAPI keeps hitting a recurring failure mode: **meta-commentary outranks the actual artifact.** F5 was pinned to a Trust-Threshold plan (meta) when the gold-mine moment lived in a claude-web thread (episodic). A1's status anchor edges out the project anchor. H4's plan ranks above the conversation that prompted it. Every time we patch this with a one-line bank or anchor tweak — we're treating a symptom.

The root cause: **embeddings reward surface similarity to the query.** Meta-docs repeat the query's exact vocabulary ("the X does Y, the X needs Z"); episodic artifacts use domain forms (transcripts, function signatures, structured fields) that look nothing like a natural-language question. Commentary wins on similarity even when it's the wrong answer.

This is the standard-RAG **#1 lever**: tag at ingestion, filter/weight at query. The system stays dumb; the corpus declares its own nature.

## What we're not doing

- Not adding a cross-encoder reranker (#3 — separate, larger architectural lift; revisit after #1 produces measurable wins).
- Not adopting HyDE (#4 — premature without eval cases).
- Not adopting full query routing into sub-indices (#5 — partial via existing `QueryClassification`; can extend after #1).
- Not inventing new frontmatter where folder structure can carry the signal. The corpus already has a free taxonomy in its directory layout.

## The proposal

### Stamp every doc with `source_type` at ingestion

Add a `source_type` field to the corpus document schema, derived from the canonical path the doc lives under.

```
folder pattern                                            → source_type
─────────────────────────────────────────────────────────────────────────
**/source-of-truth-anchors/**                             → anchor
**/handoffs/**                                            → handoff
**/Daily/**                                               → daily_note
**/_chats/**, **/chatgpt/**, **/claude-web/**             → conversation
**/claude-code-sessions/**                                → cli_session
**/codex-sessions/**                                      → cli_session
**/_code/**, **/repos/**/*.{py,ts,go,rs,md}               → code (tighten later)
**/project-docs/** (excluding handoffs, anchors)          → spec
**/4.*.daily.project.md                                   → daily_note
(everything else)                                          → note
```

`source_type` is computed by the ingestion adapter (Khoj-side or pre-PATCH) from the file's path and stamped into the doc's metadata. No content inspection.

### Wire intent → source_type weights at query time

Existing `QueryClassification.intent` already produces categories like `factual`, `project_overview`, `operational`, `temporal`, `synthesis`. Define a weight matrix (rough sketch — tune empirically):

```
intent              → boost                  | downweight
─────────────────────────────────────────────────────────────────
factual             → anchor 1.5, code 1.5   | conversation 0.5
project_overview    → anchor 1.7, spec 1.2   | cli_session 0.6
operational         → anchor 1.4, handoff 1.3| daily_note 0.7
temporal            → daily_note 1.5,        | anchor 0.7
                      cli_session 1.4,
                      conversation 1.4
source_specific     → (use sources filter)   | (n/a)
synthesis           → anchor 1.3, spec 1.3   | (none)
decision            → handoff 1.4,           | anchor 0.8
                      conversation 1.3
meta                → handoff 1.5, spec 1.3  | code 0.5
```

Applied in `ResultReranker` as a multiplicative bias on `final_score`, after the existing keyword-density and specialized-anchor bonuses. This is the same shape as the current `_specialized_anchor_bonus` — extends the pattern rather than replacing it.

### Backfill stance

**Forward-only is acceptable.** New docs ingested with stamps; existing 1791 docs get stamps lazily on next re-index. No big migration needed — the path-derivation rule is deterministic, so a one-time pass over the corpus produces stable stamps.

### Sequencing

1. **Define the path → source_type mapping** as a single function (Python, in `context_refinery/`). Unit tests for each pattern. **First commit.**
2. **Plumb `source_type` through the ingestion path** — Khoj adapter writes it to doc metadata. **Second commit.**
3. **Backfill the existing corpus** — one-shot script that re-stamps everything in place. Re-index. **Third commit.**
4. **Define the intent → weight matrix** as a config (YAML or Python dict). **Fourth commit.**
5. **Apply weights in `ResultReranker`** — multiplicative bias post existing bonuses. **Fifth commit.**
6. **Re-run acceptance harness** — measure: A1 should resolve cleanly (project_overview intent + anchor boost should cleanly pick obsidian-myapi-anchor over status anchor), F5 should hold (episodic source still wins), S1 holds, A3/H4/A7/H1 should hold or improve.
7. **Add new bank entries** that exercise meta-vs-episodic explicitly — e.g., a query designed to require an episodic answer where the meta-doc is also present. This is where #1 starts producing trust-bench wins.

### Followups (downstream of this plan)

- **`references_events: [...]` frontmatter on meta-docs** — declares lineage to source episodic threads. Once `source_type=anchor|spec|handoff` is set, retrieval can offer referenced events alongside the meta-doc.
- **Cross-encoder rerank (#3)** — once `source_type` weights have a measurable baseline, add a cross-encoder pass over the top 20-50. The combination should make the "is this the answer or someone discussing the answer" judgment robust.
- **Eval bank category: episodic precision** — gold doc must be the originating event-doc, not the retrospective summary. Exposes meta-doc bias quantitatively.

## Open design questions

- **Where does `source_type` live?** Khoj-side metadata (so retrieval has it on hit) or MyAPI-side enrichment (so we can iterate without Khoj reindex)? Probably both — Khoj for cheap surfacing, MyAPI for richer transformation.
- **How do hybrid docs get classified?** A claude-code transcript that includes meta-commentary blocks: stamp as `cli_session` (path wins) and let the reranker handle nuance? Or split-and-classify? Default: path wins; revisit if it bites.
- **Does code need its own family?** Code-as-corpus is a different beast from notes-as-corpus. Maybe out of scope for now (MyAPI is notes-first); revisit when code enters the corpus seriously.
- **Stability of folder structure.** The mapping is only as good as the layout. If folders churn, the mapping churns. Worth pinning a "corpus directory contract" doc at the same time as this rolls out.
