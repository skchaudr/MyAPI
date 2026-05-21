## 2026-04-12 - Fix eval command injection in deploy script
**Vulnerability:** The deployment script `deploy_to_brain.sh` contained an unsafe `eval` statement designed to expand the tilde (`~`) character when evaluating user input for a directory path: `eval LOCAL_DIR="$LOCAL_DIR"`. This introduced a critical command injection vulnerability. A malicious actor could provide input like `"; ls -al; echo "` to execute arbitrary commands with the privileges of the script user.
**Learning:** Shell scripts processing user input should avoid the `eval` builtin wherever possible as it evaluates arbitrary code. While `eval` is often tempting for tasks like tilde expansion, safer alternatives exist in bash.
**Prevention:** Rather than utilizing `eval`, use safe bash parameter expansion constructs. In this case, `LOCAL_DIR="${LOCAL_DIR/#\~/$HOME}"` performs a simple pattern substitution, replacing a leading tilde with the user's home directory path without executing the input as a command.

## 2024-05-24 - Secure Error Handling API Boundary
**Vulnerability:** API routes were leaking internal exceptions and stack trace details directly to client responses via `str(e)` in 500 status codes.
**Learning:** Returning direct exception strings in production APIs can unintentionally expose framework versions, paths, environment configurations, and database details.
**Prevention:** Catch top-level generic exceptions locally, log them securely with `exc_info=True`, and return a sanitized, static generic response (e.g. "An internal server error occurred") to clients.
