# Khoj metadata behavior

**Node:** `node-02-chat-path-scorer`  
**Lane:** `part2/probe/metadata-behavior.md` plus `part2/probe/metadata-*` evidence  
**Checked:** 2026-08-16T10:07:05Z  
**Worktree HEAD:** `fe52852c0690004253886b6c713fb7f1cc1113ce`  
**Result:** **Observed — Khoj 1.42.10 sees temporal and provenance values as document text, not as named structured metadata.**

This file records observed behavior. It does not redesign the corpus or drop envelope fields.

## 1. Verdict

| Question | Observed answer | Kind |
|---|---|---|
| Does installed Khoj consume Part 2 envelope fields (`occurred_at`, `recorded_at`, `origin_*`, `item_id`, …) as structured metadata? | **No named consumption observed.** Those 12 keys are absent from Khoj search `additional` objects and from the Khoj 1.42.10 `Entry` model. | measured |
| Does Khoj see temporal / provenance values at all? | **Yes, as document text.** YAML frontmatter and body `Record` / `Sources` sections are chunked and returned inside `entry` / `additional.compiled`. | measured |
| Does Khoj have *any* structured metadata on a hit? | **Yes, but only Khoj-native fields:** `additional.source`, `additional.file`, `additional.compiled`, `additional.heading`, plus `score` and `corpus-id`. | measured |
| Does Khoj have a structured date index? | **Yes, `EntryDates.date`, populated by regex over compiled text, not by reading a field named `occurred_at` / `decided_on`.** It is only applied when the query contains `dt` comparators. | source-measured (1.42.10 wheel); not re-queried live this run |
| Did Part 1 probe queries use that date filter? | **No.** Q1–Q5 used `t=all` with no `dt` / `file:` / `+"word"` syntax. | measured |

**Contract implication (not a corpus change):** keep the 12 envelope keys on Part 2 items even though Khoj 1.42.10 will index them as text. Do not rely on Khoj to filter by `occurred_at`, `recorded_at`, `source_class`, or `origin_sha256` as fields.

## 2. Version and live state

### 2.1 Version

| Source | Value | Kind |
|---|---|---|
| Last live isolated-user ingest / retrieval | Khoj **1.42.10** on GCE `khoj-38-b`, user `gddp-part1@local`, `http://localhost:42110` | prior measured (`03-ingestion/output/ingest-report.md`, `03-ingestion/output/retrieval-check.md`, `04-evaluation/results/part1-summary.md`) |
| This-run PyPI | `https://pypi.org/pypi/khoj/json` → `info.version` = `1.42.10`; release `1.42.10` present | measured this run |
| This-run wheel METADATA | `Name: khoj` / `Version: 1.42.10` from `khoj-1.42.10-py3-none-any.whl` | measured this run |
| This-run live process | **Unreachable.** No local listener on `127.0.0.1:42110`. SSH `khoj-38` timed out. | measured this run |

Command evidence for the wheel:

```text
Run on Mac: curl -fsSL -o /tmp/khoj-1.42.10-src/khoj-1.42.10-py3-none-any.whl https://files.pythonhosted.org/packages/fd/30/850869ceb13ec2446b573ee1660ecd620afa45c4dbd96a280f4dbb5949c1/khoj-1.42.10-py3-none-any.whl
```

### 2.2 Host reachability this run

`khoj-38-b` is **TERMINATED**. It is not started by this lane.

```text
Run on Mac: gcloud compute instances describe khoj-38-b --zone=us-east1-b --format='value(status,lastStartTimestamp,lastStopTimestamp)'
```

Observed: `TERMINATED	2026-08-15T14:09:15.950-07:00	2026-08-16T02:09:07.163-07:00`

```text
Run on Mac: ssh -o ConnectTimeout=10 -o BatchMode=yes khoj-38 'hostname'
```

Observed: `ssh: connect to host 100.75.255.75 port 22: Operation timed out`

```text
Run on Mac: curl -sS -m 2 -o /dev/null -w '%{http_code}' http://127.0.0.1:42110/api/health
```

Observed: connect failure, HTTP `000`.

Raw capture: `part2/probe/metadata-live-host-status.txt`.

Because the VM is down, this lane did **not** send a new `/api/search` or `/api/chat` and did **not** inspect the runtime database. Indexed-probe behavior is taken from the already-captured isolated-user search payloads.

## 3. What was inspected

Safe, read-only surfaces only:

| Surface | Path / object | Used for |
|---|---|---|
| Existing isolated-user search captures | `04-evaluation/results/raw-search-responses.json` (Q1, Q2) | live hit schema + frontmatter-as-text |
| Existing isolated-user search captures | `04-evaluation/results/q3-supersession.md`, `q4-relationship.md` embedded JSON | same schema on later queries |
| Existing ingest/retrieval reports | `03-ingestion/output/ingest-report.md`, `retrieval-check.md` | version, user, `t=all` |
| Indexed payload bytes (unchanged) | `03-ingestion/output/khoj-corpus/D09.md` | source of `decided_on` / `sources` text |
| Khoj 1.42.10 wheel | `/tmp/khoj-1.42.10-src/khoj-1.42.10-py3-none-any.whl` | Entry model, search response, markdown splitter, date filter |
| Local regex demo of 1.42.10 `DateFilter.extract_dates` | `part2/probe/metadata-datefilter-local-demo.json` | ISO dates are harvested from compiled text |

Not inspected / not mutated: Postgres, Django admin, graph truth, job state, corpus files.

## 4. Measured search-response schema

Census of **20** isolated-user hits (Q1–Q4, `t=all`, `n=5`):

| Bucket | Keys observed on every hit |
|---|---|
| Top-level | `entry`, `score`, `cross-score`, `additional`, `corpus-id` |
| `additional` | `source`, `file`, `compiled`, `heading` |

No other `additional` key appears. In particular, none of the Part 2 envelope keys and none of the Part 1 YAML keys (`decided_on`, `sources`, `evidence_paths`, `related_decisions`, …) appear as `additional` fields.

Raw census: `part2/probe/metadata-search-key-census.json`.

This matches Khoj 1.42.10 `SearchResponse` plus `collate_results()`:

- `khoj/utils/rawconfig.py`: `entry`, `score`, `cross_score`, `additional`, `corpus_id`
- `khoj/search_type/text_search.py` `collate_results()` sets `additional` to `{source: file_source, file: file_path, compiled, heading}`

`GET /api/search` accepts `q`, `n`, `t`, `r`, `max_distance`, `dedupe` (`khoj/routers/api.py`). There is no query parameter for YAML field filters.

## 5. Measured: temporal / provenance are document text

### 5.1 Frontmatter is a separate text chunk

On Q1 (`What decision was made about how nodes enter GDDP graphs?`), Khoj returned two `D09.md` hits with different `corpus-id`s:

| Rank | `corpus-id` | `score` | `entry` shape |
|---|---|---:|---|
| 0 | `6048f5f1-a203-46c1-9f0e-629a7929da82` | 0.1024 | Markdown **body** (`# D09 — …`, Decision / Rationale / Record / Sources) |
| 3 | `0c91bccc-0b20-48e2-b170-9e4dba1fa13a` | 0.1432 | YAML **frontmatter only** (starts with `---`, ends with `---`) |

The frontmatter chunk’s `entry` contains, as literal text:

```yaml
decided_on: "2026-08-08"
decided_by: "Sab"
sources:
  - kind: "review_sheet"
    ref: "project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md"
evidence_paths:
  - "project-docs/corpus-work-2026-08/2026-08-08-last2w-decisions.md"
```

The body chunk contains the same facts rewritten as prose:

```text
## Record
- **Decided on:** `2026-08-08`
## Sources
- `review_sheet` `project-docs/corpus-work-2026-08/DECISIONS-REVIEW-SHEET.md`
```

Paired raw extract: `part2/probe/metadata-q1-d09-frontmatter-vs-body.json`.  
Source bytes: `03-ingestion/output/khoj-corpus/D09.md`.  
Original capture: `04-evaluation/results/raw-search-responses.json`.

Across Q1–Q4: **6 / 20** hits start with `---`; **14 / 20** are body/index sections. Frontmatter-only hits are the only ones whose `entry` contains the YAML keys `decided_on`, `evidence_paths`, `schema_version`, `review_mark`, `confidence`.

### 5.2 Part 2 envelope keys are not in the indexed Part 1 payload

The currently indexed isolated corpus is the Part 1 18-file snapshot. Those files use Part 1 decision YAML (`id`, `decided_on`, `sources`, …), not the Part 2 12-key envelope. A string scan of the 20 returned `entry` bodies found **zero** occurrences of `occurred_at`, `recorded_at`, `item_id`, `source_class`, `origin_sha256`, `content_sha256`, `temporal_confidence`, `authority_rank`, `inclusion_status`, or `replaces`.

That is expected by `part2/contract/evidence-contract.md` §7 / rationale `RAT-khoj-metadata`: the Part 1 control payload must not grow these fields. Node 02 records Khoj behavior; it does not add the fields to Part 1 bytes.

### 5.3 Structured relationship field was not used as a filter

Q4 (`How do two decisions relate?`, `t=all`) returned `index.md`, `D01.md`, `D16.md`, `D07.md`. It did **not** return `D18.md` / `D17.md`, the only pair with `related_decisions`. The YAML key therefore survived ingest as text (it is in `03-ingestion/output/khoj-corpus/D18.md`) but was not consumed as a structured relation by this search. Prior Stage H already recorded this; this lane does not re-interpret it as a ranking bug to fix.

## 6. Khoj 1.42.10 source: what *is* structured

Schema excerpt: `part2/probe/metadata-khoj-1.42.10-schema-excerpt.json`.

### 6.1 `Entry` model — no envelope / YAML field columns

`khoj/database/models/__init__.py` `class Entry` stores:

`user`, `agent`, `embeddings`, `raw`, `compiled`, `heading`, `file_source`, `file_type`, `file_path`, `file_name`, `url`, `hashed_value`, `corpus_id`, `search_model`, `file_object`

There is no column for `occurred_at`, `recorded_at`, `decided_on`, `item_id`, `source_class`, `origin_path`, `origin_sha256`, or any other Part 2 envelope key.

`class EntryDates` is only `{date: DateField, entry: FK(Entry)}`.

### 6.2 Markdown ingest does not parse YAML

`khoj/processor/content/markdown/markdown_to_entries.py` splits on ATX headings (`^#{n} `) and token length. It never calls a YAML parser. Frontmatter is ordinary leading text. When the heading-split / 256-token split separates it, it becomes its own `Entry` whose `raw`/`compiled` is the `--- … ---` block.

Embeddings are computed on `compiled` (`update_embeddings(..., key="compiled")`), i.e. filename-prefixed **text**, not a metadata map.

### 6.3 The only structured filters

`EntryAdapters.apply_filters()` (`khoj/database/adapters/__init__.py`):

| Query syntax | Structured target | Notes |
|---|---|---|
| `file:"…"` / `-file:"…"` | `Entry.file_path` regex | Khoj-native filename, not `origin_path` |
| `+"word"` / `-"word"` | `Entry.raw` `icontains` | substring of document text |
| `dt>="…"` / `dt<"…"` / `dt:"…"` | `Entry.embeddings_dates.date` | only if the query contains this syntax |

Date population (`text_to_entries.py`): `DateFilter.extract_dates(added_entry.compiled)` regex-scans compiled **text** for ISO / natural dates and writes `EntryDates` rows. It does not read a field name.

Local replay of those exact 1.42.10 regexes against `D09.md`:

- frontmatter compiled text → dates `["2026-08-08"]` (from `decided_on: "2026-08-08"`)
- body compiled text → dates `["2026-08-08"]` (from `Decided on: \`2026-08-08\``)
- actual Q1 query → `dt` filter terms `[]`

Raw: `part2/probe/metadata-datefilter-local-demo.json`.

**Inference, labeled:** if later Part 2 items put `occurred_at: 2026-08-08` in YAML or body, Khoj would likely harvest `2026-08-08` into `EntryDates` as another text-derived date. That is still not named-field metadata. A query without `dt` syntax would not use those rows.

## 7. Field-by-field

| Field class | Examples | How Khoj 1.42.10 treats them |
|---|---|---|
| Khoj-native hit metadata | `file`, `source=computer`, `heading`, `compiled`, `corpus-id`, `score` | **Structured.** Present on every search hit. |
| Part 1 temporal | `decided_on`, body `Decided on:` | **Document text.** Also eligible for `EntryDates` regex if ISO-shaped. Not a queryable named field unless the caller adds `dt` syntax. |
| Part 1 provenance | `sources[]`, `evidence_paths[]`, body `Sources` | **Document text only.** No structured source graph. |
| Part 1 identity / status | `id`, `project`, `status`, `related_decisions` | **Document text only.** `related_decisions` did not act as a relation filter on Q4. |
| Part 2 envelope temporal | `occurred_at`, `recorded_at`, `temporal_confidence` | **Not present** on the indexed Part 1 payload. **No Entry column.** If later serialized into Markdown, they will be text (+ possible `EntryDates` harvest). |
| Part 2 envelope provenance / identity | `item_id`, `source_class`, `source_id`, `origin_path`, `origin_sha256`, `content_sha256`, `authority_rank`, `inclusion_status`, `replaces` | **Not present** on the indexed payload. **No Entry column.** Same text-only fate if later written into files. |

## 8. Residual limits

- No live `/api/search` this run: VM terminated; this file does not claim a 2026-08-16 live hit.
- Runtime `EntryDates` rows were not read (forbidden runtime-DB access, and host down). Date-index behavior is from 1.42.10 source + a local regex replay.
- Chat generation is out of this lane. Prior isolated-user chat was HTTP 500 (`04-evaluation/results/raw-api-responses.json`).
- Local `dateparser` / `dateutil` are not installed; `get_query_date_range()` was not executed. `get_filter_terms()` / `extract_dates()` regexes were.
- Probe questions stay throwaway. Evaluation questions stay unfrozen until node-10.

## 9. Evidence index

| File | Contents |
|---|---|
| `part2/probe/metadata-behavior.md` | this record |
| `part2/probe/metadata-live-host-status.txt` | gcloud / SSH / localhost health this run |
| `part2/probe/metadata-search-key-census.json` | 20-hit key census |
| `part2/probe/metadata-q1-d09-frontmatter-vs-body.json` | Q1 `D09.md` body vs YAML chunks |
| `part2/probe/metadata-khoj-1.42.10-schema-excerpt.json` | Entry / SearchResponse / filter map from the wheel |
| `part2/probe/metadata-datefilter-local-demo.json` | 1.42.10 date regexes on `D09.md` |
| `04-evaluation/results/raw-search-responses.json` | original isolated-user Q1/Q2 search bodies |
| `03-ingestion/output/ingest-report.md` | live version pin 1.42.10, user `gddp-part1@local` |
