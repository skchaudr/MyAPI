## 2026-04-12 - Fix eval command injection in deploy script
**Vulnerability:** The deployment script `deploy_to_brain.sh` contained an unsafe `eval` statement designed to expand the tilde (`~`) character when evaluating user input for a directory path: `eval LOCAL_DIR="$LOCAL_DIR"`. This introduced a critical command injection vulnerability. A malicious actor could provide input like `"; ls -al; echo "` to execute arbitrary commands with the privileges of the script user.
**Learning:** Shell scripts processing user input should avoid the `eval` builtin wherever possible as it evaluates arbitrary code. While `eval` is often tempting for tasks like tilde expansion, safer alternatives exist in bash.
**Prevention:** Rather than utilizing `eval`, use safe bash parameter expansion constructs. In this case, `LOCAL_DIR="${LOCAL_DIR/#\~/$HOME}"` performs a simple pattern substitution, replacing a leading tilde with the user's home directory path without executing the input as a command.

## 2025-06-02 - Prevent Path Traversal in Imports
**Vulnerability:** User-supplied `root` parameters in import endpoints (`/codex`, `/claude-code`) were passed directly to scanning functions, allowing path traversal outside the intended base directory.
**Learning:** Even internal tool endpoints can be vulnerable if user-supplied paths aren't validated against their intended base directories.
**Prevention:** Use `os.path.commonpath([base_dir, target_path]) == base_dir` after expanding and resolving both paths to strictly enforce that the target path remains within the base directory.
