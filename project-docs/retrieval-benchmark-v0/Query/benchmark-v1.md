# Benchmark v0 Queries

Use this set to probe retrieval quality across source families, time, and synthesis.

For each query, inspect:

- which sources came back
- whether the sources are the right kind
- whether the result set is fragmented
- whether one source family dominates
- whether time is being respected
- whether titles / anchors / file names are helping enough

## Queries

| # | Query | Primary intent | What to inspect |
|---|---|---|---|
| 1 | What is My_DevInfra? | project identity | Does the answer stay anchored to the correct project and avoid generic infra noise? |
| 2 | What have I been working on recently? | temporal recall | Are the results ordered by recency and do they reflect the last meaningful work? |
| 3 | What was I doing around the time I was debugging Tailscale? | episodic reconstruction | Does the system recover the right time window and related artifacts? |
| 4 | What keeps showing up as friction in my Neovim workflow? | recurring pattern | Does it find multiple notes with the same theme, not just one isolated hit? |
| 5 | Find the Claude Code session where I set up the web adapter. | source-specific recall | Does it return the correct Claude corpus item instead of a similar but wrong session? |
| 6 | Find the ChatGPT export note about iTerm2 and shell setup. | source-specific recall | Does it surface ChatGPT-derived content with the right anchors? |
| 7 | What was I learning about retrieval systems? | cross-source synthesis | Does it combine notes, sessions, and docs into one coherent answer? |
| 8 | What did I decide about the vault schema? | decision recall | Does it prefer authoritative notes over incidental mentions? |
| 9 | Which notes discuss tagging strategy and taxonomy? | metadata recall | Does it find schema and normalization notes, not just content notes? |
| 10 | What notes mention Khoj deployment or indexing? | system context | Does it retrieve deployment, corpus, and endpoint material together? |
| 11 | What notes are about Claude, Codex, and Jules working together? | toolchain synthesis | Does it connect the agent workflow across multiple corpora? |
| 12 | What is the status of the API deployment? | operational recall | Does it find the live deployment notes and avoid stale references? |
| 13 | Show me notes about my Obsidian folder schema. | note organization | Does it surface structure and hierarchy notes with useful anchors? |
| 14 | What did I write about semantically related notes and clean-up passes? | workflow memory | Does it surface normalization and triage planning notes? |
| 15 | What are the strongest notes for a retrieval benchmark? | quality selection | Does it find notes that are likely high-signal instead of broad and noisy? |
| 16 | What notes are tied to Tailscale, SSH, or VM access? | infrastructure recall | Does it return the right operational cluster and preserve time context? |
| 17 | Which notes are about prompts, schemas, or evaluation rubrics? | meta-work recall | Does it retrieve the governing docs rather than example notes? |
| 18 | What docs should I use to understand the current system end to end? | synthesis / overview | Does it return the right cross-corpus overview and not fragment badly? |

## Manual notes

- Mark whether the result set felt coherent or fragmented.
- Mark whether one corpus dominated the answer.
- Mark whether titles and anchors were enough to land the right content.
- Mark whether the answer was useful without extra digging.
