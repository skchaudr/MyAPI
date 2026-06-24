# 003 — Final v0 benchmark run

Date: 2026-05-04
Branch: main

## Empirical Reality

Scope touched:
- Deleted `project-docs/retrieval-benchmark-v0/Query/query-bank-trust-categorized-v1.md` — Sab confirmed it was a complexity layer on top of the canonical `benchmark-v0.md`, not the bank itself. Removed.
- Copied `benchmark-v0.md` → `benchmark-v1.md` in the same folder. v1 is byte-identical to v0; reserved as the in-place refinement target for the corpus-normalization-v1 work.
- Deleted two mid-session scaffolds created under a misguided 3-phase Phase-0 plan that Sab rejected: `project-docs/retrieval-benchmark-v1/diagnostic-sweep-2026-05-04.md` (and its empty parent dir), and `~/.claude/projects/-home-sab-ssd-repos-MyAPI/memory/feedback_query_authorship.md` (a premature memory save).
- VM not touched. No `/query` calls. Acceptance harness state unchanged from 002 — 6/7 mechanical, A1 known-fail.
- Out-of-tree reference: `~/.claude/plans/velvet-yawning-eich.md`, the rejected 3-phase plan, kept on disk as a record of the misread (treating the task as a sweep architecture rather than surgical bank refinement).

Current state:
- `benchmark-v1.md` exists, identical to v0, no edits applied.
- Git status: `D project-docs/retrieval-benchmark-v0/Query/query-bank-trust-categorized-v1.md`, `?? project-docs/retrieval-benchmark-v0/Query/benchmark-v1.md`. Uncommitted.
- 8 commits from 002 still unpushed; this session adds no commits.

Artifacts:
- No commits this session.
- Pending commit: 1 file deleted, 1 file added.

Resume point:
- Walk `benchmark-v1.md` top-down, query 1 → 18. For each, classify keep / rewrite / delete / unsure. Edit in place only after Sab's word-for-word approval per query — no synthetic AI phrasings, no multiple-choice menus for query authorship.
- Apply Sab's taxonomy as a column: **known-answer retrieval / existence check / synthesis / operational recall / pattern extraction.**
- Apply Sab's 6-outcome grading scheme: **right artifact / wrong-but-useful / stale / meta-eclipse / missing canonical / synthesis-needed.**
- Load-bearing principle: **null answers count as correct passes** when no documented evidence exists. Worked example Sab gave: "What friction am I facing in Neovim?" (silently assumes documented Neovim friction — returns plausible-but-wrong setup docs and gets graded as a pass) → "Have I documented any friction in Neovim?" (null is a valid pass).
- Likely first offenders to inspect: query #4 (Neovim friction), #8 (vault schema decision), #14 (semantically related notes / clean-up passes) — all have the silent-assumption shape. Validate per query against Sab.
- Target ~30 queries total in v1 (current 18 + ~12 to cover taxonomy gaps).
- Once v1 stabilizes, run it against the current corpus → produces the actual "final v0 benchmark run" data → that data is the blueprint for corpus normalization v1 (source_type taxonomy plan + ingestion priorities).
- VM auto-shutdown 3h; confirm VM is up before any retrieval calls. Tailscale IP `100.85.100.52:8000`.

## Narrative / Trajectory

Intent: Validate whether or not a V1 normalization of corpus needed to be done immediately or after a highly targeted benchmark meant to validate trust  
Interpretation: I was finally able to understand how agent confabulation works and notice that some of the benchmark questions are terrible questions because they're not actually things that ever happen and so their data wouldn't be in the set. I realized that our tests didn't account for this reality that something could not be present in the set. At least my understanding of it was that we were not actively testing for that outcome or reality 
Tension: Coming up with a meaningful question set that actually corresponds to, for the most part, data in the corpus without being too broad or too generalized but without being too hyper-specific either 
Momentum: The questions the benchmarks should realistically be anywhere from five to ten targeted high-quality. "This exposes how good this is running" 
