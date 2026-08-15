# MyAPI Decision Fixture Review — F01–F10 (Summary)

Status: reviewer pass; non-canonical | Date: 2026-08-10 | Reviewer: Codex

Critique of initial fixture passes (`6b58429` Grok F06–F10, `b5105ab` Codex F01–F05). Proves evidence backing; does not freeze M1 gold.

## Verdict Summary

| Fixture | Origin | Verdict | Key Action Required |
|---|---|---|---|
| F01 | Codex | Retain after repair | Resolve accepting session Evidence ID & predecessor Decision ID. |
| F02 | Codex | Retain after repair | Resolve acceptance provenance for ownership boundary. |
| F03 | Codex | Retain after repair | Record open divergence for missing MCP transport & args. |
| F04 | Codex | Split or narrow | Separate July corpus-tier policy from August 4-source MVP. |
| F05 | Codex | Retain after repair | Resolve receipt; retain benchmark raw evidence gap. |
| F06 | Grok | Reclassify / Replace | Move to `DecisionCandidate` (pending Sab review in handoff 029). |
| F07 | Grok | Retain after narrowing | Cite plan/arch policy; narrow divergence to golden usage. |
| F08 | Grok | Retain as historical | Mark historical/refined under 2026-08-10 Decision Graph plan. |
| F09 | Grok | Retain after repair | Resolve receipt; keep runtime enforcement gap explicit. |
| F10 | Grok | Retain after repair | Normalize `refined_by` relation vocabulary and receipt. |

## Core Findings & Rules

1. **Evidence & Truth:** Evidence pointers, git hashes, and symbols pass verification, but canonical status requires unresolved `AcceptanceReceipt` pointers.
2. **Acceptance Invariant:** `Decision` requires human acceptance (`CONTEXT.md:22-24`). Missing receipts require repair or reclassification as `DecisionCandidate`.
3. **Relation Direction:** Standardize on active directed relations (`refines`, `supersedes`, `constrains`) rather than passive `refined_by`.
4. **Scope Boundaries:** Keep divergence strictly tied to the reviewed Decision. Keep one Decision per object (split compound nodes like F04).

## Freeze Recommendation

- **Gold candidates (after repair):** F01, F02, F03, F05, F09, F10
- **Narrowed / Historical / Split:** F07 (narrow), F08 (historical), F04 (split)
- **Reclassify / Replace:** F06 (`DecisionCandidate`)

## Verification

Parsed YAML, validated line ranges, git commit SHAs, and AST symbols across all ten fixtures.
