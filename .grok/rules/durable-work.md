# Durable work on multi-machine / VM hosts

This machine can go dark. Untracked planning packs and local-only commits have
already cost real access loss. Follow this every session.

## Keep vs trash

**Keep (commit + push):** code, scripts, `.scratch/` wayfinder/node maps, intent
docs, research, handoffs, AGENTS/rules changes, anything the operator would be
angry to lose after a 36h VM outage.

**Trash (do not commit):** `venv/`, `__pycache__/`, `.env` and secrets, bulk
corpus dumps, caches.

**Unsure → ask.** Do not default to “leave untracked because scratch.”

## Behavior

1. Commit keep-worthy work as soon as it is real (named branch OK).
2. Push so it can leave this host; if push fails, say so and offer SCP.
3. End-of-session: lead with uncommitted/unpushed inventory, not asides.
4. Agent commits need `Co-authored-by: grok-cli <grok-cli@x.ai>`.

## Forbidden

- Leaving multi-file planning packs only under `.scratch` with no commit
- Ending a session with “here’s the map” and zero version-control state
- Treating `.scratch` as permission to skip git
