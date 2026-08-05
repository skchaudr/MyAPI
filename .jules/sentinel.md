## 2026-04-12 - Fix eval command injection in deploy script
**Vulnerability:** The deployment script `deploy_to_brain.sh` contained an unsafe `eval` statement designed to expand the tilde (`~`) character when evaluating user input for a directory path: `eval LOCAL_DIR="$LOCAL_DIR"`. This introduced a critical command injection vulnerability. A malicious actor could provide input like `"; ls -al; echo "` to execute arbitrary commands with the privileges of the script user.
**Learning:** Shell scripts processing user input should avoid the `eval` builtin wherever possible as it evaluates arbitrary code. While `eval` is often tempting for tasks like tilde expansion, safer alternatives exist in bash.
**Prevention:** Rather than utilizing `eval`, use safe bash parameter expansion constructs. In this case, `LOCAL_DIR="${LOCAL_DIR/#\~/$HOME}"` performs a simple pattern substitution, replacing a leading tilde with the user's home directory path without executing the input as a command.

## 2024-07-16 - Prevent Exception Detail Leakage in FastAPI Endpoints
**Vulnerability:** Multiple FastAPI routes (`enrich`, `query`, `imports`, `export`) were catching generic `Exception`s and returning the raw stringified exception (`str(e)`) in a 500 `HTTPException` directly to the client.
**Learning:** Returning `str(e)` in HTTP responses leaks sensitive internal implementation details, file paths, or infrastructure state (stack traces) to end users, aiding attackers in reconnaissance.
**Prevention:** Always log the full exception locally (`logger.error(..., exc_info=True)`) for debugging, but return a generic string like `"An internal server error occurred"` to the client when handling generic exceptions in FastAPI routes.
