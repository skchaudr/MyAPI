## 2026-04-12 - Fix eval command injection in deploy script
**Vulnerability:** The deployment script `deploy_to_brain.sh` contained an unsafe `eval` statement designed to expand the tilde (`~`) character when evaluating user input for a directory path: `eval LOCAL_DIR="$LOCAL_DIR"`. This introduced a critical command injection vulnerability. A malicious actor could provide input like `"; ls -al; echo "` to execute arbitrary commands with the privileges of the script user.
**Learning:** Shell scripts processing user input should avoid the `eval` builtin wherever possible as it evaluates arbitrary code. While `eval` is often tempting for tasks like tilde expansion, safer alternatives exist in bash.
**Prevention:** Rather than utilizing `eval`, use safe bash parameter expansion constructs. In this case, `LOCAL_DIR="${LOCAL_DIR/#\~/$HOME}"` performs a simple pattern substitution, replacing a leading tilde with the user's home directory path without executing the input as a command.
## 2026-06-25 - Fix information exposure in API exception handlers
**Vulnerability:** API endpoints were returning raw exception strings directly to the client via HTTP 500 errors. This could leak internal stack traces or system state details.
**Learning:** In FastAPI endpoints, returning raw  text using  in  detail fields allows malicious users to map out internal system configurations.
**Prevention:** Catch generic exceptions, log them locally using  with , and return a generic safe message (e.g., 'An internal server error occurred') to the client.
## 2026-04-12 - Fix information exposure in API exception handlers
**Vulnerability:** API endpoints were returning raw exception strings directly to the client via HTTP 500 errors. This could leak internal stack traces or system state details.
**Learning:** In FastAPI endpoints, returning raw Exception text using `str(e)` in HTTPException detail fields allows malicious users to map out internal system configurations.
**Prevention:** Catch generic exceptions, log them locally using logger.error with `exc_info=True`, and return a generic safe message (e.g., 'An internal server error occurred') to the client.
