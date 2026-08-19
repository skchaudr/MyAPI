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
