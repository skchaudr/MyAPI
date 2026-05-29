# 011 — Corpus v1 Obsidian substrate architecture

Date: 2026-05-29
Branch: feat/corpus-v1-normalization

## Empirical reality

The corpus v1 direction changed from a narrow "curate a tiny perfect seed" frame into a stronger architecture frame:

> Corpus v1 is an Obsidian-style working memory substrate: normalized markdown, meaningful folders, frontmatter provenance, stable headers, and explicit trust/canonicality fields, built on Big Pi from raw exports but admitted into retrieval through reviewable structure.

Mac remains the source-of-truth branch surface. Big Pi is the preferred work surface for heavy corpus shaping because it has the storage and the staged inputs.

The branch already has:

- `scripts/normalize_corpus.py` for scanning and materializing mixed corpus sources.
- `context_refinery/normalization_schema.py` for shared source/type metadata.
- `corpus_v1/manifests/` for scan and copy manifests.
- `corpus_v1/documents/`, `corpus_v1/conversations/`, and `corpus_v1/artifacts/` as the planned materialized layout.
- Big Pi synced with the May 22 ChatGPT shard export, materialized conversations/documents, manifests, and Claude export archive.

The important correction is that a useful v1 corpus is not just smaller. It is more legible.

## Architecture decision

The bad version of corpus v1 is bulk-loading raw chaos.

The better version is a modest-sized, model-assisted, Obsidian-shaped substrate where folders, filenames, YAML frontmatter, stable headers, and review fields all give retrieval and agents more handles.

This means corpus size is less dangerous when structure is strong. Agents do not need perfect context; they need context that narrows the possibility space quickly.

## Required shape

Each admitted v1 artifact should become readable markdown with:

- meaningful folder placement;
- descriptive filename;
- YAML provenance and routing metadata;
- stable section headers;
- clear distinction between source material, claims, decisions, artifacts, and open questions.

Baseline frontmatter fields:

- `source_type`
- `project`
- `status`
- `created_at`
- `captured_at`
- `tool`
- `agent`
- `decision_type`
- `confidence`
- `canonical`
- `supersedes`
- `related_to`

Baseline body headers:

- `# Source`
- `# Context`
- `# Decisions`
- `# Claims`
- `# Artifacts`
- `# Open Questions`
- `# Transcript / Raw Material`

## Trust model

Raw exports can live on Big Pi, but availability is not admission.

Admission into corpus v1 should mean:

- the artifact has been converted into structured markdown;
- provenance is stamped;
- the intended project/source role is visible;
- trust fields are explicit;
- raw material is preserved or linked for audit;
- canonicality is deliberate rather than inferred from volume.

Conversations should not be suppressed just because they are conversations. They should win retrieval when the question is about history, thought process, comparison, prior exploration, or what Sab was thinking at the time.

Canonical notes should win for source-of-truth, operational contract, status, architecture, and decision questions.

## Agent role

Frontier subagents are part of the architecture.

Their useful role is not deciding final truth. Their role is to transform raw candidates into reviewable Obsidian-shaped notes:

- summarize long threads into stable sections;
- propose metadata;
- identify decisions, claims, artifacts, and open questions;
- link related notes;
- surface uncertainty and contradictions.

The consequential fields stay gated by Sab or the primary operator agent:

- `canonical`
- `supersedes`
- `confidence`
- `status`
- `decision_type`
- project relevance

## Evaluation implication

Retrieval tests become meaningful after structure exists.

If retrieval fails against raw exports, the failure is ambiguous: chunking, embeddings, stale docs, duplicate docs, metadata, reranking, missing source selection, or contradictory source material could all be responsible.

If retrieval fails against an Obsidian-shaped substrate, the failure is more diagnosable:

- missing source means admission/corpus selection problem;
- wrong source type means metadata/routing problem;
- right note but wrong section means chunking/header problem;
- right evidence buried means ranking problem;
- contradictory answers mean trust/canonicality problem.

## Anti-goals

- Do not treat `corpus_v1/normalized/` or any flat ingest output as the final v1 corpus.
- Do not bulk-index raw ChatGPT, Claude, Codex, or Claude Code exports as trusted memory.
- Do not force anchors to win every query.
- Do not invent authority where only episodic history exists.
- Do not keep adding normalization machinery when the next bottleneck is corpus shape and admission.

## Resume point

The next project movement should be toward a corpus v1 substrate pass on Big Pi:

1. Use the existing staged inputs as raw/candidate material.
2. Select a modest working batch across Obsidian notes, agent sessions, ChatGPT/Claude conversations, and durable artifacts.
3. Convert candidates into Obsidian-shaped markdown with stable folders, frontmatter, and headers.
4. Gate trust/canonical fields deliberately.
5. Index the shaped substrate.
6. Evaluate retrieval against real MyAPI questions and agent cold-start tasks.

The stable architecture note for future work is `project-docs/corpus-v1-obsidian-substrate-architecture.md`.
