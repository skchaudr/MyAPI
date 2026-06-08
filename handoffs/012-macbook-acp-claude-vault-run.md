# 012 — MacBook ACP Claude setup: Obsidian corpus vault run

Date: 2026-06-04
Branch: feat/corpus-v1-normalization
From: Big Pi (big-ssd) running Claude Code (Sonnet 4.6)
To: MacBook Claude Code — Pass B vault normalization run

---

## Current state on Pi

**Pass A is complete.** The deterministic vault materialization ran on Pi and
produced:

```text
corpus_v1/vault-v1.0/
  2,951 generated notes
  2,675 selected source files inventoried
  0 parse failures
```

Vault structure is scaffolded and populated:

```text
00-index/          10-current-state/     20-projects/
30-systems-and-workflows/               40-decisions-and-trajectories/
50-timeline/       60-sessions-and-conversations/
70-artifacts-and-reference/             80-candidates/
90-raw-provenance/ _manifests/          _reports/
```

Build reports at `corpus_v1/vault-v1.0/_reports/`:
- `build-summary.md` — counts and paths
- `validation-summary.json` — coverage numbers
- `parse-failures.jsonl` — empty (no failures)
- `build-manifest.jsonl` — 2,951-row provenance index

Project bundles scaffolded under `20-projects/`:
- `MyAPI/` — contains `MyAPI Index.md` only
- `GDDP/`, `DevInfra/`, `Vault Normalization/` — present

**Pass B has not started.** Project bundle notes (Anchor, Current State, Work
Queue, Timeline), timeline events, and normalized session notes have not been
written yet.

---

## Branch sync

`corpus_v1/` is gitignored — the vault travels out-of-band. The vault is
already present on Mac. Just pull the branch to get the latest code and docs:

```
Run on Mac: cd /Users/saboor/repos/MyAPI && git fetch --all && git checkout feat/corpus-v1-normalization && git pull origin feat/corpus-v1-normalization
```

---

## Open the vault in Obsidian

After sync:

```text
Open in Obsidian: /Users/saboor/repos/MyAPI/corpus_v1/vault-v1.0
```

Verify:
- Folder view shows all 9 numbered sections plus `_manifests/` and `_reports/`
- Global search finds expected session titles and note names
- `_reports/build-summary.md` renders cleanly

Do not open the raw input bundle (`raw-v1.0/`) as a vault.

---

## Pass B: normalization run on Mac

The implementation plan is at:

```text
project-docs/corpus-v1-vault-v1.0-implementation-plan.md
```

Read it before starting. Key constraints:
- Never write generated files back into `corpus_v1/raw-v1.0/`.
- Raw integrity: `corpus_v1/raw-v1.0/manifests/selected-checksums.sha256` must
  pass before and after any materialization.
- No confidential Obsidian paths (`02 Areas/Confidential/`) in any API
  allowlist.

**Ordered Pass B steps:**

1. **Verify checksums** before touching anything:

   ```
   Run on Mac: cd /Users/saboor/repos/MyAPI && python3 -c "import subprocess, sys; r = subprocess.run(['sha256sum', '--check', 'corpus_v1/raw-v1.0/manifests/selected-checksums.sha256'], capture_output=True, text=True, cwd='.'); print(r.stdout[-500:] if r.stdout else r.stderr[-500:])"
   ```

2. **Inspect a mixed sample in Obsidian** before normalizing:
   - One note from `60-sessions-and-conversations/claude-code/`
   - One from `60-sessions-and-conversations/chatgpt/`
   - One from `60-sessions-and-conversations/claude-web/`
   - One from `90-raw-provenance/obsidian/`
   - Confirm provenance frontmatter is present and readable

3. **Build project bundles** for the four initial projects:
   - `MyAPI`, `GDDP`, `DevInfra`, `Vault Normalization`
   - Each bundle needs: `<Project> Anchor.md`, `<Project> Current State.md`,
     `<Project> Work Queue.md`, `<Project> Timeline.md`
   - Update `<Project> Index.md` to link all four
   - Use workflow markers: `[/]` in progress, `[!]` blocked, `[?]` question,
     `[-]` deferred, `[*]` important

4. **Extract timeline events** into `50-timeline/` for the v1 window
   (2026-03-22 to 2026-05-22 for Obsidian; 2026-04-22 to 2026-05-22 for
   chats/sessions). Each event links to source evidence — no synthetic facts.

5. **Normalize a small batch first** — do not attempt the full corpus:
   - 40 Obsidian notes (project docs, anchors, handoffs)
   - 20 ChatGPT conversations
   - 20 Claude web conversations
   - 30 Claude Code sessions
   - 20 Codex sessions
   - All repo docs and handoffs relevant to MyAPI, GDDP, DevInfra

6. **Place uncertain outputs** in `80-candidates/needs-review/` — do not
   promote unreviewed normalized notes to numbered folders.

---

## Minimal metadata floor (do not over-stamp)

For generated notes:

```yaml
normalization_version: vault-v1.0
source_kind:
source_id:
source_path:
captured_at:
occurred_at:
concepts: []
tags: []
derived_from: []
```

`note_role` where needed: `anchor | current_state | work_queue | timeline_event | artifact_summary | raw_pointer`

Do NOT add experimental fields (`project`, `area`, `status`, `confidence`,
`canonical`, `supersedes`) until they are tested in retrieval ablations.

---

## Key files to read before starting

```text
project-docs/corpus-v1-vault-v1.0-implementation-plan.md   # full spec
handoffs/011-corpus-v1-obsidian-substrate-architecture.md   # architecture decisions
handoffs/010-corpus-v1-mac-readiness.md                     # prior Mac scan state
scripts/build_vault_v1.py                                   # Pass A materializer (reference)
corpus_v1/vault-v1.0/_reports/build-summary.md              # what was built
corpus_v1/vault-v1.0/_reports/validation-summary.json       # coverage counts
```

---

## Relay

If using the jules-relay operator relay, AGENTS.md has the full protocol.
Set `RELAY_URL` and `RELAY_TOKEN` as env vars before starting. Post STATE at
task start and finish only — no checkpoints.

---

## Non-goals for this run

- Do not re-run `build_vault_v1.py` unless checksums fail or a specific adapter
  needs repair.
- Do not upload any vault content to VM or external API.
- Do not force V4 Obsidian schema fields onto generated notes.
- Do not add graphification infrastructure before plain Markdown navigation
  works.
- Do not collapse project Anchor + Current State + Work Queue + Timeline into
  one note.
