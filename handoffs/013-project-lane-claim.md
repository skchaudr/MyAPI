> **Git durable copy** of `Lane A project claim`.
> **VM root reflection (preferred on host):** `/home/sab-mini/00-*.md`
> Keep root + this file in sync when either changes.

# Lane A — Project / corpus (this Grok)

**Host:** `khoj-38` · **User:** `sab-mini`  
**Updated:** 2026-08-08  
**Lane:** A — what goes *into* Khoj and whether retrieval serves the product  
**Peer:** Lane B (other Grok) — engine upkeep + Mini portability · see `00-ENGINE-LANE.md` / `deploy/khoj-engine/`

**Session (historical origin of this thread):** `019fc25b-bded-7c61-92c7-3cd002a7bfc2`  
(cwd was aa-cli; **product work is MyAPI + corpus**. Resume by ID if needed; do not re-wayfinder aa-cli verify unless asked.)

---

## Mission (one line)

Make **corpus + project goals + golden briefs + retrievals + embeddings-backed search** honest and Mini-continuable so an agent cold-start over MyAPI works — independent of which box runs Khoj.

North star (locked): **Semantic Graphify cold-start** — 30–90s orientation via **two MCP tools + `/query`**, meaning not AST. Prove on MyAPI first.

```text
wayfinder → node map → human promote → GDDP / factory-droid execute
```

Canonical intent:  
`/home/sab-mini/MyAPI/.scratch/semantic-graphify-cold-start/CANONICAL-INTENT-FOR-MISSION-PLANNING.md`

---

## Owns / does not own

| Owns (Lane A) | Hand to Lane B |
|---------------|----------------|
| Corpus layout truth (what should be indexed) | Khoj systemd / Docker / compose |
| Anchors, golden briefs, smoke questions, query bank | Postgres install, pgvector image |
| Reindex *content* decisions (what files, denylist) | Making engine start on Mini |
| `/query` quality, hybrid ranking, brief composition | Port conflicts, unit files as primary |
| Cold-start N2–N6 product surfaces (contract, briefs, MCP, prove) | N1 “surface online” machinery half |
| Commit/push of product packs so Mini can pull | Secrets in `/etc/khoj.env` |

**N1 split:** “rebuild surface online” needs **both** — B makes engine portable; A ensures goldens + packs + env contract live on one tip agents can pull.

---

## Current ground truth (project side)

### Working tree

| Item | Value |
|------|--------|
| Prefer | `/home/sab-mini/MyAPI` |
| Branch | `feat/corpus-v1-normalization` |
| Tip (at last write) | check `git log -1` — semantic pack committed in `8d32200` era |
| Remote | `origin` → `github.com/skchaudr/MyAPI` |

Also exists (do not confuse):

- `/home/saboor/MyAPI` — alternate home; docs branch with handshake `012`
- `/data/repos/MyAPI` — **running venv** tree (`feat/claude-web-adapter`) — may diverge from sab-mini edits

### Live quality (2026-08-08 sample)

| Check | Result |
|-------|--------|
| Khoj health `:42110` | green |
| MyAPI health `:8000` | green, Vertex ADC, `khoj_url=localhost:42110` |
| Khoj `database_entry` count | **very thin** (~tens–low hundreds; far below ~3.3k notes on disk) |
| Sample `/query` “What is MyAPI?” | **weak** — low-signal / template-ish hits, not project anchors |
| Wave-1 goldens (2026-07-30) | **7/8 HIT** on Khoj search with corpus-hot-v1 filenames — **host-local** under `~/work/state/khoj-goldens/` |

Connectivity ≠ product. **Lane A job is quality + corpus truth.**

### Corpus layers

| Layer | Path | Role |
|-------|------|------|
| Bulk notes | `~/khoj-data/notes` (~3.3k md) | Full personal dump; competes in ranking if fully indexed |
| Hot pack | `/data/corpus-hot/v1`, `v1-notes` | Lean product slice + smoke |
| Smoke questions | `/data/corpus-hot/smoke-questions.txt` | 8 cold-start-ish questions |
| Goldens | `~/work/state/khoj-goldens/` | Results — **push copies into repo when keep-worthy** |
| Intent pack | `MyAPI/.scratch/semantic-graphify-cold-start/` | Wayfinder tickets, NODE-MAP N1–N6, draft YAML |

### Product node spine (A executes content; B enables runtime)

1. N1 surface online (shared)  
2. N2 `/query` agent contract  
3. N3 project context brief  
4. N4 person context brief  
5. N5 MCP two tools live  
6. N6 prove eight must-questions  

---

## If VM dies overnight → continue on Mini (Lane A checklist)

1. **Pull MyAPI** on Mini:
   ```bash
   cd ~/repos/MyAPI   # or sab-mini path
   git fetch origin
   git checkout feat/corpus-v1-normalization
   git pull
   ```
2. Read:
   - `handoffs/001-MyAPI-VM-Situated.md`
   - `handoffs/013-project-lane-claim.md`
   - `.scratch/semantic-graphify-cold-start/CANONICAL-INTENT-FOR-MISSION-PLANNING.md`
   - `.scratch/semantic-graphify-cold-start/NODE-MAP.md`
3. Wait for / coordinate with **Lane B** so Khoj is up (native or docker).
4. Rebind notes path + reindex **high-signal set first** (anchors, corpus-hot, status docs) before full dump.
5. Re-run smoke questions → write new golden under repo `project-docs/` or `handoffs/` (not only `~/work/state`).
6. Prove A1 / identity-class and A7 / broken-blocked-class with evidence paths.
7. Do **not** re-grill locked cold-start intent unless product cut fails in practice.

---

## Near-term Lane A queue (ordered)

1. **Single tip discipline** — prefer `/home/sab-mini/MyAPI`; do not silently edit `/data/repos/MyAPI` API without sync plan.
2. **Corpus truth decision** — document active index set: lean hot pack vs full notes vs staged hybrid; fix denylist.
3. **High-signal reindex** — get anchors + corpus-hot-v1 + status docs into live Khoj entries; measure entry count + golden HIT rate.
4. **Durable goldens** — copy latest smoke results into MyAPI git; push.
5. **Agent `/query` contract** — short doc + examples (`q`, `n`) agents can paste (N2).
6. **Briefs** — project + person orientation payloads (N3–N4) with honest empty/weak.
7. **Eight must-questions prove** (N6) with receipts — definition of v1 done.
8. **Mini continuation test** — after a push, confirm Mini can pull packs without this disk.

**Leave alone (Lane B):** `deploy/khoj-engine/*` authorship, docker compose health on Mini, postgres container — coordinate only.

---

## Anti-patterns

- Declaring success from `/health` alone  
- Re-wayfinding cold-start from zero (intent is captured)  
- Leaving goldens only under `~/work/state/`  
- Editing the wrong MyAPI clone and assuming systemd serves it  
- Stealing engine/container work from the other session  

---

## Pointers

| Doc | Why |
|-----|-----|
| `~/00-READ-ME-FIRST.md` | Machine face |
| `~/001-MyAPI-VM-Situated.md` | Full VM situated state |
| `MyAPI/handoffs/013-project-lane-claim.md` | Git-durable copy of this claim |
| `MyAPI/project-docs/STATUS_AND_NEXT_STEPS.md` | Older trust-bank queue (May) — useful, may lag |
| `MyAPI/project-docs/source-of-truth-anchors/` | Anchor set for ranking |
| `/data/corpus-hot/smoke-questions.txt` | Live smoke list |
