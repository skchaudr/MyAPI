# Benchmark Run — 2026-04-16 Narrow Anchors

Live rerun against `http://localhost:8000/query` after the narrow project-identity and operational retrieval expansion pass.

## What improved

- `What is My_DevInfra?` now lands in `obsidian` instead of generic `chatgpt` or `claude`.
- `What is the status of the API deployment?` now lands in `claude` instead of generic `chatgpt`.
- `What notes are tied to Tailscale, SSH, or VM access?` now lands in `claude-code` instead of generic `chatgpt`.
- Source-specific and Obsidian/schema retrieval stayed stable.

## Still imperfect

- `What is My_DevInfra?` is still not clearly on the canonical project anchor note.
- Some temporal and broad factual queries still drift to generic ChatGPT material.
- The benchmark is now mostly exposing ranking quality inside the right corpus family rather than broad routing failures.

## Takeaway

- Retrieval query expansion helped candidate generation.
- Project identity and operational recall are now much closer to the right neighborhood.
- The remaining work is narrowing from "right family" to "right exact note."
