# gddp / GAPS — merged v1

Date: 2026-07-29
Mini = repo/prod bias. Air = vault/operator bias. Both kept as evidence.

---

## From mini

# GDDP — GAPS (mini pass-1)

## Why graphify / semantic alone would fail

- Ownership is **cross-repo**; a single-repo graphify of runtime or config alone loses the “who may write truth” rule.
- GRAPH_REPORT hubs are code labels (reconciler.py, etc.) — they do not encode the human-acceptance invariant.
- Job state vs graph state look similar in prose; without AGENTS.md rules, agents silently “complete” nodes from PR merges.
- Practice graphs vs live graphs vs verification-runtime paths need path discipline files give; semantic blend muddies them.
- No reindex this pass — dated graphify-out folders may lag HEAD.

## Still missing

- Air-side GDDP state (clone lag? vault notes? sessions) — expected thinner; truth remains mini.
- Deep walk of every `graphs/<project>/` node set (only ownership + samples harvested).
- Live heartbeat / SQLite now-state (ops, not corpus-hot).
- Full adapter matrix beyond Jules mention in README.

## Pass-1 stop

Ownership pair covered · sources ≥5 · queries ≥8 · brief + gaps. No commits / reindex.


---

## From air

# GDDP — GAPS (air)

## Why graphify / semantic would fail alone
- graphify-out on both repos is **code symbol soup** (e.g. `_json_stdout`, `has_authorization`) — dense, not the human project graph in `gddp-config/graphs/`.
- Semantic search over README fragments without the ownership sentence (“config owns graph; runtime does not mutate truth”) yields tool-shaped wrong answers.
- Production topology (ports, launchd, webhook) is operational prose; graphify won’t surface “who runs intake.”

## Still missing / weaker on air
- Live **queue.db**, launchd status, webhook secret material — production on **mini** (air may lack runtime state).
- Deep read of every `graphs/` project folder content (inventory only this pass).
- Evaluator canary proof docs exist under `docs/` — not fully folded into brief.
- Stage1 repo (`gddp-config-stage1`) role vs main config not adjudicated here.

## Air-unique vs mini
- Air: rich Claude/Codex session trail + flashcards + both repos checked out on main.
- Mini (per TOPOLOGY): production intake, heartbeat, pass/GPG, Funnel URL — **truth for live ops**.

