# Durable work (backup + version control)

Same rule as AGENTS.md top section and `.grok/rules/durable-work.md`.

Keep-worthy work on this host must be **committed and pushed** (or explicitly
SCP’d). `.scratch/` is not a discard bin. VM downtime is expected; local-only
artifacts are not acceptable for intent maps, nodes, scripts, or code.

Session end: inventory dirty/unpushed keep-worthy paths **first**.
