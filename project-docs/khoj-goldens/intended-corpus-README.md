# Intended corpus (VM assemble → Khoj)

**Script:** `scripts/assemble_intended_corpus_vm.py`  
**Stage on VM:** `/data/corpus-hot/intended-v1/stage/`  
**Receipts:** `/data/corpus-hot/intended-v1/receipts/`

## Intended mix

Not the full ChatGPT/Claude dump. Bounded hot slice:

| Category | Examples |
|----------|----------|
| project-handoffs | MyAPI `handoffs/`, `origin/main:.handoffs/`, aa-cli `.handoffs` |
| project-documents | `project-docs/`, anchors, AGENTS, GDDP briefs, plans |
| golden-briefs | `evals/golden_briefs/*` from `origin/main` |
| graphify | `graphify-out` tip + wayfinder semantic-graphify pack |
| agent-sessions | Grok `summary.json` digests, Codex rollout summaries, Pi harness handoffs |
| git-history | Recent commit digests for MyAPI / aa-cli / gddp-* |
| corpus-hot | Wave-1 pack |

## Run on khoj-38

```bash
cd ~/MyAPI
python3 scripts/assemble_intended_corpus_vm.py --dry-run   # stage only
python3 scripts/assemble_intended_corpus_vm.py --index --force  # stage + batch index
python3 scripts/assemble_intended_corpus_vm.py --status
```

Env: `MYAPI_KHOJ_URL` (default `http://127.0.0.1:42110`), `INTENDED_CORPUS_ROOT` (default `/data/corpus-hot/intended-v1`).

**Index rule:** Khoj `PUT` regenerates from the files in *that* request only. The assembler does **first batch PUT, then PATCH** — never one-file PUT in a loop.

## Live status (2026-08-09 on khoj-38)

- Staged: 303 files  
- Searchable entries: ~2590  
- Khoj search smoke: **8/8** high-signal (see `intended-corpus-smoke-2026-08-09.md`)

## Mini continuity

1. Pull this branch.
2. Ensure Khoj is up (Lane B).
3. Re-run assemble if paths differ, or rsync `/data/corpus-hot/intended-v1/stage` + index with batch PUT/PATCH.
