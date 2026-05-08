# MyAPI — Context Retrieval for AI Agents and Personal RAG

MyAPI is a context retrieval layer for AI agents and human operators. Instead of having Claude Code, Codex, or Cursor scan a project's files on every cold start, agents query MyAPI for the relevant context — decisions, prior work, architectural constraints, recent changes — and get back structured answers with reranked evidence in under 3 seconds.

Underneath, MyAPI indexes 3+ years of personal knowledge: Obsidian notes (~3,200 markdown files), exported ChatGPT and Claude conversations, and CLI agent session logs (Codex, Claude Code). A Python pipeline (`context_refinery/`) normalizes heterogeneous sources into canonical knowledge objects. Khoj provides semantic vector search; Context Refinery sits on top to handle query classification, multi-lane retrieval (semantic + keyword + synthesized-note boosting), metadata-aware filtering, and reranking.

The system is benchmarked, not vibes-tested. Retrieval quality is measured against a categorized query bank with seven diagnostic buckets (win, weak win, corpus gap, retrieval gap, metadata gap, intent gap, answer-shape gap). Corpus shaping and intent classification are the primary levers for improving results — not model swaps or hyperparameter tuning.

**Status:** Phase 1 (build the pipeline) is closed and deployed. Phase 2 (trust calibration via benchmark-driven refinement) is the active work.

---

## Quick Start

**Deploy the API locally:**

```bash
# Run on Mac:
GEMINI_API_KEY=your_key_here python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
PYTHONPATH=/path/to/MyAPI uvicorn api.main:app --reload --port 8000
```

**Query the live endpoint:**

Deployed on a cloud VM, accessed over Tailscale. The VM auto-shuts down after a few hours of inactivity to keep idle costs low; the operator starts it before benchmarking sessions.

```bash
# Run on Mac (with Tailscale up and the VM started):
curl -X POST http://[TAILSCALE_HOST]:8000/query \
  -H "Content-Type: application/json" \
  -d '{"query": "What is MyAPI and what is its current goal?"}'
```

**Run tests:**

```bash
# Run on Mac:
pytest tests/
```

---

## Table of Contents

- [Architecture](#architecture)
- [The Trust Calibration Model](#the-trust-calibration-model)
- [Notable Technical Decisions](#notable-technical-decisions)
- [Current Gaps and Roadmap](#current-gaps-and-roadmap)
- [The Handoff System](#the-handoff-system)
- [Source-of-Truth Anchors](#source-of-truth-anchors)
- [Testing](#testing)
- [Deployment](#deployment)

---

## Architecture

### The Problem

Every AI agent session starts the same way: the agent scans files, greps through logs, tries to infer project context from filenames and README fragments, and maybe hallucinates a few capabilities that don't exist. By the time the agent has enough context to do useful work, 30-90 seconds have elapsed, and the user has burned tokens on orientation rather than execution.

For personal knowledge retrieval, the problem is worse: conversations, notes, and logs pile up across ChatGPT exports, Obsidian vaults, and CLI agent session dumps. Semantic search returns plausible-but-wrong answers; keyword search floods you with noise; and no single tool understands that a ChatGPT thread from March is the episodic source for an Obsidian summary from April.

### The Solution

MyAPI is a **two-audience retrieval layer** over a unified personal corpus:

1. **Agent-facing:** structured `/query` endpoint returning reranked evidence with confidence scores, source metadata, and timestamps. Designed for cold-start context elimination and inter-agent handoffs.
2. **Human-facing:** episodic recall ("find that thread where I figured out X"), decision retrieval ("what did I decide about the vault schema"), and synthesis questions ("which projects mention both Khoj and Tailscale").

Same corpus, same retrieval pipeline, different response shapes.

### Core Components

**`context_refinery/` — The Python package this repo is built around**

- **`retrieval.py`** (1,383 lines) — multi-lane retrieval + reranking + intent classification. Three retrieval lanes:
  - Semantic (Khoj vector search)
  - Keyword (exact phrase + term matching with hyphen/space/no-space normalization)
  - Synthesized-note boost (prior for canonical anchors, guarded against chat-dump sources)
- **`adapters/`** — five source adapters (`chatgpt.py`, `claude.py`, `claude_code.py`, `codex.py`, `obsidian.py`) that parse heterogeneous exports into normalized documents with YAML frontmatter.
- **`enrichment.py`** — Gemini-1.5-Flash-backed batch enrichment (max 50 docs/request). Extracts tags, projects, key assertions, and summaries from raw conversation logs.
- **`sanitization.py`, `exporter.py`, `models.py`, `services.py`, `triage/`** — supporting modules for normalization, metadata validation, and diagnostic triage.

**`api/` — FastAPI service**

- **`main.py`** — three routers: `/enrich`, `/import`, `/query`, plus `/health`.
- **`routers/query.py`** — the agent-facing endpoint. Accepts `{"query": "...", "source_filter": [...], "n": 10}`, returns structured JSON with reranked results, metadata, and retrieval diagnostics.

**Deployment**

- Khoj search backend: port `42110`, systemd `khoj.service`
- MyAPI (Context Refinery): port `8000`, systemd `context-refinery.service`
- Corpus: `~/khoj-data/notes/` on the VM (~3,201 non-empty `.md` files)
- **No auth.** Tailscale-only service; trust boundary is the network.

---

## The Trust Calibration Model

**MyAPI's quality claim is grounded in a categorized query bank, not vibes.**

The benchmark (`project-docs/retrieval-benchmark-v0/Query/benchmark-v0.md`) contains 18 queries across multiple intent classes:

- **Project identity** — "What is MyAPI and what is its current goal?"
- **Temporal recall** — "What was I working on around the time I was debugging Tailscale?"
- **Source-specific recall** — "Find the Claude Code session where I set up the web adapter."
- **Decision recall** — "What did I decide about the vault schema?"
- **Operational recall** — "What's broken or blocked in MyAPI right now?"
- **Synthesis** — "What docs should I use to understand the current system end to end?"

Each query is diagnosed with one of **seven failure buckets:**

1. **Win** — correct answer at #1-3, high confidence
2. **Weak win** — correct answer present but low margin or buried below noise
3. **Corpus gap** — documented evidence doesn't exist
4. **Retrieval gap** — evidence exists but candidate-set selection or ranking missed it
5. **Metadata gap** — evidence exists but source/title/tag metadata is insufficient to route correctly
6. **Intent gap** — query classifier misrouted (e.g., operational query routed to project-overview intent)
7. **Answer-shape gap** — retrieval succeeds but response format doesn't match the question's implicit contract

**The rubric forces diagnosis at the lowest-leverage layer first.** Don't patch the reranker when the real issue is a missing anchor doc. Don't add vocabulary synonyms when the query intent is being misclassified. Don't expand candidate sets when the answer is a corpus gap.

Fixes are tracked in numbered session handoffs (`handoffs/000-004`) and acceptance runs (`scripts/acceptance.py`). The acceptance harness is a mechanical test against the live `/query` endpoint with gold-document assertions per query.

Current acceptance state: **6/7 mechanical. A1 is a known bank-evolution question** — the status anchor currently wins the project-overview query, and whether that's correct depends on Corpus v1 normalization (active Phase 2 work). **A7** is the active retrieval-quality investigation (subject-scope gap diagnosed; fix is anchor authoring, not retrieval changes). The remaining five queries pass.

The acceptance harness lives in `scripts/acceptance.py`; per-run details and current state are in `handoffs/` (most recent: `003-final-v0-benchmark-run.md`).

---

## Notable Technical Decisions

**1. Three retrieval lanes, OR'd, with a synthesized-note prior** (commit `5d713ab`)

The semantic lane alone couldn't distinguish between a canonical anchor doc and a noisy ChatGPT thread that happened to mention the same terms. The keyword lane closes exact-phrase queries. The synthesized-note prior gives a `+0.14` boost to docs with frontmatter tags like `document_kind: synthesized_note` or titles containing "anchor|summary|overview." The prior is **guarded** against chat-dump sources (chatgpt/claude/claude-code/codex) so a synthesized summary doesn't outrank real anchors when the query is about a chat thread.

**2. Operational-vs-Project classifier reorder** (commit `5d713ab`)

OPERATIONAL intent fires before PROJECT so a query like "MyAPI is broken" routes to operational intent rather than project-explainer intent. Operational verbs (`broken|blocked|failing|stuck|...`) are recognized before project-name detection.

**3. Exact-phrase boost with hyphen/space/no-space normalization** (commit `28a22b0`)

Closes the F5/H4 exact-term sentinel pair without overfitting. When a query contains quoted phrases like `"gold mine"`, the reranker normalizes both the query and document text to handle `gold mine`, `gold-mine`, and `goldmine` as equivalent. Phrase matches get a `+0.45` score boost.

**4. Keyword lane skips bare-term filter when phrases are present** (commit `28a22b0`)

The keyword lane was requiring every bare term in a query to appear in the document body, even when a quoted phrase was present. Long-sentence phrase queries silently dropped the answer document from the candidate set. Fix at `context_refinery/retrieval.py:269`: `not phrases and terms and ...`

**5. No idempotency, by design**

`/enrich` and `/query` are stateless. Clients dedupe themselves if needed. MyAPI doesn't track "have I seen this query before" — caching is upstream (agent harness layer) or downstream (Khoj's internal cache), not here.

**6. Append-only logs with `AUTOINCREMENT` ids throughout**

The benchmark wants stable references to specific runs and specific anchor docs. Never reuse ids.

---

## Current Gaps and Roadmap

**What works (functional, tested, used in production):**

- Multi-lane retrieval + reranking on ~3,200 indexed documents
- Intent classification (factual / lookup / operational / project_overview)
- Source-aware metadata parsing for five adapter types
- Batch ingestion (`ingest_all.py`) and deploy automation (`deploy_to_khoj.sh`)
- 13 test files (retrieval, enrichment, sanitization, modular triage, per-adapter tests)
- Mechanical acceptance harness (`scripts/acceptance.py`)

**What's intentionally incomplete / out of scope:**

- **~27 Obsidian files still missing from the Khoj index** per delta-patch report. Tracked, not blocking.
- **Acceptance harness has one bank-evolution question (A1) and one active retrieval investigation (A7).** See *The Trust Calibration Model* for the canonical state and rationale; per-run detail in `handoffs/`.
- **No auth on MyAPI.** It's a Tailscale-only service; trust boundary is the network.

**Active work (Phase 2 — trust calibration):**

- Corpus v1 normalization — `source_type` taxonomy, folder-derived metadata, temporal routing
- Extend the query bank to ~30 queries covering agent-cold-start and episodic-recall axes
- Field-test retrieval quality with fresh cold-start agents (no memory/handoff beyond "use MyAPI first")
- Build a "best practices, not perfect practices" polish pass

---

## The Handoff System

**Every session leaves a numbered handoff** in `handoffs/000-*.md`, `handoffs/001-*.md`, etc. Each handoff contains:

- **Empirical Reality** — what scope was touched, what commits landed, what the acceptance set state is, what verifications ran
- **Resume Point** — next session's entry point with explicit load-bearing context
- **Narrative / Trajectory** — intent, interpretation, tension, momentum (operator's reflection)

The handoff system is load-bearing. It's the cleanest signal of "what's actually true *right now*" — more reliable than `STATUS_AND_NEXT_STEPS.md` if the two ever diverge (status doc updates intermittently; handoffs are written every session).

Read them in order:

- **000** — F5 phrase-lane fix, A7 initial diagnosis, acceptance harness creation
- **001** — A7 anchor variant fix (hyphen/space/no-space normalization), episodic-vs-meta axis design realization
- **002** — F5 episodic gold-doc swap, S1 schema filter test, `source_type` taxonomy plan alignment
- **003** — Final v0 benchmark run prep (bank refinement, not sweep architecture)
- **004** — Corpus v1 field-test realization, two-audience endpoint framing, "do not normalize toward anchors always win"

If this README ever conflicts with a handoff numbered higher than 004, trust the handoff.

---

## Source-of-Truth Anchors

Four canonical anchor docs in `project-docs/source-of-truth-anchors/`:

- **`khoj-deployment-indexing-anchor.md`** — Khoj backend deployment, corpus size, indexing mechanics
- **`my-devinfra-system-anchor.md`** — dev infrastructure topology (Mac, VM, Tailscale, GCP, systemd services)
- **`myapi-status-anchor.md`** — current open issues, recently closed issues, failure modes (targets benchmark query A7)
- **`vm-tailscale-ssh-access-anchor.md`** — VM SSH mechanics, gcloud IAP, Tailscale IP, auto-shutdown behavior

These are the canonical context the benchmark queries are tuned against. Agents should query MyAPI for these before grep'ing.

---

## Command Discipline

Per `AGENTS.md` and `CLAUDE.md`, every command needs a location label:

- **Run on Mac:** local workstation
- **Run in VM shell:** after SSH into the VM
- **Run in Cloud Shell:** Google Cloud Shell
- **Run on VM:** gcloud command targeting the VM but executed from Mac

Never give multi-line `-c` python commands (they break in zsh). Write a temp script or use semicolons. Never use `$(cat file | tr '\n' ' ')` when paths contain spaces. Set `PYTHONPATH=/path/to/MyAPI` when running scripts outside the repo directory.

---

## Testing

**Run the full test suite:**

```bash
# Run on Mac:
cd /path/to/MyAPI
pytest tests/
```

**Run the acceptance harness against the live VM:**

```bash
# Run on Mac:
python3 scripts/acceptance.py
```

See *The Trust Calibration Model* above for the canonical acceptance state and the per-query interpretation. Per-run scores are recorded in `handoffs/`.

**Key test files:**

- `tests/test_retrieval.py` (27 KB, 13 test methods) — multi-lane retrieval, reranking, intent classification
- `tests/test_triage_modular.py` (14 KB) — diagnostic triage and metadata validation
- `tests/test_chatgpt.py`, `test_claude_code.py`, `test_codex.py`, `test_obsidian.py` — per-adapter normalization tests

---

## Deployment

**Deploy script:**

```bash
# Run on Mac:
./deploy_to_khoj.sh
```

The script:
1. Syncs `context_refinery/` and `api/` to the VM via `gcloud compute scp`
2. Restarts `context-refinery.service` on the VM
3. Verifies `/health` responds at `http://[IP_ADDRESS]:8000/health`

**Corpus ingestion:**

```bash
# Run on Mac:
python3 ingest_all.py --output-dir ./khoj-ready-bundle

# Then sync to VM and reindex (see deploy_to_khoj.sh for mechanics)
```

**Systemd services on the VM:**

- `khoj.service` — Khoj backend on port `42110`
- `context-refinery.service` — MyAPI FastAPI app on port `8000`

---

## References

**Core documentation:**

- `project-docs/STATUS_AND_NEXT_STEPS.md` — canonical "where are we" doc (last updated 2026-05-02)
- `project-docs/My-API-Trust-Threshold-Plan.md` — strategic / product frame (agent-facing vs human-facing two-audience model)
- `project-docs/retrieval-benchmark-v0/Query/benchmark-v0.md` — 18-query bank with intent classes
- `project-docs/retrieval-benchmark-v0/Harness evaluation/run-2026-05-02-tighten-pass.md` — most recent full run with margins
- `handoffs/000-004` — session handoffs (sequential reality, 2026-05-03 through 2026-05-05)

**Code entry points:**

- `api/main.py` — FastAPI app (~30 LOC)
- `context_refinery/retrieval.py` — multi-lane retrieval + reranker + intent classifier (1,383 lines)
- `ingest_all.py` — batch ingestion entry point
- `scripts/acceptance.py` — mechanical acceptance harness
- `tests/` — 13 test files

---

## License

MIT — see LICENSE file.

---

## Author

Built by Saboor Chaudry.

This project began with a simple realization: years of notes in Obsidian, exported conversations from ChatGPT, Anthropic's Claude, and Google's Gemini already contained the context needed for long-term memory, agent handoffs, and personal retrieval — but there was no reliable system for taking it from raw corpus to actionable, structured, and trusted recall.

MyAPI is my response to that problem. It reflects an ongoing push toward the technical frontier of multi-agent orchestration, auditable agent dispatch, and context retrieval systems. The scope and growing relevance of this problem demanded that benchmark-driven refinement, heterogeneous corpus normalization, and trust calibration be treated as first-class engineering concerns.

For questions, reach out via GitHub or sbkchaudry@gmail.com.
