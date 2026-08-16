# 03-ingestion — Stage E/F/G room

## Purpose
Transform the decision corpus into Khoj’s ingestible representation, load it
into a clean target corpus, and verify presence plus basic retrieval.

## Consumes
- Fresh corpus snapshot from `02-corpus/output/`
- Decision schema (field/metadata expectations for chunks)

## Produces
- `output/khoj-corpus/` — exact Markdown files staged for Khoj ingestion
- `output/transform-notes.md` — format, deployment-discovery, and transform evidence
- Later nodes add ingest logs and verification notes under `output/`

## Transform
Run on Mac, from the repository root:

```bash
python3 03-ingestion/transform_for_khoj.py
```

The transform copies the flat Stage D Markdown snapshot byte-for-byte and
atomically replaces only the derived `output/khoj-corpus/` directory.

## Next room
`04-evaluation` runs the fixed query set against the ingested corpus and stops.
