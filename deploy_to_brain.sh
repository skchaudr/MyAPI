#!/bin/bash

# ==========================================
# Delivery Bridge: Mac to Khoj (Tailscale)
# ==========================================

# 1. Fill these in with your details:
REMOTE_USER=""      # e.g., "saboor"
TAILSCALE_IP=""     # e.g., "100.x.y.z"
DEST_DIR="~/khoj-data/notes/"

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
LOCAL_DIR="${LOCAL_DIR/#\~/$HOME}"

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
echo "✅ Sync complete! Khoj will automatically ingest the new files."
