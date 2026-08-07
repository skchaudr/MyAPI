# Cold-start question bank from agent demand

Type: research
Status: resolved

## Question

What are the **agent questions that define v1 success** for Semantic Graphify cold-start — mined from existing demand signals, not invented from a blank page?

Sources to harvest (primary): corpus-hot MyAPI `QUERIES.md` / `GAPS.md`, retrieval trust bank (A/H/F classes that map to cold-start), Graphify-class “steal shapes,” status-anchor style operational questions, and any logged agent queries that asked Graphify for meaning it could not provide.

Output: a short ranked bank (target ~8–15 questions) grouped by intent (ownership, now-state, evidence, decisions, danger/open, meaning-of-code). Mark which ones a thin v1 *must* answer vs defer.

## Answer

Full findings: [02-cold-start-question-bank.md](../research/02-cold-start-question-bank.md)

**Gist — v1 must-set (8):**
1. What is this project and its current goal? (A1)
2. Who owns MyAPI vs MyMCP / what may be written?
3. Current phase / north star / tip lag
4. What’s broken or blocked? (A7)
5. Where should I begin (entry paths)?
6. What decisions constrain this work? (project-scoped)
7. What evidence paths back the above?
8. What does this code area *mean* (module narrative, not AST)?

**Defer:** human find-thread (H1), exact-phrase probes (F5/H4), F1–F4 failure classes, full decision-recovery, symbol-level dual graph.

**Graphify alone fails:** plan-as-live, AST≠narrative, tree≠main, volume RAG, vault truth outside git.

## Comments

- Chart session: research subagent completed. Findings: `../research/02-cold-start-question-bank.md`
