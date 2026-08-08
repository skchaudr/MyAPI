# Khoj engine — portable deploy (Mac Mini first-class)

**Goal:** Run the **Khoj search engine** (API on `:42110`) on the Mac Mini with Docker, without baking embeddings into the image. MyAPI / Context Refinery can stay on the VM or move later; this pack is **engine only**.

**Live reference host:** `khoj-38` / user `sab-mini` (see `handoffs/001-MyAPI-VM-Situated.md`).

---

## What “clear to move” means

You are **go** when:

| Check | Pass condition |
|---|---|
| Pack in git | This directory on `feat/corpus-v1-normalization` (or main after merge) |
| Mini has Docker | Docker Desktop / Colima / OrbStack with Compose v2 |
| Mini has Tailscale | Can `ssh sab-mini@khoj-38` or rsync the other way |
| Disk on Mini | ≥ notes size + models (~41M notes now; plan multi-GB for full re-embed) |
| Secrets ready | New Postgres + admin passwords in local `.env` (not VM’s `/etc/khoj.env`) |
| Clients known | Who will point at Mini (`KHOJ_URL`) vs stay on VM |

You do **not** need to move before using MyAPI on the VM. Mini is a **portability capability**; VM is the **use-it-now** surface.

---

## Layout

```text
deploy/khoj-engine/
  docker-compose.yml   # engine + pgvector only
  .env.example
  export-from-vm.sh    # package notes from khoj-38
  README.md            # this file
```

---

## A. Prepare export on the VM (optional until move day)

```bash
# Run in VM shell:
cd /home/sab-mini/MyAPI/deploy/khoj-engine
chmod +x export-from-vm.sh
EXPORT_DRY_RUN=1 ./export-from-vm.sh          # sizes only
./export-from-vm.sh                           # notes + corpus-hot → ~/exports/...
INCLUDE_PG_DUMP=1 ./export-from-vm.sh         # + Postgres custom dump (heavier)
```

---

## B. Start on Mac Mini (when you choose to)

```bash
# Run on Mini:
git clone git@github.com:skchaudr/MyAPI.git   # or pull existing
cd MyAPI/deploy/khoj-engine
cp .env.example .env
# edit: POSTGRES_PASSWORD, KHOJ_ADMIN_PASSWORD, KHOJ_NOTES_HOST_PATH=/Users/you/khoj-data/notes

mkdir -p models notes
# rsync notes from VM (see export script epilogue)
docker compose pull
docker compose up -d
curl -sS http://127.0.0.1:42110/api/health
```

### After first healthy boot

1. Open Khoj admin (or API) and point a **Local Markdown** content source at `/data/notes` (compose mount).
2. Trigger index/update (UI or `POST` update endpoint per Khoj version).
3. Smoke search:  
   `curl -sS 'http://127.0.0.1:42110/api/search?q=MyAPI&n=5'`
4. Point MyAPI: `KHOJ_URL=http://127.0.0.1:42110` (if MyAPI also on Mini) or Tailscale Mini hostname from other machines.

### Models / embeddings

Mounted at `./models` (or `KHOJ_MODELS_HOST_PATH`). First index download may pull `gte-small` / rerankers. That cache is **portable** across restarts; it is **not** what we containerize as the product.

### What we deliberately omit

Official Khoj compose also ships SearxNG, Terrarium sandbox, and “Computer”. MyAPI only needs **vector search**. Keep the engine lean.

---

## C. VM dry-run (prove compose without killing bare-metal)

Bare-metal Khoj already owns `:42110`. Dry-run on another port:

```bash
# Run in VM shell:
cd /home/sab-mini/MyAPI/deploy/khoj-engine
cp -n .env.example .env
# set passwords; set KHOJ_HOST_PORT=42112 and KHOJ_NOTES_HOST_PATH=/home/sab-mini/khoj-data/notes
mkdir -p models
docker compose up -d
curl -sS http://127.0.0.1:42112/api/health
docker compose down   # leave bare-metal khoj.service as primary
```

Do **not** stop `khoj.service` for a dry-run unless you intend cutover.

---

## D. Cutover checklist (Mini becomes primary)

1. [ ] Mini health green on Tailscale
2. [ ] Index has real hits for smoke questions (not empty)
3. [ ] Flip client `KHOJ_URL` / launchd on Air/Mini
4. [ ] Leave VM `khoj.service` running as backup **or** stop after soak
5. [ ] Update `handoffs/001-MyAPI-VM-Situated.md` changelog

---

## E. Relation to MyAPI on the VM

| Surface | Role now |
|---|---|
| VM `khoj.service` :42110 | Primary search backend |
| VM `context-refinery` :8000 | MyAPI `/query`, `/health`, enrich |
| Mini Docker (this pack) | Optional portable primary later |

Using MyAPI today = talk to **VM** `:8000`. Moving the engine = change where `:42110` lives; MyAPI just follows `KHOJ_URL`.
