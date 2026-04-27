---
type: utility
title: V4 Owner-Pass Queue
area: "[[Vault]]"
source: original
created: 2026-04-26
---

# V4 Owner-Pass Queue

Generated 2026-04-26 after Phase 4 batch normalization (11 batches, ~1700 notes).
Items here need **human judgment** that the bulk normalizer can't apply:
- Concepts assignment (the V4 graph backbone)
- Unprefixed tag cleanup
- Edge cases the script couldn't reach

The interactive owner-pass tool: `python3 -m context_refinery.triage --vault-root ~/obsidian/SoloDeveloper [files...]`

---

## Tier 1 — Edge cases the bulk normalizer skipped (9 files)

These are root-level vault files or files in folders the `--subdir` safety
constraint can't address. Each needs the V4 floor (`type`, `area`, `source`)
stamped manually.

### Has `format:` in frontmatter (needs strip)
- `hand-therapy-master-plan 2026.04.15.md` — root-level. Likely `type: resource`, `area: [[Health]]`.
- `Git conflicts - rebasing when both sides must stay.md` — root-level. Likely `type: resource`, `area: [[My_DevInfra]]`, `tags: [tool/git]`.

### Missing `type:` (needs full V4 floor)
- `Git remote history core workflow.md` — root-level. Likely `type: resource`, `area: [[My_DevInfra]]`, `tags: [tool/git]`.
- `Twitter triage box.md` — root-level. Likely `type: log` or `type: utility`, `area: [[Career]]` or `[[Vault]]`.
- `Water and Stone hours tracking.md` — root-level. Likely `type: log`, `area: [[Career]]`.
- `__Tasks__/NeoVim Multi-Week Plan for 2026 proficiency.md` — TaskNotes folder. Project-anchored.

### No frontmatter at all
- `NoteboomLM CLI - User guide for artifacts like audio, flashcards, infographics, etc.md` — root-level.
- `WOW YAY.md` — root-level.
- `Zed threads naming - repo/Zed threads naming - Project Name + Goal.md` — `Zed threads naming - repo/` is a one-off subdir at root.

**Quick fix recipe**: `cd ~/Obsidian/SoloDeveloper && nvim "<file>"` and prepend frontmatter, OR run the owner-pass CLI on each file individually.

---

## Tier 2 — Files with unprefixed tags or type conflicts

Source: each batch's `project-docs/v4-batch-NN-*-dryrun.json` lists `review_needed`
items. Use the JSON to build a concrete list per cluster.

To extract the tier-2 worklist for a single batch:
```bash
cd ~/Repos/MyAPI
python3 -c "
import json
data = json.load(open('project-docs/v4-batch-09-areas-dryrun.json'))
review = [s for s in data if s['confidence'] != 'high']
for s in review:
    print(s['path'])
    for r in s['review_needed']:
        print(f'    {r}')
"
```

Recommended order matches the batch order (smallest blast first):
1. `v4-batch-01-archive-dryrun.json` (22 notes)
2. `v4-batch-02-inbox-dryrun.json` (29)
3. `v4-batch-03-*-dryrun.json` (small folders, 25)
4. `v4-batch-04-utilities-dryrun.json` (100)
5. `v4-batch-05-periodic-dryrun.json` (109)
6. `v4-batch-06-projects-dryrun.json` (174)
7. `v4-batch-07-08-resources-rest-dryrun.json` (185)
8. `v4-batch-09-areas-dryrun.json` (782)
9. `v4-batch-10-resources-rest-dryrun.json` (237)
10. `v4-batch-11-templates-dryrun.json` (32)

---

## Tier 3 — Concepts assignment (the V4 graph backbone)

Almost no notes have `concepts:` populated yet (the bulk normalizer
intentionally doesn't write concepts — that's owner-pass territory).

Recommended approach (per Phase 5 of the plan):
1. **Top-down seed** — create ~20–30 concept stub notes in `03 Resources/Concepts/`.
   Suggested starting set: `[[Automation]]`, `[[Client Work]]`, `[[Scope Control]]`,
   `[[AI Tooling]]`, `[[Vault Normalization]]`, `[[Knowledge Management]]`,
   `[[Agentic AI]]`, `[[Infrastructure]]`, `[[Homelab]]`, `[[Career]]`,
   `[[Hand Therapy]]`, `[[Terminal Workflows]]`, `[[Neovim]]`, `[[Obsidian]]`,
   `[[Portfolio Design]]`, `[[Peer Benchmarking]]`, `[[Benchmarking]]`,
   `[[Freelance]]`, `[[Code Problem Solving]]`, `[[Documentation]]`.
2. **Harvest pass** — count `[[wiki link]]` occurrences vault-wide; promote any
   appearing in 3+ notes to a concept stub.
3. **Owner-pass cycles** — `python3 -m context_refinery.triage --queue-json
   project-docs/v4-batch-NN-*-dryrun.json --vault-root ~/obsidian/SoloDeveloper`
   per batch. Pick concepts interactively from the seed list.

---

## Coverage Snapshot — 2026-04-26 (post-Phase-4)

- Total `.md` files: **1704**
- With frontmatter: **1701** (99.8%)
- With `migration_status: v4-applied`: **1695** (99.5%)
- With `source` field: **1695** (99.5%)
- With `type:` in frontmatter: **1697** (99.6%)
- With deprecated `format:` in frontmatter: **2** (0.1%) — Tier 1
- No frontmatter at all: **3** (0.2%) — Tier 1
- With `concepts:` populated: **~28** (~1.6%) — Tier 3 priority
