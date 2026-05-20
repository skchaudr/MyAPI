import sys
import os
sys.path.append(os.getcwd())
from context_refinery.retrieval import ResultReranker, MetadataParser

parser = MetadataParser()
reranker = ResultReranker()

results = [
    {
        "corpus_id": "uuid1",
        "file": "myapi-status-anchor.md",
        "score": 0.1335,
        "title": "myapi-status-anchor.md",
        "snippet": "# MyAPI Status Anchor\n## What This Is\nThis note is the canonical answer to \"what's broken or blocked in MyAPI right now?\".",
        "additional": {"file": "myapi-status-anchor.md"}
    },
    {
        "corpus_id": "uuid2",
        "file": "obsidian-myapi-anchor.md",
        "score": 0.150,
        "title": "primary-project-anchor-template",
        "snippet": "# Objective\n> Create a context retrieval tool that processes and semantically links...",
        "additional": {"file": "obsidian-myapi-anchor.md"}
    }
]

# We need to run the metadata parser first to inject the metadata
for r in results:
    r["score"] = 1.0 - r["score"]
    entry = r.get("snippet", "")
    metadata, _, _ = parser.parse(entry, filename=r.get("additional", {}).get("file"))
    r["metadata"] = metadata

query = "What is MyAPI and what is its current goal?"
reranked = reranker.rerank(results, intent="project_overview", query=query)

for r in reranked:
    print(f"File: {r['file']}")
    print(f"Final Score: {r['final_score']}")
    print(f"Metadata: {r['metadata']}")
