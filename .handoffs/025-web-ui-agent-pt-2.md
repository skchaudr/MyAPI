I think this is second to Codex's status/next steps handoff ---

Here's the handoff document — copy this wherever you keep context for future sessions:

---

# Context Refinery — Handoff Summary

**Date:** April 9, 2026
**Status:** Foundation built, needs review and iteration

---

## What This Project Is

**Context Refinery** is a personal, general-purpose data refinery web app. The core purpose: ingest heterogeneous personal data exports (Obsidian vaults, ChatGPT/Claude/Gemini exports, LinkedIn data, CLI agent logs), scrub and normalize the content, and export it either as RAG-ready markdown (for feeding a personal vector database/knowledge graph) or as clean readable output (for non-technical users).

The end goal is a self-hosted tool that functions as a personal RAG API endpoint — a database the user owns, usable by themselves or by local agents.

---

## Current State

### What Was Built

Google AI Studio (aistudio.google.com) generated a working prototype called **"Refinery Alpha"** / **"Digital Atelier"**, delivered as a zip file. It is a React app with the following:

**Tech Stack:**

- React 19
- Vite
- Tailwind CSS 4
- Gemini Flash model (for AI distillation/summarization)
- Public Sans + Inter typography
- Deep indigo (#2b3896) + teal (#006a63) color palette with glassmorphism nav

**Pages Built:**

1. **Source Lab (Import)** — Drag-and-drop zone supporting .zip, .json, .md, .csv. Auto-detects source types with confidence scoring. Confirmed working in screenshot: Obsidian Vault (HIGH), ChatGPT Export (HIGH), Claude Export (MEDIUM), LinkedIn Data (HIGH). Manual override dropdown. Stats bar showing total archive size, detected nodes, vector capacity.

2. **Refinery Workspace (Refine)** — Master-detail layout. Document list sidebar + rich preview pane. "Scrub Noise" button. AI Distillation via Gemini (semantic summarization to 3-sentence RAG-optimized output). Metadata panel with tags, title override, maturity tags (Mature / Scratchpad / Deprecated).

3. **Delivery Lab (Export)** — Two modes: RAG Export (YAML frontmatter .md files bundled as zip) and Personal Read Export (HTML or PDF). Output manifest staging area. Download button.

**AI Studio Project URL:** `https://aistudio.google.com/apps/6feb050a-f290-42c1-9890-8f195453c223`

**Stitch Project URL:** `https://stitch.withgoogle.com/projects/15483887809816326802` (used for UI design exploration — the earlier 3-page design here is the _wrong direction_, ignore it)

---

## What Has NOT Been Verified

- Whether the Refine page master-detail UI actually renders and functions correctly
- Whether the Gemini AI distillation button does anything real vs. being UI-only
- Whether the Export page RAG/Personal Read toggle exists and works
- Whether the zip download actually produces valid YAML frontmatter .md files
- Whether the app runs locally (npm install / npm run dev has not been tested in this session)

---

## Primary Data Sources (User's Actual Data)

- ~3,000 Obsidian markdown notes (highest priority)
- ChatGPT export (conversations.json format)
- Claude export
- Gemini export
- LinkedIn data export
- Command-line agent logs

---

## Next Steps for Incoming Agent

1. **Open and run the app locally.** The zip was already downloaded. Run `npm install && npm run dev` in the project directory. Confirm it boots on localhost.

2. **Navigate all 3 pages** and do a functional audit: does the dropzone accept files? Does source detection work? Does the Refine view render a document? Does Scrub Noise do anything? Does Export produce a real file?

3. **If Gemini integration is UI-only**, wire it up properly — the user has access to Gemini via Google AI Studio and the model is Gemini Flash.

4. **Test with real data** — drop in a small Obsidian vault export or a ChatGPT conversations.json and trace the full pipeline end to end.

5. **If the app is solid**, pivot to productionizing: add the Obsidian-specific parser (frontmatter preservation, wikilink handling), improve the ChatGPT/Claude parsers, and harden the RAG export format.

6. **Do NOT restart the Stitch session** (toggling the sidebar resets it — that session context is gone). Stitch is secondary to the AI Studio build.

---

## User Context

- Technical user building a personal RAG system on Ubuntu 22.04
- Khoj is installed as the RAG backend (systemd service, PostgreSQL 14, DB name: khoj, user: khoj, port 42110)
- Non-technical friends may also use this tool — UI must stay approachable
- User wants to own the data pipeline end-to-end

---

That's the full picture. A fresh agent picking this up should be able to get productive in under 2 minutes.
