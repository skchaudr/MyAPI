## 2026-04-12 - Fix eval command injection in deploy script
**Vulnerability:** The deployment script `deploy_to_brain.sh` contained an unsafe `eval` statement designed to expand the tilde (`~`) character when evaluating user input for a directory path: `eval LOCAL_DIR="$LOCAL_DIR"`. This introduced a critical command injection vulnerability. A malicious actor could provide input like `"; ls -al; echo "` to execute arbitrary commands with the privileges of the script user.
**Learning:** Shell scripts processing user input should avoid the `eval` builtin wherever possible as it evaluates arbitrary code. While `eval` is often tempting for tasks like tilde expansion, safer alternatives exist in bash.
**Prevention:** Rather than utilizing `eval`, use safe bash parameter expansion constructs. In this case, `LOCAL_DIR="${LOCAL_DIR/#\~/$HOME}"` performs a simple pattern substitution, replacing a leading tilde with the user's home directory path without executing the input as a command.

## 2026-04-12 - Prevent sensitive information leakage via error messages
**Vulnerability:** Fast API generic exception handlers were exposing raw exception details back to clients by returning `detail=str(e)` on unhandled internal server errors.
**Learning:** Returning `str(e)` in an HTTPException allows malicious actors to infer backend configurations, internal variables, and possible attack vectors by forcing unexpected errors.
**Prevention:** Exception details should be hidden behind generic error messages like "An internal server error occurred" for all 5XX responses. Instead, log the actual raw error serverside using `logger.error(msg, exc_info=True)` so debugging capability is not lost.
