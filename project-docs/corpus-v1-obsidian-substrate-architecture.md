# Corpus v1 Obsidian Substrate Architecture

Date: 2026-05-29
Status: Active architecture direction

## Core Thesis

Corpus v1 should not start as a tiny hand-picked archive or as a bulk dump of raw exports.

Corpus v1 should start as an Obsidian-style working memory substrate:

> normalized markdown, meaningful folders, frontmatter provenance, descriptive filenames, stable headers for block retrieval, and explicit trust/canonicality fields.

The goal is a legible knowledge environment that can later be indexed, queried, audited, and expanded. Retrieval becomes one access path into the substrate, not the whole memory system.

## Why This Changed

The original retrieval problem became a corpus problem. The corpus problem became a source-of-truth problem.

Raw volume makes retrieval failures ambiguous. A tiny perfect seed makes evaluation cleaner, but it can underuse the actual advantage of this project: years of notes, conversations, agent sessions, handoffs, and project artifacts.

The better middle path is a modest-sized, model-assisted corpus with strong navigational structure. Corpus size is less dangerous when structure is strong.

Agents do not need perfect context. They need context that narrows the possibility space quickly.

## Architecture Layers

### 1. Raw Source Layer

Raw exports and session logs remain available but untrusted:

- Obsidian vault notes
- ChatGPT exports
- Claude web exports
- Claude Code sessions
- Codex sessions
- repo docs and handoffs

This layer is storage and provenance, not trusted memory.

### 2. Candidate Layer

Candidates are scanned, fingerprinted, and materialized with source provenance.

This layer answers:

- what exists;
- where it came from;
- when it was captured;
- what source type it appears to be;
- whether it can be converted safely.

### 3. Obsidian-Shaped Substrate Layer

Admitted corpus v1 artifacts are markdown notes with folder-level meaning, descriptive filenames, YAML frontmatter, and predictable headers.

This layer is the first real v1 corpus.

It should feel like a working vault, not like an export directory.

### 4. Review And Trust Layer

Agents may propose structure and metadata, but consequential trust fields are gated.

The system must distinguish:

- available raw source;
- admitted structured artifact;
- reviewed artifact;
- canonical source-of-truth artifact;
- superseded artifact retained for history.

### 5. Retrieval And Evaluation Layer

Only after substrate shaping should retrieval tests be used to judge the system.

Failures should map to interpretable causes:

- source missing;
- metadata wrong;
- folder/header structure weak;
- chunk boundary poor;
- reranker ranking the wrong evidence;
- contradiction between canonical and episodic material;
- fair no-evidence result.

## Required Note Shape

Every admitted v1 note should be reviewable by a human and useful to an agent.

### Frontmatter

Baseline fields:

```yaml
source_type:
project:
status:
created_at:
captured_at:
tool:
agent:
decision_type:
confidence:
canonical:
supersedes:
related_to:
```

Field intent:

- `source_type`: what kind of source this is, such as note, handoff, project_doc, cli_session, or conversation.
- `project`: primary project or domain.
- `status`: active, archived, superseded, candidate, reviewed, or canonical.
- `created_at`: when the underlying source was created, if known.
- `captured_at`: when this source entered the corpus pipeline.
- `tool`: originating tool or platform, such as Obsidian, ChatGPT, Claude, Claude Code, Codex, or repo.
- `agent`: agent identity when relevant.
- `decision_type`: architecture, implementation, operations, planning, personal-context, evaluation, or unknown.
- `confidence`: low, medium, high, or explicit numeric equivalent.
- `canonical`: whether this note is allowed to answer source-of-truth questions.
- `supersedes`: older note/source this one replaces.
- `related_to`: sibling notes, raw sources, artifacts, handoffs, or project anchors.

### Body Headers

Baseline headers:

```markdown
# Source
# Context
# Decisions
# Claims
# Artifacts
# Open Questions
# Transcript / Raw Material
```

Header intent:

- `# Source`: provenance, source path/export id/session id, tool, and capture context.
- `# Context`: why this artifact matters and what project/question space it belongs to.
- `# Decisions`: durable decisions made or confirmed in the source.
- `# Claims`: important assertions, observations, or hypotheses that may need later validation.
- `# Artifacts`: files, commits, PRs, commands, notes, screenshots, or outputs produced.
- `# Open Questions`: unresolved issues and future review prompts.
- `# Transcript / Raw Material`: source excerpt, compressed transcript, or link/path back to raw material.

## Folder Meaning

Folder structure should carry retrieval meaning. A useful v1 substrate can be larger than a tiny seed because retrieval can exploit path, title, headers, and metadata.

Recommended conceptual layout:

```text
corpus_v1/substrate/
  00-index/
  10-projects/
  20-agent-sessions/
  30-conversations/
  40-artifacts/
  50-source-of-truth/
  90-raw-provenance/
```

Folder intent:

- `00-index/`: overview maps and corpus navigation notes.
- `10-projects/`: project-specific structured memory.
- `20-agent-sessions/`: Codex, Claude Code, Jules, and other agent work traces promoted into readable form.
- `30-conversations/`: ChatGPT and Claude web conversations converted into structured notes.
- `40-artifacts/`: outputs, handoffs, run logs, benchmark results, and produced deliverables.
- `50-source-of-truth/`: canonical notes and anchors that can answer authority questions.
- `90-raw-provenance/`: pointers to raw exports and preserved source ids, not the main retrieval target.

## Agent Use

Frontier subagents can make the substrate practical at corpus scale.

Good agent work:

- convert raw threads into structured markdown;
- propose frontmatter values;
- extract decisions, claims, artifacts, and open questions;
- identify related notes and supersession candidates;
- flag contradictions or uncertainty;
- preserve raw provenance.

Gated work:

- final canonicality;
- source-of-truth promotion;
- supersession;
- confidence;
- status;
- project relevance.

This keeps agents useful without letting them silently invent authority.

## Evaluation Model

The v1 benchmark should test the shaped substrate, not raw chaos.

Good evaluation questions should ask:

- What is true right now about a project?
- What did Sab decide?
- What source supports that decision?
- What was the trajectory of an idea?
- What is blocked?
- Which artifact should an agent load before acting?
- When is there no fair evidence?

Expected failure diagnosis:

- `corpus_gap`: no admitted source exists.
- `metadata_gap`: source exists but routing fields are weak.
- `structure_gap`: source exists but headers/chunks make the answer hard to retrieve.
- `ranking_gap`: right evidence exists but loses.
- `trust_gap`: retrieved source conflicts with canonical source.
- `source_selection_gap`: conversation should win but anchor wins, or anchor should win but conversation wins.
- `fair_null`: the corpus honestly lacks evidence.

## Retrieval Principle

Do not normalize toward anchors always winning.

Normalize toward honest routing:

- canonical project docs and source-of-truth notes win authority questions;
- conversations win history, thought process, comparison, and idea-development questions;
- agent sessions win operational trace and "what happened in the terminal" questions;
- handoffs win session state and next-step questions;
- artifact summaries reduce raw-thread noise while preserving provenance.

## Anti-Goals

- Bulk-indexing raw exports as trusted memory.
- Treating a flat normalized export as corpus v1.
- Building more tooling before the corpus has a reviewable substrate shape.
- Inventing source-of-truth notes that erase episodic history.
- Suppressing conversations because they are messy.
- Letting agents decide final truth fields with no review gate.

## Direction

The next consequential work is a substrate pass on Big Pi:

1. Keep raw exports and full materialized candidates available.
2. Choose a modest working batch across sources.
3. Use agents to convert candidates into Obsidian-shaped notes.
4. Review and gate trust/canonical fields.
5. Index the substrate.
6. Evaluate retrieval with real project and agent cold-start questions.
7. Expand by diagnosed failure mode, not by raw volume.

This makes corpus v1 a memory architecture, not just an ingestion milestone.
