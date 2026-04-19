# Query Typing, Post-Retrieval Grouping and Expansion

This folder defines the second-layer evaluation after raw retrieval.

## Query typing

Classify each query before retrieval:

- factual
- temporal
- project identity
- source-specific recall
- cross-source synthesis
- episodic reconstruction
- recurring-pattern / analytic
- metadata / governance

## Post-retrieval grouping

Check whether results should be grouped by:

- note
- session
- project
- source family
- time window
- topic cluster

## Expansion rules

After raw hits return, evaluate whether the system should expand:

- adjacent notes with the same topic
- sibling notes in the same folder or cluster
- previous / next sessions in a time sequence
- source-adjacent material with a clear semantic tie

## Failure modes

Record whether the bad result came from:

- wrong query type
- weak retrieval
- bad grouping
- missing expansion
- corpus noise
- time mismatch
- one-source domination
- weak titles / anchors

## Desired behavior

- prefer coherent answer units over isolated hits
- preserve temporal ordering when the query is temporal
- preserve source identity when the query is source-specific
- avoid mixing too many unrelated corpora unless the query demands synthesis
