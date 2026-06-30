## 2026-04-12 - Fix eval command injection in deploy script
**Vulnerability:** The deployment script `deploy_to_brain.sh` contained an unsafe `eval` statement designed to expand the tilde (`~`) character when evaluating user input for a directory path: `eval LOCAL_DIR="$LOCAL_DIR"`. This introduced a critical command injection vulnerability. A malicious actor could provide input like `"; ls -al; echo "` to execute arbitrary commands with the privileges of the script user.
**Learning:** Shell scripts processing user input should avoid the `eval` builtin wherever possible as it evaluates arbitrary code. While `eval` is often tempting for tasks like tilde expansion, safer alternatives exist in bash.
**Prevention:** Rather than utilizing `eval`, use safe bash parameter expansion constructs. In this case, `LOCAL_DIR="${LOCAL_DIR/#\~/$HOME}"` performs a simple pattern substitution, replacing a leading tilde with the user's home directory path without executing the input as a command.

## 2026-05-24 - Prevent internal exception details from leaking in API responses
**Vulnerability:** FastAPI endpoints in `enrich.py`, `imports.py`, `query.py`, and `export.py` were returning raw exception strings (`str(e)`) to clients when internal server errors occurred.
**Learning:** Returning `str(e)` in HTTP 500 responses can expose sensitive information, such as stack traces, internal file paths, or backend configuration issues to end users.
**Prevention:** Use generic error messages like "An internal server error occurred" in HTTP responses for generic exceptions, and log the detailed error server-side using `logger.error("...", exc_info=True)` for debugging.
