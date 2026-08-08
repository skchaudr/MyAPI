# Wayfinder → GDDP handoff

**Effort:** Semantic Graphify cold-start (MyAPI)  
**Purpose:** How decision work on this map becomes executable graph truth without blurring the two systems.

---

## Roles (do not merge)

| Surface | Repo / path | Owns | Does **not** own |
|---|---|---|---|
| **Wayfinder** | `MyAPI/.scratch/semantic-graphify-cold-start/` | Fog clearing, product cuts, decision tickets, research | Dispatch, status of capabilities, “done” in production |
| **GDDP config** | `gddp-config/graphs/myapi/` (on this host: `/home/sab-mini/gddp-config/graphs/myapi/`) | Human-owned graph truth: nodes, depends_on, acceptance, constraints | Inventing product identity mid-flight |
| **GDDP runtime** | `gddp-runtime` | Dispatch, jobs, results, receipts, review state | Writing completion into the graph |

**Principle:** Wayfinder *reveals and decides*. GDDP *executes and verifies*. Runtime stops at review; humans accept graph updates (receipts → optional `graph-update.yaml` proposals only).

---

## What may become a GDDP node

| Input | Becomes a node? | When |
|---|---|---|
| Open wayfinder **grilling / research** ticket | **No** | Still a question |
| Resolved wayfinder decision (Answer section) | **Not automatically** | Decision is fuel, not a node |
| Capability implied by one or more decisions | **Yes, after human authoring** | When `why` + acceptance + artifacts can be stated |
| Matt-flow implementation ticket (`/to-tickets`) | **Often yes** | If it is a bounded, user-visible, verifiable capability slice |
| Pure chore (“fix typo”, “bump dep”) | **Usually no** | Too small / not a capability; keep off the graph |

**Node size rule** (from GDDP / aa-cli canonical practice): a node is a bounded capability the operator can feel is usable, inspectable, and verifiable — not a random chore and not an unresolved question.

---

## Pipeline

```text
1. Wayfinder session
   - Claim ≤1 HITL ticket (research may parallel)
   - Resolve → ## Answer on ticket + one line on map Decisions so far

2. Map nearly clear (or a coherent decision cluster locked)
   - Optional but clean: /to-spec collapses linked decisions into a build brief
   - List capability slices: each must have acceptance in one focused pass

3. Human (or human-directed scaffold) updates gddp-config
   - Path: graphs/myapi/nodes/<node_id>.yaml
   - Tools: gddp-config scripts/new_node.py + validate.py
   - Patch graphs/myapi/project.yaml node index
   - Prefer PR to gddp-config main (protected); human merges

4. Reconcile existing myapi graph with Decisions so far
   - For each current node: keep | rewrite | defer | split
   - Do not dispatch nodes that contradict locked wayfinder answers

5. gddp-runtime
   - Dispatch ready nodes → executors → receipts
   - Human: accept | retry | block | defer
   - Only then update node status in gddp-config (human)
```

---

## Field mapping (decision → node)

When drafting a node from wayfinder outputs, map fields deliberately:

| GDDP node field | Pull from |
|---|---|
| `title` / `node_id` | Capability name (verb + outcome), not the question title |
| `why` | Destination + resolved decision gist; cite ticket names/paths |
| `depends_on` | Other capabilities (not “blocked by decision ticket N” — those are already closed) |
| `acceptance_criteria` | Measurable “done”; include honest-answer / cold-start bar when relevant |
| `constraints` | Path constraint (reuse machinery), non-goals, trust gates |
| `required_artifacts` | Receipts, manifests, test evidence — never silent success |
| `status` | `pending` / `ready` only after human says the node is graph-true |

**Link back:** In the node `why` or a short comment in the PR, point at:

- map: `.scratch/semantic-graphify-cold-start/map.md`
- tickets: `issues/NN-….md`
- research: `research/….md` when evidence-backed

Do **not** paste full ticket bodies into YAML.

---

## Current myapi graph vs this wayfinder map

Existing nodes under `gddp-config/graphs/myapi/` (as of chart/reconcile era):

| Node | Role | Wayfinder relationship |
|---|---|---|
| `capture-live-vertex-baseline` | Freeze live retrieval baseline | Execution; may stay early if baseline still perishable |
| `assemble-current-personal-corpus` | Active handoff corpus assembly | Heavy; **scope must match** thin-loop decision (04) — may defer or shrink |
| `mine-real-agent-query-benchmark` | Mine real agent questions | Aligns with ticket 02 research; may reuse corpus-hot + wayfinder bank as partial input |
| `prove-myapi-context-retrieval` | Prove retrieval vs baseline | After substrate + question bank |
| `serve-context-via-mcp` | Two MCP tools → ContextBrief | Aligns with north star surface; acceptance must absorb honest-answer + thin-loop decisions |
| `prove-incremental-refresh` | Incremental corpus updates | Likely **after** first cold-start proof |

**Graph authoring rule (updated):** Prefer a **new** `graphs/myapi/` (or clearly versioned graph) authored from wayfinder decisions — simple put of nodes that match the locked thin loop. The prior six-node graph is **reference / loot**, not mandatory scaffold. Optionally archive or leave the old graph; do not dispatch it as approved for this north star until explicitly rewritten.

**After tickets 03 + 04 resolve:** write the new graph’s node list from Decisions so far (keep useful acceptance language from old nodes only when it still fits).
---

## Session hygiene

| Do | Don’t |
|---|---|
| Resolve decisions on the wayfinder map first | Open GDDP jobs for open questions |
| Author nodes only when acceptance is writeable | Auto-generate nodes from open ticket titles |
| One capability node per focused verify pass | Mega-nodes that mix corpus rewrite + MCP + eval |
| Point nodes at MyAPI machinery that exists | Invent greenfield pipelines wayfinder already ruled out |
| Keep runtime receipt-only on return path | Let agents merge graph status |

---

## “Map clear” → GDDP ready checklist

Wayfinder handoff is ready for node authoring when:

- [ ] Destination still accurate in one glance
- [ ] Thinnest v1 loop decided (ticket 04)
- [ ] Honest answer contract decided (ticket 03)
- [ ] Enough of levels / sources / ownership / code-meaning decided that acceptance criteria won’t thrash
- [ ] A short list of 2–5 capability slices exists (spec or bullet list)
- [ ] Reconcile table for existing `graphs/myapi` nodes is written (even if “all defer except X”)

Then: update `gddp-config`, validate, dispatch via runtime.

---

## Pointers

| What | Where |
|---|---|
| This effort’s map | `MyAPI/.scratch/semantic-graphify-cold-start/map.md` |
| Decision tickets | `…/issues/` |
| Research | `…/research/` |
| MyAPI project graph | `/home/sab-mini/gddp-config/graphs/myapi/` |
| Node schema / scaffold | `gddp-config/schemas/`, `scripts/new_node.py`, `templates/` |
| Runtime boundary | `gddp-runtime/README.md` (receipts, no auto graph writeback) |
