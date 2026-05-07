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
