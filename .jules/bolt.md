
## 2024-05-31 - Optimize Reinforcement Scoring with Inverted Index
**Learning:** The document retrieval pipeline calculated a reinforcement score by checking overlap between every pair of results, causing an O(N^2) bottleneck when large result sets (e.g. 1000 items) are processed in python. Precomputing an inverted index (tag to document index) allows checking overlaps in O(N * K) where K is number of tags.
**Action:** Next time an O(N^2) pairwise comparison over metadata (tags, properties) is spotted, try refactoring into a two-pass approach with an inverted index.
