# 002 — F5 episodic + S1 schema + source_type design alignment

Date: 2026-05-04
Branch: main

## Objective Reality (Agent ONLY)

Scope touched:
- Modified: `scripts/acceptance.py` — F5 gold-doc swapped to `claude-web-converting-opclaw-to-final-system-repo.md` (episodic source thread, not the meta-doc). Adds `request_filters` plumbing on entries + new S1 entry exercising `sources=["claude-code"]` against the API filter contract.
- Modified: `api/schemas.py:10` — `SourceSystem` Literal now includes `claude-code` (was the only gap; `claude-code` already used in `retrieval.py` and tests). VM `/data/repos/MyAPI/api/schemas.py` synced via gcloud scp to `/tmp/schemas.py` then sudo cp'd into place; `context-refinery.service` restarted.
- New: `project-docs/source-type-taxonomy-plan.md` — design artifact for the next-session Lane 3 work (source_type-at-ingestion guardrail per the standard-RAG #1 framing).

Current state:
- Acceptance: **6/7 mechanical · 0 skipped**
- A1 FAIL (known, unchanged from 001) — `myapi-status-anchor.md` wins by 0.002 over `obsidian-myapi-anchor.md`. **Real diagnosis** (re-run this session, supersedes 001's "candidate-set indexing gap" hypothesis): `my-devinfra-system-anchor.md` IS indexed (fs=1.19 #1 on direct "devinfra" query), but Khoj only returns 8 candidates total for the A1 query, and the devinfra anchor's embedding has low semantic similarity to "What is MyAPI and what is its current goal?" — the doc isn't *about* MyAPI or goals. A1 is a bank-evolution question, not an indexing bug.
- A3, H4, F5, H1, A7, S1 all PASS
- 8 commits on `main`, **unpushed** (5 carried from 001 + 3 from this session)

Artifacts/deliverables (this session):
- `43b0f82` fix(api): allow claude-code in SourceSystem filter literal
- `f74f3f2` feat(benchmark): F5 gold-doc points at episodic source thread
- `f183211` feat(benchmark): S1 schema-filter sanity test for claude-code source
- (carryover from 000/001) `ccd58f4`, `28a22b0`, `5b847ea`, `a81da20`, `497afc4`

Verifications run:
- F5: `claude-web-converting-opclaw-to-final-system-repo.md` @ #3, fs=0.867 → PASS
- S1: `claude-code` source filter accepted (would 422 pre-fix), top result is a claude-code doc fs=1.349 → PASS
- A1 candidate probe: `n=30` returns only 5 results, `total_from_khoj=8`; devinfra anchor not in candidate set
- A1 devinfra-direct probe: query "devinfra system anchor" returns devinfra anchor #1 fs=1.19 (proves it's indexed)

Resume point:
- (push) **8 commits awaiting `git push origin main`** — held for Sab approval per his discipline ("not complete until brought into main"). Push is the only hard-to-reverse item on the queue.
- (Lane 3) **`source_type` ingestion guardrail** — design artifact at `project-docs/source-type-taxonomy-plan.md`. Aligned with Sab this session: stamp every doc with `source_type` at ingestion (folder-derived), wire intent → source_type weights at query time. This subsumes the `recall_type` framing from 001's episodic-vs-meta memory; folder taxonomy is the cleaner carrier than new frontmatter.
- (A1) **bank refresh per source_type** — once Lane 3 lands, A1's gold list should be re-evaluated. Status anchor winning A1 may be correct post-corpus-evolution. Defer A1 fix until source_type weights exist to give project_overview intent its own routing.
- (process) Add `references_events: [...]` lineage on meta-docs as a Lane 3 follow-on (still useful, just downstream of the directory-as-taxonomy move).
- VM auto-shutdown 3h; confirm VM is up before next acceptance run.

Open questions for Sab (non-blocking):
- Push 8 commits now, or batch with Lane 3's first commit next session?
- For source_type taxonomy: is the folder structure on the corpus side already stable enough to be the canonical signal, or do you want to re-organize first?

## Narrative / Trajectory (Sab ONLY)

_**Note to self (delete when filling in):** Per the convention from 001, Sab section is being drafted in Obsidian. Vault is sync'd here. Inline + delete this note when you fill in._

Intent:
Interpretation:
Tension:
Momentum:
