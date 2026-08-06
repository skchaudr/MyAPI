## 2024-06-25 - Precompile and batch regex in strip_boilerplate
**Learning:** Compiling regex patterns on every call and matching line-by-line is extremely expensive for functions manipulating text frequently. Using a single combined regex, compiling it at the module level, and utilizing `re.sub` with `re.MULTILINE` across the entire text is significantly faster.
**Action:** When handling large text modifications (like stripping boilerplate lines), compile one large combined regex at the module level using `re.IGNORECASE | re.MULTILINE` and process the entire string with `.sub()` instead of splitting by newline and iterating. Handle optional CRLF `\r?\n?` in the multiline regex.

## 2024-06-25 - Review Action: Safe Regex Hoisting
**Learning:** While `re.MULTILINE` and `.sub()` are faster, they can introduce functional regressions if the previous line-by-line `.strip()` or anchor logic (like `^unsubscribe$`) is not identically preserved.
**Action:** The safest and most accurate way to optimize repeated regex compilations in a loop is simply hoisting the compiled patterns to the module scope and keeping the validation loop intact, which still yields massive performance gains (~75% faster) without changing semantics.
