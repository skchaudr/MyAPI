## 2026-04-12 - Fix eval command injection in deploy script
**Vulnerability:** The deployment script `deploy_to_brain.sh` contained an unsafe `eval` statement designed to expand the tilde (`~`) character when evaluating user input for a directory path: `eval LOCAL_DIR="$LOCAL_DIR"`. This introduced a critical command injection vulnerability. A malicious actor could provide input like `"; ls -al; echo "` to execute arbitrary commands with the privileges of the script user.
**Learning:** Shell scripts processing user input should avoid the `eval` builtin wherever possible as it evaluates arbitrary code. While `eval` is often tempting for tasks like tilde expansion, safer alternatives exist in bash.
**Prevention:** Rather than utilizing `eval`, use safe bash parameter expansion constructs. In this case, `LOCAL_DIR="${LOCAL_DIR/#\~/$HOME}"` performs a simple pattern substitution, replacing a leading tilde with the user's home directory path without executing the input as a command.

## 2024-08-12 - Secure CORS Configuration
**Vulnerability:** The FastAPI backend had a hardcoded `allow_origins` array in `api/main.py` that included an overly permissive wildcard-like address (`http://0.0.0.0:3000`).
**Learning:** Hardcoded, overly permissive CORS origins can expose the application to cross-origin attacks and bypass same-origin policy protections. Configuration should be managed dynamically rather than hardcoded in the application source.
**Prevention:** Use environment variables (like `ALLOWED_ORIGINS`) to configure CORS allow-lists. Parse the environment variable as a comma-separated list to dynamically construct the `allow_origins` array, avoiding hardcoded wide-open configurations and allowing different environments to define their own safe origins.
