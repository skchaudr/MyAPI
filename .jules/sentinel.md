## 2026-04-12 - Fix eval command injection in deploy script
**Vulnerability:** The deployment script `deploy_to_brain.sh` contained an unsafe `eval` statement designed to expand the tilde (`~`) character when evaluating user input for a directory path: `eval LOCAL_DIR="$LOCAL_DIR"`. This introduced a critical command injection vulnerability. A malicious actor could provide input like `"; ls -al; echo "` to execute arbitrary commands with the privileges of the script user.
**Learning:** Shell scripts processing user input should avoid the `eval` builtin wherever possible as it evaluates arbitrary code. While `eval` is often tempting for tasks like tilde expansion, safer alternatives exist in bash.
**Prevention:** Rather than utilizing `eval`, use safe bash parameter expansion constructs. In this case, `LOCAL_DIR="${LOCAL_DIR/#\~/$HOME}"` performs a simple pattern substitution, replacing a leading tilde with the user's home directory path without executing the input as a command.

## 2026-04-12 - Prevent Path Traversal in File Import Endpoints
**Vulnerability:** The `/codex` and `/claude-code` import endpoints accepted a `root` parameter that was expanded and used in file system operations without validation, allowing a malicious user to supply paths like `../../etc` to traverse outside the intended base directory.
**Learning:** When APIs accept file paths, strictly validating them using `os.path.commonpath` against the expanded absolute base directory is required to prevent path traversal, avoiding `.startswith()` which is vulnerable to partial traversal.
**Prevention:** Always validate user-provided paths by expanding them with `os.path.abspath(os.path.expanduser(path))` and asserting that `os.path.commonpath([base_dir, target_path]) == base_dir`.
