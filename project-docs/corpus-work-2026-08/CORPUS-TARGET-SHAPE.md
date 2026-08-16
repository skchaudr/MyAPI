# Corpus target shape (Sab 2026-08-08/09)

## North star — QUERIES ground everything

All corpus work (what to keep, strip, promote, index, extract, eval) is judged by:

- `scratch/corpus-hot/myapi/QUERIES.md`
- `scratch/corpus-hot/gddp/QUERIES.md`
- `scratch/corpus-hot/pi-needle-gemma/QUERIES.md`

(VM mirrors under `~/khoj-data/notes/corpus-hot-v1-*-QUERIES.md` and `/data/corpus-hot/v1/*/QUERIES.md`.)

**Rule:** If a note/session/decision does not help answer those questions, it is optional noise. If it does, it is in-scope. Acceptance = `/query` (or agent) can answer the query set from the corpus.

## In
- In-repo project docs worth keeping (README, PROJECT-BRIEF, AGENTS.md, high-value project-docs) + `.handoffs` + stray high-value repo docs
- **Recent** agent CLI sessions that are context/decision-rich → clean UA markdown for human value-mark → later **decisions only**
- Golden briefs / anchor notes
- **Few** AI conversations (majority noise)
- Graphify artifacts (reports / query dumps) optional, small
- **Git history as truth layer** — commit IDs, branches, event linkage on decisions; diffs via graphify later; keep surface small

## Out
- Full Obsidian vault dumps
- Bulk chat exports
- Full eternal session archives in the hot index

## Eval
Graphify-style agent questions: "does the corpus answer this?"

## Steady state
Corpus grows with the three projects; session path collapses to decision extraction + git receipts — not infinite transcript retention in Khoj.
