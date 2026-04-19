#!/usr/bin/env python3
"""Run the retrieval benchmark against the Context Refinery /query endpoint."""

import json
import time
import urllib.error
import urllib.request
from pathlib import Path


QUERIES = [
    "What is My_DevInfra?",
    "What have I been working on recently?",
    "What was I doing around the time I was debugging Tailscale?",
    "What keeps showing up as friction in my Neovim workflow?",
    "Find the Claude Code session where I set up the web adapter.",
    "Find the ChatGPT export note about iTerm2 and shell setup.",
    "What was I learning about retrieval systems?",
    "What did I decide about the vault schema?",
    "Which notes discuss tagging strategy and taxonomy?",
    "What notes mention Khoj deployment or indexing?",
    "What notes are about Claude, Codex, and Jules working together?",
    "What is the status of the API deployment?",
    "Show me notes about my Obsidian folder schema.",
    "What did I write about semantically related notes and clean-up passes?",
    "What are the strongest notes for a retrieval benchmark?",
    "What notes are tied to Tailscale, SSH, or VM access?",
    "Which notes are about prompts, schemas, or evaluation rubrics?",
    "What docs should I use to understand the current system end to end?",
]


def post_query(base_url: str, query: str, n: int) -> dict:
    body = json.dumps({"q": query, "n": n}).encode("utf-8")
    request = urllib.request.Request(
        f"{base_url.rstrip('/')}/query",
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=60) as response:
        return json.loads(response.read().decode("utf-8"))


def result_summary(result: dict) -> tuple[str, str, int, int]:
    docs = result.get("results", [])
    classification = result.get("classification", {})
    intent = classification.get("intent", "unknown")
    total = result.get("total_after_filter", len(docs))
    from_khoj = result.get("total_from_khoj", 0)
    top = []
    for doc in docs[:5]:
        source = doc.get("source") or "unknown"
        file_name = doc.get("file") or doc.get("title") or "unknown"
        top.append(f"{source}:{file_name}")
    return intent, "<br>".join(top), total, from_khoj


def main() -> int:
    base_url = "http://localhost:8000"
    out = Path("/tmp/retrieval-benchmark-new-vm.md")
    lines = [
        "# Retrieval Benchmark - New VM Baseline",
        "",
        f"Run timestamp: `{time.strftime('%Y-%m-%dT%H:%M:%S%z')}`",
        "",
        "| # | Query | Intent | After filter | From Khoj | Top results |",
        "|---|---|---|---:|---:|---|",
    ]

    failures = 0
    for index, query in enumerate(QUERIES, 1):
        try:
            result = post_query(base_url, query, 10)
            intent, top, total, from_khoj = result_summary(result)
            print(f"{index:02d} OK {intent} total={total} khoj={from_khoj}", flush=True)
            safe_query = query.replace("|", "\\|")
            safe_top = top.replace("|", "\\|")
            lines.append(f"| {index} | {safe_query} | {intent} | {total} | {from_khoj} | {safe_top} |")
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
            failures += 1
            print(f"{index:02d} FAIL {type(exc).__name__}: {exc}", flush=True)
            safe_query = query.replace("|", "\\|")
            lines.append(f"| {index} | {safe_query} | ERROR | 0 | 0 | `{type(exc).__name__}: {exc}` |")

    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"WROTE {out}", flush=True)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
