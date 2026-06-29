## 2026-04-12 - Fix eval command injection in deploy script
**Vulnerability:** The deployment script `deploy_to_brain.sh` contained an unsafe `eval` statement designed to expand the tilde (`~`) character when evaluating user input for a directory path: `eval LOCAL_DIR="$LOCAL_DIR"`. This introduced a critical command injection vulnerability. A malicious actor could provide input like `"; ls -al; echo "` to execute arbitrary commands with the privileges of the script user.
**Learning:** Shell scripts processing user input should avoid the `eval` builtin wherever possible as it evaluates arbitrary code. While `eval` is often tempting for tasks like tilde expansion, safer alternatives exist in bash.
**Prevention:** Rather than utilizing `eval`, use safe bash parameter expansion constructs. In this case, `LOCAL_DIR="${LOCAL_DIR/#\~/$HOME}"` performs a simple pattern substitution, replacing a leading tilde with the user's home directory path without executing the input as a command.

## 2024-06-29 - Prevent Leaking Internal Errors to Client
**Vulnerability:** FastApi HTTPExceptions with status 500 were leaking internal raw exception strings (`str(e)`) to the client.
**Learning:** Leaking full stack traces or inner exception details in 500 API responses can expose sensitive information about the backend infrastructure to attackers.
**Prevention:** Use `logger.error("Message", exc_info=True)` for logging the error details, and return a generic 500 response message (e.g. "An internal server error occurred").
