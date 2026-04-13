# Jules Task: Modular Triage System — Fill In Scaffolded Package

## Summary
The package structure at `context_refinery/triage/` has been scaffolded with 12 files containing exact function signatures, docstrings, and `raise NotImplementedError(...)` placeholders. Your job is to **replace every NotImplementedError with working code** by extracting logic from the monolithic `context_refinery/triage.py`.

**This is a fill-in-the-blanks task, not a design task.** Do not change any file names, function signatures, class names, or import structure. Just implement the bodies.

## CRITICAL RULES

1. **DO NOT create new files.** All files already exist in the scaffold.
2. **DO NOT rename, move, or delete any scaffold files.**
3. **DO NOT change function signatures, class names, or property names.**
4. **DO NOT add new dependencies.** Only `rich`, `pyyaml`, and Python stdlib.
5. **DO NOT modify `passes/base.py`** — the abstract base class is complete.
6. **DO NOT modify `__init__.py` or `__main__.py`** — they are complete.
7. **DO NOT modify `passes/__init__.py`** — it is complete.
8. **DELETE `context_refinery/triage.py`** (the monolith) after all implementations are done.
9. Every `raise NotImplementedError(...)` message tells you exactly which lines of `triage.py` to reference.

## Source File
The monolithic source is `context_refinery/triage.py` (681 lines). Read it FIRST. All code to extract is in this file unless noted as NEW.

## File-by-file Instructions

### `terminal.py` — 3 functions to implement
| Function | Source | Notes |
|----------|--------|-------|
| `getch()` | triage.py lines 89-117 | Copy verbatim. Uses the module-level `console` already defined. |
| `getline(prompt)` | triage.py lines 120-139 | Copy verbatim. |
| `getnum(prompt)` | triage.py lines 142-161 | Copy verbatim. |

### `writers.py` — 6 functions to implement
| Function | Source | Notes |
|----------|--------|-------|
| `parse_file(filepath)` | triage.py lines 166-186 | Copy verbatim. |
| `preview(filepath)` | triage.py lines 189-205 | Copy verbatim. |
| `write_frontmatter(filepath, frontmatter, body)` | triage.py lines 208-229 | Copy verbatim. Add `"related"` to `field_order` list after `"projects"`. |
| `write_related_section(body, related_filenames)` | **NEW** | See spec below. |
| `gather_files(directory)` | triage.py lines 232-236 | Copy verbatim. |
| `make_record(filepath, frontmatter)` | triage.py lines 241-249 | Copy verbatim. Add `"related": [str(r) for r in (frontmatter.get("related") or [])]` to the returned dict. |

**`write_related_section` spec:**
```python
def write_related_section(body, related_filenames):
    # If body already has a ## Related section, replace its content.
    # Otherwise append it.
    # Format:
    #   ## Related
    #   - [[filename-one]]
    #   - [[filename-two]]
    #
    # related_filenames are already without .md extension.
    # Return the updated body string.
```

### `passes/status.py` — 2 methods to implement
The class `StatusPass` and constants `STATUSES`, `STATUS_COLORS` are already defined.

| Method | Source | Notes |
|--------|--------|-------|
| `print_legend()` | triage.py lines 254-263 | Copy the console.print call. Use `self` — no arguments needed. |
| `process_file(record, index, total)` | triage.py lines 314-347 | Adapt the inner loop of `status_phase`. Show filename + preview via `writers.preview()`. Use `getch()` from terminal module. Return `False` on `q`, `True` otherwise. **Important**: `Ctrl+C` (`\x03`) → `sys.exit(0)`. `s` → keep current, return `True`. |

### `passes/doctype.py` — 2 methods to implement
| Method | Source | Notes |
|--------|--------|-------|
| `print_legend()` | triage.py lines 266-276 | Copy the console.print call. |
| `process_file(record, index, total)` | triage.py lines 360-387 | Same pattern as StatusPass. Return `False` on `q`, `True` otherwise. |

### `passes/tags.py` — 2 methods to implement
| Method | Source | Notes |
|--------|--------|-------|
| `print_legend()` | triage.py lines 279-289 | Copy. Reference `PRESET_TAGS` (already defined in the file). |
| `process_file(record, index, total)` | triage.py lines 399-446 | Multi-select toggle. `t` = custom tag via `getline()`. Enter/space = done with file (return `True`). `q` = done with all (return `False`). |

### `passes/projects.py` — 2 methods to implement
| Method | Source | Notes |
|--------|--------|-------|
| `print_legend()` | triage.py lines 292-301 | Copy. Reference `PRESET_PROJECTS` (already defined). |
| `process_file(record, index, total)` | triage.py lines 458-498 | Same toggle pattern as tags. |

### `passes/links.py` — 2 methods to implement (NEW)
The class `LinksPass` already has `__init__(self, all_records)`.

| Method | Source | Notes |
|--------|--------|-------|
| `print_legend()` | **NEW** | Print: `[number] toggle link  [enter/space] done  [q] quit  [/] filter` |
| `process_file(record, index, total)` | **NEW** | See spec below. |

**LinksPass.process_file spec:**
1. Build candidate list = `self._all_records` minus current record
2. If >20 candidates, show filter prompt: `Type to filter, or press Enter to show all:`
3. Display numbered list of candidates (basename of filepath)
4. User types a number to toggle that candidate in/out of `record["related"]`
5. Show current selections after each toggle
6. Enter/space = done with file, return `True`
7. `q` = done with all files, return `False`
8. Store selected filenames WITHOUT .md extension in `record["related"]` (list of strings)

### `review.py` — 2 functions to implement
| Function | Source | Notes |
|----------|--------|-------|
| `review_phase(records, active_passes)` | triage.py lines 502-583 | Adapt to use DYNAMIC columns from `active_passes`. For each pass in `active_passes`, add a column named `pass.name` and populate with `pass.get_display_value(record)`. The `#` and `File` columns are always present. `r` re-edit should let user pick a pass to re-edit (not hardcoded to status+doctype). |
| `execute_writes(records)` | triage.py lines 586-617 | Copy and add: if `record.get("related")`, update `frontmatter["related"] = record["related"]` and `body = write_related_section(body, record["related"])`. |

### `runner.py` — 3 functions to implement
| Function | Source | Notes |
|----------|--------|-------|
| `show_menu()` | **NEW** | Display menu (see scaffold docstring), read one keypress, return list of pass CLASSES. E.g., `[1]` → `[StatusPass, DocTypePass, TagsPass, ProjectsPass, LinksPass]`. `[7]` Custom: show numbered list of passes, let user toggle, enter to confirm. `q` → return empty list. |
| `run_passes(records, pass_classes)` | **NEW** | For each class: instantiate (LinksPass gets `all_records=records`), print Rule header, print legend, iterate records calling `process_file`. Collect instances into list, return them. |
| `main()` | triage.py lines 622-677 | Adapt: parse args same way, build records same way, then call `show_menu()` → `run_passes()` → `review_phase()` → `execute_writes()`. If menu returns empty, quit. |

## Final Step
After all implementations are complete:
- **DELETE** `context_refinery/triage.py` (the monolith)
- Verify that `python3 -c "from context_refinery.triage import main"` succeeds

## Verification Checklist
Before submitting your PR, verify:
- [ ] `context_refinery/triage.py` has been DELETED
- [ ] `context_refinery/triage/__init__.py` exists and exports `main`
- [ ] `context_refinery/triage/__main__.py` exists
- [ ] No `raise NotImplementedError` remains in any file under `context_refinery/triage/`
- [ ] `python3 -c "from context_refinery.triage import main"` succeeds
- [ ] No new files were created beyond the scaffold
- [ ] No new dependencies were added

## Tests
Add `tests/test_triage_modular.py`:
1. `test_write_related_section_new` — body without ## Related → appended
2. `test_write_related_section_replace` — body with existing ## Related → replaced
3. `test_make_record_includes_related` — verify related field in record
4. `test_frontmatter_roundtrip` — parse → modify → write → parse gives same result
5. `test_pass_interface` — verify StatusPass, DocTypePass, TagsPass, ProjectsPass, LinksPass all have name, print_legend, process_file, get_display_value

## Key files to reference (don't modify except as instructed)
- `context_refinery/triage.py` — the source of truth (READ this, then DELETE it)
- `docs/01-taxonomy.md` — valid values for status, doc_type
- `docs/02-target-output.md` — field ordering

## Do NOT
- Create any new files beyond `tests/test_triage_modular.py`
- Change function signatures in the scaffold
- Add dependencies beyond rich and pyyaml
- Keep `context_refinery/triage.py` — it MUST be deleted
- Use async/await — this is a synchronous terminal tool
- Modify files outside `context_refinery/triage/` and `tests/`
