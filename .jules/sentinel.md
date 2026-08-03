## 2026-04-12 - Fix eval command injection in deploy script
**Vulnerability:** The deployment script `deploy_to_brain.sh` contained an unsafe `eval` statement designed to expand the tilde (`~`) character when evaluating user input for a directory path: `eval LOCAL_DIR="$LOCAL_DIR"`. This introduced a critical command injection vulnerability. A malicious actor could provide input like `"; ls -al; echo "` to execute arbitrary commands with the privileges of the script user.
**Learning:** Shell scripts processing user input should avoid the `eval` builtin wherever possible as it evaluates arbitrary code. While `eval` is often tempting for tasks like tilde expansion, safer alternatives exist in bash.
**Prevention:** Rather than utilizing `eval`, use safe bash parameter expansion constructs. In this case, `LOCAL_DIR="${LOCAL_DIR/#\~/$HOME}"` performs a simple pattern substitution, replacing a leading tilde with the user's home directory path without executing the input as a command.

## 2024-05-18 - Prevented exception detail leakage in HTTP responses
**Vulnerability:** Raw `Exception` strings were being exposed in HTTP 500 error responses (e.g., `raise HTTPException(status_code=500, detail=str(e))`), which can leak sensitive stack traces, internal configuration details, or internal system states to end users.
**Learning:** FastAPI's `HTTPException` detail field should not blindly mirror raw exception strings. Generic messages must be used for unknown internal exceptions to prevent information disclosure.
**Prevention:** Always log generic exceptions server-side using `logger.error(..., exc_info=True)` and return a safe, generic message to the client (e.g., "An internal server error occurred").
