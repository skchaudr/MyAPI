> **Git durable copy** of `VM read-me-first`.
> **VM root reflection (preferred on host):** `/home/sab-mini/00-*.md`
> Keep root + this file in sync when either changes.

# khoj-38 — READ ME FIRST (VM root reflection)

**Host:** `khoj-38` · Tailscale `100.75.255.75` · operator user **`sab-mini`** (not `saboor`)  
**Updated:** 2026-08-08  

This home root is the **machine face**. Agents that land here should not need to open a project repo just to learn *who does what* and *what is broken*.

---

## Two concurrent Grok sessions (lanes)

| Lane | Owns | Does **not** own |
|------|------|------------------|
| **A — Project / corpus** | What goes *into* Khoj: corpus truth, project goals, golden briefs, retrieval quality, anchors, cold-start prove path, Semantic Graphify intent → nodes → GDDP | Dockerizing Khoj, Mini engine deploy, systemd/unit surgery as primary work |
| **B — Engine / machinery** | Khoj process upkeep, portability, `deploy/khoj-engine/`, Mini runbook, compose, dump/restore | Product intent grilling, query-bank goldens, brief composition content |

**Assignment (2026-08-08):**

| Lane | Session | Root claim file |
|------|---------|-----------------|
| **A Project** | This / project Grok — claim: `00-PROJECT-LANE.md` | *you are here for corpus & quality* |
| **B Engine** | Other Grok — claim: see `00-ENGINE-LANE.md` if present, else `MyAPI/deploy/khoj-engine/` + `001-MyAPI-VM-Situated` §7–8 | *you are here for portable runtime* |

Shared ground truth (long form): **`~/001-MyAPI-VM-Situated.md`** → `MyAPI/handoffs/001-MyAPI-VM-Situated.md`

Cross-machine durability failure + aa-cli / MyAPI wayfinder spine: **`/home/saboor/002-Sab-Air-Sab-Mini-VM-handshake.md`** and MyAPI `handoffs/012-…` (git).

---

## Live stack (smoke)

```bash
curl -sS http://127.0.0.1:42110/api/health
curl -sS http://127.0.0.1:8000/health
curl -sS -X POST http://127.0.0.1:8000/query \
  -H 'Content-Type: application/json' \
  -d '{"q":"What is MyAPI?","n":3}'
```

| Service | Port | Role |
|---------|------|------|
| Khoj | `42110` | Search engine / index |
| Context Refinery (MyAPI) | `8000` | `/query`, briefs, hybrid retrieval |
| Postgres | `5432` | Khoj vectors + metadata |

**Quality reality (project lane):** connectivity is green; **index is thin and ranking is weak**. Do not declare cold-start “working” from health alone.

---

## Paths that matter

| Path | What |
|------|------|
| `/home/sab-mini/MyAPI` | **Agent working tree** (prefer this) |
| `/data/repos/MyAPI` | Systemd **venv** tree — may diverge; Lane B / ops care |
| `/home/sab-mini/khoj-data/notes` | Bulk notes on disk (~3.3k md) |
| `/data/corpus-hot/` | Lean hot pack + smoke questions |
| `/home/sab-mini/work/state/khoj-goldens/` | Golden smoke results (host-local; copy into git when keep-worthy) |
| `/data/corpus-gens/snapshots/` | PG restore archives |
| `MyAPI/.scratch/semantic-graphify-cold-start/` | Wayfinder → node map pack (product intent) |

**Footgun:** dual MyAPI clones. Edit under `/home/sab-mini/MyAPI` unless you know the unit points elsewhere.

---

## Durability rule (VM)

If the VM sleeps overnight, **only git remotes and what Mini already has survive.**

- Keep-worthy project work → **commit + push** same session (`MyAPI` `AGENTS.md` durable-work rule).
- Engine work → same; leave compose/runbooks in `deploy/` and push.
- Host-only goldens under `~/work/state/` are **not** a backup until copied into the repo or SCP’d to Mini.

---

## Continue on Mini if this box dies

1. Pull `MyAPI` (`feat/corpus-v1-normalization` + any docs branches with packs).
2. Read: `handoffs/001-MyAPI-VM-Situated.md`, `handoffs/013-project-lane-claim.md` (if present), `.scratch/semantic-graphify-cold-start/CANONICAL-INTENT…`.
3. Lane B starts Khoj engine (native or `deploy/khoj-engine`).
4. Lane A rebinds corpus, reindexes, re-runs goldens / eight must-questions.

---

## Root file index

| File | Purpose |
|------|---------|
| `00-READ-ME-FIRST.md` | This file — dual lanes + smoke |
| `00-PROJECT-LANE.md` | Lane A claim + project status |
| `00-ENGINE-LANE.md` | Lane B claim (other Grok writes/maintains) |
| `001-MyAPI-VM-Situated.md` | Full situated handoff (symlink into repo) |
| `VM-PREP-STATUS.md` | Older prep baseline |
| `sab-dev-to-khoj-38-migration-note.md` | Session migration IDs |
| `00-GROK-SESSION.md` | Older session ID pin (agents-home) |
