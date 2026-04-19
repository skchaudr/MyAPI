# VM Migration Handoff

This note captures the current known-good state for the Context Refinery / Khoj setup so the project can be moved to a new VM with minimal guesswork.

## What Is Already In Git

- Retrieval/classifier/ranking tuning is committed and pushed on `feat/claude-web-adapter`
- Commit: `1989500` `feat: tune retrieval classifier and source ranking`
- OpenClaw pull command:
  ```bash
  git pull origin feat/claude-web-adapter
  ```

## Current Runtime Assumptions

### Context Refinery

- Service name: `context-refinery.service`
- Health endpoint: `http://localhost:8000/health`
- Local dev command: `./run_dev.sh`
- FastAPI app entrypoint: `api.main:app`
- Port: `8000`

### Khoj

- Service name: `khoj.service`
- Health endpoint: `http://localhost:42110/api/health`
- Port: `42110`
- Database: PostgreSQL `khoj`
- DB user: `khoj`
- DB host: `localhost`
- DB port: `5432`

### Important Environment Variables

- `GEMINI_API_KEY` for context-refinery enrichment and UI flows
- `KHOJ_URL` for retrieval pipeline access to Khoj
- `KHOJ_NOTES_DIR=/home/sbkchaudry_gmail_com/khoj-data/notes` for hybrid keyword search
- `VITE_API_URL=http://localhost:8000` for the frontend

## Current Repo State Worth Preserving

- Retrieval parser now infers missing `source` from filename prefix
- Query classifier now recognizes:
  - temporal
  - project overview
  - source-specific
  - operational
  - decision
  - meta
  - synthesis
  - cross-source
  - pattern
- Response schema now allows those intents

## What To Move To The New VM

- MyAPI repo checkout
- Git branch state: `feat/claude-web-adapter`
- The `context-refinery` service config
- The Khoj service config
- The notes corpus path and any rsynced data under `~/khoj-data/notes`
- Any scripts used for incremental indexing or benchmark runs

## Suggested Bring-Up Order

1. Provision the new VM.
2. Install system packages, Python, Node, and any service dependencies.
3. Clone or rsync `MyAPI` onto the new VM.
4. Pull `origin/feat/claude-web-adapter`.
5. Restore the note corpus to the expected `KHOJ_NOTES_DIR`.
6. Recreate or copy the `context-refinery.service` unit.
7. Recreate or copy the `khoj.service` unit.
8. Export env vars and secrets.
9. Start Khoj first, then context-refinery.
10. Verify both health endpoints.
11. Rerun the retrieval benchmark.

## Verification Checklist

- `curl http://localhost:42110/api/health`
- `curl http://localhost:8000/health`
- `ss -tlnp | grep 42110`
- `ss -tlnp | grep 8000`
- `git status --short --branch`
- `python3 /tmp/run_benchmark.py` or the benchmark recreation script

## Unknowns Still Needed From You

- New VM host/IP
- New zone/project if different
- Whether the new VM should reuse the existing PostgreSQL data or start fresh
- Whether the benchmark notes corpus should be rsynced first or re-indexed from scratch
- Whether OpenClaw should be pointed at the new VM immediately or after validation

## What I Can Still Do Before You Return

- Turn this into a more formal step-by-step migration runbook
- Draft the exact `gcloud` / `scp` / `ssh` command list for the new VM once you know the host and zone
- Prepare a minimal restore checklist for `khoj.service` and `context-refinery.service`
- Reformat the benchmark results into a migration acceptance check if you want a pass/fail gate
