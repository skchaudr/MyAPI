# Pass-1 corpus-hot (sab-mini)

You are Grok-mini. Read-heavy harvest only. No commits, no push, no Khoj reindex, no full ~/.pi ingest, no secrets in files (env NAMES only).

## Top 3 projects
1. myapi (MyAPI-rebuild) — this repo main is truth
2. gddp (gddp-runtime + gddp-config)
3. pi-needle-gemma (~/.pi + Needle + Gemma, scoped)

## Write path
~/repos/MyAPI/scratch/corpus-hot/{myapi,gddp,pi-needle-gemma}/

## Per project — four files only
- SOURCES.md  — ≥5 real paths, type, freshness
- QUERIES.md  — ≥8 questions: ownership, now-state, evidence, A→B
- BRIEF-DRAFT.md — Short Answer, Why, Relationships, Evidence (≥3 existing paths), Risks, Next
- GAPS.md — why graphify/semantic failed; what is missing

## Focus (mini)
- MyAPI: IMPLEMENTATION-PLAN, PROJECT-BRIEF, golden briefs, .handoffs, mcp/, sample Corpus v1.0 buckets only
- GDDP: what runtime owns vs config; handoffs; graphify-out as label vocab only (do not rebuild graph)
- Pi/Needle/Gemma: Needle paths, harness/sessions, model config paths — not weights, not whole ~/.pi dump
- Steal real query shapes from graphify history / zsh if available

## Done when
scratch/corpus-hot/README.md table: project | thin/ok/solid | biggest gap
Then idle one-line status. No scope expansion.
