# Benchmark Run — 2026-04-16 Canonical Anchor

Live rerun against `http://localhost:8000/query` after renaming the canonical project anchor and syncing it into the live corpus.

## What changed

- `What is My_DevInfra?` now lands on `obsidian` with the top title `Personal Briefing & Capture System`.
- The canonical anchor note is now searchable by both the new project name and the old `My_DevInfra` alias.
- The alias-aware metadata path is active in retrieval, so the note identity is no longer only implicit.

## What stayed the same

- Source-specific routing remains stable.
- Obsidian/schema queries still land in the right family.
- Broad temporal and some operational prompts still drift toward generic chat material, but that is now a separate problem from project identity.

## Takeaway

- `My_DevInfra` was semantically muddy as a project label.
- The canonical name now better matches the real behavior of the system.
- Retrieval now has a cleaner identity anchor to work with, which should help both humans and ranking logic going forward.
