## 2026-04-12 - Fix eval command injection in deploy script
**Vulnerability:** The deployment script `deploy_to_brain.sh` contained an unsafe `eval` statement designed to expand the tilde (`~`) character when evaluating user input for a directory path: `eval LOCAL_DIR="$LOCAL_DIR"`. This introduced a critical command injection vulnerability. A malicious actor could provide input like `"; ls -al; echo "` to execute arbitrary commands with the privileges of the script user.
**Learning:** Shell scripts processing user input should avoid the `eval` builtin wherever possible as it evaluates arbitrary code. While `eval` is often tempting for tasks like tilde expansion, safer alternatives exist in bash.
**Prevention:** Rather than utilizing `eval`, use safe bash parameter expansion constructs. In this case, `LOCAL_DIR="${LOCAL_DIR/#\~/$HOME}"` performs a simple pattern substitution, replacing a leading tilde with the user's home directory path without executing the input as a command.

## 2024-05-18 - Fix information disclosure in FastAPI error responses
**Vulnerability:** Multiple FastAPI routing endpoints were directly embedding raw Python exceptions (`str(e)`) into the 500 error responses returned to the client (e.g., `raise HTTPException(status_code=500, detail=str(e))`).
**Learning:** In a web API, exposing raw error traces or exception strings can inadvertently leak sensitive system architecture, configuration details, database schemas, or API keys (Information Disclosure) to potential attackers.
**Prevention:** Catch top-level generic exceptions, internally log them completely using standard logging with `exc_info=True` for debugging, and return safe, standardized and generic error messages (e.g., "An internal server error occurred") to clients.
