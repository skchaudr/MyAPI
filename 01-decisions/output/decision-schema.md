# Canonical decision object schema

Part 1 Stage A artifact. Every later stage (corpus, ingestion, evaluation)
consumes decision objects in this shape. Source of examples:
`project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md`
(Sab-accepted D01–D10, D12–D18).

## Evaluation coverage

| Fixed eval question | Primary fields |
|---|---|
| What was decided? | `statement`, `summary`, `status` |
| Why was it chosen? | `rationale`, `alternatives_considered` |
| Which decision replaced an earlier one? | `replaces`, `replaced_by`, `status` |
| How do two decisions relate? | `related_decisions[]` (`rel`, `target_id`, `note`) |
| Negative control | (no field — absence of matching objects is the signal) |

---

## Object type: `Decision`

Serialization: one Markdown file per decision under a future corpus snapshot,
with YAML frontmatter matching these fields, **or** one JSON object in a
decision-set array. Field names below are canonical in both forms.

### Identity

| Field | Type | Required | Notes |
|---|---|---|---|
| `id` | string | yes | Stable slug. Pattern: `dec-{project}-{short-kebab}` or legacy `D##` when importing the 2026-08-08 set. |
| `schema_version` | string | yes | This document: `"1.0"`. |
| `project` | string | yes | Owning project: `MyAPI`, `GDDP`, `Pi`, or a slash-joined multi-home (e.g. `MyAPI/Khoj`). |
| `title` | string | yes | Short human label (≤80 chars). |
| `summary` | string | yes | One-line restatement of the choice. |
| `statement` | string | yes | Full normative statement of what was decided. |
| `status` | enum | yes | `accepted` · `provisional` · `superseded` · `rejected` · `deprecated` |

### Decision content

| Field | Type | Required | Notes |
|---|---|---|---|
| `rationale` | string | yes | Why this choice; the answer surface for eval Q2. |
| `decided_on` | date (`YYYY-MM-DD`) | yes | Calendar date of acceptance or recorded decision. |
| `decided_by` | string | no | Person or role (usually `Sab`). |
| `alternatives_considered` | string[] | no | Options explicitly rejected or deferred. |
| `consequences` | string | no | What changes operationally because of this decision. |
| `tags` | string[] | no | Freeform topical labels. |

### Supersession

| Field | Type | Required | Notes |
|---|---|---|---|
| `replaces` | string[] | no | `id`s this decision supersedes. Empty/omitted = not a replacement. |
| `replaced_by` | string \| null | no | Single `id` that supersedes this one. When set, `status` must be `superseded`. |

Invariant: if A.`replaces` contains B, then B.`replaced_by` = A.`id` and
B.`status` = `superseded` (and usually A.`status` = `accepted`).

### Relationships (non-supersession)

| Field | Type | Required | Notes |
|---|---|---|---|
| `related_decisions` | `Relation[]` | no | Edges to other decisions. |

#### `Relation` object

| Field | Type | Required | Notes |
|---|---|---|---|
| `target_id` | string | yes | Other decision `id`. |
| `rel` | enum | yes | `depends_on` · `enables` · `constrains` · `companion` · `clarifies` · `conflicts_with` |
| `note` | string | no | One-line edge rationale. |

Supersession uses `replaces` / `replaced_by`, not `related_decisions`.
Do not encode replacement as `rel: supersedes`.

### Provenance

| Field | Type | Required | Notes |
|---|---|---|---|
| `sources` | `SourceRef[]` | yes | At least one authoritative source. |
| `evidence_paths` | string[] | no | Repo- or vault-relative paths supporting the record. |
| `git_refs` | string[] | no | Commit SHAs / branch names that enact or record the decision. |

#### `SourceRef` object

| Field | Type | Required | Notes |
|---|---|---|---|
| `kind` | enum | yes | `memo` · `handoff` · `session` · `anchor` · `review_sheet` · `commit` · `other` |
| `ref` | string | yes | Path, URL, session id, or commit SHA. |
| `note` | string | no | What this source contributes. |

### Optional operational metadata

| Field | Type | Required | Notes |
|---|---|---|---|
| `confidence` | enum | no | `high` · `medium` · `low` — extractor confidence, not decision quality. |
| `review_mark` | enum | no | Sab review: `Y` · `N` · `clarified` (from review sheets). |
| `notes` | string | no | Non-normative commentary for maintainers. |

---

## Minimal required set (extractor checklist)

Every accepted object must carry at least:

```text
id, schema_version, project, title, summary, statement, status,
rationale, decided_on, sources[]
```

Plus, when applicable:

```text
replaces[] / replaced_by
related_decisions[]
```

---

## JSON sketch

```json
{
  "id": "dec-gddp-job-disposal-path",
  "schema_version": "1.0",
  "project": "GDDP",
  "title": "Dedicated job disposal path",
  "summary": "Failed jobs use mark_job_failed + durable reason; never node_status or graph mutation.",
  "statement": "Job failure uses a dedicated disposal path (mark_job_failed + durable reason/receipt). Do not use node_status and do not mutate graph truth for disposal.",
  "status": "accepted",
  "rationale": "Separates runtime job bookkeeping from graph/node truth so disposal cannot rewrite the schedule.",
  "decided_on": "2026-08-08",
  "decided_by": "Sab",
  "alternatives_considered": [
    "Reuse node_status transitions for job failure",
    "Mutate graph truth to reflect failed attempts"
  ],
  "consequences": "Executors and evaluators write job receipts only; graph import remains the sole graph write path (see dec-gddp-nodes-via-import).",
  "tags": ["runtime", "disposal", "graph-truth"],
  "replaces": [],
  "replaced_by": null,
  "related_decisions": [
    {
      "target_id": "dec-gddp-nodes-via-import",
      "rel": "companion",
      "note": "Both protect graph truth: disposal must not write it; nodes enter only via import."
    },
    {
      "target_id": "dec-gddp-no-merge-on-accept",
      "rel": "constrains",
      "note": "Acceptance and failure both stay off main; results live on worktree/result-branch."
    }
  ],
  "sources": [
    {
      "kind": "review_sheet",
      "ref": "project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md",
      "note": "D02 marked Y"
    },
    {
      "kind": "memo",
      "ref": "project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md",
      "note": "D02 canonical prose"
    }
  ],
  "evidence_paths": [
    "project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md"
  ],
  "git_refs": [],
  "confidence": "high",
  "review_mark": "Y"
}
```

---

## Filled examples (real MyAPI / GDDP decisions)

### Example 1 — factual + rationale + relationships (D15)

```yaml
id: dec-myapi-graphify-structural-khoj-semantic
schema_version: "1.0"
project: MyAPI/Khoj
title: Graphify structural; Khoj semantic
summary: >-
  Graphify stays the structural layer; Khoj answers over normalized notes
  including decision objects.
statement: >-
  Graphify (graph.json, reports, graphify query paths) stays the structural
  layer. Khoj is the semantic answer layer over normalized notes, including
  these decision notes.
status: accepted
rationale: >-
  Agents need path structure and answered meaning; neither layer replaces
  the other alone. Part 1 evaluates Khoj against decision objects without
  collapsing Graphify into the semantic index.
decided_on: 2026-08-08
decided_by: Sab
alternatives_considered:
  - Put structural graph edges only into Khoj and drop Graphify query paths
  - Use Graphify alone as the answer surface
consequences: >-
  Decision corpus builds for Khoj ingestion; Graphify remains code/structure
  map. Eval queries hit Khoj, not graphify query, for semantic checks.
tags: [corpus, khoj, graphify, retrieval]
replaces: []
replaced_by: null
related_decisions:
  - target_id: dec-myapi-khoj-corpus-composition
    rel: depends_on
    note: Semantic layer only works if the Khoj corpus stays curated.
  - target_id: dec-myapi-decision-scan-order
    rel: enables
    note: Newest decisions feed Khoj first under the last-2w-then-widen order.
sources:
  - kind: review_sheet
    ref: project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md
    note: D15 marked Y
  - kind: memo
    ref: project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md
    note: D15 prose
  - kind: anchor
    ref: project-docs/REBUILD-CONTEXT-ANCHOR.md
    note: Rebuild rejects v0 single RAG pool; layers stay distinct.
evidence_paths:
  - project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md
  - project-docs/corpus-work-2026-08/CORPUS-TARGET-SHAPE.md
confidence: high
review_mark: Y
```

### Example 2 — supersession pair (rebuild MCP naming)

Canonical current decision:

```yaml
id: dec-myapi-mcp-two-tools
schema_version: "1.0"
project: MyAPI
title: MCP surface is two tools
summary: >-
  Public MCP tools are get_project_context and get_person_context only.
statement: >-
  The MCP surface exposes exactly two tools — get_project_context and
  get_person_context. Do not fork into get_user_context or "operator context"
  as separate tools; those names alias get_person_context.
status: accepted
rationale: >-
  Tool schemas are standing prompt overhead. A tiny roster keeps MyMCP
  budget-aware and stops agents re-litigating person vs operator naming.
  Person context is first-class and does not wait on LinkedIn/WhatsApp exports.
decided_on: 2026-06-21
decided_by: Sab
alternatives_considered:
  - Three-tool surface with separate operator context
  - Defer get_person_context until friend-refinery exports land
consequences: >-
  AGENTS.md and ARCHITECTURE.md lock the two names; extractors treat older
  operator/user-context wording as superseded aliases.
tags: [mcp, naming, rebuild]
replaces:
  - dec-myapi-mcp-operator-context-alias
replaced_by: null
related_decisions:
  - target_id: dec-myapi-graphify-structural-khoj-semantic
    rel: constrains
    note: Briefs from these tools consume layered retrieval, not a single dump pool.
sources:
  - kind: anchor
    ref: project-docs/REBUILD-CONTEXT-ANCHOR.md
    note: MCP tools table; glossary locks the two names
  - kind: memo
    ref: project-docs/ARCHITECTURE.md
    note: §0.1 cost posture — two public tools
evidence_paths:
  - project-docs/REBUILD-CONTEXT-ANCHOR.md
  - AGENTS.md
confidence: high
review_mark: Y
```

Superseded prior naming decision:

```yaml
id: dec-myapi-mcp-operator-context-alias
schema_version: "1.0"
project: MyAPI
title: Operator/user context as distinct MCP framing
summary: >-
  Older framing treated operator/user context as a separate retrieval concern
  from person context.
statement: >-
  Expose or discuss operator context / get_user_context as a distinct tool
  or framing alongside project context.
status: superseded
rationale: >-
  Early rebuild drafts split "operator" from "person" and deferred person
  context behind LinkedIn/WhatsApp export work. That hair-split re-litigated
  naming every cold start and buried person context.
decided_on: 2026-06-01
decided_by: Sab
replaces: []
replaced_by: dec-myapi-mcp-two-tools
related_decisions: []
sources:
  - kind: anchor
    ref: project-docs/REBUILD-CONTEXT-ANCHOR.md
    note: Explicitly retires get_user_context / operator-context forks
  - kind: memo
    ref: project-docs/ARCHITECTURE.md
    note: Records incorrect deferral framing for get_person_context
evidence_paths:
  - project-docs/REBUILD-CONTEXT-ANCHOR.md
confidence: medium
notes: >-
  Date is approximate (pre-anchor freeze). Kept so supersession eval can
  resolve replaces/replaced_by against real project vocabulary.
```

---

## Stage handoff

- **Produces:** this schema; later Stage B emits concrete `Decision` objects.
- **Consumers:** `02-corpus` (normalize to snapshot), `03-ingestion` (Khoj shape),
  `04-evaluation` (fixed query set against fields above).
- **Non-goals for this file:** full decision extraction, task contracts, Khoj
  chunk rules, query text.
