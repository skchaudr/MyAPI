## 2026-04-12 - Fix eval command injection in deploy script
**Vulnerability:** The deployment script `deploy_to_brain.sh` contained an unsafe `eval` statement designed to expand the tilde (`~`) character when evaluating user input for a directory path: `eval LOCAL_DIR="$LOCAL_DIR"`. This introduced a critical command injection vulnerability. A malicious actor could provide input like `"; ls -al; echo "` to execute arbitrary commands with the privileges of the script user.
**Learning:** Shell scripts processing user input should avoid the `eval` builtin wherever possible as it evaluates arbitrary code. While `eval` is often tempting for tasks like tilde expansion, safer alternatives exist in bash.
**Prevention:** Rather than utilizing `eval`, use safe bash parameter expansion constructs. In this case, `LOCAL_DIR="${LOCAL_DIR/#\~/$HOME}"` performs a simple pattern substitution, replacing a leading tilde with the user's home directory path without executing the input as a command.

## 2026-08-05 - Prevent Exception Information Leakage via HTTP 500 Responses
**Vulnerability:** Fast API routes were passing `str(e)` directly to the client inside `HTTPException(status_code=500, detail=str(e))` statements during unhandled exception blocks, which leaks sensitive internals like stack traces or backend connection strings to users.
**Learning:** Returning unhandled `Exception` contents exposes backend architectures (e.g. GEMINI_API_KEY exceptions, internal file paths). Errors returned to the client should be generic.
**Prevention:** Always log generic exceptions using `logger.error("Context...", exc_info=True)` for backend debugging and return generic messages like `"An internal server error occurred"` to the client.
