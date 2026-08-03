## 2026-04-12 - Fix eval command injection in deploy script
**Vulnerability:** The deployment script `deploy_to_brain.sh` contained an unsafe `eval` statement designed to expand the tilde (`~`) character when evaluating user input for a directory path: `eval LOCAL_DIR="$LOCAL_DIR"`. This introduced a critical command injection vulnerability. A malicious actor could provide input like `"; ls -al; echo "` to execute arbitrary commands with the privileges of the script user.
**Learning:** Shell scripts processing user input should avoid the `eval` builtin wherever possible as it evaluates arbitrary code. While `eval` is often tempting for tasks like tilde expansion, safer alternatives exist in bash.
**Prevention:** Rather than utilizing `eval`, use safe bash parameter expansion constructs. In this case, `LOCAL_DIR="${LOCAL_DIR/#\~/$HOME}"` performs a simple pattern substitution, replacing a leading tilde with the user's home directory path without executing the input as a command.

## 2024-08-02 - Prevent Exception Detail Leaks in API Responses
**Vulnerability:** Uncaught internal errors in FastAPI endpoints (`enrich.py`, `imports.py`, `query.py`, `export.py`) were returning raw exception messages (`str(e)`) to the client, leading to potential information leakage regarding internal workings and stack traces.
**Learning:** Using `str(e)` in HTTP 500 error responses is common during development but highly insecure for production because it exposes sensitive internal application details.
**Prevention:** Catch generic exceptions, log them securely on the server with `exc_info=True` using Python's `logging` module, and strictly return standardized generic error messages (e.g., "An internal server error occurred") to clients.
