# 02-corpus — Stage D room

## Purpose
Build a fresh, reproducible corpus snapshot from validated decision objects.
Corpus is derived from decisions — not a bulk vault dump.

## Consumes
- Validated decision objects from `01-decisions/output/`
- Schema rules in `01-decisions/output/decision-schema.md`
- Corpus target shape notes under `project-docs/corpus-work-2026-08/`

## Produces
- `output/` — snapshot ready for Khoj transform (Stage E lives with ingestion)

## Local layout
- `inputs/` — pinned decision-set inputs for a snapshot build
- `output/` — corpus snapshot artifacts

## Next room
`03-ingestion` transforms and loads the snapshot into a clean Khoj target.
