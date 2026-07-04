## 2026-04-12 - Fix eval command injection in deploy script
**Vulnerability:** The deployment script `deploy_to_brain.sh` contained an unsafe `eval` statement designed to expand the tilde (`~`) character when evaluating user input for a directory path: `eval LOCAL_DIR="$LOCAL_DIR"`. This introduced a critical command injection vulnerability. A malicious actor could provide input like `"; ls -al; echo "` to execute arbitrary commands with the privileges of the script user.
**Learning:** Shell scripts processing user input should avoid the `eval` builtin wherever possible as it evaluates arbitrary code. While `eval` is often tempting for tasks like tilde expansion, safer alternatives exist in bash.
**Prevention:** Rather than utilizing `eval`, use safe bash parameter expansion constructs. In this case, `LOCAL_DIR="${LOCAL_DIR/#\~/$HOME}"` performs a simple pattern substitution, replacing a leading tilde with the user's home directory path without executing the input as a command.

## 2024-07-04 - Fix unhandled exception stack traces in API endpoints
**Vulnerability:** Fast API endpoints in `api/routers/` were returning raw stringified exceptions (`detail=str(e)`) with a 500 status code when unexpected errors occurred. This can lead to stack trace or sensitive system detail leakage.
**Learning:** Returning `str(e)` in unexpected error scenarios breaks the "fail securely" principle by directly propagating internal state to the client in HTTP responses.
**Prevention:** Catch generic exceptions, log them securely server-side using `logger.error("Message", exc_info=True)`, and return a generic user-facing message like "An internal server error occurred" to avoid leaking internals.
