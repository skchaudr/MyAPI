# MyAPI Part 1 — preserved result

**Part 1 status: complete.** The fixed decision snapshot was validated, rebuilt, staged, ingested into an isolated Khoj user, retrieved, and queried with the five predetermined prompts. Results are preserved as returned; answer quality is evidence, not a completion gate.

## Run metadata and evidence chain

| Stage | Date (UTC) | Graph job / attempt | Preserved evidence |
|---|---|---|---|
| C — validate decisions | 2026-08-14 | `job_20260814T214732845a5af48c5dcf:attempt:0` | [validation report](../../01-decisions/output/validation-report.md) |
| D — build corpus | 2026-08-14 | `job_20260814T221953847cb1e568ca22:attempt:0` | [repro report](../../02-corpus/output/repro-report.md) |
| E — transform for Khoj | 2026-08-14 | `job_20260814T224730724b54653349fe:attempt:0` | [transform notes](../../03-ingestion/output/transform-notes.md) |
| F — ingest | 2026-08-15T00:15:36Z | `job_20260814T230941010d62b35d8fee:attempt:3` | [ingest report](../../03-ingestion/output/ingest-report.md) |
| G — verify retrieval | 2026-08-15T00:34:47Z | `job_20260815T003321819242e8d5833a:attempt:0` | [retrieval check](../../03-ingestion/output/retrieval-check.md) |
| H — factual + rationale | 2026-08-15T00:48:03Z–00:48:56Z | `job_20260815T0045189219fa28cd0235:attempt:0` | [Q1 factual](q1-factual.md) · [Q2 rationale](q2-rationale.md) |
| H — supersession + relationship | 2026-08-15T00:49:41Z | `job_20260815T0045189302c8fd4a6af3:attempt:0` | [Q3 supersession](q3-supersession.md) · [Q4 relationship](q4-relationship.md) |
| H — negative control | 2026-08-15T00:47:45Z | `job_20260815T00451894af7b62cd267e:attempt:0` | [Q5 negative control](q5-negative-control.md) |
| I — preserve and stop | 2026-08-15T01:34:15Z | `job_20260815T01274996591cd849b786:attempt:0` | this summary |

- **Base for Stage I:** `74a45f80ca8eff2b8a14328513ecaa3d5090e0c6`.
- **Decision snapshot:** 17 accepted decisions (`D01`–`D10`, `D12`–`D18`); D11 was rejected. The corpus contains 18 Markdown files: one per accepted decision plus `index.md`. See the [canonical JSONL](../../01-decisions/output/decisions-canonical.jsonl) and [corpus index](../../02-corpus/output/corpus/index.md).
- **Khoj target:** durable experiment name `myapi-part1-decisions-job_20260814T230941010d62b35d8fee`; physical isolation user `gddp-part1@local` on `khoj-38-b`, project `khoj-r2`, zone `us-east1-b`; Khoj `1.42.10` at VM-local `http://localhost:42110`.
- **Raw captures:** [Q1/Q2 chat responses](raw-api-responses.json) and [Q1/Q2 search responses](raw-search-responses.json). Q3–Q5 raw responses are embedded verbatim in their result files above. The predetermined prompts are [Q1](../queries/q1.txt), [Q2](../queries/q2.txt), [Q3](../queries/q3.txt), [Q4](../queries/q4.txt), and [Q5](../queries/q5.txt).

## Fixed evaluation result

| Query | Observed result |
|---|---|
| Q1 — factual | Chat returned HTTP 500 because no chat model was configured. Search returned HTTP 200 and ranked `D09.md`, containing the requested decision, first. |
| Q2 — rationale | Chat returned the same HTTP 500. Search returned HTTP 200 and ranked the `D09.md` rationale first. |
| Q3 — supersession | Search returned HTTP 200 with five passages, none supporting a replacement claim; the validated set contains zero `replaces` or `replaced_by` links. |
| Q4 — relationship | Search returned HTTP 200, but its top five omitted `D18.md` and `D17.md`, which hold the set's sole relationship: D18 `companion` → D17. |
| Q5 — negative control | Chat returned HTTP 500 without an answer. Search returned five unrelated decision passages; none contains the absent front-door fact. |

## Diagnostic closure

These annotations locate the observed signal; they do not prescribe work beyond this slice.

| Memo diagnostic | Stages that clear or implicate it |
|---|---|
| **Decision representation** | **Stage C clears structural validity and closed-set completeness:** all 17 objects conform, with one valid D18 → D17 relation. **Stages C/H implicate evaluation coverage:** the snapshot contains no supersession claim, so Q3 has no represented fact to retrieve. |
| **Corpus construction** | **Stages D–F clear reproducibility and fidelity:** the deterministic 18-file rebuild is byte-identical through staging and exactly that file set was ingested. **Stage H observes** `index.md` competing for several top-five positions, without showing a snapshot defect. |
| **Chunking** | **Stage E clears the transform as a source of re-chunking:** it copied bytes unchanged. **Stage H implicates Khoj-side splitting:** body, YAML frontmatter, and index sections from the same file appear as distinct corpus IDs and can occupy multiple ranks; this evidence does not isolate chunking as the cause of the Q4 file miss. |
| **Metadata** | **Stages D/E clear preservation:** canonical frontmatter and relationship fields survive into the ingest payload and are returned as text. **Stage H leaves structured use unresolved:** every search used `t=all` without field filters, and Q4 did not surface the only `related_decisions` record. |
| **Retrieval** | **Stage G clears corpus presence and quote fidelity; Stage H clears factual/rationale lookup:** D18 was retrieved verbatim by the probe and D09 ranked first for Q1/Q2. **Stage H implicates conditioned ranking:** Q4 missed the present D18/D17 relationship, while Q3 and Q5 still returned five passages despite lacking supporting facts. |
| **Query formulation** | **Stage H clears predetermination and alignment for Q1/Q2/Q5. Stage H implicates Q3/Q4 formulation:** Q3 asks for an absent supersession, and Q4 is generic—it names neither D18/D17 nor the `companion` relation—so its effect cannot be separated from ranking in this evidence. |
| **Khoj** | **Stages F/G clear the isolated content and search APIs:** clean-user ingest and authenticated search returned HTTP 200. **Stage H implicates answer generation:** chat returned HTTP 500 for Q1/Q2/Q5 because the isolated user lacked a configured LLM; therefore no natural-language answers, decline, or confabulation were observed. Khoj-side chunking/ranking is visible but not causally isolated. |

**Stop:** the complete Part 1 evidence chain is preserved above. Part 1 ends here regardless of answer quality.
