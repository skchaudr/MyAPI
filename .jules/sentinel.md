## 2026-04-12 - Fix eval command injection in deploy script
**Vulnerability:** The deployment script `deploy_to_brain.sh` contained an unsafe `eval` statement designed to expand the tilde (`~`) character when evaluating user input for a directory path: `eval LOCAL_DIR="$LOCAL_DIR"`. This introduced a critical command injection vulnerability. A malicious actor could provide input like `"; ls -al; echo "` to execute arbitrary commands with the privileges of the script user.
**Learning:** Shell scripts processing user input should avoid the `eval` builtin wherever possible as it evaluates arbitrary code. While `eval` is often tempting for tasks like tilde expansion, safer alternatives exist in bash.
**Prevention:** Rather than utilizing `eval`, use safe bash parameter expansion constructs. In this case, `LOCAL_DIR="${LOCAL_DIR/#\~/$HOME}"` performs a simple pattern substitution, replacing a leading tilde with the user's home directory path without executing the input as a command.
## 2024-07-13 - Fix Information Exposure in FastAPI Exception Handling
**Vulnerability:** FastAPI endpoints caught generic exceptions and passed the raw exception string to the client via `detail=str(e)`, exposing internal details and stack traces.
**Learning:** In FastAPI endpoints, returning raw exception strings can leak sensitive internal state or configuration to attackers.
**Prevention:** Handle generic exceptions by logging the error internally with `exc_info=True` and returning a generic 500 error message (e.g., "An internal server error occurred").
