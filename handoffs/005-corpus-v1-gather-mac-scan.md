# 005 — Corpus v1 gather: Mac scanned, pi-big pending

Date: 2026-05-18
Branch: feat/corpus-v1-normalization

## Empirical reality

### What shipped this session

- Pushed `feat/corpus-v1-normalization` from pi-small to origin. It was local-only before tonight; Mac couldn't pull until the push.
- Set up Python venv on Mac at `venv/` (Mac's Homebrew Python is PEP 668-protected, so a system pip install was blocked). Installed pyyaml 6.0.3.
- Mac is now checked out on `feat/corpus-v1-normalization`. Sab's uncommitted edit on `handoffs/004-corpus-v1-field-test-realization.md` was carried across cleanly and preserved.
- Ran `scripts/normalize_corpus.py scan` on Mac with `--obsidian /Users/saboor/Obsidian/SoloDeveloper`, the full ChatGPT export (`_archive/chatgpt_ALL_CONVOS-2026-02-01.zip`, 534M), the full Claude.ai export (`_archive/claude-ALL-conversation-history.zip`, 5.1M), and CLI defaults for Claude Code + Codex.
- Result: **4114 entries** in `corpus_v1/manifests/scan-2026-05-18.jsonl` on Mac.
  - By source: obsidian 1674, repo_docs 58, claude_code 669, codex 78, chatgpt 1291, claude_web 344.
  - By source_type: project_doc 1049, cli_session 747, reference 458, conversation 1635 (so chatgpt + claude_web), daily_note 142, note 74, handoff 5, anchor 4.

### Where things stand

- **pi-small** (this host): scan + copy already done 2026-05-14, materialized at `corpus_v1/` with 1787 items. Unchanged tonight.
- **Mac**: scan done tonight; **copy not done yet**. The manifest is on disk; no stamped files have been written to `corpus_v1/{documents,conversations,...}/`.
- **pi-big** (Tailscale `100.78.181.120`): untouched. Holds its own Claude Code + Codex session histories that exist nowhere else. SSH access not yet probed; unknown whether the repo is cloned or Python is set up there.
- **Re-exports**: Sab plans to re-export Claude + ChatGPT. ChatGPT export takes ~days per OpenAI's notice. Gemini deferred — the CLI has no Gemini adapter yet. The exports used tonight are dated 2026-02-01 (ChatGPT) and 2026-04-14 (Claude). Sab decided that's good enough to proceed; fresh exports will trigger a re-run when they land.

### Findings worth carrying forward

- Mac vault is at `/Users/saboor/Obsidian/SoloDeveloper` (capital `O`). The CLI's `DEFAULT_OBSIDIAN_VAULT` is hardcoded to the pi-small path — Mac runs require `--obsidian` override on every invocation. Worth a one-line edit later, not blocking.
- Mac Codex layout uses both `~/.codex/command-logs/` and `~/.codex/sessions/`, so the CLI's default `--codex` path works there. pi-small lacks `command-logs/` and silently skipped Codex.
- Mac Claude Code projects: 53 (vs 5 on pi-small). This is the primary workstation for that source.
- The 534M ChatGPT zip is loaded fully into memory by `scan` and `copy` (both eagerly extract all conversation shards). Mac is 8GB RAM — scan ran fine; copy is untested but expected to fit.

### Memory writes this session

- `feedback_obsidian_not_icloud.md` — never describe Obsidian as iCloud-synced or guess a sync mechanism.
- `feedback_organize_by_source_not_host.md` — corpus framing is by source × project, not by host machine. Host is incidental I/O.
- `reference_workstations.md` — Tailscale IPs for Mac / pi-small / pi-big / VM.
- `feedback_dont_rush_cadence.md` — wait for Sab's signal between steps; don't propose "run it twice" workarounds to manufacture forward motion.

## Resume point

Next session, in order:

### 1. Mac copy (one command)

```bash
ssh saboor@100.109.233.105
cd ~/repos/MyAPI
PYTHONPATH=/Users/saboor/repos/MyAPI venv/bin/python scripts/normalize_corpus.py copy \
  --manifest corpus_v1/manifests/scan-2026-05-18.jsonl \
  --chatgpt "_archive/chatgpt_ALL_CONVOS-2026-02-01.zip" \
  --claude-web "_archive/claude-ALL-conversation-history.zip"
```

Optional `--limit 50` for a smoke pass before the full run. Writes `corpus_v1/{documents,conversations,artifacts,manifests}/` on the Mac, gitignored.

### 2. pi-big

SSH `saboor@100.78.181.120`. First probe: is `~/repos/MyAPI` present? Is Python 3.10+ available? If yes, mirror the Mac setup (checkout `feat/corpus-v1-normalization`, create `venv/`, install pyyaml, scan, copy). pi-big has no Mac-side exports — only Claude Code + Codex sessions matter there.

### 3. Re-exports (async, Sab-driven)

When fresh ChatGPT / Claude.ai exports land in Mac's `_archive/`, re-run the Mac scan + copy with the new paths. Only the conversation slice changes; documents and CLI sessions don't re-process.

### 4. Indexer consumption

Once Mac and pi-big both have their `corpus_v1/`, the indexer needs config pointing at all three trees (pi-small + Mac + pi-big). This is **not** a merge — the data partitions naturally by where it physically lives. Just a config concern downstream.

### 5. Loose ends

- Uncommitted handoff 004 edits on pi-small and Mac (different content, Sab's writing in progress).
- Untracked `project-reference.html` on pi-small.
- Untracked `handoffs/004-...md.bak-pre-claude-fillin` on Mac (claude-created backup from a prior session).
- `DEFAULT_OBSIDIAN_VAULT` in `scripts/normalize_corpus.py` is pi-small-hardcoded. Trivial one-line config edit if it becomes annoying.

## Narrative / Trajectory

Intent: Gather Sab's full corpus into v1-stamped form so retrieval can route by intent (canonical vs. conversation vs. CLI session) instead of by raw similarity alone.

Interpretation: Tonight crossed a real threshold. pi-small's earlier run produced 1787 items with **zero conversations** — the actual scratchpad/thought-process evidence was missing. Mac's run added 1635 conversations + 669 Claude Code sessions + 78 Codex sessions. The corpus now contains the kind of evidence that conversation-shaped queries need.

Tension: Sab corrected the framing twice — Obsidian is not "iCloud sync", and the work is not organized by machine. The corpus's primary axes are source × project; machines are just where the bytes live. The CLI already encodes this (no `host` field in the schema), but I drifted back into host-centric framing in conversation and got called on it. Also got called on problem-first/rush behavior — pacing memory now exists.

Momentum: Two clean execution steps remain (Mac copy, pi-big scan+copy). No design decisions blocking. Re-exports run async on Sab's side. The next session should be able to ship the rest in one focused pass.
