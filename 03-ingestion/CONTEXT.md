# 03-ingestion — Stage E/F/G room

## Purpose
Transform the decision corpus into Khoj’s ingestible representation, load it
into a clean target corpus, and verify presence plus basic retrieval.

## Consumes
- Fresh corpus snapshot from `02-corpus/output/`
- Decision schema (field/metadata expectations for chunks)

## Produces
- `output/` — transform receipts, ingest logs, verification notes

## Local layout
- `output/` — ingestion evidence only (no second corpus copy required)

## Next room
`04-evaluation` runs the fixed query set against the ingested corpus and stops.
