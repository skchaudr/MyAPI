# Retrieval Benchmark - Post Anchor V2

Run timestamp: `2026-04-23`

Context: Three source-of-truth anchor notes were strengthened from v1 to v2 and indexed into Khoj. This is the first benchmark run with all three anchors in the vector index.

## Anchor Results

| # | Query | Intent | After filter | From Khoj | Top results |
|---|---|---|---:|---:|---|
| 1 | What is My_DevInfra? | project_overview | 4 | 10 | unknown:my-devinfra-system-anchor.md<br>obsidian:obsidian-usr-anchor.md<br>claude-code:claude-local-command-caveatcaveat-the-messages-below-were-generated-6d8ab6da.md<br>codex:codex-help-me-set-up-on-all-three-devices-the-shortcuts-described--019cfbbb.md |
| 10 | What notes mention Khoj deployment or indexing? | operational | 1 | 10 | unknown:khoj-deployment-indexing-anchor.md |
| 12 | What is the status of the API deployment? | operational | 4 | 10 | unknown:khoj-deployment-indexing-anchor.md<br>unknown:vm-tailscale-ssh-access-anchor.md<br>claude-code:claude-local-command-caveatcaveat-the-messages-below-were-generated-2a98a9e1.md<br>claude-code:claude-local-command-caveatcaveat-the-messages-below-were-generated-a476a891.md |
| 16 | What notes are tied to Tailscale, SSH, or VM access? | operational | 3 | 10 | unknown:vm-tailscale-ssh-access-anchor.md<br>unknown:khoj-deployment-indexing-anchor.md<br>claude-code:claude-local-command-caveatcaveat-the-messages-below-were-generated-a476a891.md |
| 18 | What docs should I use to understand the current system end to end? | synthesis | 36 | 10 | chatgpt:chatgpt-dispatch-pipeline-handoff.md<br>chatgpt:chatgpt-opencode-overview.md<br>chatgpt:chatgpt-dashboard-setup-guide.md<br>chatgpt:chatgpt-walletconnect-resolv-overview.md<br>claude:claude-web-task-system-integration-handoff-document.md |

## Full Run

| # | Query | Intent | After filter | From Khoj |
|---|---|---|---:|---:|
| 1 | What is My_DevInfra? | project_overview | 4 | 10 |
| 2 | What have I been working on recently? | temporal | 38 | 9 |
| 3 | What was I doing around the time I was debugging Tailscale? | temporal | 12 | 8 |
| 4 | What keeps showing up as friction in my Neovim workflow? | factual | 25 | 10 |
| 5 | Find the Claude Code session where I set up the web adapter. | source_specific | 7 | 10 |
| 6 | Find the ChatGPT export note about iTerm2 and shell setup. | source_specific | 20 | 6 |
| 7 | What was I learning about retrieval systems? | synthesis | 24 | 10 |
| 8 | What did I decide about the vault schema? | decision | 29 | 8 |
| 9 | Which notes discuss tagging strategy and taxonomy? | meta | 8 | 9 |
| 10 | What notes mention Khoj deployment or indexing? | operational | 1 | 10 |
| 11 | What notes are about Claude, Codex, and Jules working together? | cross_source | 17 | 10 |
| 12 | What is the status of the API deployment? | operational | 4 | 10 |
| 13 | Show me notes about my Obsidian folder schema. | source_specific | 37 | 9 |
| 14 | What did I write about semantically related notes and clean-up passes? | meta | 4 | 8 |
| 15 | What are the strongest notes for a retrieval benchmark? | factual | 8 | 9 |
| 16 | What notes are tied to Tailscale, SSH, or VM access? | operational | 3 | 10 |
| 17 | Which notes are about prompts, schemas, or evaluation rubrics? | meta | 7 | 10 |
| 18 | What docs should I use to understand the current system end to end? | synthesis | 36 | 10 |

## Analysis

### Wins (vs run-2026-04-19-source-aware-priors baseline)

- **Q1**: `my-devinfra-system-anchor.md` now #1 (was not in top 5). Margin thin — 1.297 vs 1.288.
- **Q10**: `khoj-deployment-indexing-anchor.md` now #1 and only result after filter (was raw claude/codex logs).
- **Q12**: Both anchors top 2 (was daily note + raw logs).
- **Q16**: Both anchors top 2 (was raw claude log #1).

### Known issues

- All three anchors show `source: "unknown"` because filenames lack the `obsidian-` prefix that the MetadataParser uses to infer source. They're winning without source/title boosts — fixing the filename or parser would widen the margin.
- Q1 margin is razor thin (0.009 gap). Fragile against corpus changes.
- Q18 still unimproved — needs its own `current-system-end-to-end-anchor.md`.

### Remaining refinement queue targets

- Q7: `retrieval-rag-learning-anchor.md` — not built yet
- Q8: `obsidian-vault-schema-anchor.md` — not built yet
- Q18: `current-system-end-to-end-anchor.md` — not built yet

### What changed

- Anchor notes v1 → v2: added Core Components, Operating Loop, Runtime Topology, Indexing Flow, Verification Checks, Access Paths, Recovery Cases, Benchmark Relevance sections.
- First paragraph of each anchor rewritten to directly answer the benchmark query.
- Anchors indexed into Khoj vector store via `khoj_repair_index_delta.py`.
