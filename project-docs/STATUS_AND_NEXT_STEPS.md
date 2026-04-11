# Status And Next Steps

## Current Situation

This repo contains two relevant tracks:

- `context-refinery`, a prototype web UI intended to prepare data for Khoj
- a live Khoj instance on the GCP VM `khoj-headless-engine`

As of April 9, 2026, the Khoj VM is healthy again. The service had been failing due to an inconsistent Python package install inside the virtualenv. The installed `khoj==1.42.10` runtime code and shipped migrations did not match, which caused runtime queries against a missing `database_chatmodeloptions` table. I connected to the VM, verified the DB/service config, force-reinstalled `khoj==1.42.10` in the existing venv, restarted the service, and confirmed the health endpoint returns `200 OK`.

The remaining warnings on the VM are about optional authentication/email configuration, not service availability.

## VM Environment

- VM: `khoj-headless-engine`
- Zone: `us-central1-a`
- OS: Ubuntu 22.04
- Khoj service: `khoj.service`
- Khoj working directory: `/home/sbkchaudry_gmail_com/khoj-engine`
- Virtualenv: `/home/sbkchaudry_gmail_com/khoj-engine/venv`
- Health endpoint: `http://localhost:42110/api/health`
- PostgreSQL host: `localhost`
- PostgreSQL port: `5432`
- PostgreSQL DB: `khoj`
- PostgreSQL user: `khoj`

Service status verified on April 9, 2026:

- `systemctl status khoj` showed `active (running)`
- `curl http://localhost:42110/api/health` returned `200 OK`

## What Context Refinery Is Right Now

The `context-refinery` app is a UI foundation, not yet a complete ingestion and normalization system.

What is real:

- React/Vite frontend scaffold
- review-oriented UI for import, refine, and export flows
- Gemini summarization hook in `src/services/geminiService.ts`

What is still mostly conceptual or mocked:

- actual file/folder ingestion
- source-specific parsing
- canonical schema generation
- sanitization and normalization pipeline
- deduplication
- structured validation
- actual Khoj-ready export logic

Important current files:

- `context-refinery/src/components/ImportView.tsx`
- `context-refinery/src/components/RefineView.tsx`
- `context-refinery/src/components/ExportView.tsx`
- `context-refinery/src/services/geminiService.ts`
- `context-refinery/src/mockData.ts`
- `context-refinery-foundation.md`

## Architectural Reality

Khoj should not be expected to do the bulk of upstream data cleanup.

Khoj is good at:

- indexing
- embeddings
- chunking/retrieval
- using metadata when metadata exists
- serving search/chat over prepared content

Khoj is not the right place to rely on for:

- source normalization
- heavy sanitization
- deduplication
- metadata repair
- provenance reconstruction
- canonical content modeling

The highest-value move is to make Context Refinery produce a canonical intermediate format before handing documents to Khoj.

## Recommended Canonical Model

Statuses already under discussion should become first-class schema fields:

- `mature`
- `scratchpad`
- `deprecated`
- `reference`

Suggested canonical document shape:

```ts
type CanonicalDocument = {
  id: string
  title: string
  source: {
    system: string
    type: string
    path?: string
    url?: string
    conversation_id?: string
    external_id?: string
  }
  timestamps: {
    created_at?: string
    updated_at?: string
    ingested_at: string
  }
  author?: string
  status: "mature" | "scratchpad" | "deprecated" | "reference"
  doc_type: "note" | "conversation" | "spec" | "article" | "dataset" | "log" | "other"
  tags: string[]
  summary?: string
  relationships: Array<{
    type: string
    target_id: string
    label?: string
  }>
  content: {
    raw_text?: string
    cleaned_markdown: string
  }
  quality: {
    noisy: boolean
    duplicate_of?: string
    warnings: string[]
  }
}
```

Recommended primary export format for Khoj:

- one Markdown file per canonical document
- YAML frontmatter containing metadata
- cleaned body content below the frontmatter
- export manifest summarizing counts, warnings, failures, and source lineage

## Why This Matters

The better the upstream structure, the more useful Khoj becomes.

Better input should mean:

- better retrieval precision
- less token waste from boilerplate/noise
- stronger provenance and trust
- clearer filtering by status/type/tag
- easier dedupe and lifecycle management
- cleaner future automation

If the refinery outputs raw or weakly structured exports, Khoj can still index them, but the quality ceiling will be lower.

## Recommended Pipeline To Build

Build the system in these stages:

1. Ingest
   - file/folder upload
   - ZIP extraction
   - manifest generation

2. Detect
   - identify source type
   - route to the correct parser

3. Parse
   - source adapters for Obsidian, ChatGPT, Claude, Markdown/text, CSV

4. Sanitize
   - strip wrappers, nav junk, legal/footer noise, duplicated boilerplate
   - normalize markdown/text

5. Canonicalize
   - convert every parsed item into the canonical document schema

6. Enrich
   - summaries
   - tag suggestions
   - doc type classification
   - relationship extraction
   - maturity/status assignment where appropriate

7. Validate
   - schema validation
   - missing metadata checks
   - duplicate detection
   - quality warnings

8. Export
   - Markdown + YAML frontmatter
   - JSONL if useful for downstream tooling
   - ZIP package or directory layout for Khoj ingestion
   - output manifest

## What Can Be Parallelized

Once the canonical schema and normalization rules are defined, much of the implementation can be delegated to an async agent.

Good parallel work streams:

- schema/types/validation
- source adapters
- sanitizers
- enrichment modules
- export packager
- UI wiring for review/edit/approve/export
- fixture generation and tests

What should stay human-directed first:

- canonical schema design
- required vs optional metadata fields
- exact meaning of statuses
- chunking policy
- sanitization and dropping rules
- acceptance criteria for output quality

## Immediate Next Steps

Recommended order of operations:

1. Write a formal schema spec for canonical documents and manifests.
2. Define lifecycle/status semantics for `mature`, `scratchpad`, `deprecated`, and `reference`.
3. Choose the first source adapters to support.
4. Implement canonicalization and validation before expanding the UI.
5. Add real export logic for Khoj-ready Markdown with YAML frontmatter.
6. Only then wire the current UI prototype to live processing jobs.

## Handoff Prompt For The Next VM Session

Use the following prompt with the next Codex instance on the VM:

```text
Context:
- Khoj on this VM is healthy. `khoj.service` is running and `/api/health` returns 200.
- The local project includes a `context-refinery` prototype UI, but it is still mostly mock-driven and does not yet implement the real ingestion/normalization/export pipeline.
- The architectural priority is to build a canonical intermediate format for knowledge documents before expanding UI behavior.
- Status fields like `mature`, `scratchpad`, `deprecated`, and `reference` should be first-class schema fields.
- The goal is for Context Refinery to output Khoj-ready normalized documents, not raw source exports.

Task:
1. Inspect the current `context-refinery` codebase in this workspace.
2. Draft and implement a canonical document schema and validation layer.
3. Build the first pass of the ingestion pipeline to normalize source inputs into that schema.
4. Prefer Markdown + YAML frontmatter as the primary Khoj export format.
5. Keep provenance, tags, relationships, timestamps, and status fields explicit.
6. Verify what is mock-only in the existing UI and wire live processing incrementally.
```
