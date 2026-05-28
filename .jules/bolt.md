
## 2024-05-18 - Tag Overlap Calculation in Result Reranker
**Learning:** Found an O(N²) nested loop bottleneck in reinforcement scoring (`ResultReranker.rerank`) where every document's tags were checked against every other document's tags. For large datasets, this approach scales quadratically and can severely throttle CPU cycles.
**Action:** Always employ an inverted index (e.g., `tag_to_docs`) when calculating overlaps among sets across a large array of objects to maintain O(N) linear time complexity.
