## 2026-04-12 - Fix eval command injection in deploy script
**Vulnerability:** The deployment script `deploy_to_brain.sh` contained an unsafe `eval` statement designed to expand the tilde (`~`) character when evaluating user input for a directory path: `eval LOCAL_DIR="$LOCAL_DIR"`. This introduced a critical command injection vulnerability. A malicious actor could provide input like `"; ls -al; echo "` to execute arbitrary commands with the privileges of the script user.
**Learning:** Shell scripts processing user input should avoid the `eval` builtin wherever possible as it evaluates arbitrary code. While `eval` is often tempting for tasks like tilde expansion, safer alternatives exist in bash.
**Prevention:** Rather than utilizing `eval`, use safe bash parameter expansion constructs. In this case, `LOCAL_DIR="${LOCAL_DIR/#\~/$HOME}"` performs a simple pattern substitution, replacing a leading tilde with the user's home directory path without executing the input as a command.
## 2024-05-25 - Secure Error Handling in FastAPI
**Vulnerability:** Raw exception strings (`str(e)`) were being leaked to the client via `HTTPException` detail fields.
**Learning:** Returning `str(e)` directly in HTTP 500 responses exposes sensitive internal state, such as stack traces, file paths, or upstream API error formats.
**Prevention:** Always log exceptions with `logger.error("Message", exc_info=True)` for backend debugging and return a generic 500 error string (e.g., "An internal server error occurred") to the client.
