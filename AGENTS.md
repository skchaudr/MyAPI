# AGENTS.md

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
- Post `STATE:` before any high-risk or irreversible step (deploy, migration,
  destructive file ops, network calls with side effects).
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
