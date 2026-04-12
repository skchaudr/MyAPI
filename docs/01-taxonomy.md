# Context Refinery: RAG Taxonomy & Rules

> **Agent Rule:** When writing any adapter, parser, or export function, you MUST use only the exact string values defined in this file. Do not invent new status or doc_type values.

---

## 1. Maturity Status

Every document must be tagged with one of the following statuses. This is the primary trust signal for the Khoj AI when retrieving context.

> **Default for all new imports: `scratchpad`**
> This is a failsafe. Even if a user uploads 500 documents without reviewing them, Khoj will know they are low-trust and noisy. A human must manually promote a document to `incubating` or `mature`.

| Status | Meaning |
|---|---|
| `mature` | Ground truth. Finalized specs, completed code, established knowledge. High signal, high reliability. |
| `incubating` | Fully fleshed out, architected, or outlined, but not yet acted upon or deployed. |
| `scratchpad` | Raw brainstorming, stream of consciousness, or messy AI chats. High noise, low reliability. **Default for new imports.** |
| `deprecated` | Old ideas or superseded code. Kept for historical context. Agents MUST ignore this for active problem-solving. |
| `reference` | External data (e.g., pasted articles, API docs) that is factual but not original thought. |

**Valid values (exact strings):** `"mature"` | `"incubating"` | `"scratchpad"` | `"deprecated"` | `"reference"`

---

## 2. Document Types (`doc_type`)

| Type | Meaning |
|---|---|
| `conversation` | Multi-turn AI or human chats. |
| `note` | Standard Obsidian-style personal notes. |
| `spec` | Formal project specifications or architectural documents. |
| `log` | Daily logs, terminal outputs, or journal entries. |
| `article` | Long-form written content (blogs, essays). |
| `other` | Fallback for unrecognized formats. |

**Valid values (exact strings):** `"conversation"` | `"note"` | `"spec"` | `"log"` | `"article"` | `"other"`

---

## 3. Source Systems

The system that originally produced this document.

**Valid values:** `"chatgpt"` | `"claude"` | `"obsidian"` | `"linkedin"` | `"manual"`

---

## 4. Source Types

The file format of the original source.

**Valid values:** `"json"` | `"html"` | `"md"` | `"csv"`
