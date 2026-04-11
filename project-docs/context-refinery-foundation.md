I have built the foundation for Context Refinery, a high-performance data ingestion and refinement lab designed for both technical and non-technical users.
Key Features Implemented:
Source Lab (Import View):
High-Volume Ingestion: A centralized drop zone supporting .zip, .json, .md, and .csv files.
Auto-Scan Intelligence: A "Detected Sources" panel that identifies data types (e.g., Obsidian Vaults, ChatGPT History) with confidence scoring.
Ingestion Manifest: A detailed table to track recently uploaded datasets, their sizes, and processing status.
Refinery Workspace (Refine View):
Master-Detail Interface: A document list for quick navigation and a rich preview area for content review.
AI Distillation: Integrated Gemini AI to perform semantic summarization, distilling complex documents into 3-sentence core concepts optimized for RAG embedding indexes.
RAG Optimization Panel: Tools for "Scrubbing Noise," managing metadata overrides, and tagging document maturity (Mature, Scratchpad, Deprecated).
Delivery Lab (Export View):
RAG Export: Optimized output for LLMs with structural YAML frontmatter and relationship preservation.
Personal Read Export: Distilled for human consumption with high-end editorial layouts in HTML or PDF formats.
Output Manifest: A staging area for finalized files ready for download.
Technical & Design Excellence:
Typography: Utilizes Public Sans for bold, technical headlines and Inter for highly legible body text.
Aesthetic: A sophisticated "Refinery" theme using deep indigo (#2b3896) and teal (#006a63) accents, glassmorphism navigation, and intentional spacing for a professional lab feel.
Performance: Built with React 19, Vite, and Tailwind CSS 4 for lightning-fast interactions.
AI Powered: Leverages the Gemini 3 Flash model for real-time data distillation.
You can now begin by dropping your data exports into the Source Lab to start the refinery process.
