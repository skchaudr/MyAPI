# Corpus v1.0 Vault Implementation Plan

Date: 2026-06-02
Updated: 2026-06-03
Status: Proposed for review only
Execution state: Do not run until reviewed on Mac

## Decision Summary

Build a derived Obsidian vault from the frozen `corpus_v1/raw-v1.0/selected/`
working set, and make that vault immediately useful in the Obsidian GUI.

The governing rule is:

> Everything in the selected corpus is worth retrieving. Normalization
> improves access, routing, and legibility. It does not decide whether the
> underlying material has value.

The implementation should therefore separate three concerns:

1. Preserve every selected raw source and make it addressable.
2. Deterministically materialize every source into a readable local vault.
3. Apply heavier model-assisted extraction only where it creates useful
   navigation, project state, timeline, or retrieval leverage.

This is not a plan to build a giant RAG system before the data becomes usable.
The vault is the durable substrate. Obsidian visibility is the first outcome:
structured knowledge visible by sight, searchable by humans, and scannable by
agents from source family down to stable note headings and blocks.

Khoj is downstream of that substrate. It should index an allowlisted, shaped
vault slice and expose a faster semantic API lane. It should not be the thing
that makes the corpus legible in the first place.

## Frozen Input Contract

The raw bundle already exists locally and must remain immutable:

```text
corpus_v1/raw-v1.0/
  README.md
  source-archives/
  selected/
  manifests/
```

The derived vault should read only from:

```text
corpus_v1/raw-v1.0/selected/
```

Current selected source counts:

| Source | Selected material |
| --- | ---: |
| Obsidian markdown notes | 1,922 |
| ChatGPT conversations | 170 |
| Claude web conversations | 108 |
| Claude Code top-level sessions | 516 |
| Claude Code selected files, including support files | 698 |
| Codex rollout JSONL sessions | 53 |
| Total selected raw files | 2,675 |

Corrected generated-new counts:

| Source | Generated new in v1 window | Selected because touched/updated | Notes |
| --- | ---: | ---: | --- |
| Obsidian markdown notes | 390 known-new | 1,922 total selected | Creation metadata exists for 1,573 selected notes; 349 have unknown creation date |
| ChatGPT conversations | 165 new | 170 total selected | 5 older conversations were updated in the window |
| Claude web conversations | 106 new | 108 total selected | 2 older conversations were updated in the window |
| Claude Code top-level sessions | 512 new | 516 total selected | 4 older sessions were touched in the window |
| Codex rollout sessions | 43 new | 53 total selected | 10 older sessions were touched in the window |

The Obsidian generated-new count uses note-level `created`, `created_at`, or
`date` metadata where present. It is therefore a known-new lower bound, not a
claim that the remaining 349 unknown-date notes are old.

The v1 windows are:

- Obsidian: `2026-03-22` through `2026-05-22`.
- ChatGPT, Claude web, Claude Code, and Codex: `2026-04-22` through
  `2026-05-22`.

The upper bound is exclusive `2026-05-23`.

The raw integrity manifest is:

```text
corpus_v1/raw-v1.0/manifests/selected-checksums.sha256
```

The build must verify this manifest before and after materialization.

## Important Corrections To The Earlier Architecture Note

The earlier substrate note at
`project-docs/corpus-v1-obsidian-substrate-architecture.md` remains useful, but
this plan supersedes three assumptions:

1. A heavy universal metadata schema is not the starting point.
2. Admission is not a value judgment. Every selected source becomes locally
   retrievable, even when it has not been enriched.
3. `project`, `area`, `type`, `status`, `confidence`, and similar fields must
   earn their place through retrieval tests rather than being stamped
   everywhere by default.

The V4 Obsidian schema is prior experience and a useful comparison point. It is
not the automatic canonical metadata stamp for this vault.

## Output Contract

Create a new derived vault:

```text
corpus_v1/vault-v1.0/
```

First success condition:

```text
Open corpus_v1/vault-v1.0/ in Obsidian and immediately browse, search, inspect
links, follow provenance, and visually understand the corpus shape.
```

Never write generated files back into:

```text
corpus_v1/raw-v1.0/
```

Recommended top-level layout:

```text
corpus_v1/vault-v1.0/
  README.md
  00-index/
  10-current-state/
  20-projects/
  30-systems-and-workflows/
  40-decisions-and-trajectories/
  50-timeline/
  60-sessions-and-conversations/
  70-artifacts-and-reference/
  80-candidates/
  90-raw-provenance/
  _manifests/
  _reports/
```

### Folder Responsibilities

| Folder | Primary question class |
| --- | --- |
| `00-index/` | Where should a cold-start agent begin? |
| `10-current-state/` | What is true, active, blocked, or unresolved right now? |
| `20-projects/` | What is this project and how should an agent orient itself? |
| `30-systems-and-workflows/` | How does a recurring technical or personal system work? |
| `40-decisions-and-trajectories/` | Why did this direction change and what alternatives were considered? |
| `50-timeline/` | What happened when? What changed between two points in time? |
| `60-sessions-and-conversations/` | What happened in a specific AI chat or terminal session? |
| `70-artifacts-and-reference/` | Which durable note, report, handoff, or produced artifact should be loaded? |
| `80-candidates/` | What has been materialized but still needs review or richer routing? |
| `90-raw-provenance/` | Where is the preserved raw source and how can it be audited? |

`50-timeline/` replaces the earlier `periodic` framing. Time is a primary
retrieval axis, not a special class of journal note.

### Obsidian GUI Role

The vault should make the corpus visible before any API layer is involved:

- Global search finds source titles, concepts, tags, headings, and exact terms.
- Graph and backlinks reveal project, timeline, session, and artifact clusters.
- Folder view communicates question routes at a glance.
- Headings create block-level retrieval surfaces.
- Tags and concepts remain light, human-readable navigation aids.
- Tasks, Dataview, Kanban, Canvas, and bookmarks can be layered on later without
  changing the source contract.

The point is not just "store data as Markdown." The point is to make structured
knowledge visible and operable through a GUI that humans and agents can both
reason about.

## Git-Like Navigation Model

The vault should behave more like a legible project history than a pile of
normalized documents.

| Git concept | Vault equivalent |
| --- | --- |
| Blob | Raw conversation, session, note, or source artifact |
| Commit | Derived timeline event describing what changed and why |
| Commit history | `50-timeline/` |
| Branch or ref | Project current-state note |
| `HEAD` | Current focus |
| `git status` | Work queue with active, blocked, deferred, and unresolved items |
| Commit graph | Links between projects, decisions, sessions, artifacts, and superseded notes |
| Diff | Changes between project-state snapshots |
| Tag | Milestone or stable version |

The physical vault should remain plain Markdown. Graph views, Dataview tables,
Kanban boards, and API indexes are derived interfaces over those files.

## Project Bundle

Each active project gets a small bundle:

```text
20-projects/MyAPI/
  MyAPI Index.md
  MyAPI Anchor.md
  MyAPI Current State.md
  MyAPI Work Queue.md
  MyAPI Timeline.md
```

This is an upgrade over the v0 project-anchor pattern through separation of
concerns:

- `MyAPI Anchor.md` is durable: identity, purpose, architecture, vocabulary,
  durable constraints, and key links.
- `MyAPI Current State.md` is mutable: the closest vault equivalent of `HEAD`
  plus `git status`.
- `MyAPI Work Queue.md` is queryable: in progress, blocked, deferred,
  questions, and important facts.
- `MyAPI Timeline.md` is chronological: links to relevant event notes.
- `MyAPI Index.md` is the cold-start entry point joining the other four.

An agent asking "what is MyAPI?" and an agent asking "where did we leave off?"
should not need to load the same document.

Start with bundles for:

```text
MyAPI
GDDP
DevInfra
Vault Normalization
```

Add more bundles only when the first pass reveals active subjects that deserve
their own cold-start route.

## Workflow Markers

Use readable task markers inside project state and queue notes:

```markdown
# Current State

## In Progress
- [/] Build corpus v1.0 vault

## Blocked
- [!] Decide which metadata fields improve retrieval enough to keep

## Questions
- [?] Does API retrieval outperform vault-only cold starts?

## Deferred
- [-] Graphify the admitted corpus

## Important
- [*] Raw corpus v1.0 is preserved and checksummed
```

These markers can later drive Obsidian Tasks, Dataview, or Kanban views. They
must remain understandable without any plugin.

## Metadata Floor

Do not stamp one large schema onto every note.

Use a minimal provenance envelope for generated notes:

```yaml
normalization_version: vault-v1.0
source_kind:
source_id:
source_path:
captured_at:
occurred_at:
concepts: []
tags: []
derived_from: []
```

Rules:

- `source_kind`, `source_id`, and `source_path` make every generated note
  auditable.
- `captured_at` records when the source entered the derived vault.
- `occurred_at` records the best-known event or source time when one exists.
- `concepts` and `tags` remain the primary lightweight semantic fields.
- `derived_from` is required for synthesized project-state, timeline,
  decision, and artifact-summary notes.
- Omit fields that are unknown rather than filling the vault with
  low-confidence placeholders.
- Preserve existing Obsidian frontmatter where present.

### Structurally Scoped Fields

Use extra fields only where the note class needs them:

```yaml
note_role: anchor | current_state | work_queue | timeline_event | artifact_summary | raw_pointer
time_range:
related_projects: []
related_sessions: []
```

Do not overload `status`. Project workflow state belongs in readable body
markers. Authority belongs in note role, folder placement, evidence links, and
human review.

### Experimental Fields

Test these in metadata ablations before making them universal:

```yaml
type:
project:
area:
status:
temporal_mode:
thread_type:
outcome:
signal_strength:
confidence:
canonical:
supersedes:
raw_thread_weight:
```

The question is not whether these fields can be generated. The question is
whether each field improves routing, retrieval quality, cold-start success, or
human navigation enough to justify its maintenance cost.

## Privacy Boundary

The selected Obsidian input contains an explicit `02 Areas/Confidential/`
subtree. The local vault may materialize and retrieve it. Any indexing path that
leaves the local machine must be allowlisted.

Default policy:

```text
local vault materialization: complete selected corpus
local filesystem retrieval: complete selected corpus
VM or external API indexing: deny by default
VM or external API indexing: explicit allowlist only
```

Implement the allowlist as a build policy file rather than relying on every
note to carry correct metadata:

```text
corpus_v1/vault-v1.0/_manifests/api-index-allowlist.txt
```

The initial API benchmark should use a deliberately non-confidential slice.

## Type-Specific Note Contracts

### CLI Agent Session

Claude Code and Codex sessions are operational records. Their normalized layout
should expose the session as a sequence of work:

```markdown
# Session Identity
# Initial Goal
# Context Loaded
# Plan And Task State
# Timeline Of Actions
# Tool Calls
# Files Read
# Mutations
# Commands And Verification
# Decisions
# Failures And Surprises
# User Corrections
# Artifacts Produced
# Unresolved Questions
# Final State
# Raw Transcript
```

The deterministic pass should populate identity, timestamps, raw transcript,
and provenance. A model-assisted pass may extract higher-value sections and
emit timeline events.

### ChatGPT Or Claude Web Conversation

Web chats are exploratory and reflective more often than operational:

```markdown
# Conversation Identity
# Context
# Questions Explored
# Key Ideas
# Claims And Hypotheses
# Decisions
# Useful Frameworks
# Action Items
# Open Questions
# Related Concepts
# Notable Excerpts
# Raw Conversation
```

The raw conversation remains available even when an artifact summary is
generated.

### Obsidian Note

Obsidian notes should receive the lightest touch:

- Preserve the authored body.
- Preserve the original relative path beneath a provenance namespace.
- Preserve existing frontmatter.
- Add only the minimal provenance envelope when missing.
- Treat the original folder path as meaningful routing evidence.
- Extract tasks, events, concepts, and links into derived notes or views.
- Flag title cleanup candidates rather than silently renaming authored notes.

Do not force transcript headings onto authored notes.

### Project Current State

```markdown
# Current State
# In Progress
# Blocked
# Questions
# Deferred
# Important
# Recent Changes
# Key Decisions
# Relevant Artifacts
# Next Actions
```

### Timeline Event

```markdown
# Event
# Timestamp
# Subject
# What Changed
# Why It Matters
# Related Project
# Evidence
# Follow-Ups
```

Timeline events are synthesized navigation notes. They must link to source
evidence and never replace it.

### Raw Provenance Pointer

```markdown
# Source Identity
# Raw Path
# Checksum
# Source Kind
# Captured At
# Related Normalized Notes
```

## Physical Materialization Layout

Use a stable namespace for deterministic source copies:

```text
60-sessions-and-conversations/
  chatgpt/
  claude-web/
  claude-code/
  codex/

90-raw-provenance/
  obsidian/
  chatgpt/
  claude-web/
  claude-code/
  codex/

80-candidates/
  obsidian/
  conversations/
  cli-sessions/
  needs-review/
```

Recommended rule:

- `90-raw-provenance/` holds compact pointer notes, not duplicated raw blobs.
- `80-candidates/` holds deterministic readable materializations awaiting
  richer placement or review.
- Promoted routing notes live in `20-projects/`, `30-systems-and-workflows/`,
  `40-decisions-and-trajectories/`, `50-timeline/`, and
  `70-artifacts-and-reference/`.
- `60-sessions-and-conversations/` holds normalized full-fidelity readable
  transcripts regardless of whether a richer summary exists.

## Builder Design

Implement a new builder around the frozen raw bundle instead of running the
older materializer unchanged.

Proposed entry point:

```text
scripts/build_vault_v1.py
```

Proposed supporting package:

```text
context_refinery/vault_v1/
  inventory.py
  policy.py
  scaffold.py
  materialize_obsidian.py
  materialize_chatgpt.py
  materialize_claude_web.py
  materialize_claude_code.py
  materialize_codex_rollout.py
  derive_views.py
  validate.py
```

Proposed CLI:

```text
scripts/build_vault_v1.py inventory
scripts/build_vault_v1.py scaffold
scripts/build_vault_v1.py materialize
scripts/build_vault_v1.py derive
scripts/build_vault_v1.py validate
scripts/build_vault_v1.py all
```

Common arguments:

```text
--raw-root corpus_v1/raw-v1.0
--vault-root corpus_v1/vault-v1.0
--dry-run
--apply
--source obsidian|chatgpt|claude-web|claude-code|codex
--limit N
```

Requirements:

- Default to dry-run for any command that writes.
- Require `--apply` for materialization or derived-view writes.
- Use deterministic filenames with source ids and short fingerprints.
- Never overwrite a non-generated file.
- Write a JSONL inventory and a JSONL build manifest.
- Be idempotent: a second run over unchanged inputs produces no content diff.
- Preserve Unicode in authored source material.
- Record parse failures without aborting the entire batch.
- Emit counts by source, note role, parse result, and privacy policy.

## Existing Code To Reuse Carefully

The repo already contains useful pieces:

```text
scripts/normalize_corpus.py
context_refinery/normalization_schema.py
context_refinery/adapters/chatgpt.py
context_refinery/adapters/claude.py
context_refinery/adapters/claude_code.py
context_refinery/adapters/codex.py
scripts/normalize_vault_schema_v4.py
```

Reuse parser logic where it matches the frozen inputs. Do not inherit the older
output layout or schema wholesale.

Known adapter gaps against `raw-v1.0`:

1. The selected Claude web source is an extracted `conversations-*.json` file,
   while the current Claude web scanner expects a zip.
2. The selected Codex source is rollout JSONL under dated directories, while
   the current Codex adapter expects a `command-logs` session directory with
   `session-meta.json`.
3. The selected Claude Code subtree includes support files such as subagent
   logs, tool results, and memory files. The builder must distinguish
   top-level sessions from supporting evidence.
4. The raw-bundle windows were selected by filesystem modification time where
   documented. Internal source timestamps may be older and must be preserved
   separately rather than rewritten.

## Materialization Strategy

Materialize in two passes.

### Pass A: Obsidian-Visible Batch

Make the entire selected raw corpus locally visible, browsable, and searchable
as one Obsidian vault batch:

1. Verify raw checksums.
2. Build one mixed-source inventory.
3. Scaffold the vault.
4. Convert every selected source family into readable Markdown with minimal
   source-specific layouts.
5. Write provenance pointers, manifests, and source coverage reports.
6. Validate idempotency, source coverage, and Obsidian-openable structure.
7. Open the vault and inspect it with Obsidian search, folder view, backlinks,
   tags, and graph.

This pass should not depend on an LLM. It should also avoid overbuilding each
adapter before the vault exists. The first batch can use simple source-specific
layouts as long as the output is readable, deterministic, linked to provenance,
and searchable in Obsidian.

Pass A is allowed to be mechanically rough. It is not allowed to be invisible.

### Pass B: Bounded Derived Views

Once the full selected batch is visible in Obsidian, create high-leverage
navigation without blocking retrieval of the rest:

1. Build the four initial project bundles.
2. Extract timeline events for the target date window.
3. Produce artifact summaries for high-signal CLI sessions and conversations.
4. Populate project queues with task markers.
5. Link decisions, events, sessions, conversations, and artifacts.
6. Place uncertain outputs in `80-candidates/needs-review/`.

Start with a mixed review batch:

| Source | Initial enriched sample |
| --- | ---: |
| Obsidian notes | 40 |
| ChatGPT conversations | 20 |
| Claude web conversations | 20 |
| Claude Code sessions | 30 |
| Codex rollout sessions | 20 |
| Repo docs and handoffs relevant to initial project bundles | All relevant |

The enriched sample is intentionally reviewable. Pass A remains complete and
queryable regardless of how much enrichment has been applied.

## Validation Contract

The build is acceptable only when:

- Raw checksums pass before and after generation.
- Every selected raw file has an inventory row.
- Every generated Markdown note has parseable frontmatter when frontmatter is
  expected.
- Every generated note has a raw provenance route.
- Every synthesized note links to evidence.
- No authored Obsidian body is silently modified.
- No confidential path appears in the API allowlist unless explicitly added.
- No duplicate generated output path exists.
- A second identical build produces no generated content changes.
- Parse failures are listed in a reviewable report.
- The vault opens as an Obsidian vault and supports immediate GUI search.
- A small mixed-source sample is inspected manually inside Obsidian before
  enrichment expands.

Write reports under:

```text
corpus_v1/vault-v1.0/_reports/
```

Recommended reports:

```text
inventory-summary.md
materialization-summary.md
validation-summary.md
parse-failures.jsonl
unresolved-links.jsonl
metadata-ablation-results.md
retrieval-comparison.md
```

## Retrieval Experiment

After the Obsidian-visible vault exists, compare retrieval lanes over the same
question bank.

### Lane A: Routed Vault Retrieval

Use Obsidian search, folder routing, filenames, headings, backlinks, tags,
links, and local `rg` over the Markdown vault.

### Lane B: Khoj / API Endpoint Retrieval

Index only the allowlisted non-confidential shaped vault slice into Khoj and
query it through the API endpoint.

### Lane C: Khoj With Vault Fallback

Try the API first. On timeout, unavailable service, weak evidence, or no result,
fall back to routed vault retrieval.

Measure:

```text
answer correctness
evidence recall
citation quality
no-evidence honesty
cold-start task success
p50 and p95 latency
timeout and hang behavior
fallback success
human review cost
metadata maintenance cost
```

Expected result: Khoj/API will probably be faster for broad semantic lookup.
The vault should remain the durable source, visible workspace, inspectable
fallback, and structure that makes failures understandable.

## Metadata Ablation Experiment

Use the same question bank and compare:

```text
A. folder path + filename + headings + provenance only
B. A + concepts + tags
C. B + project + temporal_mode
D. C + thread_type + outcome + signal_strength
E. D + authority fields on reviewed synthesized notes
```

Keep only fields that measurably improve retrieval, routing, cold-start
success, or manual navigation.

## Graphification

Do not make graphification a prerequisite for vault v1.0.

Prepare for it by keeping stable links among:

```text
projects
timeline events
decisions
sessions
conversations
artifacts
raw provenance pointers
```

Once the vault is useful in plain Markdown, generate graph views from those
links. The graph should be a derived interface, not a second source of truth.

## Rough Execution Checklist

1. Freeze and verify the raw v1.0 input contract.
2. Implement the inventory, privacy policy, and dry-run report.
3. Scaffold `vault-v1.0/` and its question-oriented folders.
4. Implement minimal deterministic Markdown materializers for all selected
   source families.
5. Materialize the complete selected corpus locally with provenance pointers.
6. Open the generated vault in Obsidian and inspect/search the batch.
7. Validate coverage, raw integrity, linkability, Obsidian-openability, and
   idempotency.
8. Build the first four project bundles, timeline events, and work queues.
9. Run metadata ablations plus vault-vs-Khoj/API cold-context retrieval tests.
10. Promote useful metadata and structure, then expand to `v1.1`.

## Explicit Non-Goals For v1.0

- Do not mutate the preserved raw bundle.
- Do not upload the complete vault to an API endpoint.
- Do not require model enrichment before a source becomes locally retrievable.
- Do not force V4 storage metadata onto every generated note.
- Do not build graph infrastructure before plain Markdown navigation works.
- Do not collapse durable project identity, current status, work queue, and
  timeline into one anchor note.
- Do not let Khoj/API indexing substitute for a visually coherent Obsidian
  vault.

## Review Questions Before Execution

1. Is the folder structure close enough to how Sab and agents actually ask
   questions?
2. Is the minimal metadata floor still too large, or is each field justified?
3. Should the first Khoj/API allowlist be technical-project-only?
4. Are `MyAPI`, `GDDP`, `DevInfra`, and `Vault Normalization` the right first
   project bundles?
5. Is the proposed mixed enrichment batch large enough to expose real layout
   problems while staying manually reviewable?
6. Should full readable transcripts live in
   `60-sessions-and-conversations/`, or should that folder contain pointers to
   a sibling generated-transcript tree?
