## 2024-05-27 - ResultReranker Reinforcement Score O(1) loop Optimization
**Learning:** The `ResultReranker._reinforcement_score` function previously iterated through all tags across all documents for every single document, causing an O(N^2) CPU bottleneck for large document sets.
**Action:** Always consider pre-computing inverted indices (like mapping tags to document indices) to perform overlap checks using set union instead of nested loops. This brings the time complexity to O(N) when tags are reasonably bounded.
