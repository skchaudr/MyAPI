# Pi / Needle / Gemma — QUERIES (air)

## Ownership
1. What does **Needle** own (route/assemble/serve) vs **Pi agent** (`~/.pi/agent`) vs **harness**?
2. Who owns the **needle-gemma-v1 bundle** schemas vs Camber upload approval?
3. Who may launch a Camber job/app/engine (Sab gate per ledger)?

## Now-state
4. Does air have a complete local `needle-gemma-v1` bundle with manifest + schemas?
5. What model config files exist (`models.json`, ollama functiongemma) without loading weights?
6. Is Needle serve configured via `com.needle.serve.plist` on this host?
7. What does the execution ledger say status is (Part 1 local vs upload vs train)?

## Evidence
8. Where is the Camber launch approval contract written (duration, budget, shutdown)?
9. Where is harness choice / NEEDLE handoff documented?
10. What vault notes capture Needle×Gemma×Pi postmortem and execution plan?

## Connect
11. How does Needle routing inventory (`routing-inventory/staged/*_report.json`) relate to multi-host (sab-air, pi-big, pi-small)?
12. How does Gemma row schema connect to eval assembler jsonl without treating training dumps as corpus?
13. How should MyAPI golden brief `get_project_context_pi_needle` (on MyAPI main) attach to these paths?
14. What must never be swallowed by Khoj/corpus ingest from `~/.pi` (auth, weights, quarantine, full session dumps)?
