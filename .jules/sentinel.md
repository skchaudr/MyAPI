## 2026-04-12 - Fix eval command injection in deploy script
**Vulnerability:** The deployment script `deploy_to_brain.sh` contained an unsafe `eval` statement designed to expand the tilde (`~`) character when evaluating user input for a directory path: `eval LOCAL_DIR="$LOCAL_DIR"`. This introduced a critical command injection vulnerability. A malicious actor could provide input like `"; ls -al; echo "` to execute arbitrary commands with the privileges of the script user.
**Learning:** Shell scripts processing user input should avoid the `eval` builtin wherever possible as it evaluates arbitrary code. While `eval` is often tempting for tasks like tilde expansion, safer alternatives exist in bash.
**Prevention:** Rather than utilizing `eval`, use safe bash parameter expansion constructs. In this case, `LOCAL_DIR="${LOCAL_DIR/#\~/$HOME}"` performs a simple pattern substitution, replacing a leading tilde with the user's home directory path without executing the input as a command.

## 2026-08-01 - Avoid leaking sensitive internal errors in FastAPI responses
**Vulnerability:** FastAPI endpoints directly returned the raw exception string (e.g., `str(e)`) in generic 500 HTTP responses. This allowed potential stack traces or underlying backend details (such as database structure, path specifics, or internal errors) to be exposed directly to end users, introducing an Information Exposure vulnerability.
**Learning:** Returning `str(e)` in catch-all Exception blocks within FastAPI endpoints is highly unsafe as it may contain unintended sensitive information leakage.
**Prevention:** Always log the full error with `exc_info=True` for internal debugging, but return a static, generic error message (e.g., "An internal server error occurred") to the API client.
