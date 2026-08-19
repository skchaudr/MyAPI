# myapi / BRIEF-DRAFT — merged v1

Date: 2026-07-29
Mini = repo/prod bias. Air = vault/operator bias. Both kept as evidence.

---

## From mini

# MyAPI — BRIEF-DRAFT (mini pass-1)

## Short Answer

MyAPI-rebuild is a personal **context engine** rebuilt around durable handoffs and two MCP tools (`get_project_context`, `get_person_context`), not v0’s single RAG pool. MyAPI owns corpus/retrieval/briefs; MyMCP is the lean paid doorway (fixture-backed until reader lands). On mini `main` @ `b56e47a`, work is docs/plan-heavy with `context_refinery/`, golden briefs, and `.handoffs/`; `myapi-db-plan.md` (2026-07-28) is the current six-node execution redirection. Corpus v1.0 remains cold substrate (PARA buckets); active policy is a short hot window + stamped durable material.

## Evidence paths (exist on mini)

1. `/Users/sab-mini/repos/MyAPI/PROJECT-BRIEF.md`
2. `/Users/sab-mini/repos/MyAPI/IMPLEMENTATION-PLAN.md`
3. `/Users/sab-mini/repos/MyAPI/mcp/README.md`
4. `/Users/sab-mini/repos/MyAPI/evals/golden_briefs/get_project_context_myapi_rebuild.md`
5. `/Users/sab-mini/repos/MyAPI/.handoffs/029-gddp-first-durable-handoff-node.md`
6. `/Users/sab-mini/repos/MyAPI/myapi-db-plan.md`
7. `/Users/sab-mini/repos/MyAPI/Corpus v1.0/README.md`

## Operator one-liner

Cold agent: read PROJECT-BRIEF + REBUILD-CONTEXT-ANCHOR (under project-docs) + latest handoff; treat Corpus v1.0 as baseline only.


---

## From air

# MyAPI — BRIEF-DRAFT (air)

## Short Answer
MyAPI-rebuild is Sab’s **personal context engine**: durable handoffs and event traces packaged so agents can continue work without re-litigating origin — surfaced primarily as two MCP tools (`get_project_context`, `get_person_context`) returning **context briefs**, not a single blended RAG pool. Air holds strong **operator narrative** (Obsidian Corpus v1.0 + SSD notes) and a **lagging product clone** (`feat/corpus-v1-normalization`); canon product docs/goldens/MCP/GDDP node live on `main` and need `git show` or mini pull. Vertex/ADC is out of scope for this harvest (done on VM).

## Why it exists
v0 dumped vault + chat exports + CLI sessions into one retrieval pool; volume drowned intent. Rebuild centers **who/what/when/why** of project and operator as first-class, boxable context for agentic workflows.

## Relationships
- Portfolio triptych with **GDDP** (control/graph integrity) and **.pi / Needle** (routing/harness).
- **MyMCP** = lean paid doorway; MyAPI = engine (Khoj/VM, manifests, readers — per main brief).
- First GDDP project node on main: prove durable handoff → golden briefs → reader → MCP.

## Evidence (paths exist on air)
1. `air: ~/Obsidian/Corpus v1.0/README.md` + bucket dirs `00-index` … `90-raw-provenance`
2. `air: ~/Obsidian/SSD/What MyAPI v1 corpous normalization is really becoming.md`
3. `air: ~/repos/MyAPI/handoffs/004-corpus-v1-field-test-realization.md` (and siblings through 012)
4. `air: git -C ~/repos/MyAPI show main:PROJECT-BRIEF.md`
5. `air: git -C ~/repos/MyAPI show main:.handoffs/029-gddp-first-durable-handoff-node.md`

## Risks
- Agents on air that only read working tree will miss main’s plan/goldens/MCP.
- Graphify-out is code-symbol dense; will not answer “what is MyAPI for?” alone.
- Session stores (Claude/Codex) are sparse/legacy-path for MyAPI; vault carries more operator truth.

## Next (for pass 2 / humans)
- Pull or worktree `main` on air before product edits.
- Merge air operator notes + mini repo tip into golden-brief shape.
- Do not reindex Khoj as part of corpus-hot.

