## 2024-05-24 - Precompiled Inverted Index Optimization
**Learning:** O(N^2) tagging logic and repetitious inner-loop regex compilations bottlenecked Khoj retrieval pipeline filtering significantly across large datasets due to tag set intersection overhead.
**Action:** Replaced regex loops with precompiled arrays and used a precalculated `tag_to_docs` inverted index lookup mapping to compute overlapping sets in O(1) time.
