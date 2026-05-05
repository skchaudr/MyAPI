---
title: Corpus v1 normalization readiness
status: planning
projects: [myapi, gddp, context-refinery]
tags: [corpus, normalization, retrieval, benchmark, ingestion]
date: 2026-05-05
references_events:
  - handoffs/000-cleared-context-bare-retrieval.md
  - handoffs/001-a7-anchor-variant-fix-episodic-axis.md
  - handoffs/002-f5-episodic-s1-schema-source-type-design.md
  - handoffs/003-final-v0-benchmark-run.md
  - project-docs/source-type-taxonomy-plan.md
---

# Corpus v1 normalization readiness

## Current ground truth

This project has crossed from retrieval tuning into corpus architecture.

The v0 acceptance and benchmark work proved that the retrieval stack can be mechanically improved, but the remaining trust failures are mostly caused by corpus shape:

- Meta-commentary can outrank the source artifact.
- Fresh or broad status docs can edge out canonical identity docs.
- Episodic source threads and retrospective writeups are not differentiated strongly enough.
- Some benchmark queries silently assume evidence exists, when a correct system should sometimes return a null/no-evidence answer.
- Conversation imports are currently too blunt: the whole thread is treated as one noisy document instead of a source event plus extracted artifact summary.

Recent handoff state:

- Acceptance is at 6/7 mechanical, with A1 known-failing because it is now a bank/corpus-evolution question rather than a clear retrieval bug.
- `benchmark-v1.md` exists as the refinement target for the v1 query bank.
- The next benchmark pass should walk the current bank query by query, with owner approval for wording changes.
- The relevant taxonomy direction is already captured in `project-docs/source-type-taxonomy-plan.md`, but it needs to be expanded beyond a single `source_type` field into a normalization schema that handles conversation data honestly.

May 5 pivot:

- Replace MyAPI-first benchmark questions with GDDP-first questions for the v1 baseline. MyAPI is the active project and did not have enough historical vault evidence until mid/late April, so it is unfair as an early normalization benchmark.
- Use GDDP / graph-driven development as the primary corpus-grounded benchmark subject because its anchor and control-plane docs entered the vault around `2026-03-11` through `2026-03-12`.
- Keep MyAPI in the readiness plan as the normalization target and runtime project, but do not use MyAPI history questions as ground truth unless their `fair_after` date is `2026-04-14` or later, with stronger confidence after `2026-04-25`.
- A live smoke query for `"What is graph-driven development, and what problem is GDDP trying to solve?"` returned a strong Obsidian top hit but also ranked several ChatGPT/meta conversation chunks nearby. That is a representative v1 failure mode: anchor/source material is visible, but conversation artifacts still need classification and weighting.
- A live smoke query for `"How does GDDP turn events into bounded agent work without letting executors freestyle?"` returned only ChatGPT conversation chunks in the top results, despite direct Obsidian evidence in GDDP pipeline, graph, and roadmap docs. This is a stronger v1 benchmark case for meta-eclipse and missing source-type routing.

## Existing assets

Code and scripts already present:

- `context_refinery/adapters/chatgpt.py` parses ChatGPT conversation export JSON into canonical markdown.
- `context_refinery/adapters/claude.py` parses Claude.ai `conversations.json` exports.
- `context_refinery/adapters/claude_code.py` parses Claude Code JSONL sessions from `~/.claude/projects`.
- `scripts/normalize_vault_schema_v4.py` already performs conservative Obsidian frontmatter normalization with dry-run reports, manifests, backups, and a coverage ledger.
- `scripts/run_query_benchmark.py` runs the current broad query benchmark against `/query`.
- `scripts/acceptance.py` is the smaller mechanical acceptance harness.

Local corpus locations observed:

- Obsidian vault: `/home/sab-ssd/obsidian/SoloDeveloper`
- Claude Code sessions: `/home/sab-ssd/.claude/projects`
- Claude session JSON: `/home/sab-ssd/.claude/sessions`
- Codex history/session material: `/home/sab-ssd/.codex`, `/home/sab-ssd/.pi/agent/sessions`
- OpenClaw sessions and normalized events: `/home/sab-ssd/.openclaw`

## Proposed v1 objective

Corpus v1 should not try to make every document perfect.

The objective is to make each corpus item honest enough that retrieval can route by intent:

- What kind of source is this?
- What kind of work does it represent?
- Is this an event, a summary, or a hybrid?
- If it is a conversation, what artifact or decision came out of it?
- Should the raw thread be shown, or should a companion artifact summary rank first?

## Canonical metadata

Primary field:

```yaml
source_type: anchor | project_doc | handoff | daily_note | conversation | code | test | config | reference
```

Secondary fields:

```yaml
work_type:
  - project_work
  - configuration
  - experiment
  - reflection
  - creative
  - research

temporal_mode: episodic | meta | hybrid
```

Conversation-specific fields:

```yaml
thread_type: execution | configuration | exploration | reflection | research | support
primary_project: myapi | devinfra | vault | unknown
outcome: decision | code_change | diagnosis | plan | insight | no_artifact
signal_strength: high | medium | low
artifact_summary: path-or-null
raw_thread_weight: normal | downweighted | excluded
review_status: inferred | needs_review | approved
```

These fields should allow multi-label reality. For example:

```yaml
source_type: conversation
work_type: [project_work, reflection]
temporal_mode: hybrid
thread_type: execution
primary_project: myapi
outcome: decision
signal_strength: high
```

## Benchmark readiness plan

### Benchmark contract

Every v1 benchmark query must satisfy at least one of two tests:

- It is grounded in something the current corpus actually contains.
- It is an actual question Sab or an agent would plausibly ask, even if the answer may not exist in the corpus.

This matters because the benchmark is measuring trust, not just hit-rate. A query can be valid even when the correct answer is "no documented evidence found." What is invalid is a synthetic query that quietly assumes nonexistent evidence and then rewards the system for returning a plausible-looking wrong note.

### Temporal fairness

Every v1 query also needs a corpus-availability cutoff. A question is only fair if the relevant evidence existed in the vault, or if the benchmark explicitly expects a no-evidence answer.

Initial vault Git-history findings:

- GDDP / graph-driven development is fair much earlier. The first observed GDDP anchor appears on `2026-03-11`, and the GDDP control-plane/schema corpus becomes dense across `2026-03-12` through `2026-03-16`.
- MyAPI is not fair as an early-vault query. The MyAPI project folder and first anchor/context notes appear in Obsidian on `2026-04-14`.
- MyAPI benchmark/run evidence is much stronger only after `2026-04-25`, when the MyAPI project docs were added experimentally.
- The MyAPI folder/frontmatter became materially more normalized on `2026-04-26`, when the V4 floor was applied to `01 Projects`.
- Vault schema questions need their own cutoffs: V2 appears on `2026-02-14`, V3-related notes appear on `2026-04-19` and `2026-04-23`, and V4 material appears on `2026-04-20` and `2026-04-26`.

Practical rule: each benchmark query should carry a `fair_after` date and, where relevant, a `corpus_state_required` note. This prevents unfair failures caused by asking the system about notes that had not entered Obsidian yet.

### 1. Freeze v0

Create a stable frozen copy of the current benchmark/corpus state before normalization changes:

- Keep the current v0 benchmark evidence readable.
- Record the current top winners and failure modes.
- Do not keep patching retrieval weights against v0 after this point.

Suggested artifact:

```text
project-docs/retrieval-benchmark-v0/corpus_v0_frozen/
```

### 2. Build the v1 eval set from observed failures

Use `benchmark-v1.md` as the query-bank refinement target.

For each candidate query, record:

```yaml
query:
admission_basis: corpus_grounded | realistic_user_or_agent_question
expected_answer_type:
evidence_expectation: documented | possibly_absent | intentionally_unknown
actual_winner:
why_winner_won:
failure_mode:
metadata_that_would_fix_routing:
owner_decision: keep | rewrite | delete | unsure
```

Target categories:

- good hit
- embarrassing miss
- meta-eclipse
- stale-doc win
- conversation beats artifact
- artifact beats conversation when conversation was desired
- no-evidence/null should pass

Target size:

- Start with 10-15 high-signal approved queries.
- Expand toward 25-40 only after the categories are clear and the review process feels cheap.

### 3. Build a corpus normalizer CLI

Extend the existing vault-normalizer pattern into a corpus normalizer:

```bash
normalize-corpus scan
normalize-corpus inspect <path-or-id>
normalize-corpus apply
normalize-corpus export
```

The CLI should support at least four input families:

- Obsidian markdown files
- ChatGPT export JSON
- Claude.ai export JSON
- Claude Code / Codex / OpenClaw JSONL sessions

Output should be a normalized corpus bundle for MyAPI, not destructive edits by default.

Suggested output layout:

```text
corpus_v1/
  documents/
  conversations/
  artifacts/
  manifests/
  review_queue/
  eval/
```

### 4. Add conversation viewer and approval workflow

Conversation imports need a clean review surface before they are trusted.

Minimum useful workflow:

- Parse raw JSON/JSONL into readable markdown.
- Show thread metadata, inferred classification, and extracted artifact summary.
- Allow owner approval/editing of only the classification block and artifact summary.
- Keep raw conversation intact for provenance.
- Export approved artifact summaries as first-class corpus docs.
- Downweight raw threads unless the query intent asks for the conversation itself.

This can start as markdown plus JSON manifests before becoming a web UI.

### 5. Normalize routing after the data exists

Only after the v1 corpus has stamped metadata:

- Add intent-to-source weighting.
- Add conversation artifact boosting.
- Add raw thread downweighting.
- Add null/evidence-absence grading to the harness.

Do not tune this blind. Tune against the v1 eval set.

## Immediate next implementation slice

The next useful slice is small:

1. Add a shared normalization schema module for `source_type`, `work_type`, `temporal_mode`, conversation fields, confidence, and review status.
2. Add a dry-run `normalize-corpus scan` command that inventories Obsidian markdown plus Claude Code sessions and emits a JSONL manifest.
3. Add `normalize-corpus inspect <id>` to render one item as readable markdown with inferred metadata.
4. Add a first artifact-summary template for conversations.
5. Run the current v1 benchmark bank against the frozen corpus and annotate 10-15 cases manually.

That creates enough ground truth to start normalizing without guessing.

## Success criteria

Corpus v1 is ready for follow-up benchmark testing when:

- Every exported item has `source_type`, `work_type`, and `temporal_mode`.
- Conversation/session items also have `thread_type`, `primary_project`, `outcome`, `signal_strength`, and `review_status`.
- Raw conversations can be viewed cleanly as markdown.
- High-signal conversations have companion artifact summaries.
- The v1 eval set includes null-answer cases and meta-vs-source cases.
- Benchmark output can classify failure as query wording, missing evidence, stale source, meta-eclipse, or routing metadata gap.

The practical target is 80 percent automatic stamping, 15 percent review queue, and 5 percent special handling.
