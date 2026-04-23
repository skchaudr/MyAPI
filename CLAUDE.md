# CLAUDE.md — MyAPI

## Shell Commands: Don't Make Me Fix Your Work

**Never give multi-line `-c` python commands.** They break in zsh because of indentation and quote handling. The user has to fix them and it's exhausting.

**Instead:**
- Write a temp script file first, then run it with `python3 /path/to/script.py`
- Or use semicolons on a single line: `python3 -c "import x; do_thing()"`
- Or use `python3 -m module.path args` when possible — that's the cleanest

**Paths with spaces break shell word-splitting.** Never use `$(cat file | tr '\n' ' ')` to expand file lists when paths contain spaces. Use a Python script that reads the file directly instead.

**PYTHONPATH must be set when running scripts outside the project directory.** If running a script from `/tmp` or anywhere that isn't `/Users/saboor/repos/MyAPI`, prefix with `PYTHONPATH=/Users/saboor/repos/MyAPI`.

**Preferred pattern for "run triage on a file list":**
```bash
cd /Users/saboor/repos/MyAPI && PYTHONPATH=/Users/saboor/repos/MyAPI python3 /tmp/run_triage.py
```
Where `/tmp/run_triage.py` is written by Claude before asking the user to run anything.

## General Rule

The shell is unforgiving. Before telling the user to run something, verify it will work exactly as written — no fixing required on their end.
