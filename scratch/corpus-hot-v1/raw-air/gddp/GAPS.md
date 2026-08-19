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
