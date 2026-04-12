#!/usr/bin/env bash
set -e

EXPORT_DIR="exports/khoj-ready-bundle"
REMOTE_IMPORT_DIR="~/khoj-data/ai-exports"
REMOTE_USER="sbkchaudry_gmail_com"
TAILSCALE_IP="[ENTER_TAILSCALE_IP_HERE]"

echo "🚀 Starting Khoj Delivery Pipeline..."

# 1. Ensure the export bundle exists
if [ -d "$EXPORT_DIR" ] && [ "$(ls -A $EXPORT_DIR)" ]; then
    echo "📦 Found exported datasets in $EXPORT_DIR."
else
    echo "❌ No exported datasets found in $EXPORT_DIR. Did you run the export via Context Refinery?"
    exit 1
fi

# 2. RSYNC over Tailscale
echo "🌐 Differentially syncing files to $TAILSCALE_IP via Tailscale..."
rsync -avz "$EXPORT_DIR/" "$REMOTE_USER@$TAILSCALE_IP:$REMOTE_IMPORT_DIR/"
echo "✅ Files successfully synced to $REMOTE_IMPORT_DIR"

# 3. Native Ingestion Trigger
echo "🔄 Khoj natively watches ~/khoj-data/ai-exports/ via background workers."
echo "If manual ingestion is required, use: curl -X POST http://localhost:42110/api/update"

echo "🎉 Delivery Pipeline Complete!"
