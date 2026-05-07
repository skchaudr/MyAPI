# HANDOFF — Pi Agent README Drafting Pass

Cold-start orientation for the Pi agent that's going to draft the portfolio `README.md`. Read this once, top to bottom, before opening any other file. It tells you what this project is, what's real and what's stale, and where to skip to avoid burning tokens.

> **Author:** Claude (Mac, this session, 2026-05-06)
> **Audience:** the Pi agent — has never seen this repo
> **Branch on disk:** `chore/portfolio-hygiene` (cleanup landed but not yet merged to `main`)

---

## Project identity

MyAPI is a personal context-retrieval layer that turns Saboor's own notes and AI-conversation history — Obsidian markdown, exported ChatGPT and Claude threads, Codex and Claude Code session logs — into something an agent (or Saboor) can search and trust. Under the hood it's a FastAPI service in front of a self-hosted Khoj index, with a Python "context refinery" pipeline (`context_refinery/`) that ingests, sanitizes, enriches, and routes queries through a multi-lane retrieval stack with reranking. The interesting work isn't the wiring — it's the *trust calibration*: a categorized query bank with seven diagnostic buckets that decides, per query class, whether a failure is a corpus gap, a retrieval gap, a metadata gap, an intent-classifier gap, or an answer-shape gap, and where to spend the next fix. The product framing is two-audience: Saboor's own episodic memory ("find that thread where I figured out X") and agent cold-start context ("here's what's true about this codebase as of today, stop grep'ing"). The trust-threshold plan in `project-docs/My-API-Trust-Threshold-Plan.md` argues the agent angle is the sharper outside-audience story; both audiences are first-class in the bench.

---

## Current state (post-hygiene)

**Pipeline is live.** Phase 1 (build the pipe) is closed. Phase 2 (trust calibration) is the active work.

### Deployment (live)
- VM: `instance-20260418-024637`, GCP `us-central1-a`, Tailscale alias `khoj-vm-new` at `100.85.100.52`
- Khoj search backend: port `42110`, systemd `khoj.service`
- MyAPI (Context Refinery): port `8000`, systemd `context-refinery.service`
- Corpus: `~/khoj-data/notes/` on the VM, ~3,201 non-empty `.md` files
- **VM auto-shuts down after 3 hours.** Almost always off between sessions — start it before any retrieval test, or `/health` will hang.

### What works (functional, tested, used in production)
- `api/main.py` — FastAPI app, three routers: `/enrich`, `/import`, `/query`, plus `/health`. CORS pre-wired for the (now-archived) Vite frontend.
- `context_refinery/` — the Python package this repo is built around. Modules: `retrieval.py` (multi-lane search + rerank), `sanitization.py`, `enrichment.py` (Gemini-backed batch enrich, max 50 docs/req), `exporter.py`, `models.py`, `services.py`, `triage/`, `adapters/` (chatgpt, codex, claude_code, claude, obsidian).
- `tests/` — 13 test files including retrieval, enrichment, sanitization, modular triage, and per-adapter tests. `pytest` from repo root.
- `scripts/acceptance.py` — six-query mechanical harness against `/query` on the VM. The latest acceptance run (handoff 003) was 5/5 mechanical, 1 skipped (A7).
- `ingest_all.py` — batch ingestion entry point. Runs all adapters and writes Khoj-ready `.md` files to a bundle dir.
- `deploy_to_brain.sh` / `deploy_to_khoj.sh` — deploy automation (read before running; they shell out to the VM).

### What's intentionally incomplete / out of scope (read these as boundaries, not gaps)
- **Frontend is archived.** The TypeScript/Vite UI scaffold (`context-refinery/`, hyphen) is at `_archive/context-refinery-vite-scaffold/`. It had real Import/Refine/Export views and a shadcn/ui-style component library, but the project pivoted to the Python API. The retired `api/routers/export.py` is a vestige of that frontend (a comment in `api/main.py` says so explicitly).
- **A7 query** is currently skipped in the acceptance set — the eval notes are subject-scoped to "retrieval benchmark," not "MyAPI," so vocab expansion can't pull them into the candidate set. The fix is to *write* a `myapi-status-anchor.md` (already in `project-docs/source-of-truth-anchors/`), not to patch retrieval. Top of the pending queue.
- **F5** regressed at the candidate-set / Khoj layer, not the reranker. Long-sentence form of the Trust-Threshold-plan query falls out of top 20; bare `"gold mine"` still surfaces at #1. Closed in handoff 000 by a keyword-lane fix (`28a22b0`). Re-run pending.
- **~27 Obsidian files still missing from the Khoj index** per delta-patch report. Tracked, not blocking.
- **No auth on MyAPI.** It's a Tailscale-only service; trust boundary is the network. (Same model as `agent-bus` in the sibling project.)
- **Idempotency** — none, by design. `/enrich` and `/query` are stateless; clients dedupe themselves if needed.

### Notable technical decisions (reasoning isn't obvious from code)
- **`AUTOINCREMENT` ids and append-only logs throughout** — the bench wants stable references to specific runs and specific anchor docs; never reuse ids.
- **Three retrieval lanes, OR'd, with a synthesized-note prior** — the prior is *guarded* against chat-dump sources (chatgpt/claude/claude-code/codex) so a synthesized summary doesn't outrank real anchors when the query is about a chat thread. See commit `5d713ab`.
- **Operational-vs-Project classifier reorder** — OPERATIONAL fires before PROJECT so a query like "MyAPI is broken" routes to operational intent rather than project-explainer intent. Commit `5d713ab`.
- **Exact-phrase boost has hyphen / space / no-space normalization** — closes the F5/H4 exact-term sentinel pair without overfitting.
- **No filter-repo on git history.** The repo had a 39 MB / 3,227-file content snapshot (`khoj-ready-bundle/`) tracked as one anchor file; cleanup did `git rm --cached -r` only — history bloat preserved on purpose to avoid rewriting public-bound history this week.

---

## Portfolio framing (Pi agent voice — quote verbatim)

> "This is a portfolio README for a project built solo by a recent CS graduate who entered the field later in life and is working at the technical frontier — multi-agent orchestration, auditable agent dispatch, real client systems. Audience is mixed: senior engineers should see technical depth and honest tradeoffs; recruiters should see scope and seriousness; people without context should understand what was built and why it's interesting. Confident and accurate — not boastful, not self-deprecating, not weaknesses dressed up as humility."

---

## Pi agent deliverables

Drafts only. **Do not push to GitHub. Do not open a PR.** Write to repo root, leave them as untracked working files until Saboor reviews.

1. **`README.md.draft`** (or `DRAFT-README.md`) — the portfolio README itself. Opens with one accessible paragraph any non-technical recruiter can read; then layers in technical depth. Concrete: name the retrieval lanes, the seven diagnosis buckets, the two-audience framing, the live VM + Khoj deployment, the categorized query bank as the artifact that proves the calibration claim. Cite source files with backtick-paths so a senior reader can verify by clicking.

2. **`POLISH-PUNCHLIST.md.draft`** — what hardening this repo would need to be "best practices, not perfect practices." Examples worth considering: pin Python version + add `pyproject.toml`; add a `Makefile` or `justfile` for `run` / `test` / `ingest` / `acceptance`; add CI (GitHub Actions: lint + pytest); type-check (mypy or pyright) on `context_refinery/`; consider a `compose.yaml` that mirrors the VM's systemd setup for local repro; the deploy scripts could grow a `--dry-run`; the `handoffs/` numbered system is good and underused — keep extending it. Order by leverage, not effort.

Both files at repo root. Saboor will review, edit, and decide what to commit.

---

## Gotchas — paths, env, files to skip

### File-system trap (read this before grepping)
- **`context_refinery/`** (underscore) — the Python package. **This is the project.**
- **`context-refinery/`** (hyphen) — does NOT exist in the live tree anymore. It was an abandoned Vite scaffold; archived to `_archive/context-refinery-vite-scaffold/`. Tab-completion may surprise you.
- The two paths look interchangeable in casual reading. They are not.

### `run_dev.sh` is half-broken
The first half (FastAPI on `:8000`) still works. The second half does `cd context-refinery && npm run dev` — that directory is gone (archived). **Don't run `run_dev.sh` as-is.** For just the API:

```
Run on Mac: GEMINI_API_KEY=... venv/bin/uvicorn api.main:app --reload --port 8000
```

(Per `AGENTS.md`, every command needs a `Run on Mac:` / `Run on VM:` / `Run in VM shell:` / `Run in Cloud Shell:` label. The label discipline is real — read `AGENTS.md` once before drafting any commands into the README.)

### Required env
- `GEMINI_API_KEY` — for `/enrich` and `ingest_all.py`. Model is `gemini-1.5-flash`.
- `PYTHONPATH=/Users/saboor/repos/MyAPI` if running scripts from outside the repo dir (per repo-local `CLAUDE.md`).
- No `.env` in the repo; pull from shell or `~/.zshrc`.

### Files to SKIP — stale Phase 1 (April 9–19) artifacts
Reading these will burn tokens on world-state that no longer applies. They're kept for history; do not use as current state.

- `project-docs/HANDOFF-hybrid-search.md`
- `project-docs/HANDOFF-modular-triage.md`
- `project-docs/HANDOFF-situational-summary.md`
- `project-docs/VM-MIGRATION-HANDOFF.md`
- `project-docs/VM-MIGRATION-SPRINT.md`
- `project-docs/4.18.26.daily.project.md`
- `project-docs/handoff-for-khoj-vm.md`
- `project-docs/web-ui-agent-handoff-pt-2.md` (refers to the archived Vite frontend)
- `project-docs/jules-spec-*.md` (Jules dispatch one-offs; not orientation material)
- `project-docs/sitrep_khoj_deployment.md` (April infra story; relocated here in this hygiene pass, kept for history)
- Anything under `_archive/`

### Files to READ first — current state
In this order:

1. `project-docs/STATUS_AND_NEXT_STEPS.md` — the canonical "where are we" doc. Last updated 2026-05-02.
2. `handoffs/000` through `handoffs/004` — sequential session reality, 2026-05-03 through 2026-05-05. Read in order; each picks up where the last left off.
3. `project-docs/My-API-Trust-Threshold-Plan.md` — the strategic / product frame.
4. `project-docs/retrieval-benchmark-v0/Query/query-bank-trust-categorized-v1.md` — the 17-query bank, the diagnosis rubric, the run protocol. The bench *is* the trust claim.
5. `project-docs/retrieval-benchmark-v0/Harness evaluation/run-2026-05-02-tighten-pass.md` — most recent full run with margins.
6. `project-docs/source-of-truth-anchors/` — four anchor docs (`khoj-deployment-indexing-anchor.md`, `my-devinfra-system-anchor.md`, `myapi-status-anchor.md`, `vm-tailscale-ssh-access-anchor.md`). These are the canonical context the bench queries are tuned against.
7. `api/main.py` and `api/routers/{enrich,imports,query}.py` — service surface. ~30 LOC each; quick read.
8. `context_refinery/retrieval.py` — the interesting code. Multi-lane retrieval + reranker + intent classifier.
9. `AGENTS.md` and `CLAUDE.md` (repo-local) — command discipline; read before drafting any shell snippets.

### Out-of-repo references
- `~/.local/share/khoj/backups/khoj.dump.20260506` — 413 MB Postgres dump from the Khoj index, relocated out of the repo during this hygiene pass. Probably irrelevant for the README, but if a recruiter asks "where's the actual data," it exists there.
- `~/khoj-data/notes/` **on the VM** — the live corpus. Not on Mac.

### Branch / push discipline
- Don't `git push` and don't open a PR. Hand drafts to Saboor.
- The `chore/portfolio-hygiene` branch contains the cleanup commits this orientation doc lives on. It hasn't been merged to `main` yet; Saboor will decide PR vs direct merge.

### One last thing
The `handoffs/` numbered system (`000-...md`, `001-...md`, ...) is the project's ground-truth log. It's the cleanest signal of "what's actually true *right now*" — much more reliable than `STATUS_AND_NEXT_STEPS.md` if the two diverge. The status doc updates intermittently; the handoffs are written every session.

If this orientation doc ever conflicts with a handoff numbered higher than 004, trust the handoff.
