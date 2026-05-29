#!/usr/bin/env python3
"""
run_comparative_benchmark.py
Dialed-in benchmarking script comparing:
1. MyAPI Smart Retrieval Pipeline (Custom retrieval, classifier, metadata-weighted reranker)
2. Vertex AI Search RAG (Enterprise Generative AI Grounding engine over clean txt store)

Outputs a comprehensive, beautiful markdown evaluation report in the brain directory.
"""

import os
import ssl
import sys
import json
import time
import urllib.request
import urllib.error
import subprocess
from pathlib import Path

import certifi
SSL_CTX = ssl.create_default_context(cafile=certifi.where())

# Configuration
PROJECT_ID = "sb-genai-2026"
MYAPI_BASE_URL = "http://100.85.100.52:8000"
BRAIN_DIR = Path("/Users/saboor/.gemini/antigravity/brain/70616246-4bf1-4f9f-b4aa-18d17be8ff18")
REPORT_PATH = BRAIN_DIR / "comparative_retrieval_benchmark.md"

# 10 Representative Diagnostic Queries
BENCHMARK_QUERIES = [
    "What is graph-driven development, and what problem is GDDP trying to solve?",
    "How many vault schemas have I gone through, and what changed between them?",
    "What have I been working on recently?",
    "What was I doing around the time I was debugging Tailscale?",
    "What keeps showing up as friction in my Neovim workflow?",
    "Find the Claude Code session where I set up the web adapter.",
    "What was I learning about retrieval systems?",
    "What did I decide about the vault schema?",
    "Which notes discuss tagging strategy and taxonomy?",
    "What notes mention Khoj deployment or indexing?"
]

def get_access_token():
    try:
        result = subprocess.run(
            ["gcloud", "auth", "print-access-token", "--account=sbkchaudry@gmail.com"],
            capture_output=True, text=True, check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"❌ Error getting gcloud access token: {e.stderr}", file=sys.stderr)
        print("Please run: gcloud auth login sbkchaudry@gmail.com", file=sys.stderr)
        sys.exit(1)

def query_myapi(query: str) -> dict:
    url = f"{MYAPI_BASE_URL.rstrip('/')}/query"
    body = json.dumps({"q": query, "n": 5}).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.URLError as e:
        return {"error": f"Connection failed: {e.reason}"}
    except Exception as e:
        return {"error": str(e)}

def query_vertex(query: str, token: str) -> dict:
    url = f"https://discoveryengine.googleapis.com/v1/projects/{PROJECT_ID}/locations/global/collections/default_collection/engines/benchmark-search/servingConfigs/default_search:answer"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "x-goog-user-project": PROJECT_ID
    }
    data = {
        "query": {"text": query}
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(data).encode("utf-8"),
        headers=headers,
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=30, context=SSL_CTX) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.URLError as e:
        if isinstance(e, urllib.error.HTTPError):
            try:
                error_body = e.read().decode("utf-8")
                return {"error": f"HTTP {e.code}: {error_body}"}
            except:
                pass
        return {"error": f"Connection failed: {e.reason}"}
    except Exception as e:
        return {"error": str(e)}

def clean_filename(uri_or_path: str) -> str:
    if not uri_or_path:
        return "Unknown"
    return uri_or_path.split("/")[-1]

def main():
    print("🚀 INITIALIZING COMPARATIVE RETRIEVAL BENCHMARK")
    print(f"MyAPI Server: {MYAPI_BASE_URL}")
    print(f"Vertex Search Engine: benchmark-search")
    print("=" * 60)
    
    token = get_access_token()
    print("✅ Authenticated with Vertex AI via active gcloud account.")
    
    results_report = []
    
    timestamp = time.strftime('%Y-%m-%dT%H:%M:%S%z')
    
    # Start compiling report markdown
    results_report.append(f"# Comparative RAG & Retrieval Benchmark")
    results_report.append(f"\nRun timestamp: `{timestamp}`")
    results_report.append("\nThis diagnostic benchmark compares the custom, deterministic **MyAPI Retrieval Pipeline** running on your remote VM against Google's **Vertex AI Enterprise Grounded Search Engine (Generative RAG)** using the synced Obsidian text corpus. It shows you side-by-side exactly how each system handles your personal developer notes.")
    
    results_report.append("\n## 📊 Summary Metrics")
    results_report.append("| Query # | Diagnostic Focus | MyAPI Result Status | Vertex AI Answer Status |")
    results_report.append("|---|---|---|---|")
    
    # Diagnostic classification map for readability
    diagnostic_types = {
        0: "Architecture & Philosophy (factual)",
        1: "System Evolution (synthesis)",
        2: "Temporal / Activity Log (recent)",
        3: "Temporal Context Sync (complex)",
        4: "Tool Friction & Pain points (topic)",
        5: "Session Logs Location (lookup)",
        6: "Topic Exploration (learning)",
        7: "Design Decisions (factual)",
        8: "Information Taxonomy (organization)",
        9: "Infrastructure & Setup (deployment)"
    }
    
    query_details = []
    
    for idx, query in enumerate(BENCHMARK_QUERIES):
        print(f"\n[{idx+1}/{len(BENCHMARK_QUERIES)}] Querying: '{query}'")
        diag_type = diagnostic_types.get(idx, "General Inquiry")
        
        # 1. Query MyAPI
        print(" -> Fetching MyAPI...")
        myapi_res = query_myapi(query)
        myapi_status = "🟢 SUCCESS" if "error" not in myapi_res else "🔴 ERROR"
        
        # 2. Query Vertex AI Search
        print(" -> Fetching Vertex AI Search...")
        vertex_res = query_vertex(query, token)
        vertex_status = "🟢 SUCCESS" if "error" not in vertex_res else "🔴 ERROR"
        
        # Add to summary table
        results_report.append(f"| {idx+1} | {diag_type} | {myapi_status} | {vertex_status} |")
        
        # Build query detail block
        detail = []
        detail.append(f"\n---")
        detail.append(f"\n### 🔍 Query {idx+1}: \"{query}\"")
        detail.append(f"**Diagnostic Focus**: {diag_type}\n")
        
        # Left-Right split styling or sequential blocks (sequential is cleaner in GFM)
        # SECTION A: MYAPI
        detail.append("#### 🛠️ MyAPI Retrieval Pipeline (Remote VM)")
        if "error" in myapi_res:
            detail.append(f"> [!CAUTION]")
            detail.append(f"> **Error**: {myapi_res['error']}")
        else:
            classification = myapi_res.get("classification", {})
            intent = classification.get("intent", "N/A")
            mode = classification.get("answer_mode", "N/A")
            detail.append(f"- **Classified Intent**: `{intent}` (Mode: `{mode}`)")
            detail.append("- **Top Scored Candidate Files (Reranked)**:")
            
            candidates = myapi_res.get("results", [])
            if not candidates:
                detail.append("  *No documents retrieved.*")
            else:
                for rank, cand in enumerate(candidates[:5], 1):
                    source = cand.get("source", "unknown")
                    file_name = clean_filename(cand.get("file", cand.get("title", "")))
                    score = cand.get("final_score", 0.0)
                    detail.append(f"  {rank}. `[{score:.4f}]` **{file_name}** (Source: `{source}`)")
        
        detail.append("")
        
        # SECTION B: VERTEX AI
        detail.append("#### ⚡ Google Vertex AI Search (Generative RAG)")
        if "error" in vertex_res:
            detail.append(f"> [!CAUTION]")
            detail.append(f"> **Error**: {vertex_res['error']}")
        else:
            answer = vertex_res.get("answer", {})
            answer_text = answer.get("answerText", "No answer text generated.")
            
            detail.append(f"> [!NOTE]")
            detail.append(f"> **Grounded Synthesis**:")
            # Indent the LLM answer
            formatted_answer = "\n> ".join(answer_text.strip().split("\n"))
            detail.append(f"> {formatted_answer}")
            detail.append("")
            detail.append("- **Citations used for grounding**:")
            
            steps = answer.get("steps", [])
            seen_citations = set()
            citation_count = 0
            for step in steps:
                actions = step.get("actions", [])
                for action in actions:
                    results = action.get("observation", {}).get("searchResults", [])
                    for r in results:
                        uri = r.get("uri", "")
                        title = r.get("title", "")
                        if uri and uri not in seen_citations:
                            seen_citations.add(uri)
                            citation_count += 1
                            filename = clean_filename(uri)
                            detail.append(f"  - **{title}** (`{filename}`)")
            if citation_count == 0:
                detail.append("  *No citations returned.*")
                
        detail.append("")
        query_details.extend(detail)
        
    # Combine everything and save
    results_report.extend(query_details)
    
    # Save report
    os.makedirs(BRAIN_DIR, exist_ok=True)
    REPORT_PATH.write_text("\n".join(results_report) + "\n", encoding="utf-8")
    
    print("\n" + "=" * 60)
    print(f"🎉 COMPARATIVE BENCHMARK RUN COMPLETED!")
    print(f"Saved highly aesthetic report to: {REPORT_PATH}")
    print("=" * 60)

if __name__ == "__main__":
    main()
