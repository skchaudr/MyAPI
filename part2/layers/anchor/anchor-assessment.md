# Anchor assessment — project-docs/REBUILD-CONTEXT-ANCHOR.md (node-03 deliverable)

Assessed 2026-08-19 on main @ d890c59 against the four evidence-contract
dimensions. Method: per-item verdict with live-state check; no competing
brief minted; anchor content untouched by this assessment (any extension is
separate, dated, additive — see §5).

## Dimension 1 — identity & purpose: ESTABLISHED

| Item | Verdict | Evidence |
|---|---|---|
| Product identity (vault of durable handoffs, briefs via MCP, not v0 RAG pool) | established | Anchor "One sentence" + root AGENTS.md repeat it verbatim in substance; Part 1/Part 2 work order (traces → golden briefs → reader → MCP) matches the anchor's integrated plan step 5 |
| v0 failure diagnosis as negative constraint | established | "The fix is shape, not more data" is consistent with Part 1's staged single-class corpus design (18 files, isolated user) |
| Ascend theme | established | Presentational only; no downstream artifact contradicts it |

## Dimension 2 — major components: PARTIALLY ESTABLISHED (two stale items)

| Item | Verdict | Evidence |
|---|---|---|
| Layer taxonomy (event trace / handoff vault / context brief / meta-handoff) | established | Matches Part 1 stages C–I and Part 2 memo's layer design |
| MCP surface: two tools | established | Root AGENTS.md locks the same two names; anchor's "two, not three names" rule is live doctrine |
| Key paths — repo roles | **STALE** | Anchor: MyAPI-rebuild = rebuild repo, MyAPI = old repo + corpus. Live state inverted: MyAPI/main carries Part 1 results + Part 2 layers (01-decisions … 04-evaluation, part2/, gddp/); MyAPI-rebuild sits on codex/myapi-decision-plan |
| Key paths — graph numbers | **STALE** | Anchor: "862 nodes, 2186 links". Live graphify-out/graph.json: 53,573 nodes / 73,117 links, built_at_commit d82a5ea, 2026-08-08 (measured today; sha256 in part2/layers/graphify/graphify-inventory.md) |
| Key paths — ARCHITECTURE.md location | partially stale | Companion doc exists at project-docs/ARCHITECTURE.md; root AGENTS.md points at project-documents/ARCHITECTURE.md, which does not exist |
| handoffs/000–012 as early instinct | stale-but-harmless | Live .handoffs/ now spans 000–036 (26 files; census in part2/layers/handoffs/handoff-manifest.jsonl) |

## Dimension 3 — stable terminology: ESTABLISHED

| Item | Verdict | Evidence |
|---|---|---|
| Glossary terms (durable handoff, event trace, handoff vault, context brief, corpus, Ascend) | established | Consistent with AGENTS.md, Part 1 stage rooms, Part 2 memo usage |
| LinkedIn/WhatsApp export origin-lock | established | No contradicting usage found in live docs |
| Context Refinery disambiguation (UI vs Python package) | established | context_refinery/ exists as the Python package; no live UI claims |
| get_person_context vs get_user_context/"operator context" | established | AGENTS.md enforces the same lock verbatim |

## Dimension 4 — current orientation: NOT ESTABLISHED as of Part 2 (dated)

| Item | Verdict | Evidence |
|---|---|---|
| Work sequence (traces → golden briefs → reader → MCP) | superseded-in-part | Part 1 (decisions→corpus→Khoj→eval) and Part 2 (source-class experiment) ran a different, evidence-first sequence; AGENTS.md "Phase" section now reflects that |
| "Git: do not ingest commit history into the corpus engine" | **contradicted by live direction** | Part 2's governing memo (gddp-config/docs/GDDPvMyAPI-Part2.md) defines git temporal/change evidence as a first-class source class; node-06 deliverable now lives at part2/layers/git/. The anchor rule predates the Part 2 experiment by ~7 weeks |
| "Graphify: current code structure map only" | tension recorded | Live graph is 96% corpus nodes (51,391 of 53,573 under Corpus v1.0), so it is a corpus map in practice — the anchor's code-only framing no longer describes reality |
| Khoj location | silent | Anchor never mentions Khoj; Part 1 ran it on GCE, and as of 2026-08-18 it runs on the mini (localhost:42110). Not an anchor error — a coverage gap for cold sessions |

## Overall verdict

The anchor ESTABLISHES identity, terminology, and component taxonomy — a cold
agent reading it will not re-litigate origin or fork the MCP names. It does
NOT establish current orientation: two key-path items are stale, one doctrine
(git exclusion) is contradicted by the governing Part 2 memo, and Khoj's move
to the mini is unrecorded. Per node-03's extension rule, §5 below is a dated,
additive extension; no anchor text above it is altered.

## §5 — Dated extension (2026-08-19, additive, Part 2 orientation)

- Active repo is `~/repos/MyAPI` (main); `MyAPI-rebuild` holds the
  codex/myapi-decision-plan branch with the local chat baseline.
- Khoj runs on the mini: `localhost:42110`, local postgres, chat path via
  OpenRouter. Isolated Part 1 corpus user: `gddp-part1@local`.
- Part 2 governs: six source classes under experiment, including git evidence
  (part2/layers/git/) and graphify (part2/layers/graphify/) — this supersedes
  the 2026-06-21 git-exclusion rule for the duration of the experiment.
- Graph: 53,573 nodes / 73,117 links @ d82a5ea (2026-08-08), not 862/2186.
- Layer census pointers: part2/layers/handoffs/handoff-manifest.jsonl,
  part2/layers/git/git-export.jsonl, part2/layers/graphify/graphify-inventory.md.
