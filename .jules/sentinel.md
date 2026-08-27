## 2026-04-12 - Fix eval command injection in deploy script
**Vulnerability:** The deployment script `deploy_to_brain.sh` contained an unsafe `eval` statement designed to expand the tilde (`~`) character when evaluating user input for a directory path: `eval LOCAL_DIR="$LOCAL_DIR"`. This introduced a critical command injection vulnerability. A malicious actor could provide input like `"; ls -al; echo "` to execute arbitrary commands with the privileges of the script user.
**Learning:** Shell scripts processing user input should avoid the `eval` builtin wherever possible as it evaluates arbitrary code. While `eval` is often tempting for tasks like tilde expansion, safer alternatives exist in bash.
**Prevention:** Rather than utilizing `eval`, use safe bash parameter expansion constructs. In this case, `LOCAL_DIR="${LOCAL_DIR/#\~/$HOME}"` performs a simple pattern substitution, replacing a leading tilde with the user's home directory path without executing the input as a command.

## 2026-08-18 - Prevent DoS via chunked file upload reads
**Vulnerability:** Reading entire files into memory via `UploadFile.read()` can cause memory exhaustion and Denial of Service (DoS) for large uploads.
**Learning:** In FastAPI, `await file.read()` buffers the whole file into RAM.
**Prevention:** Always read uploaded files in chunks (e.g., `await file.read(1024 * 1024)`). If the file must be accumulated in memory, enforce a maximum file size limit during the chunked reading loop, raising a 413 error if exceeded.
