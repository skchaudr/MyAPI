# Pi / Needle / Gemma — GAPS (mini pass-1)

## Why graphify / semantic alone would fail

- `~/.pi` is huge multi-purpose (agent, harness, needle, sessions, private). Full graphify mixes portfolio docs with operator PII and stale worktrees.
- Needle **observe-only** vs active routing is a policy fact in README/handoffs; embeddings of code alone won’t enforce it.
- Gemma/weights paths adjacent to docs — semantic “ingest models” risk without explicit denylist.
- Cross-host topology (mini Mac needle vs VM daemon) needs path + decision handoffs, not a single host graph.
- models.json secrets: any bulk index must strip `apiKey` / auth — this harvest redacts; naive reindex would leak.

## Still missing

- Air `~/.pi` / needle / gemma diff (air pass fills).
- Live daemon health (`pi-route --health`) not run this pass.
- Checkpoint contents and train metrics beyond ledger filenames.
- Full handoff series 007–032 needle topics (named, not all read).

## Ingest risks (explicit)

Do **not**: full-tree Khoj/graphify of `~/.pi`; ingest `checkpoints/`, `private/`, `auth.json`, raw sessions, nested worktrees, or secret values.

## Pass-1 stop

Scoped sources ≥5 · queries ≥8 · brief + ingest risks · no full .pi ingest · no commits.
