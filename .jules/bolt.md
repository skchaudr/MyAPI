## 2024-05-19 - Optimize ResultReranker and KeywordSearcher
**Learning:** The reinforcement score in `ResultReranker` originally used an O(N^2) approach to compare tags across all documents, which becomes a severe CPU bottleneck during large document searches. Additionally, `KeywordSearcher` recompiled regexes for each file within its search loop.
**Action:** Always precompute an inverted index (`tag_to_docs`) for matching properties across result sets to maintain O(N) complexity, and precompile regular expressions before loops.
