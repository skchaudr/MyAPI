# Intended corpus smoke — 2026-08-09 (khoj-38)

## What landed

| Item | Value |
|------|--------|
| Assembler | `scripts/assemble_intended_corpus_vm.py` |
| Stage | `/data/corpus-hot/intended-v1/stage/` — **303** markdown files |
| Khoj entries after correct batch index | **2590** `database_entry` rows |
| Indexed size | **4 MB** (`/api/content/size`) |
| Method | First **PUT** 50 high-signal files, then **PATCH** rest in chunks of 30 |

### Category mix (stage)

| Category | Count |
|----------|------:|
| project-documents | 101 |
| agent-sessions | 75 |
| project-notes | 49 |
| project-handoffs | 40 |
| corpus-hot | 15 |
| graphify-intent | 13 |
| git-history | 4 |
| golden-briefs | 3 |
| graphify | 2 |

## Critical indexing lesson

**Never one-file `PUT` in a loop.** Khoj `PUT /api/content` **regenerates** the API content index from *only the files in that request*. One-file PUTs left ~13 entries (last file wins). Use:

1. `PUT` with a multi-file high-signal batch  
2. `PATCH` for remaining files (merge)

## Khoj `/api/search` smoke (filename HIT = intended prefix in top-5)

| Query | Result |
|-------|--------|
| What is MyAPI? | HIT — `wave1-myapi--sources.md`, `proj-root--readme.md` |
| two MCP tools get_project_context | HIT — golden briefs from `origin/main` |
| gddp-config vs gddp-runtime | HIT — `gddp-runtime--topology.md` |
| Semantic Graphify cold-start | HIT — `semantic-graphify--*` |
| golden briefs project context | HIT — `git-main--golden-*` |
| myapi status broken blocked | HIT — `myapi-status-anchor` |
| verify pathway aa-cli | HIT — `aa-cli-verify--ticket-map.md` |
| PROJECT-BRIEF MyAPI rebuild | HIT — `git-main--PROJECT-BRIEF.md` |

**Score: 8/8** high-signal filenames.

## `/query` (Context Refinery)

Still returns results; titles often `untitled` (metadata surface), but underlying Khoj hits are now the intended pack.

## Honesty: what this is *not*

**This run did not sanitize or normalize the corpus.**

What happened:

1. **Allowlist / assemble** — pick intended sources (handoffs, docs, session *summaries*, git tip docs, graphify, wave-1).
2. **Light wrap** — provenance frontmatter (`source: intended-corpus-vm`, `category`, `origin_path`).
3. **Index** — batch PUT/PATCH into Khoj so search can see the mix.

What did **not** run:

| Layer | Status |
|-------|--------|
| `context_refinery/sanitization.py` (`sanitize_document`) | **not applied** to stage |
| `scripts/normalize_corpus.py` / `normalization_schema` | **not run** on this slice |
| Vault v1 / Obsidian substrate shape | **not built** |
| Conversation → event + artifact summary split | **not done** |
| Trust / canonicality / source_type backfill | **not stamped** (beyond coarse `category`) |
| Presentable narrative with evidence pointers (product bar) | **not produced** |

So: **searchable raw-ish allowlist**, not **normalized knowledge objects**. Reindex made ranking *possible*; it does not satisfy the rebuild line: *sanitize → normalize → presentable narrative*.

Next product step (Lane A): normalize this intended slice (or a smaller pilot batch) through the existing schema/adapters, then reindex **normalized** output — not re-copy raw again.

## Re-run

```bash
cd ~/MyAPI
python3 scripts/assemble_intended_corpus_vm.py --index --force
# or stage only:
python3 scripts/assemble_intended_corpus_vm.py --dry-run
```

## Mini continuity

1. Pull branch with this script + goldens docs.  
2. Bring stage via re-assemble on Mini paths, or rsync `/data/corpus-hot/intended-v1/`.  
3. Lane B: Khoj up. Lane A: `--index --force` with batch PUT/PATCH.
