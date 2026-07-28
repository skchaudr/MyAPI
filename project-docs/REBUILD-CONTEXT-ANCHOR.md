# MyAPI-Rebuild — Context Anchor

> **Read this first** in any new agent session before proposing work.
> Agent-agnostic narrative. Stops re-litigating origin, naming, and direction.

**Status:** living anchor from session 2026-06-21  
**Companion doc:** `ARCHITECTURE.md` (GLM plan — implementation shape, not this story)

---

## One sentence

Rebuild MyAPI as a **vault of durable handoffs** — event traces and decisions boxed for agent-agnostic continuity — surfaced as **context briefs** via MCP (`get_project_context`, `get_person_context`). Not v0's "dump exports into one RAG pool."

**Working theme:** *Ascend* — if the product is "capture context in a box and move it across agent sessions," the handoff **is** the tool.

---

## Paradigm shift (where this actually landed)

**Started as:** exported data (friends reclaiming ChatGPT / WhatsApp / LinkedIn dumps via a send-a-link UI).

**Evolved into:** **durable handoffs** — the thing worth preserving is not raw platform bytes but **what happened, what was decided, and what the next agent needs to know** without re-litigating.

| Layer | What it is |
|---|---|
| **Event trace** | Atomic handoff — one episode, evidence-linked, human-legible. |
| **Handoff vault** | Corpus + anchors + traces — continuity across sessions and agents. |
| **Context brief** | Query surface — MCP returns the right handoff bundle for intent. |
| **This file** | Meta-handoff — the paradigm itself, boxed for cold start. |

Exports are **input material** for traces, not the product. CLI sessions, chat logs, and Obsidian anchors are **evidence** behind handoffs. The friend-refinery UI was an early ingestion path; the rebuild is **handoff durability**.

MyAPI `handoffs/000–012` were an early version of this instinct. Rebuild makes it explicit: **normalize to handoff shape, retrieve handoffs, not dumps.**

---

## Day-zero origin (why Context Refinery had a UI)

**Not** because Sab needed buttons. **Because friends needed to reclaim their own data.**

Friends had years of life trapped in platform exports — ChatGPT, WhatsApp, LinkedIn, etc. Providers give zip/json dumps that **most people cannot read, search, or use**. The original product:

> Drop export → ingest → normalize → readable + searchable → you own your data again.

**Graphify / RAG-in-a-box for heterogeneous personal sources.** UI (web app) so Sab could **send friends a link** — not a CLI and a prayer. Friend-accessible reclaim tool.

**LinkedIn export** and **WhatsApp export** in this repo's vocabulary always mean **that origin** — platform dumps friends wanted to own — not "deferred person context" and not generic future MCP corpora.

---

## What diverged (why it got confusing)

Markdown/Obsidian, AI, and agents took off. The project forked:

| Thread | What it became |
|---|---|
| **Friend refinery (day zero)** | Send-a-link UI: ingest → normalize → searchable. React "Refinery Alpha" from AI Studio. |
| **Sab's path** | Obsidian vault, CLI sessions, agent cold-start, corpus v1, benchmarks, MCP briefs. |

**Naming collision:** "Context Refinery" attached to both the archived React UI (`_archive/context-refinery-vite-scaffold/` in old MyAPI repo) and the Python `context_refinery/` package (adapters, triage CLI, FastAPI `/query`). Sab's real toolchain is **CLI + API**, not the button app.

**Do not** describe Context Refinery as "a UI layer for coding agents." That is drift. The UI was the friend product; the Python package is what Sab actually built and runs.

---

## v0 failure (what not to repeat)

v0 put Obsidian + chat exports + CLI sessions into **one retrieval pool** and hoped ranking would sort it out.

- **ChatGPT exports dominated** (volume + conversational shape).
- **CLI sessions were ingested (~579) but never surfaced** as valuable operational traces.
- **No presentable narratives** — raw dumps, not event traces.
- **Obsidian anchors** existed but weren't framed as what retrieval should privilege.

**The fix is shape, not more data:** sanitize → normalize → **presentable narrative with evidence pointers** (event traces), then briefs/MCP — not bigger dumps.

**Tonight (2026-06-21) was the counterexample:** clarity came from tracing an event (GLM → Codex misattribution → second Codex amplification → revert), using pasted chat **and** `~/.codex/sessions/*.jsonl` — not from `/query`.

---

## Rebuild direction (trust `ARCHITECTURE.md`, not Codex voice)

- **Product:** context briefs via MCP (and study/export layer per root `AGENTS.md`).
- **Keep:** `ARCHITECTURE.md` (GLM). **Kill:** `DIRECTION.md`-style synthesis/evaluation docs.
- **Graphify:** current code structure map only — not git history as a graph.
- **Git:** agents use git tools directly; do not ingest commit history into the corpus engine.
- **Anti-patterns:** blocker jargon, courtroom synthesis, "small reader" framing, treating missing code as missing corpus, operator-vs-person hair-splitting.

---

## MCP tools (two, not three names)

| Tool | Question |
|---|---|
| `get_project_context` | What's going on with **this project**? |
| `get_person_context` | Who is **Sab**? |

`get_user_context`, `get_person_context`, and "operator context" are **the same tool**. Pick `get_person_context`. Person/human context matters; don't reduce it to builder-speak.

**Source emphasis:**
- **Project briefs / project traces:** CLI sessions + chat exports + Obsidian anchors (facts, dates).
- **Person brief:** Obsidian-primary (projects, decisions, preferences, portfolio shape) — enough to back a factual narrative.

`ARCHITECTURE.md` §5.3 deferring `get_person_context` for LinkedIn/WhatsApp is **wrong framing**. Person context does not wait on those exports. Those exports belong to the **friend refinery** thread.

---

## Glossary (stop re-deriving)

| Term | Means |
|---|---|
| **LinkedIn / WhatsApp export** | Friend-refinery origin: platform dumps → ingest → normalize → usable. |
| **Context Refinery (UI)** | Day-zero friend web app (archived prototype). |
| **Context Refinery (Python)** | `context_refinery/` — adapters, triage, retrieval API. What Sab runs. |
| **Durable handoff** | Boxed context that survives session boundaries; agent-agnostic. |
| **Event trace** | Handoff unit — when, actors, what happened, decisions, damage, evidence paths, lesson. |
| **Handoff vault** | Where durable handoffs live (corpus + traces + anchors). |
| **Context brief** | MCP answer — the right handoff bundle for a query. |
| **Ascend** | Working theme: session continuity as the product, not ingestion alone. |
| **Corpus** | `~/repos/MyAPI/Corpus v1.0/` — substrate; handoffs are the privileged retrieval target. |

---

## Integrated plan (Sab + session consensus)

1. **Sab writes two event traces** (first durable handoffs in the vault):
   - MyAPI v0 — where it went wrong (incl. friend-refinery origin vs what shipped).
   - Rebuild night — Codex derail (Jun 19–21 sessions).
2. **Agent verifies** traces against corpus, `handoffs/`, `~/.codex/sessions/`, repo state.
3. **Golden briefs:** project handoff (`get_project_context`), person handoff (`get_person_context`).
4. **Small vault refresh** — normalize a handful of examples to handoff shape, not 2,951-note re-ingest.
5. **Implement:** reader → graph → MCP returns briefs → eval against goldens. Success = new agent reads vault, continues without re-litigation.

**Event trace template:** When · Project · Actors · What happened · Decisions · Mistakes/damage · Why it matters now · Evidence (corpus/repo/raw paths) · Lesson.

---

## Key paths

| Asset | Location |
|---|---|
| Rebuild repo | `~/repos/MyAPI-rebuild/` |
| Architecture plan | `~/repos/MyAPI-rebuild/ARCHITECTURE.md` |
| Old MyAPI + corpus | `~/repos/MyAPI/`, `~/repos/MyAPI/Corpus v1.0/` |
| Graph | `~/repos/MyAPI/graphify-out/graph.json` (862 nodes, 2186 links) |
| Codex sessions | `~/.codex/sessions/2026/06/` |
| Friend-refinery handoff | `~/repos/MyAPI/.handoffs/025-web-ui-agent-pt-2.md` |
| MyAPI README origin line | `~/repos/MyAPI/project-docs/README.md` ("context database of who I am") |

---

## Communication rules for agents

- Short factual answers first when asked a direct question.
- Narratives matter; don't lecture about not dumping data — show the trace shape.
- No Codex-style blockers, synthesis docs, or tables-for-everything.
- Don't conflate friend-refinery origin with person-context MCP tool.
- Don't assume Sab needs a UI for himself; he needs briefs, traces, and CLI/API that work.

---

## Next session starter

> Read `REBUILD-CONTEXT-ANCHOR.md` and `ARCHITECTURE.md`. Product = vault of durable handoffs (Ascend theme). Path: traces → golden briefs → reader → MCP. Do not re-litigate origin or Codex derail.