# Harness Evaluation Rubric

Use this after each query in v0.

## Score each query

- `0` wrong or unusable
- `1` partially useful but materially flawed
- `2` mostly right with minor issues
- `3` correct and useful

## Checkpoints

For each run, record:

- query text
- typed query class
- top sources returned
- whether the sources were right
- whether the result was fragmented
- whether one source family dominated
- whether time was respected
- whether titles / anchors helped
- whether post-retrieval grouping would have improved the answer
- whether expansion would have helped

## Diagnose the failure

Choose one primary cause:

- query typing
- retrieval precision
- grouping
- expansion
- corpus quality
- metadata quality
- time handling

## Notes

- If the answer is wrong, do not assume the model is bad first.
- First check whether the query was typed correctly.
- Then check whether retrieval found the right cluster.
- Then check whether grouping / expansion would have repaired the result.

## Output format

Keep a short record per query:

```md
- query:
- type:
- score:
- primary failure:
- sources:
- notes:
```
