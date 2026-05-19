# Handoff 008: Needle Router v1 — Finetune to Crush It

## Goal
Get Needle's 5-tool router to production quality (target: >85% Call F1, >75% exact match) so it becomes the reusable "Needle factory" pattern for future expansions.

## Repos
- **Needle source:** `/Users/saboor/mac-needle/` (the model, training, CLI)
- **Pi agent integration:** `/Users/saboor/.pi/needle/` (router, daemon, tools, training data, evals)

## Current Baselines (from committed eval reports)

### Smoke (5/8 = 62.5%)
| Category | Score |
|----------|-------|
| delegate | 1/2 |
| edit_file | 1/2 |
| read_file | 1/1 |
| run_shell | 1/2 |
| search_code | 1/1 |

### Hard (15/30 = 50%)
| Category | Score |
|----------|-------|
| delegate_target | 3/6 |
| delegate_vs_shell | 3/6 |
| edit_vs_read | 4/6 |
| **edit_vs_shell** | **0/6** ← worst |
| path_preservation | 5/6 |

### Hard by tool
| Tool | Score |
|------|-------|
| delegate | 5/9 |
| edit_file | 4/9 |
| read_file | 4/5 |
| **run_shell** | **1/6** ← second worst |
| search_code | 1/1 |

## Key Failure Patterns to Fix
1. **`edit_vs_shell` = 0/6** — model routes edits to `run_shell` instead of `edit_file`
2. **`run_shell` = 1/6** — argument pollution (natural language leaking into command args)
3. **`delegate` confusion** — "claude_code" treated as a shell command, not a delegation target
4. **Argument garbling** — `"npm install for dependencies"` instead of `"npm install"`

## What Exists
- `training.jsonl` — 600 base synthetic examples (generated via Vertex Gemini 2.5 Flash)
- `training_router_hardening_v1.jsonl` — 120 targeted hardening examples for the above failures
- `tools.json` — 5-tool registry (edit_file, run_shell, search_code, read_file, delegate)
- `evals/` — eval suite directory
- Best checkpoint: `checkpoints/needle_finetuned_20260517065850_23895_12_512_best.pkl`

## Improvement Plan
1. **Merge training data:** Combine base (600) + hardening (120) if not already done
2. **Generate more contrast pairs** for `edit_vs_shell` and `delegate_vs_shell` — at least 60 more examples each
3. **Re-finetune** with the combined+expanded dataset: `needle finetune combined_training.jsonl`
4. **Eval against the hard suite** — target >75% on hard, 0% → >66% on edit_vs_shell
5. **Iterate** — if specific categories still fail, generate targeted data and re-finetune

## Daemon Info
- Hosted on Mac at `http://100.109.233.105:9090` (Tailnet)
- launchd job: `com.needle.serve.plist`
- After finetuning, update the checkpoint path in `router.py` and restart the daemon

## Roadmap (agreed ordering)
1. **Router v1** ← THIS HANDOFF — make the Needle factory boring and repeatable
2. **model_thinking_v1** — cost per turn, latency, verification pass/fail metrics
3. **context_injection_v1** — comes last (easier to fail silently)

## Bonus: Commit Message Needle
Record proposed commit messages before approval/adjustment during all sessions. This builds free training data for a future commit-message Needle at zero cost.
