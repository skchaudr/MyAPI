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
