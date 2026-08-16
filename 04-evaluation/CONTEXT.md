# 04-evaluation — Stage H/I room

## Purpose
Run the fixed Part 1 evaluation set against Khoj, preserve raw answers and
retrieval evidence, then stop. Answer quality is measured, not a gate.

## Consumes
- Live ingested corpus (from `03-ingestion`)
- Decision objects/schema fields: statement, rationale, supersession, relations

## Produces
- `queries/` — predetermined evaluation prompts
- `results/` — raw answers, retrieved evidence, run metadata

## Fixed evaluation set
1. Factual decision — what was decided?
2. Rationale — why was a choice made?
3. Supersession — which decision replaced an earlier one?
4. Relationship — how do two decisions relate?
5. Negative control — unanswerable from corpus (confident wrong = result)

## Stop
Part 1 ends here. Inspect evidence; do not expand into later slices in-room.
