## 2026-04-12 - Fix eval command injection in deploy script
**Vulnerability:** The deployment script `deploy_to_brain.sh` contained an unsafe `eval` statement designed to expand the tilde (`~`) character when evaluating user input for a directory path: `eval LOCAL_DIR="$LOCAL_DIR"`. This introduced a critical command injection vulnerability. A malicious actor could provide input like `"; ls -al; echo "` to execute arbitrary commands with the privileges of the script user.
**Learning:** Shell scripts processing user input should avoid the `eval` builtin wherever possible as it evaluates arbitrary code. While `eval` is often tempting for tasks like tilde expansion, safer alternatives exist in bash.
**Prevention:** Rather than utilizing `eval`, use safe bash parameter expansion constructs. In this case, `LOCAL_DIR="${LOCAL_DIR/#\~/$HOME}"` performs a simple pattern substitution, replacing a leading tilde with the user's home directory path without executing the input as a command.

## 2026-07-12 - Prevent Information Leakage in API Responses
**Vulnerability:** Fast API routes raised `HTTPException(status_code=500, detail=str(e))` for unhandled exceptions.
**Learning:** This exposes raw exception details (which can include sensitive stack traces, internal system states, or path info) to the client, leading to a Medium/Low priority Information Exposure vulnerability.
**Prevention:** Catch generic exceptions, log them securely on the server using `logger.error(..., exc_info=True)`, and return a safe, generic message to the client like `"An internal server error occurred"`.
