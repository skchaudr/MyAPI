## 2026-04-12 - Fix eval command injection in deploy script
**Vulnerability:** The deployment script `deploy_to_brain.sh` contained an unsafe `eval` statement designed to expand the tilde (`~`) character when evaluating user input for a directory path: `eval LOCAL_DIR="$LOCAL_DIR"`. This introduced a critical command injection vulnerability. A malicious actor could provide input like `"; ls -al; echo "` to execute arbitrary commands with the privileges of the script user.
**Learning:** Shell scripts processing user input should avoid the `eval` builtin wherever possible as it evaluates arbitrary code. While `eval` is often tempting for tasks like tilde expansion, safer alternatives exist in bash.
**Prevention:** Rather than utilizing `eval`, use safe bash parameter expansion constructs. In this case, `LOCAL_DIR="${LOCAL_DIR/#\~/$HOME}"` performs a simple pattern substitution, replacing a leading tilde with the user's home directory path without executing the input as a command.

## 2024-08-14 - Replace Hardcoded CORS Wildcards with Dynamic Config
**Vulnerability:** Overly permissive wildcard origin (`http://0.0.0.0:3000`) hardcoded in FastAPI CORS middleware (`api/main.py`).
**Learning:** Hardcoding wildcard origins alongside `allow_credentials=True` forces developers to manually patch the application for staging/production or risk exposing authenticated endpoints.
**Prevention:** Always use dynamic configuration (e.g., parsing environment variables) for `allow_origins`, enforcing safe fallback values for local development to maintain 12-factor compliance.
