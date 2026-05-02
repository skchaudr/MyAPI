# Context Refinery

## Summary
Context Refinery processes raw personal knowledge exports (e.g., Obsidian notes, AI conversations) into a canonical format for Retrieval-Augmented Generation (RAG) systems. It utilizes Google's Gemini AI to summarize, sanitize, and tag the data. Finally, it exports these refined documents as clean Markdown files with YAML frontmatter to power a headless Khoj personal search database.

## Core Tech Stack
**Frontend:**
- React 19
- Vite
- TypeScript
- Tailwind CSS v4

**Backend:**
- Python
- FastAPI
- Google GenAI (Gemini integration)
- Pytest (Testing)

## Current State of the Project
The project currently features a solid foundation with a complete React frontend containing Import, Refine, and Export views. The Python backend utilizes a `CanonicalDoc` schema to represent structured documents. While the AI summarization via Gemini and UI scaffolding are functional, much of the data ingestion pipeline remains conceptual or relies on mock data instead of live parsing.

## Main Unsolved Problems
- **Ingestion & Parsing:** Implementing actual file and folder parsing for various sources (such as Obsidian vaults and ChatGPT history exports).
- **Sanitization & Deduplication:** Building robust data sanitization pipelines to strip out noise and handle duplicate content.
- **Structured Validation:** Ensuring comprehensive validation against the canonical document schema.
- **Live Wiring:** Connecting the frontend UI to live backend processing jobs instead of relying on mock data.
