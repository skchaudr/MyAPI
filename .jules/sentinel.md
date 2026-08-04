## 2026-04-12 - Fix eval command injection in deploy script
**Vulnerability:** The deployment script `deploy_to_brain.sh` contained an unsafe `eval` statement designed to expand the tilde (`~`) character when evaluating user input for a directory path: `eval LOCAL_DIR="$LOCAL_DIR"`. This introduced a critical command injection vulnerability. A malicious actor could provide input like `"; ls -al; echo "` to execute arbitrary commands with the privileges of the script user.
**Learning:** Shell scripts processing user input should avoid the `eval` builtin wherever possible as it evaluates arbitrary code. While `eval` is often tempting for tasks like tilde expansion, safer alternatives exist in bash.
**Prevention:** Rather than utilizing `eval`, use safe bash parameter expansion constructs. In this case, `LOCAL_DIR="${LOCAL_DIR/#\~/$HOME}"` performs a simple pattern substitution, replacing a leading tilde with the user's home directory path without executing the input as a command.

## 2024-05-24 - Information Leakage in API Responses
**Vulnerability:** API routes (`/enrich`, `/imports`, `/query`, `/export`) were catching generic exceptions and returning `str(e)` in the `detail` field of HTTP 500 responses.
**Learning:** Returning raw exception strings directly to the client can expose sensitive internal details, file paths, stack traces, or configuration data to potential attackers.
**Prevention:** Catch generic exceptions, log them securely server-side (using `logger.error(..., exc_info=True)`), and return a generic error message (e.g., "An internal server error occurred") in the HTTP response. Ensure tests mock this behavior correctly and assert against the generic error string, not the raw exception detail.
