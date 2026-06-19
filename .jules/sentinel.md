## 2026-04-12 - Fix eval command injection in deploy script
**Vulnerability:** The deployment script `deploy_to_brain.sh` contained an unsafe `eval` statement designed to expand the tilde (`~`) character when evaluating user input for a directory path: `eval LOCAL_DIR="$LOCAL_DIR"`. This introduced a critical command injection vulnerability. A malicious actor could provide input like `"; ls -al; echo "` to execute arbitrary commands with the privileges of the script user.
**Learning:** Shell scripts processing user input should avoid the `eval` builtin wherever possible as it evaluates arbitrary code. While `eval` is often tempting for tasks like tilde expansion, safer alternatives exist in bash.
**Prevention:** Rather than utilizing `eval`, use safe bash parameter expansion constructs. In this case, `LOCAL_DIR="${LOCAL_DIR/#\~/$HOME}"` performs a simple pattern substitution, replacing a leading tilde with the user's home directory path without executing the input as a command.

## 2026-05-05 - Information Disclosure in API Endpoints
**Vulnerability:** The `/import/obsidian`, `/import/codex`, and `/import/claude-code` endpoints directly returned the raw exception string `str(e)` to the client inside a 500 HTTP response when an internal error occurred.
**Learning:** Exposing raw exception strings or stack traces to clients is an information disclosure vulnerability that can reveal internal system state or architecture.
**Prevention:** In FastAPI endpoints, handle generic exceptions by logging the error with `exc_info=True` for debugging and returning a generic 500 error message (e.g., "An internal server error occurred") instead of returning the raw exception string.
