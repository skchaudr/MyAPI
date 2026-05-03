#!/usr/bin/env python3
"""Acceptance test for MyAPI retrieval trust calibration.

Hits the Context Refinery /query endpoint with the 6-query acceptance set
from project-docs/retrieval-benchmark-v0/Query/query-bank-trust-categorized-v1.md
(post-2026-04-27 audit table) and asserts gold docs appear in top-K.

One number out. No CLI flags. Edit the QUERIES list below when criteria change.
"""

import json
import sys
import urllib.error
import urllib.request

BASE_URL = "http://100.85.100.52:8000"
TIMEOUT = 30

# Each entry: id, query, and a pass criterion.
# Criterion shapes:
#   {"kind": "file_in_top_k", "files": [...], "k": int}
#       → pass if any listed filename appears in results[:k] by `file`
#   {"kind": "source_in_top_k", "sources": [...], "k": int}
#       → pass if any result in results[:k] has `source` in the list
#   {"kind": "skip", "reason": "..."}
#       → not asserted; prints top result for human review, doesn't count toward score
QUERIES = [
    {
        "id": "A1",
        "query": "What is MyAPI and what is its current goal?",
        "criterion": {
            "kind": "file_in_top_k",
            "files": [
                "obsidian-myapi-anchor.md",
                "my-devinfra-system-anchor.md",
            ],
            "k": 1,
        },
    },
    {
        "id": "A3",
        "query": "What is the status of the API deployment?",
        "criterion": {
            "kind": "file_in_top_k",
            "files": [
                "khoj-deployment-indexing-anchor.md",
                "vm-tailscale-ssh-access-anchor.md",
            ],
            "k": 1,
        },
    },
    {
        "id": "H4",
        "query": "Find notes about the gold-mine Q1 fix",
        "criterion": {
            "kind": "file_in_top_k",
            "files": ["My-API-Trust-Threshold-Plan.md"],
            "k": 1,
        },
    },
    {
        "id": "F5",
        "query": 'Find the note where I used the term "gold mine"',
        "criterion": {
            "kind": "file_in_top_k",
            "files": ["My-API-Trust-Threshold-Plan.md"],
            "k": 5,
        },
    },
    {
        "id": "H1",
        "query": "Find the thread where I set up the Khoj VM migration",
        "criterion": {
            "kind": "source_in_top_k",
            "sources": ["codex", "claude-code"],
            "k": 5,
        },
    },
    {
        "id": "A7",
        "query": "What's broken or blocked in MyAPI right now?",
        "criterion": {
            "kind": "skip",
            "reason": "myapi-status-anchor.md not built yet — A7 fails by design",
        },
    },
]


def post_query(query: str, n: int = 10) -> dict:
    body = json.dumps({"q": query, "n": n}).encode("utf-8")
    req = urllib.request.Request(
        f"{BASE_URL}/query",
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return json.loads(resp.read().decode("utf-8"))


def evaluate(criterion: dict, results: list[dict]) -> tuple[str, str]:
    """Return (verdict, evidence_string). verdict ∈ {PASS, FAIL, SKIP}."""
    kind = criterion["kind"]

    if kind == "skip":
        top = results[0] if results else None
        evidence = (
            f"top: {top.get('file')} (fs={top.get('final_score', 0):.3f})"
            if top
            else "no results"
        )
        return "SKIP", f"{criterion['reason']} | {evidence}"

    k = criterion["k"]
    top_k = results[:k]

    if kind == "file_in_top_k":
        wanted = set(criterion["files"])
        for i, r in enumerate(top_k, 1):
            if r.get("file") in wanted:
                return "PASS", f"{r['file']} @ #{i}, fs={r.get('final_score', 0):.3f}"
        top = top_k[0] if top_k else None
        if top:
            return (
                "FAIL",
                f"wanted {sorted(wanted)} in top-{k}; got #1 {top.get('file')} "
                f"(fs={top.get('final_score', 0):.3f})",
            )
        return "FAIL", f"wanted {sorted(wanted)} in top-{k}; no results returned"

    if kind == "source_in_top_k":
        wanted = set(criterion["sources"])
        for i, r in enumerate(top_k, 1):
            if r.get("source") in wanted:
                return (
                    "PASS",
                    f"source={r['source']} @ #{i} ({r.get('file')}, "
                    f"fs={r.get('final_score', 0):.3f})",
                )
        sources_seen = [r.get("source") for r in top_k]
        return "FAIL", f"wanted source in {sorted(wanted)} in top-{k}; saw {sources_seen}"

    return "FAIL", f"unknown criterion kind: {kind}"


def main() -> int:
    print(f"MyAPI acceptance set → {BASE_URL}\n")

    passed = 0
    failed = 0
    skipped = 0

    for q in QUERIES:
        try:
            response = post_query(q["query"], n=10)
        except urllib.error.URLError as e:
            print(f"{q['id']}: ERROR  ({type(e).__name__}: {e})")
            failed += 1
            continue
        except (TimeoutError, json.JSONDecodeError) as e:
            print(f"{q['id']}: ERROR  ({type(e).__name__}: {e})")
            failed += 1
            continue

        results = response.get("results", [])
        verdict, evidence = evaluate(q["criterion"], results)
        print(f"{q['id']}: {verdict}  ({evidence})")

        if verdict == "PASS":
            passed += 1
        elif verdict == "SKIP":
            skipped += 1
        else:
            failed += 1

    total_asserted = passed + failed
    print(f"\nScore: {passed}/{total_asserted} mechanical · {skipped} skipped")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
