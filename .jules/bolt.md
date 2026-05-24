## 2024-05-24 - Optimize ResultReranker reinforcement scoring
**Learning:** Computing tag overlap between documents naively in a nested loop leads to an $O(N^2)$ algorithmic bottleneck, drastically hurting performance as the corpus retrieved gets larger.
**Action:** Use an inverted index `tag_to_docs` built upfront in $O(N)$ to aggregate overlap checks. It brings down reinforcement score computation down to $O(N \cdot T)$ which is much more efficient.
