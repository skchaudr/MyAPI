# Khoj transform notes

**Node:** `node-07-khoj-transform`  
**Execution attempt:** `job_20260814T224730724b54653349fe:attempt:0`  
**Checked:** 2026-08-14  
**Base commit:** `e1ebe5724da26a7c8d34d72da74064a7c19d8068`  
**Result:** **PASS — the staged Khoj corpus has the same 18 relative paths and exact bytes as the reproducible Stage D corpus.**

## Khoj deployment discovery

The current repository configuration identifies `http://khoj-38:42110` as the intended Khoj endpoint (`deploy/com.myapi.daily-hot-corpus.plist` and `scripts/deliver_daily_active_corpus.py`). Read-only live probes found the deployment in transition rather than an active Khoj service.

| Fact | Observed value |
|---|---|
| Configured host | `khoj-38:42110` |
| Tailscale peer | `khoj-38` / `100.75.255.75`, offline at probe time |
| SSH alias | `khoj-38` → `34.26.132.7`; connection timed out |
| GCE source/recovery host | `khoj-38-b`, `TERMINATED` |
| GCE replacement target | Regional managed group `khoj-rmig`, two running instances: `khoj-rmig-1k2j` and `khoj-rmig-h0g4` |
| Khoj version | **Unavailable from the live target:** both replacement instances had no `khoj.service`, no Khoj package, no process, and nothing listening on port `42110` |

The host is recorded as `khoj-38:42110` because that is the newest configured application target. No version is guessed: there was no running Khoj deployment from which a package version could be read. This state must be re-probed before Stage F ingestion.

Discovery used only SSH/systemd/process/package metadata, Tailscale status, and GCE resource descriptions. It did not query or modify Khoj content, graph truth, or a runtime database.

## Chosen ingest format

**Format:** one UTF-8 Markdown file per decision, with its existing YAML frontmatter, plus the generated `index.md`.

Khoj's documented content API accepts Markdown files as multipart fields, using each filename as the field key and the file contents as its value. `02-corpus/output/corpus/` already has that representation, so the Stage E transform is a byte-for-byte staging copy rather than a second renderer. This preserves the validated metadata, links, filenames, line endings, and body bytes and prevents format choices from being improvised during ingestion.

`index.md` remains included because it is part of the fixed 18-file Stage D snapshot. Stage F must ingest exactly the contents of `03-ingestion/output/khoj-corpus/` for these notes to remain an exact receipt of consumed bytes.

## Repeatable transform

Run on Mac, from the repository root:

```bash
python3 03-ingestion/transform_for_khoj.py
```

The standard-library transform validates that the source is a non-empty flat directory containing only `.md` files, copies file bytes into a staging directory, verifies a SHA-256 manifest, and atomically replaces the derived output directory.

| Input | Output |
|---|---|
| `02-corpus/output/corpus/` | `03-ingestion/output/khoj-corpus/` |

## Evidence

| Check | Result |
|---|---|
| Source snapshot | 17 decision files + `index.md` |
| Output file count | 18 |
| Output extensions | `.md` only |
| Relative path set | Identical |
| Recursive byte comparison | `diff -qr` exit `0`, no output |
| Per-file SHA-256 manifests | Identical |
| Canonical manifest SHA-256 | `c1fa76ad157d197e28d16f8e9306680e3c870329808e9c1c115dc7587d2f1a3c` |
| Independent temporary rerun | Identical to source and checked output |

The transform and checks did not read or modify graph truth or any runtime database.
