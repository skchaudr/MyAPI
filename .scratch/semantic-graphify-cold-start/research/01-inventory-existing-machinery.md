# 01 — Inventory of existing machinery (cold-start path)

**Ticket:** wayfinder `01-inventory-existing-machinery`  
**Date:** 2026-08-04  
**Scope:** read-only inventory for thin v1 semantic-graphify cold-start assembly  
**Not done:** product decisions, map.md edits, ticket resolve  

---

## 1. Host / clone inventory

| Path | Host role (inferred) | Checked-out branch | Tip SHA (short) | Notes |
|------|----------------------|--------------------|-----------------|-------|
| `/home/saboor/MyAPI` | primary worktree on this host (saboor home) | `feat/corpus-v1-normalization` | `bf7ad76` | Matches `origin/feat/corpus-v1-normalization` on this clone. Wayfinder map lives under `.scratch/semantic-graphify-cold-start/`. |
| `/home/saboor/repos/MyAPI` | second clone (older tip) | `feat/corpus-v1-normalization` | `f5c6506` | Also has local `main` @ `e65a436`. Handoffs stop at `008`. Missing later corpus vault docs present on saboor/MyAPI. |
| `/home/sab-mini/MyAPI` | mini-named path on same Linux host | `feat/corpus-v1-normalization` | `88a17ff` | Mid-rebase per `COMMIT_EDITMSG`. Has extras: `api/observability.py`, `scripts/daily_corpus_to_khoj.py`, handoff `012`, more vault scripts. **Not** the Mac path `/Users/sab-mini/repos/MyAPI`. |
| `/home/sab-mini/repos/MyAPI` | claimed by corpus-hot harvest | — | — | **Absent** on this host (`list_dir` fails). Harvest paths are Mac mini (`/Users/sab-mini/repos/MyAPI`). |
| `https://github.com/skchaudr/MyAPI` `main` | remote product tip | `main` | `5740b3c` (2026-08-03) | **Has** PROJECT-BRIEF, IMPLEMENTATION-PLAN, `mcp/`, `evals/golden_briefs/`, `myapi-db-plan.md`, `gddp/`, `graphify-out/`, `.handoffs/`. Local clones’ `origin/main` is **stale** at `e65a436`. |
| corpus-hot claim: mini `main` @ `b56e47a` | Mac mini (2026-07-29 harvest) | `main` | `b56e47a` (claimed) | Documented in `/home/saboor/khoj-data/notes/corpus-hot-v1/myapi/SOURCES.md`; not verified as a local clone here. GitHub tip has since moved past that SHA. |

**Evidence:**  
- Branch tips: `/home/saboor/MyAPI/.git/HEAD`, `…/refs/heads/feat/corpus-v1-normalization`; same pattern under `/home/saboor/repos/MyAPI`, `/home/sab-mini/MyAPI`.  
- Remote main lag: `/home/saboor/MyAPI/.git/refs/remotes/origin/main` = `e65a436…` vs GitHub API `commits/main` = `5740b3c…`.  
- Missing Mac path: list of `/home/sab-mini/repos` → does not exist.  
- GitHub tree: `GET https://api.github.com/repos/skchaudr/MyAPI/contents/?ref=main` lists `PROJECT-BRIEF.md`, `IMPLEMENTATION-PLAN.md`, `mcp/`, `evals/`, `gddp/`, `graphify-out/`, `myapi-db-plan.md`, `.handoffs/`.

### Key-file presence matrix (working trees vs main tip)

| Artifact | saboor/MyAPI (feat tip) | saboor/repos/MyAPI | sab-mini/MyAPI | GitHub `main` | corpus-hot (mini harvest) |
|----------|-------------------------|--------------------|----------------|---------------|---------------------------|
| `api/routers/query.py` + `context_refinery/retrieval.py` | **present** | **present** | **present** | present | assumed |
| adapters (`chatgpt`, `claude`, `claude_code`, `codex`, `obsidian`, `pdf_extractor`) | **present** | **present** | **present** | present | assumed |
| `project-docs/source-of-truth-anchors/` (4 anchors) | **present** | **present** | **present** | present | assumed |
| `project-docs/retrieval-benchmark-v0/` | **present** | **present** | **present** | present | assumed |
| `handoffs/` (000–011) | **000–011** | **000–008** | **000–012** | — | — |
| `.handoffs/` (rebuild series incl. 029) | **absent** | **absent** | **absent** | **present** | claimed on mini |
| `PROJECT-BRIEF.md` | **absent** | **absent** | **absent** | **present** | claimed `/Users/sab-mini/repos/MyAPI/` |
| `IMPLEMENTATION-PLAN.md` | **absent** | **absent** | **absent** | **present** | claimed |
| `myapi-db-plan.md` | **absent** | **absent** | **absent** | **present** | claimed |
| `mcp/` (`server.py`, README) | **absent** | **absent** | **absent** | **present** (fixture-backed) | claimed |
| `evals/golden_briefs/` (3 files) | **absent** | **absent** | **absent** | **present** | claimed |
| `graphify-out/` | **absent** (gitignored) | **absent** | **absent** | **present** (tracked artifacts) | claimed on mini/air |
| `gddp/` in MyAPI repo | **absent** | **absent** | **absent** | **present** | claimed |
| `Corpus v1.0/` tree | **absent** (`corpus_v1/` gitignored empty) | **absent** | **absent** | not at repo root on API listing | claimed on mini + air vault |
| `deploy_to_brain.sh` / `deploy_to_khoj.sh` | **present** | **present** | **present** | present | assumed |
| `scripts/daily_corpus_to_khoj.py` | **absent** | **absent** | **present** | — | — |
| `scripts/acceptance.py` / `run_query_benchmark.py` | **present** | **present** | **present** | present | assumed |
| corpus-hot pack `…/myapi/{SOURCES,QUERIES,BRIEF-DRAFT,GAPS}.md` | n/a | n/a | n/a | n/a | **present** under `/home/saboor/khoj-data/notes/corpus-hot-v1/myapi/` |
| GDDP myapi graph (portfolio) | n/a | n/a | **present** at `/home/sab-mini/gddp-config/graphs/myapi/` | MyAPI-repo `gddp/` also on main | — |
| wayfinder cold-start map | **present** `.scratch/semantic-graphify-cold-start/` | absent | absent | absent | n/a |

---

## 2. Capability inventory

Legend: **live** = code/docs on disk runnable or already used · **planned** = docs/nodes only · **fixture-only** = golden/fixture path without live retrieval · **absent-here** = exists on other host/branch only.

### 2.1 `/query` API (Context Refinery)

| Aspect | Status | Evidence |
|--------|--------|----------|
| FastAPI app + `/query` router | **live (code)** on all three clones | `/home/saboor/MyAPI/api/main.py` includes `query.router`; `/home/saboor/MyAPI/api/routers/query.py` posts to `RetrievalPipeline` |
| Retrieval pipeline (classify / hybrid / filter / rerank) | **live (code)** | `/home/saboor/MyAPI/context_refinery/retrieval.py` — `KhojClient`, `KeywordSearcher`, `QueryClassifier`, etc.; unit tests in `tests/test_retrieval.py` |
| Khoj dependency | **live code, runtime remote** | Default `KHOJ_URL` `http://100.107.147.16:42110` in `retrieval.py`; `/health` reports `khoj_url` from env |
| Deps | **live** | `/home/saboor/MyAPI/requirements.txt` — fastapi, uvicorn, google-genai, pytest, … |
| Whether `/query` is up on this host right now | **not verified** (no live curl this pass) | Deploy docs say VM + Tailscale; VM auto-shutdown noted in anchors |

### 2.2 Khoj + deploy path

| Aspect | Status | Evidence |
|--------|--------|----------|
| Deploy scripts | **live scripts** | `/home/saboor/MyAPI/deploy_to_brain.sh` (rsync to `100.107.147.16`, PUT index); `deploy_to_khoj.sh` (bundle → `~/khoj-data/ai-exports`, IP placeholder) |
| Daily hot allowlist → Khoj | **live script on sab-mini clone only** | `/home/sab-mini/MyAPI/scripts/daily_corpus_to_khoj.py` — allowlist + `git show main:…` for missing tip docs |
| Local corpus on this host | **partial live substrate** | `/home/saboor/khoj-data/notes/` ~3290 markdown files; `ai-exports/` empty dir; includes corpus-hot pack under `notes/corpus-hot-v1/` |
| Indexing / reindex tooling | **live scripts** | `scripts/reindex_khoj_safe.py`, `khoj_index_diff.py`, `khoj_repair_index_delta.py`, `khoj_reindex_resume_index.py` |
| Documented VM topology | **planned/ops docs (may be stale IPs)** | Anchors + `STATUS_AND_NEXT_STEPS.md` cite ports `42110` (Khoj), `8000` (refinery); multiple Tailscale IPs appear across docs (`100.107…`, `100.85…`, `100.88…` in daily script) — treat as **needs recon**, not single truth |

### 2.3 Adapters

| Adapter | Path | Status |
|---------|------|--------|
| ChatGPT | `context_refinery/adapters/chatgpt.py` | **live code** + `tests/test_chatgpt.py` |
| Claude web | `context_refinery/adapters/claude.py` | **live code** |
| Claude Code | `context_refinery/adapters/claude_code.py` | **live code** + tests |
| Codex | `context_refinery/adapters/codex.py` | **live code** + tests |
| Obsidian | `context_refinery/adapters/obsidian.py` | **live code** + tests |
| PDF | `context_refinery/adapters/pdf_extractor.py` | **live code** |
| Enrich / import / export routers | `api/routers/{enrich,imports,export}.py` | **live code** (export retired in main.py comment) |
| Normalization / vault builders | `normalization_schema.py`, `scripts/normalize_corpus.py`, `build_vault_v1.py` | **live code**; vault plan marks execution “do not run until reviewed” in places |

### 2.4 Anchors (cold-start-shaped SOTA notes)

| File | Status | Role |
|------|--------|------|
| `project-docs/source-of-truth-anchors/myapi-status-anchor.md` | **live doc** (last updated 2026-05-03 in body) | Agent “what’s broken” cold-start; A7 target |
| `…/my-devinfra-system-anchor.md` | **live doc** | Project overview / system identity |
| `…/khoj-deployment-indexing-anchor.md` | **live doc** | Khoj + `/query` topology |
| `…/vm-tailscale-ssh-access-anchor.md` | **live doc** | Access path |
| Template | `project-docs/templates/source-of-truth-anchor.md` | **live template** |

Anchors are **corpus/authoring artifacts**, not a separate runtime. They become useful when indexed into Khoj and hit by `/query`.

### 2.5 Benchmark bank

| Piece | Status | Evidence |
|-------|--------|----------|
| v0 query list (18) | **live** | `project-docs/retrieval-benchmark-v0/Query/benchmark-v0.md` |
| v1 refinement target | **live (copy of v0 shape)** | `…/Query/benchmark-v1.md` |
| Trust-categorized bank file | **deleted / absent** on feat tree | Handed off as deleted in `handoffs/003-final-v0-benchmark-run.md`; still *referenced* by `scripts/acceptance.py` and older status docs |
| Harness run notes | **live historical** | `…/Harness evaluation/run-2026-04-*.md` through `run-2026-05-02-tighten-pass.md` |
| Mechanical acceptance | **live script** | `scripts/acceptance.py` (hits `:8080` by default; gold file names for A1/A3/A7 etc.) |
| Comparative / query runners | **live scripts** | `scripts/run_query_benchmark.py`, `scratch/run_comparative_benchmark.py` |
| eval-bank-v0 (wave1 / corpus-hot) | **on GitHub main only** (this host) | `evals/eval-bank-v0.md` @ main tip commit `5740b3c` |
| corpus-hot QUERIES | **live notes** | `/home/saboor/khoj-data/notes/corpus-hot-v1/myapi/QUERIES.md` |

### 2.6 MCP tools

| Piece | Status | Evidence |
|-------|--------|----------|
| `mcp/server.py` two tools | **fixture-only on `main`**; **absent-here** on feat checkouts | GitHub raw `mcp/server.py`: `get_project_context` / `get_person_context` read `evals/golden_briefs/*.md`; raises if missing |
| `mcp/README.md` | **planned + fixture contract** | Explicit: “fixture-backed … until the reader and MCP server wrapper are ready”; MyAPI = engine, MyMCP = doorway |
| Live MCP transport / agent wiring | **planned / not proven here** | README + GAPS say runtime wiring out of scope for harvest; GDDP node `serve-context-via-mcp` status **pending** |

### 2.7 Golden briefs

| File (on `main`) | Status |
|------------------|--------|
| `evals/golden_briefs/get_project_context_myapi_rebuild.md` | **fixture-only** (expected ContextBrief shape) |
| `evals/golden_briefs/get_project_context_pi_needle.md` | **fixture-only** |
| `evals/golden_briefs/get_person_context_sab.md` | **fixture-only** |

Local feat trees: **absent**. Referenced by `daily_corpus_to_khoj.py` `git_export_main_tips()` for staging from `main:`.

### 2.8 Corpus substrate

| Layer | Status | Evidence |
|-------|--------|----------|
| Indexed notes blob on this host | **live partial** | `/home/saboor/khoj-data/notes/` large chatgpt/obsidian-style dump + corpus-hot packs |
| Corpus v1.0 PARA vault | **absent-here** (code plans only) | Plans in `project-docs/corpus-v1-vault-v1.0-implementation-plan.md`, `build_vault_v1.py`; harvest claims mini/air trees; `corpus_v1/` gitignored, empty of content in search |
| Active hot window policy (15–30d) | **planned** | PROJECT-BRIEF (main), `myapi-db-plan.md`, gddp-config `project.yaml` |
| Normalization readiness / architecture docs | **live planning** on feat | `project-docs/corpus-v1-*.md`, handoffs 004–011 |
| corpus-hot v1 merged pack | **live harvest product** | `/home/saboor/khoj-data/notes/corpus-hot-v1/{myapi,gddp,pi-needle-gemma}/` + raw-air/raw-mini; README says host-of-record sab-mini path (Mac) |

### 2.9 Plans / GDDP / Graphify adjacency

| Piece | Status | Evidence |
|-------|--------|----------|
| PROJECT-BRIEF / IMPLEMENTATION-PLAN | **on main only** (docs) | L0–L4 stack; MCP as L3; “planning / docs only — 0 implementation code” for rebuild narrative (brief) while v0 refinery remains real code |
| myapi-db-plan.md | **on main only** | Six-node execution graph; supersedes `prove-first-durable-handoff`; prove retrieval before MCP |
| MyAPI-repo `gddp/` | **on main only** | Directory listed on GitHub main |
| Portfolio GDDP myapi graph | **live YAML (pending nodes)** | `/home/sab-mini/gddp-config/graphs/myapi/project.yaml` + 6 nodes; `serve-context-via-mcp` / `prove-myapi-context-retrieval` **pending** |
| graphify-out (MyAPI) | **on main (tracked)**; **absent** on local feat trees | GitHub: `graph.json`, `.graphify_analysis.json`; feat `.gitignore` ignores `graphify-out/` |
| Graphify skills (operator) | **live skills on mini home** | `/home/sab-mini/agents-home/skills/graphify/`, `graphify-query/` — AST/code graph query, not personal memory |
| Wayfinder cold-start map | **live local tracker** | `/home/saboor/MyAPI/.scratch/semantic-graphify-cold-start/map.md` + 8 issue stubs |

### 2.10 Durable handoffs

| Series | Location | Status |
|--------|----------|--------|
| Product handoffs 000–011/012 | `handoffs/*.md` on feat clones | **live narrative** of retrieval + corpus-v1 work (May–Jun 2026 era) |
| Rebuild `.handoffs/` incl. 029 GDDP | on GitHub `main` only | **absent-here**; harvest: `029-gddp-first-durable-handoff-node.md` |

---

## 3. Thin-path candidates (glue existing pieces; no rebuild)

These are **assembly options**, not decisions.

### Path A — Fixture MCP cold-start (zero Khoj)

1. Checkout or `git show` GitHub `main` into a worktree (or fetch on this host — current `origin/main` is stale).  
2. Run `mcp/server.py` functions / wrap with MCP transport against `evals/golden_briefs/*`.  
3. Agent cold-start for **MyAPI-rebuild** and **Sab person** is deterministic fixture prose.

**Pros:** works offline; proves agent UX and ContextBrief shape.  
**Cons:** not retrieval; fixture staleness (golden cites older rebuild paths).  
**Pieces:** `mcp/server.py`, golden briefs, PROJECT-BRIEF.

### Path B — Live `/query` + anchors + benchmark bank (v0 engine)

1. Start VM/Khoj if needed; point `KHOJ_URL` at live index (`retrieval.py` / deploy scripts).  
2. Run `uvicorn api.main:app` from any clone with refinery code.  
3. Cold-start via POST `/query` with bank queries / status-anchor questions (`scripts/acceptance.py`, `run_query_benchmark.py`).  
4. Optionally stage tip docs via `daily_corpus_to_khoj.py`’s `git_export_main_tips()` once `main` is fetchable.

**Pros:** real hybrid retrieval already built and harnessed.  
**Cons:** VM/index freshness unknown; feat tree lacks rebuild MCP brief shape; volume-bias failure mode documented.  
**Pieces:** `api/`, `context_refinery/retrieval.py`, anchors, `khoj-data/notes`, deploy scripts.

### Path C — Corpus-hot wave1 pack as lean orientation substrate

1. Use `/home/saboor/khoj-data/notes/corpus-hot-v1/myapi/{BRIEF-DRAFT,SOURCES,QUERIES,GAPS}.md` (+ gddp, pi packs) as the **only** high-signal docs for cold-start.  
2. Index that pack into a lean Khoj slice (eval-bank-v0 on main references wave1 `:42111` vs archive `:42110` — **ops claim**, verify before relying).  
3. Score with `evals/eval-bank-v0.md` rows M01–M10 once main is present.

**Pros:** already harvested; denylist-aware; matches “thin hot window” narrative.  
**Cons:** not full agent-session substrate; graphify rows marked needs-refresh; IP/port dual Khoj is unproven here.  
**Pieces:** corpus-hot tree, DENYLIST, eval-bank-v0 (main), optional daily_corpus allowlist.

### Path D — MCP over `/query` (thinnest “product” glue)

1. Take fixture MCP tool names/contracts from `main:mcp/`.  
2. Replace fixture body with a thin adapter: tool call → `POST /query` (or brief-assembly stub wrapping top-k + anchor bias) → map into ContextBrief-ish fields (short answer, evidence paths, freshness placeholder).  
3. Gate with golden briefs as structural eval (sections present), not string match — as IMPLEMENTATION-PLAN Phase 4 describes.

**Pros:** reuses live engine + names agents expect; matches GDDP node order (prove retrieval → serve MCP).  
**Cons:** brief assembly not implemented; ownership of “MyMCP vs MyAPI” still open (wayfinder issue 08).  
**Pieces:** mcp fixtures + `/query` + anchors + golden structure + `myapi-db-plan.md` node 4→5.

---

## 4. Explicit gaps on this host

| Gap | Detail |
|-----|--------|
| No checked-out `main` product tip | All three clones on `feat/corpus-v1-normalization`; local `origin/main` ≠ GitHub `main` |
| Missing rebuild surface files | No working-tree `PROJECT-BRIEF.md`, `IMPLEMENTATION-PLAN.md`, `mcp/`, `evals/golden_briefs/`, `myapi-db-plan.md`, `.handoffs/`, in-repo `gddp/` |
| No local `graphify-out/` | gitignored on feat; not generated in working trees; only on GitHub main |
| No `Corpus v1.0/` PARA tree | Plans + builder scripts only; harvest claims Mac mini/air vaults |
| Mac mini canonical clone absent | `/Users/sab-mini/repos/MyAPI` / `/home/sab-mini/repos/MyAPI` not present here |
| Trust-categorized query bank file deleted | Still cited by acceptance + status docs; bank reduced to benchmark-v0/v1 tables |
| Live service proof not run | No confirmation Khoj/refinery up on current Tailscale IPs |
| MCP not retrieval-backed | Fixtures only on main; GDDP `serve-context-via-mcp` pending |
| Clone divergence | saboor/MyAPI `bf7ad76` ≠ sab-mini/MyAPI `88a17ff` (rebase) ≠ repos clone `f5c6506` |
| IP / host drift | Multiple Khoj endpoints across docs vs scripts — not reconciled |

---

## 5. What is “enough” to assemble thin v1 without rebuilding

**Already enough without new platforms:**

1. **Orientation text** — corpus-hot BRIEF/SOURCES + GitHub main PROJECT-BRIEF/IMPLEMENTATION-PLAN/myapi-db-plan (fetch or raw.githubusercontent).  
2. **Agent-facing fixture path** — main `mcp/` + 3 golden briefs.  
3. **Real retrieval path** — feat (or any) tree’s `context_refinery` + `/query` + local `khoj-data/notes` or VM Khoj + anchors + acceptance/benchmark scripts.  
4. **Execution graph** — gddp-config myapi six nodes (mirror of myapi-db-plan).  
5. **Operator graphify (code only)** — skills under agents-home; do not confuse with personal cold-start.

**Must still glue (not rebuild):** fetch current `main` onto this host or worktree; choose Path A vs B vs C vs D; verify Khoj endpoint; optionally wire MCP→`/query`.

---

## 6. Sources cited (paths / commands)

### Filesystem — MyAPI clones
- `/home/saboor/MyAPI/` (tree, `.git/HEAD`, `api/`, `context_refinery/`, `project-docs/`, `handoffs/`, `scripts/`, `deploy_*.sh`, `requirements.txt`, `.scratch/semantic-graphify-cold-start/`)
- `/home/saboor/repos/MyAPI/`
- `/home/sab-mini/MyAPI/` (incl. `scripts/daily_corpus_to_khoj.py`, `api/observability.py`, `handoffs/012-…`)

### Filesystem — adjacent
- `/home/saboor/khoj-data/notes/corpus-hot-v1/` (`README.md`, `DENYLIST.md`, `myapi/{SOURCES,QUERIES,BRIEF-DRAFT,GAPS}.md`, raw-air/raw-mini)
- `/home/saboor/khoj-data/notes/` (bulk notes substrate)
- `/home/sab-mini/gddp-config/graphs/myapi/` (`project.yaml`, `nodes/*.yaml`)
- `/home/sab-mini/agents-home/skills/graphify/`, `graphify-query/`
- `/home/sab-mini/agents-home/maps/machines.md`

### Git refs
- `/home/saboor/MyAPI/.git/refs/heads/feat/corpus-v1-normalization` → `bf7ad76…`
- `/home/saboor/MyAPI/.git/refs/remotes/origin/main` → `e65a436…`
- `/home/saboor/repos/MyAPI/.git/refs/heads/main` → `e65a436…`
- `/home/sab-mini/MyAPI/.git/refs/heads/feat/corpus-v1-normalization` → `88a17ff…`
- Remote URL in clones: `https://github.com/skchaudr/MyAPI.git`

### GitHub (main tip; not local checkout)
- `GET https://api.github.com/repos/skchaudr/MyAPI/commits/main` → `5740b3c` (2026-08-03)
- `GET …/contents/?ref=main` — tree listing
- Raw: `PROJECT-BRIEF.md`, `IMPLEMENTATION-PLAN.md`, `myapi-db-plan.md`, `mcp/README.md`, `mcp/server.py`, `evals/golden_briefs/get_project_context_myapi_rebuild.md`

### Representative local content cites
- `api/routers/query.py` — `POST /query` → `RetrievalPipeline`
- `context_refinery/retrieval.py` — Khoj client default URL
- `project-docs/source-of-truth-anchors/myapi-status-anchor.md` — cold-start status product
- `handoffs/003-final-v0-benchmark-run.md` — trust bank deletion
- `scripts/acceptance.py` — mechanical gold criteria
- `.scratch/semantic-graphify-cold-start/map.md` — destination + clone note
- `.scratch/semantic-graphify-cold-start/issues/01-inventory-existing-machinery.md` — this ticket question

---

## 7. Research constraints honored

- Read-only product tree (only wrote this findings file under `.scratch/…/research/`).  
- No map.md edit, no ticket claim/resolve.  
- No product decision resolution (paths A–D are candidates only).
