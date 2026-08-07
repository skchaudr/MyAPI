# AGENTS.md

## Durable work — version control (READ FIRST)

This host (VM / multi-machine) can go offline for long stretches. **Work that
lives only on disk here is not safe.** Agents must treat “important and not
backed up” as a first-class problem, not a footnote.

### Default assumption

Unless Sab has **explicitly** said a path is throwaway, treat new or modified
project work as **keep**: intent docs, handoffs, `.scratch/` planning packs,
scripts, API/code changes, node maps, research notes, GDDP drafts.

### Required agent behavior

1. **Do not leave keep-worthy work untracked.** As soon as a pack or change is
   real (not a 30-second temp probe), `git add` and **commit** on a named branch.
   Prefer a small dedicated branch over “I’ll commit later.”
2. **Do not consider a commit done until it can leave this host.** After commit,
   **push** the branch to `origin` (or state clearly that push failed and offer
   SCP). Local-only commits are only a half-step on a VM that sleeps.
3. **Session-end / planning-pack inventory.** Before ending a planning or
   multi-file session, list **every** keep-worthy path that is still dirty or
   unpushed. Lead with that list — not with “not in this inventory” digressions.
4. **Never bury the backup status.** If work is uncommitted or unpushed, say
   that in plain language first: path, branch, commit vs not, on origin or not.
5. **Trash only (safe to skip):** `venv/`, `__pycache__/`, `.env` / secrets,
   large corpus dumps, `node_modules/`, regenerateable caches. If unsure whether
   something is trash, **ask once** — do not silently leave it untracked.
6. **Secrets never commit:** `.env`, API keys, tokens, ADC files, private
   transcripts with credentials.

### Co-author trailer (required on agent commits)

```
Co-authored-by: grok-cli <grok-cli@x.ai>
```

(Other tools: use their trailer from home CLAUDE/AGENTS rules.)

### Quick check agents should run

```bash
# Run on VM (or wherever the clone is):
git status -sb
git log --oneline @{u}..HEAD 2>/dev/null || git log --oneline -3
```

If `status` shows keep-worthy `??` or `M`, or commits exist only locally — fix
that before more product work, or get an explicit “discard / leave local.”

---

This repository uses multiple machines. When giving a command, always state
where it should be run.

## Required command locations

- `Mac` means the local workstation where the user is typing.
- `VM` means the remote Google Cloud VM.
- `VM shell` means the command should be run after SSHing into the VM.
- `Cloud Shell` means the command should be run in Google Cloud Shell.

## Command formatting rule

Every command instruction should begin with one of these labels:

- `Run on Mac:`
- `Run on VM:`
- `Run in VM shell:`
- `Run in Cloud Shell:`

If a command depends on `localhost`, `127.0.0.1`, a service port, or a local
file path, the target machine must be explicit.

If the command only makes sense after an SSH hop or inside a specific shell
session, say that too. For example, distinguish:

- `Run on Mac: gcloud compute ssh ...`
- `Run in VM shell: curl ...`

## Example

- `Run in VM shell: curl -s http://localhost:42110/api/health`
- `Run on Mac: gcloud compute ssh ... --command 'tail -n 20 /tmp/reindex_khoj.log'`

## General rule

Do not assume the user knows which machine a command belongs to. If the
target is missing, ask or restate the command with the target included.
Do not assume the user is already inside the VM shell unless the instruction
explicitly says so.

## Command length preference

- Prefer one long command line over wrapped multi-line commands when possible.
- If a command must be multi-line, keep each line self-contained and clearly
  delimited.
- Any command being instructed to run must be placed on its own separate new
  line, not inline with surrounding prose.

### Why

In split panes or multi-window setups, wrapped text can be mistaken for a real
newline when it is copied, pasted, or reflowed by the terminal/editor/chat UI.
That can turn one intended shell command into several separate lines, which may:

- execute in the wrong order
- break quoting or heredocs
- run on the wrong machine if a pasted block loses its context label

Single-line commands are easier to copy, paste, and visually verify across
multiple machines. They also make it obvious whether a command is meant for the
Mac, the VM, VM shell, or Cloud Shell.

## Operator relay

This task may have a live operator on the other end of an HTTPS relay
(see https://github.com/skchaudr/jules-relay).

Env vars (set per-session):
- `RELAY_URL` — base URL of the relay
- `RELAY_TOKEN` — bearer token

On session start, open an SSE subscription:

```bash
curl -N "$RELAY_URL/events" -H "Authorization: Bearer $RELAY_TOKEN" &
```

Behavior rules:
- Post STATE at task start and task finish only. No checkpoints.
- If a message arrives with `from=m1` and `kind=ASK`, **pause the specific
  gated decision it refers to** until an `ACK` arrives from `m1`, or until
  the relay becomes unreachable. Continue everything else.
- If the relay is unreachable (connection refused, 5xx, timeout): proceed
  per the original task brief, EXCEPT for actions explicitly marked
  "operator-gated" in the task.
- NEVER place secrets, credentials, private URLs, tokens, SSH details, or
  sensitive repo contents in relay messages. Coordination text only.

### Message envelope

`POST $RELAY_URL/msg` with `Authorization: Bearer $RELAY_TOKEN`:

```json
{ "from": "jules", "kind": "STATE" | "ASK" | "ACK", "text": "..." }
```

`text` must be ≤ 4096 chars, non-empty.

## Environment

| Var | Purpose | Set by |
|---|---|---|
| `RELAY_URL` | Relay endpoint | Jules session env |
| `RELAY_TOKEN` | Relay auth | Jules session env |
| `KHOJ_URL` | Khoj API base URL (e.g. `http://100.107.147.16:42110`) | Operator |
| `GEMINI_API_KEY` | Google GenAI key (for reranker / embeddings) | Operator |

## Project snapshot

- **Language:** Python 3.11+
- **Install:** `pip install -r requirements.txt`
- **Test:** `pytest -q` (from project root, no PYTHONPATH needed inside repo)
- **Lint:** none configured
- **Heavy dirs excluded from git:** `corpus_v1/`, `_archive/`, `khoj-ready-bundle/`, `scratch/`
- **Key modules:** `context_refinery/` (triage pipeline), `api/`, `scripts/`, `tests/`
