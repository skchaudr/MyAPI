# Retrieval Benchmark v0 Run After Second Anchor Pass — 2026-04-15

This rerun used the latest project-anchor and body-anchor tuning.

## Notable Outcomes

- Query 1, `What is My_DevInfra?`, improved at the source-family level but still does not land on a clean project-specific note.
- Query 13, `Show me notes about my Obsidian folder schema.`, now lands on the Obsidian corpus instead of generic ChatGPT content.
- Query 17, `Which notes are about prompts, schemas, or evaluation rubrics?`, now lands on an Obsidian note instead of a generic Claude note.
- Query 8 remained good and still lands on a more authoritative schema note.

## Remaining Gaps

- Project identity for `My_DevInfra` still needs a more direct anchor or a better canonical note.
- Operational queries about Khoj deployment, API deployment, and VM access still drift toward generic ChatGPT notes.
- Temporal and source-specific behavior is stable, but not especially strong on the fuzzy operational queries.

## Readout

The second anchor pass helped the schema and prompt/rubric style queries, but it did not fully solve project identity or operational recall. Those are now the two most valuable remaining retrieval refinements.
