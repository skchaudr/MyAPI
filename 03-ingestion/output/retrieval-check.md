# Khoj retrieval check

**Node:** `node-09-verify-retrieval`  
**Execution attempt:** `job_20260815T003321819242e8d5833a:attempt:0`  
**Checked:** 2026-08-15T00:34:47Z  
**Base commit:** `36c2f18f55ba83b3bb47a5310a466ef8235c5d82`  
**Result:** **PASS — the isolated Khoj user returned `D18.md` as the top result, and the returned decision passage exactly matches the ingested corpus file.**

## Exact probe interface

Run in the VM shell on GCE instance `khoj-38-b` in project `khoj-r2`, zone `us-east1-b`. `localhost` below is the VM-local Khoj 1.42.10 service recorded by the preceding ingest node.

| Field | Exact value |
|---|---|
| Interface | Khoj HTTP search API |
| Method | `GET` |
| Endpoint | `http://localhost:42110/api/search` |
| Query parameter `q` | `What must not become load-bearing architecture?` |
| Query parameter `n` | `5` |
| Query parameter `t` | `all` |
| Canonical request URL | `http://localhost:42110/api/search?q=What+must+not+become+load-bearing+architecture%3F&n=5&t=all` |
| Authentication | `Authorization: Bearer <token>`; token read only inside the VM process from `/home/sab-mini/.khoj/gddp-part1.token` |

Before the search, the same Bearer header was used with `GET http://localhost:42110/api/health`. It returned HTTP `200` and `email: gddp-part1@local`, proving the probe addressed the isolated run user. The token value was not printed, copied to the Mac, or written to this repository.

## Retrieved evidence

The authenticated search returned HTTP `200` with five results. The first result reported:

- `additional.file`: `D18.md`
- `score`: `0.13442397117614135`
- returned passage:

> Unverified assumptions must not become load-bearing architecture.

The result's `entry` also included the surrounding corpus text:

> ## Decision
>
> Unverified assumptions must not become load-bearing architecture.
>
> ## Rationale
>
> Companion rule to D17; compounds with multi-agent proposal chains.

## Corpus match proof

The quoted decision and rationale above occur verbatim in `03-ingestion/output/khoj-corpus/D18.md`. That staged file is byte-identical to the reproducible source `02-corpus/output/corpus/D18.md`; `cmp` exited `0`, and both files have SHA-256:

`1f3f805a852a8437547ab603b82413cde6a42e8fcf197a75446ff657f595c574`

A programmatic exact-string check confirmed the quoted decision appears in both files, and the live response check confirmed the same exact string occurs in the top result's `entry`. Together with Khoj's returned filename `D18.md`, this demonstrates that retrieved evidence came from the ingested decision corpus.

## Check summary

| Check | Result |
|---|---|
| Authenticated identity | HTTP `200`; `gddp-part1@local` |
| Search response | HTTP `200`; 5 results |
| Top result | `D18.md` |
| Returned quote matches staged corpus | PASS |
| Staged `D18.md` matches Stage D source | PASS — byte-identical and same SHA-256 |
| Graph truth or runtime database access | None; read-only Khoj HTTP APIs only |

## Acceptance status

- `presence-verified`: **MET** — the live probe returned a quoted passage from `D18.md`, and the passage exactly matches the ingested corpus file.
- `method-recorded`: **MET** — the exact HTTP method, endpoint, query parameters, VM locality, authentication source, and identity precheck are recorded above for evaluation nodes to repeat.
