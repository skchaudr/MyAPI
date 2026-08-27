## 2026-04-12 - Fix eval command injection in deploy script
**Vulnerability:** The deployment script `deploy_to_brain.sh` contained an unsafe `eval` statement designed to expand the tilde (`~`) character when evaluating user input for a directory path: `eval LOCAL_DIR="$LOCAL_DIR"`. This introduced a critical command injection vulnerability. A malicious actor could provide input like `"; ls -al; echo "` to execute arbitrary commands with the privileges of the script user.
**Learning:** Shell scripts processing user input should avoid the `eval` builtin wherever possible as it evaluates arbitrary code. While `eval` is often tempting for tasks like tilde expansion, safer alternatives exist in bash.
**Prevention:** Rather than utilizing `eval`, use safe bash parameter expansion constructs. In this case, `LOCAL_DIR="${LOCAL_DIR/#\~/$HOME}"` performs a simple pattern substitution, replacing a leading tilde with the user's home directory path without executing the input as a command.

## 2024-05-18 - Prevent DoS via memory exhaustion in FastAPI file uploads
**Vulnerability:** File upload endpoints (Obsidian, ChatGPT) loaded entire file contents into memory using `await file.read()`, creating a DoS risk via memory exhaustion for large inputs.
**Learning:** FastAPI's `UploadFile` caches uploads in memory or spool files but reading entirely block by block forces it fully into RAM.
**Prevention:** Always use chunked reading (`while chunk := await file.read(1024*1024):`) and enforce strict hard limits (e.g., `if len > 50MB: raise HTTPException(413)`) when buffering to a byte array. For writing directly to disk, offload standard synchronous I/O chunks using `asyncio.get_running_loop().run_in_executor(...)`.
