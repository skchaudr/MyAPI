# 01-decisions — Stage A/B/C room

This needs to be re-done for clarity on what directionally sounds great but sounds lost all the same - Sab  

## Purpose
Canonical decision-object work for MyAPI Part 1. Define the schema, then
extract/normalize/validate decision objects from authoritative sources.

## Consumes
- Governing memo: Part 1 first-slice boundary (decisions → corpus → Khoj → eval)
- Authoritative sources: `project-docs/corpus-work-2026-08/*`, anchors,
  handoffs, accepted review sheets (D01–D18 set)

## Produces
- `output/decision-schema.md` — canonical Decision shape (this stage’s gate)
- Later: validated decision objects in `output/` for `02-corpus`

## Local layout
- `inputs/` — source pointers or copies used during extraction
- `output/` — schema + normalized decision artifacts

## Next room
`02-corpus` builds a fresh reproducible corpus snapshot from validated decisions.
