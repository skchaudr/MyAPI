# 02-corpus — Stage D room

## Purpose
Build a fresh, reproducible corpus snapshot from validated decision objects.
Corpus is derived from decisions — not a bulk vault dump.

Ok so the shape is not a "bulk vault dump" - then what is the shape? - Sab 

Reading the rest of this file, it's not clear what the shape is; it's not a bulk dump, just a focused targeted "dump" - how do these decision objects make up the structure of this corpus/project knowledge?  

## Consumes
- Validated decision objects from `01-decisions/output/`
- Schema rules in `01-decisions/output/decision-schema.md`
- Corpus target shape notes under `project-docs/corpus-work-2026-08/`

## Produces
- `output/corpus/` — generated snapshot: one Markdown document per decision plus `index.md`
- `output/repro-report.md` — clean-rebuild byte comparison evidence

## Build
Run on Mac, from the repository root:

```bash
python3 02-corpus/build_corpus.py
```

The builder uses only the Python standard library and reads
`01-decisions/output/decisions-canonical.jsonl` by default.

## Project taxonomy rule
Preserve canonical `project` values such as `MyAPI`, `Pi`, `GDDP`,
`MyAPI/Khoj`, and `MyAPI/Pi/GDDP` **verbatim** in decision YAML frontmatter.
For corpus index/grouping only, derive project homes exclusively with
`project.split("/")`; do not normalize, reorder, alias, or mint another taxonomy.
A multi-home decision is indexed once under every split result while retaining
its original frontmatter value.

## Local layout
- `inputs/` — pinned decision-set inputs for a snapshot build
- `output/corpus/` — reproducible generated Markdown snapshot
- `output/repro-report.md` — reproducibility check evidence

## Next room
`03-ingestion` transforms and loads the snapshot into a clean Khoj target.
