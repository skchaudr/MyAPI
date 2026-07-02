# Corpus Tier Policy - 2026-07-02

MyAPI already has `Corpus v1.0`. The rebuild question is what enters the active
corpus, how recent dynamic data stays fresh, and what older material earns
durable or canonical status.

## Tier Model

| Tier | Meaning | Default retrieval role |
|---|---|---|
| `hot` | Recent dynamic material, refreshed daily. Default window: roughly 15-30 days. | First-class context for ordinary project/person questions. |
| `durable` | Older or cross-window material explicitly promoted because it still matters. | First-class context even when old. Durable/canonical status overrides recency decay. |
| `cold` | Older bulk material, including Corpus v1.0 and historical exports. | Searchable for recovery, history, and benchmarks; lower default gravity. |

## What Goes Where

`hot` includes active Obsidian notes, current repo docs, recent Codex/Claude
sessions, `.pi` traces, handoffs, VM/Khoj manifests, and fresh benchmark output.

`durable` includes architecture anchors, project origin notes, decisions,
benchmark conclusions, canonical commands, stable preferences, and handoffs that
future agents must preserve.

`cold` includes Corpus v1.0, historical exports, and older session material that
has not been promoted.

## Retrieval Policy

Default project/user context:

```text
hot + durable
```

Deep history or recovery:

```text
hot + durable + cold
```

Verification:

```text
durable first
then hot evidence
then cold only when needed
```

Freshness is a ranking signal. Durable/canonical status is the override.

## MyAPI vs MyMCP

MyAPI owns corpus policy: source refresh, tier classification, normalization,
indexes, manifests, caches, and promotion rules.

MyMCP stays lean: two public tools, compact arguments, visible budgets, and small
context briefs. It asks MyAPI for bounded context instead of carrying corpus
complexity in the MCP surface.

## VM / Khoj Role

The Google Cloud VM, buckets, and Khoj-backed embeddings can remain a retrieval
backend or benchmark oracle. The rebuild is less about inventing a new RAG engine
and more about controlling what gets indexed, what gets trusted by default, and
what answer budget returns through MyMCP.

## CLI Normalization Pass

A useful next implementation slice is a CLI normalization pass:

1. Read candidate sources from the live vault, repo docs, session logs, `.pi`
   traces, Corpus v1.0, and VM/Khoj manifests.
2. Stamp each item as `hot`, `durable`, or `cold`.
3. Require explicit durable/canonical reasons for old material that should outrank
   recency.
4. Emit a source manifest and a small daily active corpus bundle.
5. Reindex or benchmark against Khoj using the active bundle first.

Corpus v1.0 stays valuable without becoming the gravity well.
