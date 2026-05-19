# Handoff 007: Vertex AI Infrastructure & OCR Pipeline Established

## Objective Completed
We successfully established a Google-managed RAG system to serve as a reference implementation against the custom `MyAPI` retrieval pipeline, heavily utilizing the $1,000 Vertex AI Agent Builder credits.

## Infrastructure Built (GCP Project: `sb-genai-2026`)

### 1. Data Ingestion
- **GCS Bucket:** `gs://sb-myapi-corpus`
- **Obsidian Sync:** Uploaded all 4 vaults (SoloDeveloper, Coding-Tech, Personal, workout-tracker) preserving directory structures. Total of 30.3k objects (1.1 GiB).
- **Export Normalization:** A secondary agent ran `ingest_all.py` to normalize ChatGPT, Claude, and Codex exports into `corpus_v1/normalized/` and uploaded them to `gs://sb-myapi-corpus/exports/`.

### 2. Vertex AI Data Stores & Engines
*Note: We bypassed the need to use the Google Cloud Browser UI by leveraging the Discovery Engine REST API to build everything programmatically.*

- **Data Store 1 (Benchmark):** `myapi-benchmark` (pointed strictly at `gs://sb-myapi-corpus/obsidian/SoloDeveloper/**`)
  - **Engine:** `benchmark-search` (Search App for 1:1 MyAPI comparisons)
- **Data Store 2 (Full Corpus Search):** `all-notes`
  - **Engine:** `notes-search` (Enterprise Search App over all vaults)
- **Data Store 3 (Full Corpus Chat):** `all-notes-chat` *(Chat apps require dedicated data stores)*
  - **Engine:** `notes-chatbot` ("Ask My Notes" conversational agent)

### 3. Document Processing Pipeline (OCR)
- Created a permanent **Document AI OCR Processor** (`6e8cfb681fa4264f`).
- Built a permanent adapter script for MyAPI: `context_refinery/adapters/pdf_extractor.py`.
- **Capability:** Converts any PDF (including scanned documents) into high-quality, normalized Markdown for ingestion into `MyAPI`'s local corpus using `google-cloud-documentai-toolbox`.
- Successfully field-tested on `Seed-Tracer-Public-Address-to-Wallets.pdf`.

## Pending / Next Steps

1. **Wait for Initial Sync:** The Vertex AI data stores are currently processing the initial 30k+ object import. This happens server-side and takes ~15-30 minutes.
2. **Import Exports:** Once the initial sync finishes, run an incremental import on the data stores to ingest the normalized chat exports:
   ```bash
   TOKEN=$(gcloud auth print-access-token)
   curl -s -X POST "https://discoveryengine.googleapis.com/v1/projects/sb-genai-2026/locations/global/collections/default_collection/dataStores/all-notes-chat/branches/default_branch/documents:import" \
     -H "Authorization: Bearer $TOKEN" \
     -H "Content-Type: application/json" \
     -H "x-goog-user-project: sb-genai-2026" \
     -d '{"gcsSource": {"inputUris": ["gs://sb-myapi-corpus/exports/**"], "dataSchema": "content"}, "reconciliationMode": "INCREMENTAL"}'
   ```
3. **Verify Billing:** Check the GCP Billing Console tomorrow to ensure the operations successfully hit the $1,000 promotional credit bucket.
4. **Test & Compare:** Open the [Gen App Builder Console](https://console.cloud.google.com/gen-app-builder) to test the Search and Chat interfaces against the `retrieval-benchmark-v0` queries.
