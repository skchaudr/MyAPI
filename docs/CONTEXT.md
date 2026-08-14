# Part 1 — Context Map

Governing memo: `GDDP v MyAPI Part 1 - the first slice.md` (operator repos).

## Sequence

`decisions → corpus → ingestion → evaluation → stop`

Part 1 asks whether a clean decision snapshot can become a reproducible corpus that Khoj retrieves against. Query results end the slice; answer quality is recorded, not a gate.

## Rooms

| Room | Role | Task contracts |
|---|---|---|
| `01-decisions/` | Schema, extract, normalize, validate decision objects | `tasks/*.md` |
| `02-corpus/` | Fresh corpus snapshot + Khoj transform | `tasks/*.md` |
| `03-ingestion/` | Load into Khoj + verify retrieval | `tasks/*.md` |
| `04-evaluation/` | Fixed five-intent queries + preserve results | `tasks/*.md` |

## Fixed evaluation intents

1. Factual decision — what was decided?
2. Rationale — why that choice?
3. Supersession — what replaced an earlier decision?
4. Relationship — how do two decisions relate?
5. Negative control — ask what the corpus cannot answer

## Navigation

1. Read root `AGENTS.md` for node → room routing.
2. Read the room `CONTEXT.md`.
3. Open only the task contract named by the GDDP node.
4. Write artifacts exactly where the contract says.
5. Run the contract’s verification check.

## Rules

- Fresh agent, no session history assumed.
- Do not invent schema fields, source lists, or eval queries beyond the five intents.
- Do not modify graph truth or runtime databases from scaffold nodes.
- Stage outputs are filesystem artifacts consumed by the next room.
