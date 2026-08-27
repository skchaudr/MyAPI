## 2026-04-12 - Fix eval command injection in deploy script
**Vulnerability:** The deployment script `deploy_to_brain.sh` contained an unsafe `eval` statement designed to expand the tilde (`~`) character when evaluating user input for a directory path: `eval LOCAL_DIR="$LOCAL_DIR"`. This introduced a critical command injection vulnerability. A malicious actor could provide input like `"; ls -al; echo "` to execute arbitrary commands with the privileges of the script user.
**Learning:** Shell scripts processing user input should avoid the `eval` builtin wherever possible as it evaluates arbitrary code. While `eval` is often tempting for tasks like tilde expansion, safer alternatives exist in bash.
**Prevention:** Rather than utilizing `eval`, use safe bash parameter expansion constructs. In this case, `LOCAL_DIR="${LOCAL_DIR/#\~/$HOME}"` performs a simple pattern substitution, replacing a leading tilde with the user's home directory path without executing the input as a command.

## 2026-05-05 - Fix overly permissive CORS configuration
**Vulnerability:** The FastAPI application used a hardcoded CORS configuration that allowed the `http://0.0.0.0:3000` wildcard origin. This could potentially allow unauthorized cross-origin requests.
**Learning:** Hardcoding overly permissive origins, such as `0.0.0.0`, bypasses intended CORS protections. Security configurations should be environment-specific rather than universally broad in the codebase.
**Prevention:** Configure CORS `allow_origins` dynamically using an environment variable (like `ALLOWED_ORIGINS` parsed as a comma-separated list), defaulting to safe local development origins if absent, to strictly restrict cross-origin access.
