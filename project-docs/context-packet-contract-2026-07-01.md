# Context Packet Contract - 2026-07-01

Lane B adds a small Python contract in `context_refinery/context_packets.py`.
It is deliberately just dataclasses and helpers, not a framework.

## Shared Unit

`ContextPacketItem` mirrors `context-packs-cli` JSON bundle items:
`path`, `depth`, `mtime`, `chars`, `content`, and `approx_tokens`.

`ContextPacket` groups those items, keeps totals, and exposes evidence paths.
The adapter accepts ctxpack JSON-style payloads without importing ctxpack.

`ContextBrief` wraps the packet into the MyAPI output shape: machine-readable
metadata plus human-readable Markdown. The envelope validates that a brief has a
short answer, evidence, open risks, and at least one evidence path.

## Why It Bridges The Three Surfaces

- MyAPI can use it as the reusable foundation for golden briefs and future MCP
  returns.
- aa-cli can treat the rendered Markdown as a human-checkable packet envelope.
- GDDP can reuse the same bounded evidence mindset without depending on MyAPI,
  Obsidian, or MCP internals.

The contract stays small so MyMCP can import it directly later.
