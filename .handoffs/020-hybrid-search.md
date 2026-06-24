# Task: Add Hybrid Search (Vector + Keyword) to Retrieval Pipeline

## Problem
The retrieval pipeline uses only Khoj's vector/embedding search. This misses exact phrase matches — e.g., searching "gold mine" fails to find a document containing "goldmine" because vector similarity pulls toward Bitcoin mining content instead.

## Solution
Add a keyword search step that runs in parallel with vector search, then merge results before reranking. Keyword hits get a score boost so exact matches rank higher.

## Architecture

Current flow:
```
Classify → Khoj vector search → Filter → Rerank → Group
```

New flow:
```
Classify → [Khoj vector search + Keyword search] → Merge/dedup → Filter → Rerank → Group
```

## Implementation

### 1. Add `KeywordSearcher` class to `context_refinery/retrieval.py`

```python
class KeywordSearcher:
    """Searches indexed markdown files for exact keyword matches."""

    def __init__(self, notes_dir=None):
        self.notes_dir = notes_dir or os.environ.get(
            "KHOJ_NOTES_DIR", "/home/sbkchaudry_gmail_com/khoj-data/notes"
        )

    def search(self, query, n=10):
        """Grep the corpus for keyword matches. Returns list of result dicts."""
        # Normalize query: split into terms, search for each
        # For quoted phrases, search as exact match
        # For unquoted, search for all terms appearing in the same file
        # Return results with a synthetic score based on match density
```

Key behaviors:
- If query contains quoted phrases like `"gold mine"`, search for exact string
- Otherwise split into terms and find files containing ALL terms
- Score by: number of term occurrences / file length (density)
- Parse YAML frontmatter from matched files using the existing `MetadataParser`
- Return same dict shape as the vector search parsed results so merge is trivial

### 2. Modify `RetrievalPipeline.execute()`

After the Khoj vector search (step 2), run keyword search in parallel:

```python
# Step 2a: Vector search (existing)
raw_results = self.khoj.search(q, n=fetch_n)

# Step 2b: Keyword search (new)
keyword_results = self.keyword_searcher.search(q, n=fetch_n)
```

Then merge before filtering:

```python
# Step 2c: Merge and deduplicate
# Use filename as dedup key
# If a result appears in both, keep it and flag it as keyword_match=True
seen_files = {r.get("file") for r in parsed}
for kr in keyword_results:
    if kr.get("file") not in seen_files:
        parsed.append(kr)
        seen_files.add(kr.get("file"))
    else:
        # Flag existing result as also a keyword match
        for p in parsed:
            if p.get("file") == kr.get("file"):
                p["keyword_match"] = True
```

### 3. Boost keyword matches in `ResultReranker.rerank()`

Add a keyword boost factor:

```python
W_KEYWORD = 0.15  # boost for exact text matches

# In the scoring loop:
keyword_boost = 0.0
if r.get("keyword_match"):
    keyword_boost = 1.0

r["final_score"] = (w_sem * sem + w_rec * rec +
                    w_trust * trust + w_reinf * reinf +
                    W_KEYWORD * keyword_boost)
```

Rebalance the other weights so they sum to ~1.0 when keyword boost is active.

### 4. Handle local vs VM execution

The keyword searcher needs access to the markdown files. Two options:
- **On VM (preferred):** reads from `~/khoj-data/notes/` directly
- **Local dev:** reads from `./khoj-ready-bundle/`

Use `KHOJ_NOTES_DIR` env var, defaulting to the VM path.

## Files to modify
- `context_refinery/retrieval.py` — add KeywordSearcher, modify execute(), modify reranker
- `tests/test_retrieval.py` — add tests for keyword search and hybrid merge

## Test cases
1. `test_keyword_exact_phrase` — searching `"goldmine"` finds the file containing it
2. `test_keyword_multi_term` — searching `openclaw harness leak` finds files with all three terms
3. `test_hybrid_merge_dedup` — same file from both searches appears once, flagged as keyword_match
4. `test_keyword_boost_ranking` — a keyword match outranks a higher vector-similarity non-match
5. `test_keyword_no_results` — graceful empty return when no files match

## Verification
```bash
# After implementation, this should find the goldmine conversation:
curl -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{"q": "goldmine openclaw harness leak", "n": 3}'

# Expected: claude-web-converting-opclaw-to-final-system-repo.md ranks #1
```

## Deploy
Restart context-refinery.service on the VM after pushing.
Set `KHOJ_NOTES_DIR=/home/sbkchaudry_gmail_com/khoj-data/notes` in the service env.
