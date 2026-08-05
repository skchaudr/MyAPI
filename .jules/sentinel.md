## 2026-04-12 - Fix eval command injection in deploy script
**Vulnerability:** The deployment script `deploy_to_brain.sh` contained an unsafe `eval` statement designed to expand the tilde (`~`) character when evaluating user input for a directory path: `eval LOCAL_DIR="$LOCAL_DIR"`. This introduced a critical command injection vulnerability. A malicious actor could provide input like `"; ls -al; echo "` to execute arbitrary commands with the privileges of the script user.
**Learning:** Shell scripts processing user input should avoid the `eval` builtin wherever possible as it evaluates arbitrary code. While `eval` is often tempting for tasks like tilde expansion, safer alternatives exist in bash.
**Prevention:** Rather than utilizing `eval`, use safe bash parameter expansion constructs. In this case, `LOCAL_DIR="${LOCAL_DIR/#\~/$HOME}"` performs a simple pattern substitution, replacing a leading tilde with the user's home directory path without executing the input as a command.

## 2026-04-12 - Fix generic error information leakage in FastAPI exception handling
**Vulnerability:** Fast API routes throughout the application, such as `/enrich` and `/imports`, were raising `HTTPException` directly with exception error messages as the `detail` when they failed unexpectedly (`raise HTTPException(status_code=500, detail=str(e))`). This is a bad practice as it leaks stack traces, paths, or service details to clients or logs that should not expose them.
**Learning:** Returning `str(e)` directly inside of `HTTPException` creates a risk of sensitive configuration information being leaked if underlying dependencies raise errors revealing their internal states.
**Prevention:** Instead of exposing `str(e)`, we should log the original exception internally using `logger.error(..., exc_info=True)` and return a generic string response such as `"An internal server error occurred"` as the `detail` to clients in the 500 status code response.

## 2026-04-12 - Prevent DoS via excessively large inputs
**Vulnerability:** The `EnrichRequest` pydantic model in `api/schemas.py` permitted a client to post a string of any size as the `content` field. If processed blindly by Gemini or other LLMs, very large strings would quickly exhaust memory or processing time, leading to Denial of Service (DoS) for other users.
**Learning:** Data classes in API specifications can be vulnerable vectors when the system has no bounds.
**Prevention:** Use the `pydantic.Field` component to enforce boundaries like `max_length`. E.g., `content: str = Field(..., max_length=50000)` sets a sensible limit and ensures large strings never execute the target function logic in `api/routers/enrich.py` in the first place.
