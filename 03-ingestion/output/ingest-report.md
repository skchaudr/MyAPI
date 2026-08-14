# Khoj ingest report

**Node:** `node-08-khoj-ingest`  
**Execution attempt:** `job_20260814T230941010d62b35d8fee:attempt:0`  
**Checked:** 2026-08-14  
**Base commit:** `36d32fb8efa44787981d271ee3c881a998bc0913`  
**Result:** **BLOCKED — the discovered Khoj deployment is healthy but its only anonymously accessible corpus is pre-existing and non-empty; no clean named corpus or credential for an isolated user was available. No ingestion request was sent.**

## Target corpus

- Requested target corpus name: `myapi-part1-decisions-job_20260814T230941010d62b35d8fee`.
- Discovered deployment: GCE VM `khoj-38-b` in project `khoj-r2`, zone `us-east1-b`; Khoj `1.42.10`; service URL on the VM: `http://localhost:42110`.
- Accessible Khoj identity: anonymous-mode user `default@example.com`.
- Actual content scope exposed by Khoj 1.42.10: all content belongs to the authenticated user. The `client` query parameter is telemetry metadata, not a corpus namespace. The content API has no corpus-name parameter.
- Clean-target state: **FAIL — the accessible user corpus was neither empty nor newly created for this run.** Khoj returned `num_pages: 395` from `GET /api/content/files?client=api&truncated=true&page=0` (10 files per page) and returned pre-existing filenames including `vault_dailies__bb605cf4df__2026.08.07_-_Daily_Rebuild.md`.

The requested named target therefore does not exist on this deployment. Creating or authenticating a separate Khoj user requires credentials that were not supplied by the packet and were not available through the anonymous deployment surface. No secret was guessed.

## Exact intended ingestion method

Once an empty/new Khoj user scope is provided, the bounded method is:

1. Call `GET /api/content/files?client=api&truncated=true&page=0` and require Khoj's response to contain `num_pages: 0` before any write.
2. Send one multipart `PUT` to `http://localhost:42110/api/content?client=api`, with each of the 18 files under `03-ingestion/output/khoj-corpus/` supplied as a repeated `files` form field with media type `text/markdown`.
3. Require HTTP `200`; Khoj 1.42.10's own success body is the comma-separated set of indexed filenames.
4. Call `GET /api/content/files?client=api&truncated=true&page=0` and page through the response; require exactly the 18 staged filenames and no extras.

This is the repository's documented first-batch method (`PUT /api/content?client=api`). On Khoj 1.42.10, `PUT` sets `regenerate=True`; using it against `default@example.com` would replace that user's existing Markdown index. `PATCH` is additive, but would mix the snapshot into the existing corpus and would not satisfy the clean-target criterion. Neither request was sent.

## Khoj confirmation and probes

| Probe | Khoj / deployment response |
|---|---|
| `systemctl is-active khoj.service` | `active` |
| Service command | `/data/khoj-venv/bin/khoj --host 0.0.0.0 --port 42110 --no-gui --anonymous-mode` |
| Package metadata | `khoj 1.42.10` |
| `GET /api/health` | HTTP `200`, `{"email": "default@example.com"}` |
| `GET /api/content/files?client=api&truncated=true&page=0` | HTTP `200`, `num_pages: 395`, pre-existing files returned |
| Multipart `PUT /api/content?client=api` | **Not sent: clean-target precondition failed** |
| Post-ingest file confirmation | **Unavailable because ingestion did not occur** |

The health and file-list responses are Khoj's own API state. They confirm the deployment is reachable and confirm precisely why this attempt cannot claim either acceptance criterion.

## Payload checks

The staged payload remains the exact node-07 artifact:

- 18 Markdown files: 17 decision files plus `index.md`.
- Canonical manifest SHA-256: `c1fa76ad157d197e28d16f8e9306680e3c870329808e9c1c115dc7587d2f1a3c`.
- Source: `03-ingestion/output/khoj-corpus/`.

No graph truth, direct runtime-database operation, or Khoj content mutation was performed by this attempt.

## Acceptance status

- `ingested`: **NOT MET** — no files were written, so Khoj cannot confirm their presence.
- `clean-target`: **NOT MET** — Khoj confirmed that the only accessible corpus already contained approximately 3,950 files (`395` ten-file pages).

**Exact unblock:** provide a new/empty Khoj user scope on `khoj-38-b` plus its API token or authenticated session, then rerun the four-step method above. The current anonymous `default@example.com` corpus must remain untouched.
