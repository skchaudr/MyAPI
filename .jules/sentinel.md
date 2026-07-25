## 2026-04-12 - Fix eval command injection in deploy script
**Vulnerability:** The deployment script `deploy_to_brain.sh` contained an unsafe `eval` statement designed to expand the tilde (`~`) character when evaluating user input for a directory path: `eval LOCAL_DIR="$LOCAL_DIR"`. This introduced a critical command injection vulnerability. A malicious actor could provide input like `"; ls -al; echo "` to execute arbitrary commands with the privileges of the script user.
**Learning:** Shell scripts processing user input should avoid the `eval` builtin wherever possible as it evaluates arbitrary code. While `eval` is often tempting for tasks like tilde expansion, safer alternatives exist in bash.
**Prevention:** Rather than utilizing `eval`, use safe bash parameter expansion constructs. In this case, `LOCAL_DIR="${LOCAL_DIR/#\~/$HOME}"` performs a simple pattern substitution, replacing a leading tilde with the user's home directory path without executing the input as a command.
## 2024-05-18 - Prevented Internal Error Information Disclosure
**Vulnerability:** HTTP 500 error messages returned raw exception details (e.g. stack traces, 'GEMINI_API_KEY is not set') via `detail=str(e)` in FastAPI routers.
**Learning:** Exposing raw exceptions directly in the response leaks sensitive internal system details (e.g., config problems or unhandled errors) to end-users.
**Prevention:** Catch generic exceptions, log them internally with `exc_info=True` for debugging, and return a generic 'An internal server error occurred' message to the client.
