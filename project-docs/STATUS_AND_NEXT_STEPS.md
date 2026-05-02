# Status & Next Steps

**Last updated:** 2026-05-02

## TL;DR

MyAPI's pipeline is live and serving queries. Phase 1 (build the pipe) is closed; Phase 2 (trust calibration via a categorized query bank) is the current work. As of 2026-04-25, the trust-bank blocker set passes (F5/H4/A1/A2/A3/A7). Next session picks up the deferred queue.

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

## Pending queue

Ordered by leverage — small + high-info first:

1. **A4** — corpus-vs-metadata gap test on `CLAUDE.md`. ~10 min. If retrieval finds it but mislabels → metadata gap; if it can't find it → corpus gap.
2. **A7 terminology bridge** — query expansion: `broken|blocked → known issues|fail|gap|weak`. Closes the partial result on A7.
3. **H1–H3, H5** — human-lane regression check after the classifier patches.
4. **A5, A6** — meta-corpus + collaborator topology. Likely answer-shape gaps; produces build tasks, not fixes.
5. **F1–F4** — failure probes (time-scoped, negation, cross-entity, decision-recovery). Maps trust boundary; expect failures.
6. **Q18 dedicated end-to-end anchor** — `current-system-end-to-end-anchor.md`. A2 wins now via the my-devinfra anchor, but a dedicated one is cleaner.
7. **~27 obsidian files still missing from index** — per delta-patch report.
8. **`source: "unknown"` on anchors** — filenames lack the `obsidian-` prefix that `MetadataParser` uses for source inference. Anchors win without source/title boosts; fixing the prefix or parser would widen margins.
9. **F5 thin-margin (0.006) hardening** — paypal-recruiter note got an incidental "gold mine" token match. Not blocking, but flag if it inverts on future index churn.

## Live source documents

| File | What it has |
|---|---|
| `project-docs/My-API-Trust-Threshold-Plan.md` | Strategic frame: agent-cold-start product, three-category test |
| `project-docs/retrieval-benchmark-v0/Query/query-bank-trust-categorized-v1.md` | 17-query bank, diagnosis rubric, run protocol |
| `project-docs/retrieval-benchmark-v0/Harness evaluation/run-2026-04-25-blocker-pass.md` | Latest run results, what landed, open items |
| `project-docs/source-of-truth-anchors/` | Anchor docs the bank queries are tuned against |

## Where to start next session

Recommended scope: **A4 + A7 bridge + H1–H3** (~1 hour, regression check on classifier patches). After completion, update this file's "Pending queue" and add a new dated run note.

## A note on stale docs

Older `HANDOFF-*.md`, `VM-MIGRATION-*.md`, and `4.18.26.daily.project.md` files reflect Phase 1 (April 9–19) — VM migration, hybrid search, modular triage. Keep them for history; do not read them as current state.
