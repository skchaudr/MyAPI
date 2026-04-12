#!/bin/bash

# ==========================================
# Delivery Bridge: Mac to Khoj (Tailscale)
# ==========================================

# 1. Fill these in with your details:
REMOTE_USER="sbkchaudry_gmail_com"  # GCP OS Login username
TAILSCALE_IP="100.107.147.16" # GCP VM: khoj-headless-engine
DEST_DIR="~/khoj-data/notes/"
KHOJ_PORT="42110"
MANIFEST_FILE=".indexed_manifest"

echo "=========================================="
echo "    Context Refinery -> Khoj Delivery     "
echo "=========================================="

if [ -z "$REMOTE_USER" ] || [ -z "$TAILSCALE_IP" ]; then
  echo "❌ Error: Please edit deploy_to_brain.sh and set your REMOTE_USER and TAILSCALE_IP."
  exit 1
fi

# 2. Prompt for the source directory (where you unzipped the bundle)
echo -n "Enter the path to your extracted khoj bundle (e.g., ~/Downloads/khoj-ready-bundle): "
read LOCAL_DIR

# Expand tilde just in case they use ~/
eval LOCAL_DIR="$LOCAL_DIR"

if [ -z "$LOCAL_DIR" ] || [ ! -d "$LOCAL_DIR" ]; then
  echo "❌ Error: Directory not found ($LOCAL_DIR)."
  exit 1
fi

# 3. Execute Rsync
echo ""
echo "🧠 Neural link established... Syncing to Khoj!"
echo "Target: ${TAILSCALE_IP}:${DEST_DIR}"
echo "------------------------------------------"

# -a: archive mode (preserves permissions, times, etc)
# -v: verbose
# -z: compress during transfer
# --ignore-existing: skip files that already exist on the receiver
rsync -avz --ignore-existing "${LOCAL_DIR}/" "${REMOTE_USER}@${TAILSCALE_IP}:${DEST_DIR}"

echo "------------------------------------------"
echo "✅ Sync complete!"
echo ""

# 4. Incremental Khoj indexing — only PUT new or changed files
echo "📡 Checking for new/changed files to index..."
KHOJ_URL="http://${TAILSCALE_IP}:${KHOJ_PORT}/api/content?client=api"
INDEX_FAIL=0
INDEXED=0
SKIPPED=0

# Load existing manifest or start fresh
touch "$MANIFEST_FILE"

for f in "${LOCAL_DIR}"/*.md; do
  FILENAME=$(basename "$f")
  FILE_HASH=$(md5 -q "$f")
  PREV_HASH=$(grep "^${FILENAME}:" "$MANIFEST_FILE" | cut -d: -f2)

  if [ "$FILE_HASH" = "$PREV_HASH" ]; then
    SKIPPED=$((SKIPPED + 1))
    continue
  fi

  RESPONSE=$(curl -s -o /dev/null -w "%{http_code}" -X PUT "$KHOJ_URL" -F "files=@$f")
  if [ "$RESPONSE" = "200" ]; then
    echo "  ✓ Indexed: $FILENAME"
    # Update manifest with new hash
    grep -v "^${FILENAME}:" "$MANIFEST_FILE" > "${MANIFEST_FILE}.tmp" 2>/dev/null || true
    echo "${FILENAME}:${FILE_HASH}" >> "${MANIFEST_FILE}.tmp"
    mv "${MANIFEST_FILE}.tmp" "$MANIFEST_FILE"
    INDEXED=$((INDEXED + 1))
  else
    echo "  ✗ Failed ($RESPONSE): $FILENAME"
    INDEX_FAIL=1
  fi
done

echo "------------------------------------------"
echo "  New/updated: $INDEXED | Unchanged (skipped): $SKIPPED"
if [ "$INDEX_FAIL" = "0" ]; then
  echo "🧠 All files synced and indexed. Khoj is ready to search."
else
  echo "⚠️  Sync complete but some files failed to index. Check Khoj logs."
fi
