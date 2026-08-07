# Inventory existing machinery and where truth lives

Type: research
Status: resolved

## Question

What already exists (code, plans, MCP, golden briefs, corpus, deploy path) and **on which host/branch** — such that a thin v1 cold-start path can be assembled without rebuilding?

Produce a single inventory: path, host, branch tip, one-line capability, and whether it is live vs planned vs fixture-only. Must cover at least: Context Refinery + `/query`, Khoj deploy, adapters, anchors, retrieval benchmark bank, any `mcp/` package, golden briefs, PROJECT-BRIEF / IMPLEMENTATION-PLAN if present anywhere, corpus-hot packs, graphify-out, durable handoffs.

## Answer

Full findings: [01-inventory-existing-machinery.md](../research/01-inventory-existing-machinery.md)

**Gist:**
- Local clones (saboor/MyAPI, repos/MyAPI, sab-mini/MyAPI) sit on `feat/corpus-v1-normalization` with live **Context Refinery + `/query` + adapters + anchors + benchmark bank + deploy scripts**.
- GitHub **`main` @ `5740b3c`** holds the rebuild surface missing from feat trees: `PROJECT-BRIEF`, `IMPLEMENTATION-PLAN`, `mcp/` (fixture-backed), `evals/golden_briefs/`, `myapi-db-plan`, `gddp/`, `graphify-out`, `.handoffs/`. Local `origin/main` is **stale**.
- Corpus-hot pack lives under `/home/saboor/khoj-data/notes/corpus-hot-v1/myapi/`. Full Corpus v1.0 tree and Mac mini path not present here.
- **Thin-path candidates:** (1) fixture MCP goldens only; (2) live `/query` + anchors; (3) corpus-hot lean index; (4) MCP doorway glued onto `/query`.

## Comments

- Chart session: research subagent completed. Findings: `../research/01-inventory-existing-machinery.md`
