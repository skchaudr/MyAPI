# WAVE1-LOG — snapshot corpus to VM

## 2026-07-29 — What we did

### 1. Source material (before VM)
- Two Grok agents (sab-air + sab-mini) each wrote pass-1 harvests.
- Path on both machines: `~/repos/MyAPI/scratch/corpus-hot/`
- Each harvest had the same layout:
  - `README.md`
  - `myapi/` `gddp/` `pi-needle-gemma/`
  - each project: `SOURCES.md` `QUERIES.md` `BRIEF-DRAFT.md` `GAPS.md`
- That is **12 content files + README per host** (plus charter). Not 95 yet.

### 2. Merge (on sab-mini only)
- Combined air + mini harvests into one tree:
  - `~/repos/MyAPI/scratch/corpus-hot-v1/`
- Merged files: for each of 3 projects × 4 docs = **12** markdown files
  - each file contains **both** mini section and air section (concatenated)
- Plus: `README.md`, `DENYLIST.md`
- Plus copies of originals: `raw-mini/` and `raw-air/` (full pass-1 trees preserved)
- **~95 files** = 12 merged + 2 meta + raw-mini (~14) + raw-air (~14) + nested dirs/files from raws
  - The **authoritative wave-1 content** is the **12 merged project docs + README + DENYLIST**
  - The other ~80 are **raw backups** for audit, not the “product pack”

### 3. Landed on VM
- Host: `khoj-vm-restore` (GCP, Tailscale name same)
- Path: `/data/corpus-hot/v1/`
- Same tree as mini merge (including raws) ≈ **95 files**, ~440KB

### 4. Made searchable in Khoj
Khoj’s simple reindex only sees **flat** `*.md` in `~/khoj-data/notes/` (not nested folders).

So we **copied 14 files** into the notes root with flat names:

| Flat name pattern | Source |
|---|---|
| `corpus-hot-v1-myapi-{SOURCES,QUERIES,BRIEF-DRAFT,GAPS}.md` | `/data/corpus-hot/v1/myapi/` |
| `corpus-hot-v1-gddp-…` | `/data/corpus-hot/v1/gddp/` |
| `corpus-hot-v1-pi-needle-gemma-…` | `/data/corpus-hot/v1/pi-needle-gemma/` |
| `corpus-hot-v1-README.md` | v1 README |
| `corpus-hot-v1-DENYLIST.md` | v1 DENYLIST |

**14 files** = 12 project docs + README + DENYLIST.  
These are what Khoj was told to index.

### 5. Index call
- API: `PATCH http://localhost:42110/api/content?client=api`
- Payload: those 14 markdown files
- Result: **HTTP 200** (Khoj accepted the update)
- Meaning: “content registered with Khoj” — **not** “answers are good”

### 6. Smoke test (8 questions)
Script: hit Khoj search + MyAPI `POST /query` with 8 graphify-style questions.

**HIT definition (strict):** top results include a filename containing `corpus-hot-v1`  
(i.e. our pack showed up — not that the answer prose is perfect)

| Channel | Score | Meaning |
|---|---|---|
| Khoj `/api/search` | **6/8 HIT** | 6 questions returned ≥1 pack file in top 8 |
| MyAPI `/query` | **6/8 HIT** | 6 questions’ response body mentioned pack content/filename |

**Khoj detail**
| Q (short) | Result |
|---|---|
| gddp-config vs runtime | HIT (pack BRIEF/QUERIES + old chat still ranked high) |
| MyAPI vs MyMCP | HIT |
| two MCP tools names | **MISS** (old chat/claude dumps won) |
| .pi denylist | HIT |
| Needle vs Pi | HIT |
| Who is Sab | HIT (pack + unrelated obsidian “sab” notes) |
| durable handoff intent | HIT (pack + myapi-status-anchor) |
| executor → evaluator | **MISS** (old GDD/obsidian notes won) |

**MyAPI detail**
| Q | Result |
|---|---|
| same set | 6 HIT, 1 **MISS** (executor/evaluator), 1 **ERR 500** (Who is Sab) |

### 7. What is NOT done
- No rank boost that prefers `corpus-hot-v1-*` over old dumps
- No removal of competing old notes from index
- No full 20-question bank graded Hit/Partial/Miss/OOD with gold paths
- No MyAPI skill / MCP tools wired
- No “answer quality” score — only “did the pack surface?”

### 8. What “95 vs 14” means in one line
- **95** = full tree on disk under `/data/corpus-hot/v1` (merged + raw backups)
- **14** = flat files copied into Khoj notes and **actually indexed**
- **200** = Khoj accepted the index update
- **6/8** = pack appeared in retrieval for 6 of 8 smoke questions

## Status
Wave-1 **landed and partially searchable**. First optimization still open: make pack rank above old corpus noise.
