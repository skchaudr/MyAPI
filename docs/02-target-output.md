# Target Output Format for Khoj Ingestion

> **Agent Rule:** When the Context Refinery exports a `CanonicalDocument`, the output `.md` file MUST match this format exactly. Any deviation will cause Khoj to fail silently when parsing YAML frontmatter.

---

## Critical Rules

1. **The `---` fence MUST be the very first line of the file.** There must be zero blank lines, zero spaces, and zero BOM characters above it.
2. **YAML field order is mandatory.** Follow the order below exactly.
3. **The title heading immediately follows the closing `---`.** No blank line between `---` and `# Title`.
4. **All string values in YAML must use the exact taxonomy strings** defined in `docs/01-taxonomy.md`.

---

## Example File: `auth-flow-brainstorm.md`

```
---
id: 5f8a9b2c-1234-5678-abcd-ef0123456789
title: Authentication Flow Brainstorm
source: chatgpt
created_at: 2023-10-12
author: Me & ChatGPT
status: incubating
doc_type: conversation
tags: [auth, security, web-app]
projects: [VaultSystem]
---
# Authentication Flow Brainstorm
*Summary: Explored using JWTs vs Session cookies. Settled on HTTP-only cookies for the Next.js frontend. Key concern was CSRF protection.*

### User
How should I handle auth in a Next.js app securely?

### Assistant
The most secure method is using HTTP-only cookies...
```

---

## YAML Field Order (Mandatory)

| Field | Source | Notes |
|---|---|---|
| `id` | `CanonicalDocument.id` | UUID |
| `title` | `CanonicalDocument.title` | Plain string |
| `source` | `CanonicalDocument.source.system` | One of the valid source systems |
| `created_at` | `CanonicalDocument.timestamps.created_at` | ISO date string or empty |
| `author` | `CanonicalDocument.author` | Plain string |
| `status` | `CanonicalDocument.status` | Must be a valid MaturityStatus |
| `doc_type` | `CanonicalDocument.doc_type` | Must be a valid DocType |
| `tags` | `CanonicalDocument.tags` | YAML inline list |
| `projects` | `CanonicalDocument.projects` | YAML inline list |

---

## Markdown Body Order (After `---`)

1. `# {title}` — H1 heading
2. `*Summary: {summary}*` — Italic summary line (omit if no summary)
3. Document body — `cleaned_markdown` content as-is
