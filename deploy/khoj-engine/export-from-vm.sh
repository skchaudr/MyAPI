#!/usr/bin/env bash
# Run in VM shell: package notes (+ optional pg dump) for Mini rsync.
# Does NOT start anything on the Mini. Safe dry-run with EXPORT_DRY_RUN=1.
set -euo pipefail

STAMP="${STAMP:-$(date -u +%Y%m%dT%H%M%SZ)}"
OUT_ROOT="${OUT_ROOT:-/home/sab-mini/exports/khoj-engine-$STAMP}"
NOTES_SRC="${NOTES_SRC:-/home/sab-mini/khoj-data/notes}"
HOT_SRC="${HOT_SRC:-/data/corpus-hot}"
INCLUDE_PG_DUMP="${INCLUDE_PG_DUMP:-0}"
DRY="${EXPORT_DRY_RUN:-0}"

echo "export root: $OUT_ROOT"
echo "notes: $NOTES_SRC"
echo "hot:   $HOT_SRC"
echo "pg dump: $INCLUDE_PG_DUMP  dry: $DRY"

if [[ "$DRY" == "1" ]]; then
  du -sh "$NOTES_SRC" "$HOT_SRC" 2>/dev/null || true
  echo "DRY RUN — no files written"
  exit 0
fi

mkdir -p "$OUT_ROOT/notes" "$OUT_ROOT/corpus-hot" "$OUT_ROOT/meta"

rsync -a --info=stats2 "$NOTES_SRC/" "$OUT_ROOT/notes/"
rsync -a --info=stats2 "$HOT_SRC/" "$OUT_ROOT/corpus-hot/" 2>/dev/null || true

# Manifest for the Mini operator
{
  echo "stamp=$STAMP"
  echo "host=$(hostname)"
  echo "notes_src=$NOTES_SRC"
  echo "notes_count=$(find "$OUT_ROOT/notes" -type f | wc -l)"
  echo "khoj_version=1.42.10 (bare-metal source)"
  echo "tailscale=$(tailscale ip -4 2>/dev/null || true)"
  date -u +%Y-%m-%dT%H:%M:%SZ
} | tee "$OUT_ROOT/meta/MANIFEST.txt"

if [[ "$INCLUDE_PG_DUMP" == "1" ]]; then
  # Requires /etc/khoj.env on VM
  # shellcheck disable=SC1091
  set -a
  # shellcheck source=/dev/null
  source <(sudo grep -E '^(POSTGRES_HOST|POSTGRES_PORT|POSTGRES_NAME|POSTGRES_USER|POSTGRES_PASSWORD)=' /etc/khoj.env | sed 's/^/export /')
  set +a
  export PGPASSWORD="$POSTGRES_PASSWORD"
  DUMP="$OUT_ROOT/meta/khoj.pg.dump"
  echo "dumping postgres → $DUMP"
  pg_dump -h "$POSTGRES_HOST" -p "$POSTGRES_PORT" -U "$POSTGRES_USER" -d "$POSTGRES_NAME" -Fc -f "$DUMP"
  ls -lh "$DUMP"
fi

cat <<EOF

Next (Run on Mac Mini — after Tailscale SSH works):

  rsync -avz --progress sab-mini@khoj-38:$OUT_ROOT/notes/ ~/khoj-data/notes/
  rsync -avz --progress sab-mini@khoj-38:$OUT_ROOT/corpus-hot/ ~/corpus-hot/

  cd ~/src/MyAPI/deploy/khoj-engine   # or wherever you cloned
  cp .env.example .env               # edit passwords + KHOJ_NOTES_HOST_PATH
  mkdir -p models
  docker compose up -d
  curl -sS http://127.0.0.1:42110/api/health

EOF
