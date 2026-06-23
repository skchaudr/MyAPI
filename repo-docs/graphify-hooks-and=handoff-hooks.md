
From Grok, but inspiring me on the idea of how to create durable, dynamic, continuous handoff tracking narratiives from a project  
## Git commit hook

| Command | What it does |
|---|---|
| `graphify hook install` | Installs a post-commit hook |
| `graphify hook uninstall` | Removes it |
| `graphify hook status` | Shows whether it's installed |

**After every `git commit`:**
1. Detects changed **code** files (`git diff HEAD~1`)
2. Re-runs AST extraction on those files only
3. Rebuilds `graphify-out/graph.json` and `GRAPH_REPORT.md`

- **No background process** — runs once per commit
- **Code only** — doc/image changes are ignored; use `graphify update .` or `/graphify --update` for those
- **Non-destructive** — if a post-commit hook already exists, graphify **appends** to it rather than replacing it

## Related: `graphify claude install`

Not a git hook, but often mentioned alongside it. Writes a `## graphify` section into `CLAUDE.md` so agents query the graph before answering architecture questions and rebuild after code changes.

This repo has the equivalent in `.agents/rules/graphify.md` — same idea for Cursor/Grok agents.

## project

Flow would be:

1. Run `/graphify` once to build the initial graph
2. `graphify hook install` to keep it current on commits

Want me to check whether the hook is installed globally, or set it up here after an initial graph build?


