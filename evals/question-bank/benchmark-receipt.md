# Question Bank Receipt

- Schema version: `1.0`
- Bank version: `1.0.0`
- Generated: `2026-07-30T08:10:49+00:00`
- Hosts scanned: mini, air

## Session coverage

| Host | Store | Session files |
| --- | --- | ---: |
| air | codex_sessions | 579 |
| air | pi_agent_sessions | 321 |
| mini | codex_sessions | 93 |
| mini | pi_agent_sessions | 190 |

| Host | Total session files |
| --- | ---: |
| air | 900 |
| mini | 283 |

## Per-store extraction (raw user messages)

| Host | Store | Raw user messages |
| --- | --- | ---: |
| air | codex_sessions | 8335 |
| air | pi_agent_sessions | 1940 |
| mini | codex_sessions | 1595 |
| mini | pi_agent_sessions | 1479 |

## Bank size after dedup

| Metric | Count |
| --- | ---: |
| Unique questions (after normalization dedup) | 3244 |
| Total question occurrences across all sessions | 4534 |

## Category breakdown

| Category | Unique |
| --- | ---: |
| graphify_invocation | 4 |
| graphify_meta | 4 |
| knowledge | 3236 |

## Shape breakdown (per category)

| Category | Shape | Unique |
| --- | --- | ---: |
| graphify_invocation | benchmark | 4 |
| graphify_meta | benchmark | 4 |
| knowledge | benchmark | 348 |
| knowledge | conversational | 2888 |

**Benchmark-shape subset** (self-contained retrieval queries, suitable for `capture-live-vertex-baseline` and `prove-myapi-context-retrieval`): **356** questions. Conversational follow-ups (real agent questions but context-dependent) add another **2888** for a total bank of **3244**.

## Per-host occurrence counts (post-dedup)

| Host | Occurrences |
| --- | ---: |
| air | 3340 |
| mini | 1194 |

## Per-store occurrence counts (post-dedup)

| Host | Store | Occurrences |
| --- | --- | ---: |
| air | codex_sessions | 2573 |
| air | pi_agent_sessions | 767 |
| mini | codex_sessions | 581 |
| mini | pi_agent_sessions | 613 |

## Provenance

Every bank entry in the JSONL records `host`, `store`, `session_path`, `line_index`, `timestamp`, `text_fingerprint`, `char_count`, `token_count_est`, `category`, and `shape`. The tracked manifest carries the same fields except `text` and any verbatim fragments: it is a fingerprint-and-provenance index. Categories: `knowledge`, `graphify_invocation`, `graphify_meta`. Shapes: `benchmark` (self-contained retrieval query) or `conversational` (reactive follow-up depending on prior turn).
