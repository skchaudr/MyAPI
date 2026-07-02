# MyMCP Foundation

This package is the first MyMCP foundation for MyAPI-rebuild.

It intentionally exposes only two callable Python functions:
`get_project_context(project: str)` and `get_person_context(subject: str = "Sab")`.
Both are fixture-backed from `evals/golden_briefs` until the reader and MCP server
wrapper are ready.

## Cost Posture

MyMCP is a small doorway into MyAPI, not the retrieval engine itself. MCP tool
schemas have standing prompt cost, so the public surface stays at two tools and
fine-grained behavior travels through compact arguments:

```json
{
  "intent": "next_action",
  "budget": "tiny",
  "max_tokens": 1200,
  "include_evidence": false
}
```

MyAPI owns corpus refresh, source manifests, retrieval, cached briefs, and evidence
policy. MyMCP returns the smallest useful `ContextBrief` envelope: answer,
evidence paths, freshness, visible budget metadata, and an explicit expansion path
when deeper evidence is needed.
