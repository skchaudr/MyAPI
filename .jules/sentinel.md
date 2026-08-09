## 2026-04-12 - Fix eval command injection in deploy script
**Vulnerability:** The deployment script `deploy_to_brain.sh` contained an unsafe `eval` statement designed to expand the tilde (`~`) character when evaluating user input for a directory path: `eval LOCAL_DIR="$LOCAL_DIR"`. This introduced a critical command injection vulnerability. A malicious actor could provide input like `"; ls -al; echo "` to execute arbitrary commands with the privileges of the script user.
**Learning:** Shell scripts processing user input should avoid the `eval` builtin wherever possible as it evaluates arbitrary code. While `eval` is often tempting for tasks like tilde expansion, safer alternatives exist in bash.
**Prevention:** Rather than utilizing `eval`, use safe bash parameter expansion constructs. In this case, `LOCAL_DIR="${LOCAL_DIR/#\~/$HOME}"` performs a simple pattern substitution, replacing a leading tilde with the user's home directory path without executing the input as a command.
## 2024-10-24 - Securing Public Endpoints Exposing Sensitive Information

**Vulnerability:** The unauthenticated `/health` endpoint exposed sensitive environment data including API service modes, configuration status, cloud project identifiers, and backend URLs (`KHOJ_URL`).

**Learning:** Publicly accessible endpoints (like those for deployment liveness probes) should only expose necessary indicators (e.g., `{"status": "ok"}`). More comprehensive health information intended for monitoring/administrative purposes must be protected with authentication, otherwise, it inadvertently leaks deployment configuration details.

**Prevention:** Ensure new endpoints implement strict authentication, use separated internal vs. public health probes, and limit public liveness checks to returning generic "ok" strings.
