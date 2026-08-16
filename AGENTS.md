# AGENTS.md — MyAPI / MyAPI-rebuild

Personal context engine rebuild. MyAPI maintains an evidence-backed Decision
Graph and serves current project intent as ContextBriefs through MCP.

Read the Part 1 room `CONTEXT.md` for the stage you are in (`01-decisions` …
`04-evaluation`). Canonical language lives in [`CONTEXT.md`](CONTEXT.md).
Earlier substrate remains in [`project-docs/REBUILD-CONTEXT-ANCHOR.md`](project-docs/REBUILD-CONTEXT-ANCHOR.md),
[`project-docs/ARCHITECTURE.md`](project-docs/ARCHITECTURE.md), and
[`PROJECT-BRIEF.md`](PROJECT-BRIEF.md). The M1–M8 Decision Graph plan and
fixture evals are archived at [`project-docs/archive-pre-part2/`](project-docs/archive-pre-part2/).

## Phase

Part 1 (decisions → corpus → Khoj → eval) is on this branch. Part 2 drops
next in the same room format. Do not invent run/test/lint commands for new
rebuild surfaces until the repo adds them.

## Project snapshot

- **Target stack:** Python (`context_refinery/` — adapters, triage CLI,
  FastAPI `/query`), Markdown/Obsidian (corpus + brief output,
  FSRS-migratable frontmatter), JSON/YAML (graph + schemas)
- **Existing tooling:** `graphify extract .` refreshes
  `graphify-out/.graphify_analysis.json` (no LLM cold-start needed)
- **Substrates** (layout-dependent — use the row for your machine):
  - **Mac dual worktree** (`MyAPI-rebuild` + `MyAPI`): vault at
    `../MyAPI/Corpus v1.0/` (22 PARA buckets); graph at `graphify-out/graph.json`
  - **VM sab-dev** (`myapi` + `myapi-corpus`): vault at
    `../myapi-corpus/Corpus v1.0/` when synced; graph at `graphify-out/graph.json`
  - **Single checkout:** use sibling corpus worktree path if present, else note
    vault is Mac-local until synced
- **MCP surface (target):** `get_project_context`, `get_person_context` —
  the anchor locks these two names; do not fork into `get_user_context` /
  "operator context"
- **Key dirs:** `01-decisions/` … `04-evaluation/`, `project-docs/`,
  `.handoffs/`, `graphify-out/`, `ingest/`, `rag-pipeline/`

## Command location rules

This repository has historically used both local Mac and remote VM surfaces.
When giving a command, always state where it should be run.

Required labels:

- `Run on Mac:` — local workstation where the user is typing
- `Run on VM:` — command executed from the remote Google Cloud VM target
- `Run in VM shell:` — command run after SSHing into the VM
- `Run in Cloud Shell:` — command run in Google Cloud Shell

If a command depends on `localhost`, `127.0.0.1`, a service port, or a local
file path, the target machine must be explicit. If the command only makes sense
after an SSH hop or inside a specific shell session, say that too.

Prefer one long command line over wrapped multi-line commands when possible. If
a command must be multi-line, keep each line self-contained and clearly
delimited. Any command being instructed to run must be placed on its own
separate line, not inline with surrounding prose.

## Agent-driven development workflow

The default reader of this repo is often another agent. Optimize for the next
session being able to start immediately, not for the current session merely
appearing done.

### Start-of-session contract

1. Run `git status --short --branch` before editing. If it is not clean, stop
   and classify the existing state as tracked changes, untracked files, ignored
   generated files, or branch divergence.
2. Do not overwrite, delete, rename, reformat, or "clean up" inherited changes
   until you know whether they are user work, another agent's work, or generated
   noise. If unsure, ask.
3. Verify branch and upstream before work: `git branch --show-current`,
   `git rev-parse --abbrev-ref --symbolic-full-name @{u}` when available, and
   `git fetch --prune` before merge/rebase decisions.
4. If work continues from another branch, first understand whether it should be
   merged, rebased, abandoned, or left as a PR branch. Do not create parallel
   branches for the same task without a reason recorded in the handoff.

### During-work rules

- Keep changes scoped to the requested task. Separate formatting-only churn from
  functional/doc changes unless the formatter is the task.
- Update `.gitignore` as soon as a tool creates repeatable local noise
  (`node_modules/`, `dist/`, caches, local logs, generated media, temp exports),
  but do not hide meaningful source artifacts just to get a clean status.
- Make small commits at coherent checkpoints. A repo with hours of uncommitted
  agent work is an unsafe handoff state.
- Prefer existing project commands from this file. If a command is missing or
  dependencies are unavailable, run the smallest relevant validation you can and
  record the limitation.
- Never force-push, rewrite shared history, delete remote branches, or discard
  worktree changes unless the operator explicitly authorizes that exact action.
- Inherited uncommitted changes are evidence, not debris. Commit and push them
  unless you can prove they are noise. They may be the only copy.


### Handoff requirement

At the first natural checkpoint after the initial task is complete, or sooner if
context-window reset would help, create/update a handoff so the next session can
resume without archaeology.

- Use the root `.handoffs/` folder. If it does not exist, create it.
- Keep `.handoffs/000-template.md` as the canonical template. Do not overwrite it
  with session notes.
- For each substantive session, create the next numbered handoff file, e.g.
  `.handoffs/001-brief-description.md`.
- Fill only the `Agent Section`. Do not write below `Do NOT edit this file past
  this point`; that section is reserved for Sab.
- Keep the handoff short and empirical: date, branch, touched files, git state,
  artifacts, and exact resume point.
- A handoff is required before claiming completion if the repo had merges,
  branch changes, conflicts, generated artifacts, failing validation, or any
  state the next agent would otherwise need to rediscover.

### End-of-session contract

Before saying "done":

1. Run the relevant validation/build/test commands documented above, or explain
   exactly why they could not run.
2. Run `git status --short --branch`. The target state is clean and synced with
   upstream. If anything remains, it must be intentionally ignored or explicitly
   called out with a path and reason.
3. Commit all intended changes. Do not leave staged, unstaged, or untracked task
   artifacts for the next session to interpret.
4. Push the working branch. If the task is meant to land on `main`, merge it to
   `main`, push `main`, and verify local `main` equals `origin/main`.
5. Leave a concise handoff in the final response: branch, commit, pushed status,
   validation run, changed surfaces, and any residual risk.

### Not-done triggers

Do not report completion if any of these are true:

- uncommitted task changes remain;
- local commits are not pushed;
- the branch is diverged and unresolved;
- merge conflicts or stash entries remain;
- validation failed and no explicit follow-up decision exists;
- generated files, logs, caches, screenshots, or media are untracked and
  unclassified.

The standard is: the next agent can clone/pull, read this file, run the listed
commands, and continue without first becoming a repository janitor.

## Part 1 stage rooms (ICM routing)

Minimal filesystem map for MyAPI Part 1 (decisions → corpus → Khoj → eval):

| Room | Path | Start here |
|---|---|---|
| Decisions | `01-decisions/` | `01-decisions/CONTEXT.md`; schema at `01-decisions/output/decision-schema.md` |
| Corpus | `02-corpus/` | `02-corpus/CONTEXT.md` |
| Ingestion | `03-ingestion/` | `03-ingestion/CONTEXT.md` |
| Evaluation | `04-evaluation/` | `04-evaluation/CONTEXT.md` |

Read the room `CONTEXT.md` before working in that stage. Do not invent task
contracts or later-stage content ahead of the active node.
