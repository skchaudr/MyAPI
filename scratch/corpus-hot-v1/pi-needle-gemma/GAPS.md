# pi-needle-gemma / GAPS — merged v1

Date: 2026-07-29
Mini = repo/prod bias. Air = vault/operator bias. Both kept as evidence.

---

## From mini

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


---

## From air

# Pi / Needle / Gemma — GAPS (air)

## Why graphify / semantic would fail alone
- `~/.pi/graphify-out` (if used) is code-level; won’t encode Camber **human gates** or multi-host routing policy.
- Needle has huge training/shadow/quarantine surfaces — semantic “find gemma” returns dumps, not the ledger contract.
- Model **weights** and `auth.json` are high-risk false positives for any auto-ingest.

## What’s missing / unclear this pass
- Side-by-side **mini-only** confirmation (this machine is air; both may share user home layout via Sync — production GDDP still mini).
- Live whether `needle serve` / launchd plist is loaded right now (path inventoried; service state not probed).
- Full models.json provider→gemma mapping details intentionally shallow (keys only, no secret-bearing expand).
- Sibling repos `~/repos/needle`, `mac-needle` not deep-harvested.

## Ingest risks (explicit)
Do **not** swallow: entire `~/.pi`, `agent/auth.json`, ollama blobs, `needle/training/*.jsonl`, quarantine backups, shadow corpora, hf-datasets under agent/data. Prefer: PROJECT-BRIEF, needle README, ledger, schemas/manifests, selected handoffs, vault plans.

## Air strength
- Local needle-gemma-v1 bundle + ledger + harness + vault postmortem/plan + agent model config paths all on this host.

