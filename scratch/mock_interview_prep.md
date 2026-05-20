# MyAPI Senior Engineering Mock Interview Prep Guide

This guide is structured as a high-fidelity **Senior Engineering Manager (EM) Mock Interview Session**. Each section presents a tough architectural question, the "rookie trap" response, the "senior developer" response, and the underlying conceptual mapping.

Use this to build your mental model and confidently explain the engineering decisions behind MyAPI in real interviews.

---

## 🎙️ Question 1: "Why build a custom Context Refinery instead of just using LlamaIndex or LangChain?"

### 🛑 The Rookie Trap
> "I built it because LlamaIndex was too bloated and I wanted to write my own parser in Python."
*Why this fails:* It lacks engineering justification. EMs hate "not-invented-here" syndrome unless backed by strict trade-off analysis.

### 🏆 The Senior Developer Response
> "We evaluated out-of-the-box RAG frameworks, but they are designed as general-purpose libraries. They wrap retrieval pipelines in thick, generic abstractions that make low-latency tuning, custom path-based classification, and deterministic multi-intent reranking very hard to customize and debug.
> 
> By building **Context Refinery**, we isolated the stages of **Classification**, **Retrieval**, and **Refinement** into clean, self-contained Python modules with **zero complex dependencies**. 
>
> For instance, instead of querying an LLM to classify user intent or parse metadata (which increases latency and cost), we wrote a fast, deterministic regular-expression `QueryClassifier` and a static path-to-metadata router. This dropped latency to the millisecond scale and allowed us to run the entire pipeline comfortably on a low-resource environment (like a cloud VM or an 8GB Mac)."

### 🎯 Key Interview Talking Points
1. **Dependency Consciousness**: Standard packages import hundreds of sub-dependencies, bloat container size, and create security/maintenance issues.
2. **Latent Control**: Having exact control over the scoring math in the `ResultReranker` without reading through layers of framework code.

---

## 🎙️ Question 2: "You used Khoj instead of raw pgvector or Pinecone. Why?"

### 🛑 The Rookie Trap
> "I just found Khoj and it worked well, and it was easy to deploy."
*Why this fails:* Sounds like vibes-driven decision making.

### 🏆 The Senior Developer Response
> "The choice was driven by **operational efficiency** and **hardware constraints**. 
>
> Spinning up a dedicated PostgreSQL instance with `pgvector` introduces major database administration overhead—maintaining index builds (HNSW vs IVFFlat), managing RAM allocation, and handling connection pools. A managed service like Pinecone is expensive and introduces network latency.
>
> **Khoj** operates as a lightweight, developer-focused vector search container. It handles file indexing, embeddings generation (using fast, quantized models), and semantic search in a single process. It exposes a simple API that integrated perfectly into our async architecture.
>
> This allowed us to run semantic indexing *entirely locally* or on a small remote VM instance without dedicating significant RAM to a database daemon, maintaining an ultra-light infrastructure footprint."

### 🎯 Key Interview Talking Points
1. **Operational Overhead**: Choosing a single-purpose tool (Khoj) that excels at markdown-indexing over a complex general-purpose database system.
2. **Resource Constraints**: Respecting M1 Mac / small VM memory budgets by avoiding heavy Docker service meshes.

---

## 🎙️ Question 3: "Walk me through your path-based normalization strategy. Why is it deterministic?"

### 🛑 The Rookie Trap
> "It maps folder paths to labels. I did it this way because it was easy to write."
*Why this fails:* Doesn't highlight the architectural elegance of combining deterministic heuristics with stochastic LLM features.

### 🏆 The Senior Developer Response
> "In an obsidian vault containing thousands of notes, running an LLM or even an offline embedding classifier over every single file during ingestion to extract structural context is extremely slow, expensive, and error-prone.
>
> We implemented a **path-based normalization schema** (`normalization_schema.py`). In Obsidian, users naturally group files into directories—like `01 Projects/`, `Daily/`, and `handoffs/`. Our schema translates these relative POSIX paths into structured metadata keys (`source_type`, `temporal_mode`, `primary_project`) deterministically using O(1) prefix and regex matching.
>
> This guarantees **100% accuracy** and **near-zero CPU overhead** during ingestion. We use this structured metadata to feed our downstream reranking mathematical weights, ensuring the search engine has perfect structural awareness of the vault's design without spending a single API credit or wasting processor cycles."

### 🎯 Key Interview Talking Points
1. **Deterministic Router**: Combining user-organized directory hierarchy with system rules to get free, high-fidelity metadata.
2. **Scale Performance**: A system that processes 10,000 files in under 2 seconds compared to hours with LLM-based parsers.

---

## 🎙️ Question 4: "How exactly do you down-weight AI hallucinations and score files? Explain the ResultReranker math."

### 🛑 The Rookie Trap
> "I just have a formula that adds numbers together and sorts them."
*Why this fails:* Too vague. EMs want to see the actual variables and how they interact.

### 🏆 The Senior Developer Response
> "Our `ResultReranker` calculates a unified score using a weighted sum of normalized inputs:
> 
> $$\text{Score} = w_{\text{sem}} \cdot S_{\text{sem}} + w_{\text{rec}} \cdot S_{\text{rec}} + w_{\text{trust}} \cdot S_{\text{trust}} + w_{\text{reinf}} \cdot S_{\text{reinf}} + w_{\text{kw}} \cdot S_{\text{kw}} + w_{\text{title}} \cdot S_{\text{title}}$$
>
> Where:
> *   $S_{\text{sem}}$: Dense vector similarity from Khoj.
> *   $S_{\text{rec}}$: Time recency (decayed score based on file age).
> *   $S_{\text{trust}}$: Trust priors (boosting curated handoffs and summary files).
> *   $S_{\text{reinf}}$: Reinforcement signals (boosting highly cited files).
> *   $S_{\text{kw}}$: Sparse keyword match counts.
>
> **Intent-Driven Weight Shifts**:
> When a user queries *'What did I do yesterday?'*, our regex `QueryClassifier` flags a **temporal intent**. The system dynamically shifts weights: $w_{\text{rec}}$ rises from `0.16` to `0.46`, while $w_{\text{sem}}$ drops. This guarantees that yesterday's timeline note is pushed to the top, even if a note from two years ago is semantically closer to the query.
>
> **Hallucination Control**:
> Raw vector search often pulls in messy AI-generated conversation logs or third-party scrapes containing hallucinations. We suppress this by applying negative priors to certain file kinds and boosting high-trust directories (like curated summary handoffs), ensuring only clean, grounded notes form the context window."

### 🎯 Key Interview Talking Points
1. **Multi-Lane Retrieval**: Blending dense vector representations with sparse keyword matching.
2. **Dynamic Weight Adjustment**: Tuning retrieval constraints based on structural query intent (temporal vs. factual).
