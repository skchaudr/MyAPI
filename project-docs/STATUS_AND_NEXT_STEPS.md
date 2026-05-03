# Status & Next Steps

**Last updated:** 2026-05-02 (post tighten-pass)

## TL;DR

MyAPI's pipeline is live and serving queries. Phase 1 (build the pipe) is closed; Phase 2 (trust calibration via a categorized query bank) is the current work. The 2026-05-02 tighten pass surfaced two real findings: A7 is a **subject-scope gap** (not a terminology gap, as initially thought), and F5 **regressed at the candidate-set layer**. H4 sentinel held with a wider margin; H-lane regression check completed without new code-layer issues.

## Strategic frame

MyAPI is a context retrieval layer over Saboor's personal corpus (Obsidian notes, exported LLM conversations, CLI agent session logs). It serves two audiences from the same substrate:

- **Human retrieval (Saboor):** "find me that thread," "what did I decide about X," "when was I last working on Y." Personal episodic memory — wants source links and narrative.
- **Agent retrieval (Claude Code, Codex, etc.):** structured context at the start of a session so agents stop grep'ing around to figure out what's going on. Wants assertions and shape.

Same corpus, same Khoj + Context Refinery pipeline, different response shapes. The trust-threshold plan (`My-API-Trust-Threshold-Plan.md`) frames the agent angle as the sharper positioning story for an outside audience, but both audiences are first-class — the query bank's H and A categories prove it.

Trust is built per query class via a benchmarked query bank (`retrieval-benchmark-v0/Query/query-bank-trust-categorized-v1.md`). Each query is diagnosed with one of seven buckets — `win`, `weak win`, `corpus gap`, `retrieval gap`, `metadata gap`, `intent gap`, `answer-shape gap` — and fixes target the lowest-leverage layer first.

## Current deployment

- **VM:** `instance-20260418-024637`, zone `us-central1-a`, project `project-ab32182e-5782-4a9c-939`
- **Auto-shutdown:** 3 hours. The VM is typically off between sessions — start it before any retrieval test.
- **SSH (gcloud IAP):** `gcloud compute ssh --zone us-central1-a --project project-ab32182e-5782-4a9c-939 instance-20260418-024637`
- **Tailscale IP:** `100.85.100.52` (alias `khoj-vm-new`)
- **Khoj:** port `42110`, systemd `khoj.service`
- **Context Refinery (MyAPI):** port `8000`, systemd `context-refinery.service`
- **Corpus:** `~/khoj-data/notes/`, ~3,201 non-empty `.md` files

## Phase 2 — what's closed (2026-04-25)

The trust-bank "blocking-tonight" set passes. Three retrieval.py patches deployed and committed (`5d713ab`):

1. **Exact-phrase boost** with hyphen/space/no-space normalization — closes the F5/H4 exact-term regression sentinel pair.
2. **Classifier + alias patch** — MyAPI is now a first-class project name (added to `_PROJECT` regex, specialized anchor bonus, anchor-terms expansion, query expansion); operational verbs (`broken|blocked|failing|...`) added; classifier reordered so OPERATIONAL fires before PROJECT.
3. **Synthesized_note guard** — chat-dump sources (chatgpt/claude/claude-code/codex) excluded from the loose `\b(anchor|summary|overview|...)\b` regex that grants the +0.14 synthesized_note prior.

Result detail and margins in `retrieval-benchmark-v0/Harness evaluation/run-2026-04-25-blocker-pass.md`.

## Tighten pass (2026-05-02)

H-lane regression check + A7 re-diagnosis. Full results in `retrieval-benchmark-v0/Harness evaluation/run-2026-05-02-tighten-pass.md`.

- **H4 sentinel held**, margin widened (fs=0.838, +0.371 over #2 — much wider than 04-25's +0.068).
- **A7 vocab-bridge patch deployed but no-op** — eval notes are subject-scoped to "retrieval benchmark," not "MyAPI"; vocab expansion can't pull them into the candidate set when the query subject is MyAPI. Patch kept deployed (small surface, no negative effect on H4).
- **F5 regressed**: Trust-Threshold plan absent from top 20 for the full-sentence query; bare `"gold mine"` still surfaces it at #1 (ks=0.87). Candidate-set/Khoj-layer issue, not reranker.
- **H1/H2/H3 failures are pre-existing** and acceptable severity per the bank — no new code-layer regressions from the 04-25 classifier patches.

## Pending queue

Ordered by leverage — small + high-info first:

1. **A7 real fix — `myapi-status-anchor.md`** — build a status anchor enumerating current open items. Closes A7 via subject-scope alignment (the path the no-op vocab patch couldn't take). Aligns with agent-cold-start framing.
2. **F5 candidate-set fix** — Khoj-layer regression. Either expand retrieval `n` before reranking, or add a phrase-aware retrieval lane that bypasses semantic similarity for exact-phrase matches. Bigger lift than vocab.
3. **A4** — corpus-vs-metadata gap test on `CLAUDE.md`. ~10 min. If retrieval finds it but mislabels → metadata gap; if it can't find it → corpus gap.
4. **H1 intent re-routing** — bank says human-find-thread should route to lookup, not operational. Currently OPERATIONAL fires first and grabs queries like "find the thread where I set up the Khoj VM migration." Small classifier tweak.
5. **H2 corpus check** — does a `source-aware-priors` design note exist? If yes → retrieval gap; if no → corpus gap. Decides next move.
6. **A5, A6** — meta-corpus + collaborator topology. Likely answer-shape gaps; produces build tasks, not fixes.
7. **F1–F4** — failure probes (time-scoped, negation, cross-entity, decision-recovery). Maps trust boundary; expect failures.
8. **Q18 dedicated end-to-end anchor** — `current-system-end-to-end-anchor.md`. A2 wins now via the my-devinfra anchor, but a dedicated one is cleaner.
9. **~27 obsidian files still missing from index** — per delta-patch report.
10. **`source: "unknown"` on anchors** — filenames lack the `obsidian-` prefix that `MetadataParser` uses for source inference. Anchors win without source/title boosts; fixing the prefix or parser would widen margins.

## Live source documents

| File | What it has |
|---|---|
| `project-docs/My-API-Trust-Threshold-Plan.md` | Strategic frame: agent-cold-start product, three-category test |
| `project-docs/retrieval-benchmark-v0/Query/query-bank-trust-categorized-v1.md` | 17-query bank, diagnosis rubric, run protocol |
| `project-docs/retrieval-benchmark-v0/Harness evaluation/run-2026-05-02-tighten-pass.md` | Latest run — H-lane + A7 re-diagnosis + F5 regression |
| `project-docs/retrieval-benchmark-v0/Harness evaluation/run-2026-04-25-blocker-pass.md` | Previous run — blocker set close + 3 retrieval.py patches |
| `project-docs/source-of-truth-anchors/` | Anchor docs the bank queries are tuned against |

## Where to start next session

Recommended scope: **build `myapi-status-anchor.md` + re-run A7** to verify subject-scope fix, then take one of (F5 candidate-set fix, H1 intent re-route, A4 corpus test) as a second task. After completion, update this file's "Pending queue" and add a new dated run note.

## A note on stale docs

Older `HANDOFF-*.md`, `VM-MIGRATION-*.md`, and `4.18.26.daily.project.md` files reflect Phase 1 (April 9–19) — VM migration, hybrid search, modular triage. Keep them for history; do not read them as current state.
