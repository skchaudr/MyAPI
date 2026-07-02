# MyMCP Foundation

This package is the first MyMCP foundation for MyAPI-rebuild.

It intentionally exposes only two callable Python functions for now:
`get_project_context(project: str)` and `get_person_context(subject: str = "Sab")`.
Both are fixture-backed from `evals/golden_briefs` until the reader and MCP server
wrapper are ready.
