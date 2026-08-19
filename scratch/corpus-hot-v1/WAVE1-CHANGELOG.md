# WAVE1 CHANGELOG — snapshot corpus on VM

## 2026-07-29 — wave1 land + first smoke

### Arrived on VM
- Host: `khoj-vm-restore` (GCP, Tailscale name same)
- Services already up: postgresql, khoj.service, context-refinery.service
- ADC already working for Gemini (Context Refinery health: vertex_adc)

### Corpus landed
- Path on VM: `/data/corpus-hot/v1/`
- Source: mini `~/repos/MyAPI/scratch/corpus-hot-v1/` (merge of air + mini pass-1)
- Transfer: tarball scp via air gcloud → extract on VM
- Size: ~440K
- File count under `/data/corpus-hot/v1/`: **95 files**

### What the 95 files are
Full tree, including copies of both raw harvests:

| Path under v1/ | What |
|---|---|
| `README.md`, `DENYLIST.md` | pack meta |
| `myapi/`, `gddp/`, `pi-needle-gemma/` | **merged** SOURCES/QUERIES/BRIEF-DRAFT/GAPS (mini section + air section each) = **12 md** |
| `raw-mini/` | untouched mini pass-1 tree (~14 md) |
| `raw-air/` | untouched air pass-1 tree (~14 md) |
| macOS xattr noise from tar | extra entries; content is the md trees above |

**95 = full tree on disk. Not all 95 were sent to Khoj.**

### What got indexed into Khoj (the 14)
Khoj’s simple indexer only wants **flat** files in `~/khoj-data/notes/` (top-level `.md`, no subdirs).

So we **copied only the merged product docs** (not raw-mini/raw-air) into notes as:

```
~/khoj-data/notes/corpus-hot-v1-myapi-SOURCES.md
~/khoj-data/notes/corpus-hot-v1-myapi-QUERIES.md
~/khoj-data/notes/corpus-hot-v1-myapi-BRIEF-DRAFT.md
~/khoj-data/notes/corpus-hot-v1-myapi-GAPS.md
~/khoj-data/notes/corpus-hot-v1-gddp-SOURCES.md
~/khoj-data/notes/corpus-hot-v1-gddp-QUERIES.md
~/khoj-data/notes/corpus-hot-v1-gddp-BRIEF-DRAFT.md
~/khoj-data/notes/corpus-hot-v1-gddp-GAPS.md
~/khoj-data/notes/corpus-hot-v1-pi-needle-gemma-SOURCES.md
~/khoj-data/notes/corpus-hot-v1-pi-needle-gemma-QUERIES.md
~/khoj-data/notes/corpus-hot-v1-pi-needle-gemma-BRIEF-DRAFT.md
~/khoj-data/notes/corpus-hot-v1-pi-needle-gemma-GAPS.md
~/khoj-data/notes/corpus-hot-v1-README.md
~/khoj-data/notes/corpus-hot-v1-DENYLIST.md
```

= **14 markdown files**

### Khoj API “200”
- Call: `PATCH http://localhost:42110/api/content?client=api`
- Body: those 14 files as multipart
- Response: **HTTP 200** = Khoj accepted the batch (index updated for those names)
- This is **not** a query score. It only means “ingest of the 14 succeeded.”

### What we tested
- **Not** full answer quality grading yet.
- **HIT definition:** among top search results, at least one filename contains `corpus-hot-v1` (pack showed up).
- **MISS:** pack did not appear in top results (old corpus won or pack not matched).
- 8 fixed questions (graphify-shaped: ownership, tools, denylist, Needle, person, handoff, executor).

### First retrieval results

**Khoj `/api/search` — 6/8 HIT**

| Q (short) | Result | Note |
|---|---|---|
| gddp-config vs runtime | HIT | pack BRIEF + old chat also present |
| MyAPI vs MyMCP | HIT | pack BRIEF/SOURCES |
| two MCP tools names | MISS | old chat dumps ranked above pack |
| .pi denylist | HIT | DENYLIST.md |
| Needle vs Pi harness | HIT | pack BRIEF/QUERIES |
| who is Sab / person | HIT | pack + old obsidian “i want to be sab” |
| durable handoff intent/evidence | HIT | pack + myapi-status-anchor |
| executor → evaluator | MISS | old GDD operator notes, not pack |

**MyAPI POST `/query` — 6/8 HIT** (same HIT rule: `corpus-hot-v1` appears in response body)

| Q | Result |
|---|---|
| same 6 as Khoj hits | HIT |
| two MCP tools | HIT (MyAPI path found pack even when Khoj top looked noisier) |
| who is Sab | **ERR 500** (server error, not scored as clean HIT) |
| executor → evaluator | MISS |

Counts: reported **6/8** on both surfaces; MyAPI had 1×500 so treat person-Q as broken path not a clean miss.

### What this does / does not mean
- **Does mean:** wave1 pack is on the VM, 14 docs are in Khoj’s notes index, some agent-shaped questions retrieve those docs.
- **Does not mean:** answers are correct prose, ranking is fixed, or old corpus is gone.
- **Old notes still dominate** many queries (chat/obsidian dumps still in the same Khoj index).

### First optimization (not done yet — next)
1. Prefer / boost filenames `corpus-hot-v1-*` in retrieval, **or**
2. Query against a pack-only index, **or**
3. Remove/suppress competing dumps for smoke runs  
Then re-run the same 8 Q and log a new changelog entry.

### Locations (canonical)
| What | Where |
|---|---|
| Merged pack (mini) | `~/repos/MyAPI/scratch/corpus-hot-v1/` |
| Pack on VM | `/data/corpus-hot/v1/` |
| Flat indexed copies | `/home/saboor/khoj-data/notes/corpus-hot-v1-*.md` |
| This changelog | same dir as pack + should live on VM under `/data/corpus-hot/v1/WAVE1-CHANGELOG.md` |
