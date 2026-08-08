# 001 — MyAPI VM Situated

**Host:** `khoj-38` (GCP VM, Tailscale `100.75.255.75`)  
**Operator user (real projects):** `sab-mini` — **not** `saboor`  
**Written:** 2026-08-08 (UTC)  
**Purpose:** Ground two concurrent Grok agent sessions on the VM. Document live Khoj + MyAPI setup, corpus, work done / remaining, and what it takes to (a) containerize the **Khoj engine** for portability and (b) run the same stack on the **Mac Mini** instead of this VM.

**Also committed in-repo:** `MyAPI/handoffs/001-MyAPI-VM-Situated.md`  
**Canonical home copy:** `/home/sab-mini/001-MyAPI-VM-Situated.md`

Pi harness / Pi VM harness matters long-term; it is **not** the focus of this handoff. Use this doc for MyAPI + Khoj situated state while those other sessions run.

---

## 0. Read this first (footguns)

1. **Real work lives under `sab-mini`.** Projects, services, and this handoff: `/home/sab-mini/…`. Home `saboor` on this box is a residual path, not the operator surface.
2. **Two MyAPI checkouts exist and diverge.** Systemd runs code/venv from one place and sets WorkingDirectory to another:
   - Working tree agents should use: `/home/sab-mini/MyAPI` (`feat/corpus-v1-normalization` @ `88a17ff`, Vertex ADC health OK).
   - Systemd `ExecStart` venv + older/divergent tree: `/data/repos/MyAPI` (`feat/claude-web-adapter` @ `89b4623`, different API surface).
   - Unit file forces `KHOJ_URL=http://localhost:42110` even when `.env` says wave1/42111.
3. **Index is thin vs disk.** ~3.3k note files on disk; Khoj DB currently reports **273 entries** / **3456 fileobjects**. Historical restore claimed ~42.7k entries. Search “works” but ranking quality is poor (noise hits on A1-class questions).
4. **Wave1 port is not live.** Scripts describe archive `:42110` vs wave1 `:42111`. Only **42110** is listening. `KHOJ_BACKEND=wave1` in `.env` is a label drift, not a second process.
5. **Secrets stay out of git.** `/etc/khoj.env` (mode 600), MyAPI `.env`. Never paste passwords into this handoff or agent chat logs.

---

## 1. Host snapshot (as of write)

| Item | Value |
|---|---|
| Hostname | `khoj-38` |
| Tailscale IPv4 | `100.75.255.75` |
| GCP internal | `10.128.0.2` |
| SSH | `ssh sab-mini@khoj-38` (Tailscale) |
| RAM | ~24 GiB (plenty free at idle) |
| Disk | ~99G root, ~55G free |
| CPU | 4 vCPU |
| Docker | installed (`26.1.5`), only `hello-world` image present — **no Khoj image yet** |
| Postgres | 17.10 local, extensions: `vector 0.8.0`, `pg_trgm` |
| Auto-shutdown | historically present (`auto-shutdown-12h`); confirm if still armed before long jobs |

### Live services (systemd)

| Unit | State | Role |
|---|---|---|
| `khoj.service` | active, enabled | Khoj AI engine `:42110` |
| `context-refinery.service` | active, enabled | MyAPI FastAPI / Context Refinery `:8000` |
| `postgresql` | active | Khoj metadata + vectors |
| User units | `gddp-heartbeat`, `needle-serve`, `openclaw-node` | adjacent infra; not MyAPI core |

### Health smoke (run in VM shell)

```bash
curl -sS http://127.0.0.1:42110/api/health
curl -sS http://127.0.0.1:8000/health
curl -sS -X POST http://127.0.0.1:8000/query -H 'Content-Type: application/json' -d '{"q":"What is MyAPI?","n":3}'
```

**Observed at write time:**

- Khoj `/api/health` → `200` `{"email":"default@example.com"}` (anonymous-mode).
- MyAPI `/health` → `ok`, `model=gemini-2.5-flash`, `auth_mode=vertex_adc`, `project=sb-info-notes-2026`, `location=us-central1`, `khoj_url=http://localhost:42110`.
- `/query` returns 200 but top hits are **low-signal vault inbox / unrelated transcripts** (quality problem, not connectivity).

Telemetry noise: Khoj logs show timeouts to `khoj.beta.haletic.com` telemetry — ignore for local operation.

---

## 2. Current Khoj setup (engine)

### 2.1 Process & unit

| Field | Value |
|---|---|
| Package | `khoj` **1.42.10** |
| Binary | `/data/khoj-venv/bin/khoj` (Python 3.11 venv at `/data/khoj-venv`) |
| Unit | `/etc/systemd/system/khoj.service` |
| Env file | `/etc/khoj.env` (`HOME`, `POSTGRES_*`, `KHOJ_ADMIN_*`) |
| Bind | `0.0.0.0:42110` |
| Flags | `--no-gui --anonymous-mode` |
| WorkingDirectory | `/home/sab-mini` |
| User | `sab-mini` |
| Depends | `postgresql.service`, network-online, wants tailscaled |
| Log | `~/.khoj/khoj.log` (large; also `.khoj-wave1/` residual) |
| Memory (running) | ~1.8G RSS observed |

`ExecStart` (verbatim shape):

```text
/data/khoj-venv/bin/khoj --host 0.0.0.0 --port 42110 --no-gui --anonymous-mode
```

### 2.2 Database

| Field | Value |
|---|---|
| Engine | PostgreSQL 17 + **pgvector** + pg_trgm |
| DB name | `khoj` (from env) |
| App role | `khoj` (from env; password in `/etc/khoj.env`) |
| Key tables | `database_entry`, `database_fileobject`, `database_localmarkdownconfig`, `database_searchmodelconfig`, Django auth/* |
| Search model row | single `default` |
| Markdown configs | **0 rows** — no active `LocalMarkdownConfig` pointing at notes paths |
| Entry count | **273** |
| Fileobject count | **3456** |
| Content API size | `/api/content/size` reported `indexed_data_size_in_mb: 1` (alarmingly small vs notes on disk) |

**Restore source (historical):**  
`/data/corpus-gens/snapshots/20260730T062005Z-mixed-pre-clean/` (~337M) — PG dump used when this box was prepped (`VM-PREP-STATUS.md`, 2026-07-31). Live index no longer matches that “~42.7k entries” claim.

### 2.3 Embedding / rerank models (local cache — **not** the portability target)

HuggingFace cache under `~/.cache/huggingface/hub` (~211M):

- `thenlper/gte-small` (bi-encoder / default dense)
- `mixedbread-ai/mxbai-rerank-xsmall-v1` (cross-encoder)

Containerizing the **engine** should treat these as optional mount/volume caches, not bake multi-GB weights into the image if avoidable. First start can pull; Mac Mini may share a volume.

### 2.4 Content on disk (watched / intended)

| Path | Role | Size / count |
|---|---|---|
| `/home/sab-mini/khoj-data/notes` | Primary notes tree (ChatGPT/Claude/Obsidian-ish md) | ~41M, **~3343 files** |
| `/home/sab-mini/khoj-data/ai-exports` | Export drop | present |
| `/data/corpus-hot/v1` | Hot corpus pack structure | ~456K |
| `/data/corpus-hot/v1-notes` | Lean “wave1” notes slice MyAPI `.env` points at | ~904K |
| `/data/corpus-hot/smoke-questions.txt` | Smoke questions | tiny |
| `/data/corpus-gens/snapshots/…` | PG/snapshot restore archive | ~337M |

`scripts/khoj_backend` documents intended split:

| Backend label | URL | Notes dir |
|---|---|---|
| `archive` | `http://localhost:42110` | historically `/home/saboor/khoj-data/notes` (stale path!) |
| `wave1` | `http://localhost:42111` | `/data/corpus-hot/v1-notes` |

**Reality today:** only archive process on **42110**; notes live under **sab-mini** paths; wave1 service/process missing.

### 2.5 Access surface

| Client path | URL |
|---|---|
| Local | `http://127.0.0.1:42110` |
| Tailscale hostname | `http://khoj-38:42110` |
| Tailscale IP | `http://100.75.255.75:42110` |
| Search (typical) | Khoj native search API used by MyAPI `RetrievalPipeline` |
| Update/reindex | historically `POST /api/update` (see `deploy_to_khoj.sh` comments) |

Helper scripts in MyAPI (not all proven on this tip):

- `scripts/reindex_khoj_safe.py`
- `scripts/khoj_index_diff.py`
- `scripts/khoj_reindex_resume_index.py`
- `scripts/khoj_repair_index_delta.py`
- `scripts/daily_corpus_to_khoj.py`
- `deploy_to_khoj.sh` (rsync bundle; placeholder Tailscale IP)

---

## 3. Context Refinery / MyAPI on this VM

### 3.1 Service

| Field | Value |
|---|---|
| Unit | `/etc/systemd/system/context-refinery.service` |
| Requires | `khoj.service` |
| WorkingDirectory | `/home/sab-mini/MyAPI` |
| ExecStart | `/data/repos/MyAPI/.venv-py313/bin/uvicorn api.main:app --host 0.0.0.0 --port 8000` |
| Env | `PYTHONPATH=/home/sab-mini/MyAPI`, `EnvironmentFile=/home/sab-mini/MyAPI/.env`, override `KHOJ_URL=http://localhost:42110` |
| Memory | ~125M |

### 3.2 API surface (live OpenAPI paths)

`/health`, `/query`, `/enrich`, `/enrich/batch`, `/import/obsidian`, `/import/chatgpt`, `/import/codex`, `/import/claude-code`

`/query` body field is **`q`** (not `query`). See `api/schemas.py` + `api/routers/query.py` → `RetrievalPipeline`.

### 3.3 Env keys (no secrets)

| Key | Intent on sab-mini tree |
|---|---|
| `KHOJ_BACKEND` | `wave1` (label only right now) |
| `KHOJ_URL` | unit forces `http://localhost:42110` |
| `KHOJ_NOTES_DIR` | `/data/corpus-hot/v1-notes` |
| `GOOGLE_CLOUD_PROJECT` | `sb-info-notes-2026` |
| `GOOGLE_CLOUD_LOCATION` | `us-central1` |
| `GEMINI_MODEL` | `gemini-2.5-flash` |
| Auth | Vertex **ADC** (health reports `vertex_adc`) |

### 3.4 Dual-clone detail (must fix eventually)

| Path | Branch / tip | Used for |
|---|---|---|
| `/home/sab-mini/MyAPI` | `feat/corpus-v1-normalization` @ `88a17ff` | WorkingDirectory, `.env`, semantic pack, agent edits |
| `/data/repos/MyAPI` | `feat/claude-web-adapter` @ `89b4623` | **venv that actually runs uvicorn**, divergent `api/` + retrieval |

`api/main.py` differs between the two trees. Prefer consolidating systemd onto **one** tree + one venv before serious quality work.

Remote: `https://github.com/skchaudr/MyAPI.git` (gh auth as `skchaudr` on this host).

---

## 4. Current corpus (what agents can hit)

### 4.1 Layers

1. **On-disk notes (archive-ish):** `~/khoj-data/notes` — thousands of `chatgpt-*`, `claude-*`, project md files. This is the bulk personal/work dump.
2. **Hot / lean slice:** `/data/corpus-hot/` — curated v1 structure + v1-notes (handoffs, anchors, GDDP drafts, status docs). What MyAPI *thinks* it is pointed at.
3. **Indexed subset in Khoj:** only **273** `database_entry` rows. Fileobjects higher — indexing incomplete, stale, or partially wiped relative to restore.
4. **Snapshots:** PG dump under `/data/corpus-gens/snapshots/LATEST` for disaster recovery, not live query.
5. **Semantic Graphify pack (in git on `feat/corpus-v1-normalization`):**  
   `/home/sab-mini/MyAPI/.scratch/semantic-graphify-cold-start/` — map, 8 issues, research, NODE-MAP, WAYFINDER-TO-GDDP, draft GDDP YAML N1–N6. (Also mirrored on docs branch history under other clones.)

### 4.2 Quality reality

- Connectivity green; **retrieval quality weak**.
- Sample “What is MyAPI?” → top results were Claude Code hooks docs / random YouTube transcript notes (vault_inbox), not project anchors.
- Acceptance-style goldens (A1 identity, A7 broken/blocked) need **high-signal anchors in the active index** + ranking fixes — not more infra restarts.
- Historical acceptance / trust docs live under project-docs and corpus-hot v1-notes (e.g. `myapi-status-anchor.md`, `My-API-Trust-Threshold-Plan.md`, `STATUS_AND_NEXT_STEPS.md`).

### 4.3 North star product (locked in prior thread)

**Semantic Graphify cold-start:** 30–90s agent orientation via **2 MCP tools + `/query`** over personal/project knowledge (meaning, not AST). Prove on MyAPI first. Substrate = sessions, project notes, chats, docs, anchors — via existing Khoj path.

Eight must-question bank: `.scratch/semantic-graphify-cold-start/research/02-cold-start-question-bank.md` and issues 01–08.

Executor node map N1–N6: `.scratch/semantic-graphify-cold-start/NODE-MAP.md`  
Draft YAML: `.scratch/semantic-graphify-cold-start/gddp-draft/myapi-cold-start/nodes/`

---

## 5. Work done so far (situated)

### 5.1 Infrastructure (mostly green)

- [x] VM `khoj-38` online; Tailscale address stable.
- [x] Postgres 17 + pgvector restored/running; Khoj v1.42.10 as systemd service, anonymous mode, port 42110.
- [x] Context Refinery systemd service on 8000; depends on Khoj.
- [x] Vertex ADC path for Gemini (`gemini-2.5-flash`) — `/health` reports configured.
- [x] Docker engine present (unused for Khoj).
- [x] Historical handoffs 000–012 under `MyAPI/handoffs/` (Vertex, corpus v1, VM migration, Needle, etc.).
- [x] Session migration note: `~/sab-dev-to-khoj-38-migration-note.md` (sab-dev → khoj-38 agent homes).
- [x] Prep status: `~/VM-PREP-STATUS.md` (2026-07-31 baseline).
- [x] Hot corpus trees + large PG snapshot on `/data`.
- [x] Notes tree at `~/khoj-data/notes`.
- [x] Factory Droid binary present: `~/.local/bin/droid`; `~/.factory` ~18M (missions sync from Mini/Air still pending).

### 5.2 Product / planning (decided, not fully built)

- [x] Wayfinder map + 8 decision tickets collapsed for Semantic Graphify cold-start (`.scratch/…`).
- [x] NODE-MAP for Factory/Droid-style execution (N1 rebuild surface → N6 prove 8 questions).
- [x] GDDP draft nodes YAML authored (not necessarily loaded into `gddp-config` runtime yet).
- [x] Durable-work rule intent from prior fury session (commit/push keep-worthy work; don’t leave operator locked out on untracked VM state) — **verify** whether AGENTS.md durable section made it into *this* clone tip (base multi-machine command rules are present).

### 5.3 Code tip on working tree

`feat/corpus-v1-normalization` includes recent corpus delivery, Vertex ADC fallback, gemini-2.5-flash upgrade (`88a17ff` and parents). Untracked still: `.scratch/`, `scripts/khoj_backend`, local `venv` symlink, `.remember/`.

### 5.4 Explicitly incomplete / broken

- [ ] Index integrity vs disk (273 entries vs 3k+ files).
- [ ] LocalMarkdownConfig empty — Khoj may not be watching the intended folders.
- [ ] Wave1 second process on 42111 not running; `.env` / `khoj_backend` drift.
- [ ] Dual MyAPI clone + venv split.
- [ ] Retrieval quality / high-signal prioritization for cold-start questions.
- [ ] MCP two-tool live surface + golden briefs may live on `main` more than this feat branch — inventory before claiming done.
- [ ] Containerized Khoj engine (none).
- [ ] Mac Mini as alternate Khoj host (clients may still point at old IPs per old prep notes).
- [ ] Droid mission migration Mini/Air → this VM.

---

## 6. What still needs to be done

Ordered for two Grok sessions; pick lanes deliberately.

### Lane A — MyAPI quality / cold-start (product)

1. **Consolidate clone:** one tree, one venv, systemd points only there. Prefer `/home/sab-mini/MyAPI` + its own `.venv-py313` (or repoint unit carefully).
2. **Rebind corpus truth:** decide active index = full `~/khoj-data/notes` vs lean `/data/corpus-hot/v1-notes` vs hybrid; fix `LocalMarkdownConfig` / reindex; fix `khoj_backend` paths away from `/home/saboor/…`.
3. **Reindex / repair** until entry count and search hits reflect high-signal anchors (status, trust, myapi-status-anchor, corpus-hot briefs).
4. **Prove A1 / A7-class questions** return project identity + broken/blocked with evidence paths — not vault_inbox spam.
5. **Agent query contract** (NODE-MAP N2): document `/query` args (`q`, `n`, filters) + smoke for agents.
6. **Project + person briefs** (N3–N4) and **two MCP tools** (N5) if `main` surfaces are merged/rebuilt.
7. **Prove eight must-questions** (N6) with receipts.
8. Commit/push keep-worthy packs (`.scratch` semantic pack, this handoff, durable rules).

### Lane B — Khoj engine portability (infra)

See §7 (containerize) and §8 (Mac Mini).

### Lane C — Cross-machine ops

1. Flip any Mac launchd / client `MYAPI_KHOJ_URL` still on dead IPs → `http://khoj-38:42110` or Mini-local when Mini hosts.
2. Factory Droid mission sync Mini + Air → `~/.factory` on VM (separate op; do not invent wipe).
3. Confirm auto-shutdown won’t kill long reindexes.

### Out of scope for this handoff

- Pi harness redesign.
- AST Graphify replacement.
- Multi-tenant SaaS.
- Baking embedding weights as the primary deliverable.

---

## 7. Containerizing the Khoj **engine** (not the embeddings)

Goal: portable **runtime** of Khoj (Django app + API on 42110) + its **Postgres/pgvector** dependency, so the same unit can run on VM, Mac Mini (Docker Desktop/Colima), or another Linux host. Embeddings/models are **cache volumes**, not the image’s reason to exist.

### 7.1 What to package

| Component | Container? | Notes |
|---|---|---|
| Khoj app 1.42.10 | **Yes** — primary image | Same flags: `--host 0.0.0.0 --port 42110 --no-gui --anonymous-mode` |
| PostgreSQL 17 + pgvector | **Yes** — sidecar or external | Match extensions `vector`, `pg_trgm` |
| Notes / corpus dirs | **Bind mounts** | e.g. `./khoj-data/notes:/data/notes:ro` (or rw if Khoj writes) |
| HF model cache | **Named volume** optional | `~/.cache/huggingface` — download once, reuse |
| Admin/DB secrets | **Env file** not in image | port of `/etc/khoj.env` |
| MyAPI / Context Refinery | Separate image or keep systemd for now | Do not conflate with Khoj engine image |

### 7.2 Suggested layout (repo or ops folder)

```text
deploy/khoj-engine/
  Dockerfile              # or use official ghcr if pin-compatible
  docker-compose.yml      # khoj + db
  env.example             # POSTGRES_*, KHOJ_ADMIN_*, no real secrets
  README.md               # run book
```

**Compose shape (illustrative):**

```yaml
services:
  db:
    image: pgvector/pgvector:pg17   # or ankane/pgvector: pinned
    environment:
      POSTGRES_DB: khoj
      POSTGRES_USER: khoj
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
    volumes:
      - khoj-pgdata:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U khoj"]
      interval: 5s
      retries: 10

  khoj:
    image: khoj-engine:1.42.10      # build from Dockerfile OR official pin
    depends_on:
      db: { condition: service_healthy }
    ports:
      - "42110:42110"
    env_file: [.env.khoj]
    environment:
      POSTGRES_HOST: db
      POSTGRES_PORT: 5432
      POSTGRES_NAME: khoj
      POSTGRES_USER: khoj
      # password from env_file
    volumes:
      - ${KHOJ_NOTES_HOST_PATH}:/data/notes
      - khoj-hf-cache:/root/.cache/huggingface   # or non-root home
    command: ["khoj", "--host", "0.0.0.0", "--port", "42110", "--no-gui", "--anonymous-mode"]
```

### 7.3 Migration path from current bare-metal

1. **Snapshot DB:** `pg_dump` of `khoj` (and note entry counts before/after).
2. **Pin version:** install/build Khoj **1.42.10** in image (match host).
3. **Mount notes:** same paths agents expect; reconfigure LocalMarkdownConfig inside Khoj to container paths.
4. **First boot:** migrate schema, restore dump or reindex from mounts.
5. **Cutover:** stop `khoj.service`, start compose, point MyAPI `KHOJ_URL` at `http://127.0.0.1:42110` (or docker network DNS).
6. **Keep systemd as orchestrator optional:** `khoj.service` becomes `docker compose up` oneshot/oneshot-remain, or leave compose managed manually until stable.
7. **Do not** require shipping embedding weights in git or the image layers if HF cache volume works offline-after-first-pull.

### 7.4 Effort estimate (honest)

| Step | Effort |
|---|---|
| Compose + env + volume wiring | small (hours) |
| Image pin + anonymous-mode parity | small |
| Dump/restore + path remap + reindex | medium (half day; longer if re-embed all notes) |
| MyAPI cutover + smoke | small |
| Hardening (non-root, resource limits, backup cron) | medium |

**Success criteria:** `curl :42110/api/health` from host; MyAPI `/query` still 200; entry count ≥ pre-cutover (or documented reindex plan); no secret in image.

### 7.5 What not to do

- Rebuild Khoj from source “to improve retrieval” under the containerization ticket.
- Bake full personal corpus into the image.
- Treat embeddings as the portable artifact — **engine + config + mount contract** are.

---

## 8. Deploying this onto the Mac Mini (instead of VM)

Goal: Mac Mini becomes the Khoj + (optional) MyAPI host so VM sleep / cost / SSH is not on the critical path. VM can remain backup or GCP-only Vertex workspace.

### 8.1 Prerequisites on Mini

- Docker Desktop **or** Colima/OrbStack with enough RAM (Khoj ~2G + Postgres + models; budget **8G+** free for comfort).
- Tailscale on Mini (same tailnet as Air / phones / agents).
- Notes corpus available locally (rsync from VM or existing Mini Obsidian/export paths).
- For MyAPI Gemini: either Vertex ADC on Mini or API key mode — don’t assume VM service account ADC copies cleanly.

### 8.2 Port plan (avoid collision)

| Service | Port |
|---|---|
| Khoj | `42110` |
| MyAPI | `8000` (or `18000` if Mini already uses 8000) |
| Postgres | bind **127.0.0.1 only** inside Docker network (do not publish 5432 to LAN unless needed) |

### 8.3 Data move

```text
# Run on VM (example — adjust paths; dry-run first)
rsync -avz --progress \
  /home/sab-mini/khoj-data/notes/ \
  sab-mini@<mac-mini-tailscale>:/Users/<you>/khoj-data/notes/

# Optional: lean hot slice
rsync -avz /data/corpus-hot/ sab-mini@<mac-mini-tailscale>:~/corpus-hot/
```

DB options:

- **A.** Fresh Postgres in Docker + **reindex** from notes (cleanest path semantics; CPU time).
- **B.** `pg_dump` / restore into Mini Postgres (faster continuity; watch Linux→macOS pg version parity — stick to 17 + pgvector).

### 8.4 Run engine on Mini

1. Copy `deploy/khoj-engine/` (once authored) to Mini.
2. Fill `.env.khoj` (new passwords fine).
3. `docker compose up -d`.
4. Smoke: `curl http://127.0.0.1:42110/api/health`.
5. Advertise Tailscale MagicDNS name (e.g. `http://sab-mini:42110` or Mini hostname).

### 8.5 Point clients

| Client | Change |
|---|---|
| MyAPI on Mini | `KHOJ_URL=http://127.0.0.1:42110` |
| MyAPI still on VM | `KHOJ_URL=http://<mini-tailscale>:42110` (firewall allow tailnet only) |
| Mac Air launchd / env | replace old `100.x` / `khoj-38` if Mini is primary |
| Agents AGENTS.md | document **Run on Mini** as a first-class location label |

### 8.6 What stays on VM vs moves

| Keep on VM (reasonable) | Move to Mini (reasonable) |
|---|---|
| Heavy GCP ADC / Vertex batch experiments | Always-on Khoj for laptop agents |
| Large snapshot archives `/data/corpus-gens` | Hot notes + live index |
| Ephemeral compute | Daily operator cold-start path |

### 8.7 Effort estimate

| Path | Effort |
|---|---|
| Engine-only Docker on Mini + reindex lean hot | ~half day |
| Full notes reindex + MyAPI local + client flips | 1–2 days incl. quality smoke |
| Dual-run (VM + Mini) with explicit primary | extra ops discipline, not more code |

---

## 9. Session split guidance (two Grok agents on VM)

**Live assignment (2026-08-08):**

| Lane | Role | Root claim | Git claim |
|------|------|------------|-----------|
| **A** | Project / corpus / goldens / retrieval quality / cold-start prove | `/home/sab-mini/00-PROJECT-LANE.md` | `handoffs/013-project-lane-claim.md` |
| **B** | Khoj engine upkeep + Mini portability | `/home/sab-mini/00-ENGINE-LANE.md` | `deploy/khoj-engine/` + this file §§7–8 |

Machine face (read before either repo): `/home/sab-mini/00-READ-ME-FIRST.md`

| Session | Focus | Success |
|---|---|---|
| **Grok A (project)** | Corpus truth, reindex *content*, anchors, goldens, `/query` quality, briefs, eight must-questions | High-signal answers with evidence; packs on `origin` so Mini can continue |
| **Grok B (engine)** | Khoj portable: compose, dump/restore, Mini runbook, process health | Engine green on VM; documented Mini path; no product re-grilling |

Both sessions: **read `/home/sab-mini/00-READ-ME-FIRST.md` first**, then this file; machine-label every command (`Run in VM shell:` / `Run on Mac:`); **commit keep-worthy work** to MyAPI so a VM sleep does not strand state.

Do not both rewrite systemd blindly — serialize unit file edits.

---

## 10. Key paths cheat sheet

```text
/home/sab-mini/001-MyAPI-VM-Situated.md          # this handoff (VM root)
/home/sab-mini/MyAPI/                            # preferred agent clone
/home/sab-mini/MyAPI/handoffs/001-MyAPI-VM-Situated.md
/home/sab-mini/MyAPI/.scratch/semantic-graphify-cold-start/
/home/sab-mini/khoj-data/notes/
/data/khoj-venv/                                 # bare-metal Khoj venv
/data/repos/MyAPI/                               # divergent clone + running venv ⚠️
/data/corpus-hot/                                # hot / wave1 materials
/data/corpus-gens/snapshots/LATEST               # PG snapshot
/etc/systemd/system/khoj.service
/etc/systemd/system/context-refinery.service
/etc/khoj.env                                    # secrets
```

---

## 11. Related docs (do not re-litigate; extend)

| Doc | Path |
|---|---|
| VM prep baseline | `/home/sab-mini/VM-PREP-STATUS.md` |
| sab-dev → khoj-38 sessions | `/home/sab-mini/sab-dev-to-khoj-38-migration-note.md` |
| Older VM migration handoff | `MyAPI/handoffs/009-vm-migration-handoff.md` |
| Sitrep Khoj deploy (historical) | `MyAPI/project-docs/sitrep_khoj_deployment.md` |
| Cold-start NODE-MAP | `MyAPI/.scratch/semantic-graphify-cold-start/NODE-MAP.md` |
| Map + decisions | `MyAPI/.scratch/semantic-graphify-cold-start/map.md` |
| Pi cold-start README | `MyAPI/HANDOFF-PI-README.md` (adjacent; not this mission) |

---

## 12. Update protocol

When either Grok session changes ground truth:

1. Edit **both** copies if still duplicated: `~/001-MyAPI-VM-Situated.md` and `MyAPI/handoffs/001-MyAPI-VM-Situated.md` (prefer making the home path a symlink to the repo file after first commit).
2. Bump the **Written** date and a short “Changelog” bullet at the bottom.
3. Commit + push on MyAPI so Air/Mini can pull.

### Changelog

- **2026-08-08** — Initial situated handoff: live services, corpus counts, dual-clone footgun, containerize + Mac Mini plans, session split for two Grok agents.
- **2026-08-08 (later)** — Explicit dual-lane claim: Lane A project/corpus vs Lane B engine. VM root `00-READ-ME-FIRST.md` / `00-PROJECT-LANE.md` / `00-ENGINE-LANE.md`. Git: `013-project-lane-claim.md`. Semantic pack on branch.

- **2026-08-08 (session 2)** — Mini portable pack at `deploy/khoj-engine/` (compose + export + README). VM use path: systemd Context Refinery now uses `/home/sab-mini/MyAPI/.venv-py313` (no dual-venv). Lean index: corpus-hot `v1-notes` (58 docs) reindexed; A1/A7-class `/query` returns status/trust anchors. Mini move is **ready when you choose**; primary use remains VM `:8000` + `:42110`.
