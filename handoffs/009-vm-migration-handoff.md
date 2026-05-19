# Handoff 009: Migrate MyAPI + Vertex AI Workspace to khoj-vm-new

## Context
All Vertex AI Agent Builder infrastructure was built from Mac. The VM needs to be set up as the primary workspace so Mac isn't bottlenecked. The VM has a 3-hour auto-shutdown policy — be efficient.

## VM Connection
- **Host:** `khoj-vm-new` (SSH alias)
- **Tailnet IP:** `100.85.100.52`
- **User:** `saboor`
- **Key:** `~/.ssh/google_compute_engine`
- **VM must be started first** from GCP Console (project: check `sb.info.you@gmail.com` account)

## Step 1: Clone & Setup MyAPI (~5 min)
```bash
# Clone the repo
git clone git@github.com:skchaudr/MyAPI.git ~/repos/MyAPI
cd ~/repos/MyAPI
git checkout feat/corpus-v1-normalization

# Create venv and install deps
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install google-cloud-documentai google-cloud-documentai-toolbox
```

## Step 2: Auth gcloud for Vertex AI (~2 min)
The Vertex AI resources (data stores, engines) live in project `sb-genai-2026` under `sbkchaudry@gmail.com`.
```bash
gcloud auth login sbkchaudry@gmail.com
gcloud config set project sb-genai-2026
gcloud auth application-default login
```

## Step 3: Verify Data Store Imports Completed (~2 min)
```bash
TOKEN=$(gcloud auth print-access-token)

# Check benchmark data store
curl -s "https://discoveryengine.googleapis.com/v1/projects/sb-genai-2026/locations/global/collections/default_collection/dataStores/myapi-benchmark/branches/default_branch/operations" \
  -H "Authorization: Bearer $TOKEN" \
  -H "x-goog-user-project: sb-genai-2026" | python3 -m json.tool

# Check all-notes data store
curl -s "https://discoveryengine.googleapis.com/v1/projects/sb-genai-2026/locations/global/collections/default_collection/dataStores/all-notes/branches/default_branch/operations" \
  -H "Authorization: Bearer $TOKEN" \
  -H "x-goog-user-project: sb-genai-2026" | python3 -m json.tool
```

## Step 4: Import Normalized Exports (if initial import is done) (~1 min to trigger)
The other agent uploaded 4,100 normalized ChatGPT/Claude/Codex exports to `gs://sb-myapi-corpus/exports/`.
Run incremental imports on all 3 data stores:
```bash
TOKEN=$(gcloud auth print-access-token)
for STORE in myapi-benchmark all-notes all-notes-chat; do
  echo "Importing exports into $STORE..."
  curl -s -X POST \
    "https://discoveryengine.googleapis.com/v1/projects/sb-genai-2026/locations/global/collections/default_collection/dataStores/$STORE/branches/default_branch/documents:import" \
    -H "Authorization: Bearer $TOKEN" \
    -H "Content-Type: application/json" \
    -H "x-goog-user-project: sb-genai-2026" \
    -d '{"gcsSource": {"inputUris": ["gs://sb-myapi-corpus/exports/**"], "dataSchema": "content"}, "reconciliationMode": "INCREMENTAL"}'
  echo ""
done
```

## Step 5: Test Search Query (~5 min)
```bash
TOKEN=$(gcloud auth print-access-token)

# Test a search query against the benchmark engine (SoloDeveloper only)
curl -s -X POST \
  "https://discoveryengine.googleapis.com/v1/projects/sb-genai-2026/locations/global/collections/default_collection/engines/benchmark-search/servingConfigs/default_search:search" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -H "x-goog-user-project: sb-genai-2026" \
  -d '{"query": "How does the retrieval pipeline work in MyAPI?", "pageSize": 5}' | python3 -m json.tool | head -60
```

## Step 6: Test Chatbot (~5 min)
```bash
TOKEN=$(gcloud auth print-access-token)

# Test chatbot conversation
curl -s -X POST \
  "https://discoveryengine.googleapis.com/v1/projects/sb-genai-2026/locations/global/collections/default_collection/engines/notes-chatbot/servingConfigs/default_search:answer" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -H "x-goog-user-project: sb-genai-2026" \
  -d '{"query": {"text": "What projects am I currently working on?"}}' | python3 -m json.tool | head -80
```

## Step 7: Run MyAPI Benchmark Comparison (~15 min)
Use the benchmark queries from `retrieval-benchmark-v0` to compare Vertex AI Agent Builder results vs MyAPI local retrieval.

## Resource Map

| Resource | Location |
|----------|----------|
| GCP Project | `sb-genai-2026` (sbkchaudry@gmail.com) |
| GCS Bucket | `gs://sb-myapi-corpus` |
| Data Store (benchmark) | `myapi-benchmark` — SoloDeveloper vault only |
| Data Store (search) | `all-notes` — all 4 Obsidian vaults |
| Data Store (chat) | `all-notes-chat` — all 4 vaults |
| Search Engine (benchmark) | `benchmark-search` |
| Search Engine (all) | `notes-search` |
| Chatbot Engine | `notes-chatbot` |
| Document AI Processor | `6e8cfb681fa4264f` (us region) |
| PDF Adapter | `context_refinery/adapters/pdf_extractor.py` |

## Billing Check
After running queries, verify the $1,000 GenAI App Builder credit is being consumed:
- Go to https://console.cloud.google.com/billing (as sbkchaudry@gmail.com)
- Check that the promotional credit balance has decreased
