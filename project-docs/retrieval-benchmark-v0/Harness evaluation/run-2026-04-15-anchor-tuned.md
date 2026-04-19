# Retrieval Benchmark v0 Run After Anchor Tuning — 2026-04-15

This run used the latest retrieval tuning with anchor-aware title/path boosts for project and operational queries.

## Notable Improvements

- Query 8, `What did I decide about the vault schema?`, now lands on a much better note:
  - top source: `claude`
  - top title: `PARA system vault schema implementation`
- Query 13, `Show me notes about my Obsidian folder schema.`, now routes to `obsidian` instead of drifting into generic ChatGPT notes
- Source-specific queries remained stable
- Decision and meta routing stayed intact

## Remaining Weak Spots

- Query 1, `What is My_DevInfra?`, still lands on a generic Claude note instead of a clean project anchor
- Query 10 and Query 12 still drift toward generic ChatGPT notes for deployment / operational recall
- Query 16 still needs a better Tailscale / SSH / VM-specific hit

## Takeaway

The anchor boost helped, especially for schema and Obsidian-folder style queries, but the project identity and operational queries still need one more refinement pass before they are consistently strong.
