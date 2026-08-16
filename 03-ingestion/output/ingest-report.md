# Khoj ingest report

**Node:** `node-08-khoj-ingest`

**Execution attempt:** `job_20260814T230941010d62b35d8fee:attempt:3`

**Checked:** 2026-08-15T00:15:36Z

**Base commit:** `31c1eadd28229422f8c65012d5d076e14a3ee63b`

**Result:** **PASS — Khoj authenticated the isolated target, confirmed it was empty immediately before ingestion, accepted all 18 staged Markdown files, and then listed exactly those 18 files.**

## Target corpus and clean-target state

- **Target corpus name:** `myapi-part1-decisions-job_20260814T230941010d62b35d8fee`.
- **Khoj isolation scope:** user `gddp-part1@local` on GCE VM `khoj-38-b`, project `khoj-r2`, zone `us-east1-b`; Khoj `1.42.10`; service URL on the VM: `http://localhost:42110`.
- Khoj 1.42.10 isolates content by authenticated user rather than by a caller-supplied corpus namespace. The target corpus name above is the experiment's durable name; its physical clean-corpus boundary is the dedicated `gddp-part1@local` user.
- **Clean-target state: PASS — this isolated target corpus was empty for this run.** Immediately before the write, a Bearer-authenticated `GET /api/content/files?client=api&truncated=true&page=0` returned HTTP `200`, `num_pages: 0`, and zero files.
- A Bearer-authenticated `GET /api/health` returned HTTP `200` with `email: gddp-part1@local`, proving that the precheck and write addressed the isolated user rather than anonymous `default@example.com`.
- The credential was read only on the VM from `/home/sab-mini/.khoj/gddp-part1.token` (mode `0600`, owner `sab-mini:sab-mini`). Its value was neither printed nor copied into the repository.

## Exact ingestion method

1. On the Mac, package exactly the 18 files in `03-ingestion/output/khoj-corpus/` and copy that bounded archive to `khoj-38-b` with `gcloud compute scp`.
2. In the VM shell, read the provisioned token from `/home/sab-mini/.khoj/gddp-part1.token`; authenticate requests with `Authorization: Bearer <token>`; require `/api/health` to identify `gddp-part1@local`.
3. In the VM shell, call `GET http://localhost:42110/api/content/files?client=api&truncated=true&page=0` with the same Bearer header and require HTTP `200`, `num_pages: 0`, and zero files before any write.
4. In the VM shell, send one multipart `PUT` to `http://localhost:42110/api/content?client=api` with the same Bearer header. Supply every staged file as a repeated `files` form field with media type `text/markdown`.
5. Require HTTP `200` and require Khoj's response body to contain exactly the 18 staged filenames.
6. Page through the authenticated `GET /api/content/files` response and require exactly the same 18 filenames and no extras.

The request used `PUT` because this was a verified-empty first batch. No request was sent to the anonymous user corpus.

## Khoj's confirmation

| Check | Khoj / deployment response |
|---|---|
| Authenticated identity | HTTP `200`; `email: gddp-part1@local` |
| Immediate pre-ingest file list | HTTP `200`; `num_pages: 0`; file count `0` |
| Multipart `PUT /api/content?client=api` | HTTP `200` |
| Khoj PUT response body | `D01.md,D02.md,D03.md,D04.md,D05.md,D06.md,D07.md,D08.md,D09.md,D10.md,D12.md,D13.md,D14.md,D15.md,D16.md,D17.md,D18.md,index.md` |
| Post-ingest file list | HTTP `200` on pages 0 and 1; `num_pages: 2`; exact file count `18` |
| Post-ingest filenames | `D01.md D02.md D03.md D04.md D05.md D06.md D07.md D08.md D09.md D10.md D12.md D13.md D14.md D15.md D16.md D17.md D18.md index.md` |
| Independent final read-only verification | 2026-08-15T00:15:36Z; identity `gddp-part1@local`; 2 pages; exact 18-file set |
| Anonymous corpus safety check | Still `num_pages: 395`; no write was directed to it |

Khoj's own PUT response confirms which filenames it indexed. Khoj's authenticated file-list API independently confirms that all 18 are present in the isolated target and that no extra files are present.

## Payload checks

- Source: `03-ingestion/output/khoj-corpus/`.
- Payload: 18 Markdown files — 17 decision files plus `index.md`.
- Canonical manifest SHA-256: `c1fa76ad157d197e28d16f8e9306680e3c870329808e9c1c115dc7587d2f1a3c`.
- The staged file set and bytes remain identical to `02-corpus/output/corpus/`.

The run did not modify graph truth or directly access any runtime database. Khoj content changed only through its authenticated HTTP content API for the dedicated empty user.

## Acceptance status

- `ingested`: **MET** — the exact method and target corpus name are recorded above; Khoj returned HTTP `200` with all 18 filenames and then listed exactly those files through its authenticated API.
- `clean-target`: **MET** — the report records Khoj's immediate pre-ingest confirmation that the dedicated target corpus was empty for this run.
