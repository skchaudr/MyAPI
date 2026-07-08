## 2026-04-12 - Fix eval command injection in deploy script
**Vulnerability:** The deployment script `deploy_to_brain.sh` contained an unsafe `eval` statement designed to expand the tilde (`~`) character when evaluating user input for a directory path: `eval LOCAL_DIR="$LOCAL_DIR"`. This introduced a critical command injection vulnerability. A malicious actor could provide input like `"; ls -al; echo "` to execute arbitrary commands with the privileges of the script user.
**Learning:** Shell scripts processing user input should avoid the `eval` builtin wherever possible as it evaluates arbitrary code. While `eval` is often tempting for tasks like tilde expansion, safer alternatives exist in bash.
**Prevention:** Rather than utilizing `eval`, use safe bash parameter expansion constructs. In this case, `LOCAL_DIR="${LOCAL_DIR/#\~/$HOME}"` performs a simple pattern substitution, replacing a leading tilde with the user's home directory path without executing the input as a command.
## 2026-07-08 - Information Leakage in Error Responses
**Vulnerability:** Fast API exception handling exposing raw 'str(e)' directly in HTTP 500 error responses.
**Learning:** Raw string exceptions can expose sensitive paths, environment configurations, and stack traces to end users.
**Prevention:** Catch generic exceptions, log them securely internally with 'exc_info=True', and return a safe, sanitized generic message (e.g. 'An internal server error occurred') to the client.
