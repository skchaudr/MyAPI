
## 2024-05-18 - Reinforcement Scoring O(N^2) Bottleneck
**Learning:** The reinforcement score in `ResultReranker` computes tag overlap across documents. Originally, it used an O(N^2) inner loop over `all_tags`, causing massive CPU stalls for searches generating thousands of documents.
**Action:** Use an O(N) pre-computed inverted index (`tag_to_docs`) when performing inter-document scoring in large retrieval result sets to avoid scaling bottlenecks.
