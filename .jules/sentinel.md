## 2026-04-12 - Fix eval command injection in deploy script
**Vulnerability:** The deployment script `deploy_to_brain.sh` contained an unsafe `eval` statement designed to expand the tilde (`~`) character when evaluating user input for a directory path: `eval LOCAL_DIR="$LOCAL_DIR"`. This introduced a critical command injection vulnerability. A malicious actor could provide input like `"; ls -al; echo "` to execute arbitrary commands with the privileges of the script user.
**Learning:** Shell scripts processing user input should avoid the `eval` builtin wherever possible as it evaluates arbitrary code. While `eval` is often tempting for tasks like tilde expansion, safer alternatives exist in bash.
**Prevention:** Rather than utilizing `eval`, use safe bash parameter expansion constructs. In this case, `LOCAL_DIR="${LOCAL_DIR/#\~/$HOME}"` performs a simple pattern substitution, replacing a leading tilde with the user's home directory path without executing the input as a command.

## 2026-04-12 - Fix exception leakage in FastAPI endpoints
**Vulnerability:** FastAPI endpoints across multiple routers (`query.py`, `enrich.py`, `imports.py`, `export.py`) were catching generic `Exception` objects and returning the raw error string (`str(e)`) to the client via a 500 HTTPException.
**Learning:** Returning raw exception strings in API responses can leak sensitive stack traces, internal system details, or unhandled states, which can be exploited by an attacker to gather reconnaissance on the backend architecture.
**Prevention:** Catch generic exceptions, log them securely on the backend using `logger.error(..., exc_info=True)`, and return a generic, non-informative 500 error message (e.g., "An internal server error occurred") to the client.
