#!/usr/bin/env bash
set -e
trap 'kill 0' EXIT
echo "🐍 Starting FastAPI on http://localhost:8000"
GEMINI_API_KEY="${GEMINI_API_KEY}" venv/bin/uvicorn api.main:app --reload --port 8000 &
echo "⚛️  Starting React dev server on http://localhost:3000"
cd context-refinery && VITE_API_URL="http://localhost:8000" npm run dev &
wait