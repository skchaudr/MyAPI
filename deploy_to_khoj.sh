#!/usr/bin/env bash
set -e

EXPORT_DIR="exports/khoj-ready-bundle"
REMOTE_IMPORT_DIR="~/khoj-imports"
ZONE="us-central1-a"
INSTANCE="khoj-headless-engine"
PROJECT="gen-lang-client-0824562549"

echo "🚀 Starting Khoj Delivery Pipeline..."

# 1. Ensure the export bundle exists
if [ -d "$EXPORT_DIR" ] && [ "$(ls -A $EXPORT_DIR)" ]; then
    echo "📦 Found exported datasets in $EXPORT_DIR."
else
    echo "❌ No exported datasets found in $EXPORT_DIR. Did you run the export via Context Refinery?"
    exit 1
fi

# 2. SCP over IAP tunnel
echo "🌐 Syncing files to $INSTANCE via IAP..."
gcloud compute scp --recurse "$EXPORT_DIR/"* "$INSTANCE:$REMOTE_IMPORT_DIR" --zone "$ZONE" --tunnel-through-iap --project "$PROJECT"
echo "✅ Files successfully uploaded to $REMOTE_IMPORT_DIR"

# 3. Trigger remote index (Awaiting User Command injection)
echo "🔄 Connecting to VM to trigger Khoj index cycle..."

# TODO: Inject the exact ingestion trigger based on user's cloud dive
# e.g., gcloud compute ssh --zone "$ZONE" "$INSTANCE" --tunnel-through-iap --project "$PROJECT" --command "source ~/khoj-engine/venv/bin/activate && khoj update"

echo "🎉 Delivery Pipeline Complete!"
