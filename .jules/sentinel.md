## 2026-04-12 - Fix eval command injection in deploy script
**Vulnerability:** The deployment script `deploy_to_brain.sh` contained an unsafe `eval` statement designed to expand the tilde (`~`) character when evaluating user input for a directory path: `eval LOCAL_DIR="$LOCAL_DIR"`. This introduced a critical command injection vulnerability. A malicious actor could provide input like `"; ls -al; echo "` to execute arbitrary commands with the privileges of the script user.
**Learning:** Shell scripts processing user input should avoid the `eval` builtin wherever possible as it evaluates arbitrary code. While `eval` is often tempting for tasks like tilde expansion, safer alternatives exist in bash.
**Prevention:** Rather than utilizing `eval`, use safe bash parameter expansion constructs. In this case, `LOCAL_DIR="${LOCAL_DIR/#\~/$HOME}"` performs a simple pattern substitution, replacing a leading tilde with the user's home directory path without executing the input as a command.

## 2026-08-03 - Prevent Information Leakage in API Error Responses
**Vulnerability:** The `/enrich` and `/enrich/batch` endpoints were catching generic exceptions and returning `str(e)` directly to the client. This can leak sensitive internal state, stack traces, or other operational details.
**Learning:** Always sanitize error messages returned to clients from FastAPI endpoints. Internal exceptions should be logged for debugging, but the user should only see a generic failure message to prevent reconnaissance.
**Prevention:** When catching generic exceptions, log the error locally with `exc_info=True` and return a generic 500 internal server error message (e.g., "An internal server error occurred").
