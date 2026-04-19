# Benchmark Run — 2026-04-15 Post Anchor Rerun

Live rerun against `http://localhost:8000/query` after the latest anchor and operational ranking pass.

## What improved

- `Find the Claude Code session where I set up the web adapter.` stays in `claude`.
- `Find the ChatGPT export note about iTerm2 and shell setup.` stays in `chatgpt`.
- `Show me notes about my Obsidian folder schema.` lands in `obsidian`.
- `Which notes are about prompts, schemas, or evaluation rubrics?` lands in `obsidian`.
- `What notes are about Claude, Codex, and Jules working together?` still routes correctly to `claude`.

## What is still weak

- `What is My_DevInfra?` still does not land on a clean project-specific note.
- `What notes mention Khoj deployment or indexing?` still drifts to a generic ChatGPT note.
- `What is the status of the API deployment?` still drifts to a generic ChatGPT note.
- `What notes are tied to Tailscale, SSH, or VM access?` still drifts to a generic ChatGPT note.

## Takeaway

- The latest anchor changes helped Obsidian and source-specific retrieval.
- The remaining weak spots are project identity and operational recall, not source inference or classifier routing.
- If we keep tuning, the next useful move is probably a more explicit canonical-note strategy for `My_DevInfra` and a tighter operational anchor map for `Khoj`, `deployment`, `Tailscale`, and `VM access`.
