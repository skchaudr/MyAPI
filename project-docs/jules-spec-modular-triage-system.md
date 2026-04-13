# Jules Task: Modular Triage System

## Summary
Refactor the CLI triage tool (`context_refinery/triage.py`) into a modular system with a single entry point that dispatches to interchangeable passes. Each pass uses the same interaction pattern (single keypress, Rich formatting, q=quit, s=skip) but operates on different metadata dimensions.

## Reference Implementations
Study these existing scripts to match the UX exactly:
- `context_refinery/triage.py` — the triage tool we just built (based on triage_inbox.py)
- `/Users/saboor/Obsidian/SoloDeveloper/09 Utilities/Scripts/triage_inbox.py` — the original folder routing tool (4-phase: route → review → execute → subfolder)
- `/Users/saboor/Obsidian/SoloDeveloper/09 Utilities/Scripts/propertiesWizardV2.js` — shows how related notes are linked via frontmatter `related` field + `## Related` body section with `[[wiki-links]]`

## Architecture

### Directory structure
```
context_refinery/
  triage/
    __init__.py          # exports main() entry point
    __main__.py          # allows `python3 -m context_refinery.triage`
    runner.py            # interactive menu + orchestrator
    passes/
      __init__.py
      base.py            # abstract base class for all passes
      status.py          # maturity status assignment
      doctype.py         # doc_type classification
      tags.py            # tag assignment (presets + custom)
      projects.py        # project assignment (presets + custom)
      links.py           # related note linking
    review.py            # review table + confirm + re-edit
    terminal.py          # getch(), getline(), getnum() helpers
    writers.py           # write_frontmatter(), write_related_section()
```

### Base pass interface (`passes/base.py`)
```python
from abc import ABC, abstractmethod

class TriagePass(ABC):
    """All passes share the same interaction contract."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Display name for the pass (e.g., 'MATURITY STATUS')."""

    @abstractmethod
    def print_legend(self) -> None:
        """Print the keypress legend for this pass."""

    @abstractmethod
    def process_file(self, record: dict, index: int, total: int, all_records: list = None) -> bool:
        """
        Process a single file. Returns True to continue, False to stop (q pressed).
        Mutates record in-place.
        """

    @abstractmethod
    def get_display_value(self, record: dict) -> str:
        """Return the current value for this pass (shown in review table)."""
```

### Runner (`runner.py`)
The entry point presents an interactive menu:
```
Context Refinery — Triage Console

  [1] Full pipeline (status → doc_type → tags → projects → links → review)
  [2] Status only
  [3] Doc type only
  [4] Tags only
  [5] Projects only
  [6] Links only
  [7] Custom (pick passes)
  [q] Quit
```

Each option runs the selected passes in order, then the review phase, then writes.

### Pass details

#### Status pass (`status.py`)
Move from `triage.py` Phase 1. Single keypress: 1-5 maps to maturity status taxonomy. `s` = skip, `q` = done.

#### Doc type pass (`doctype.py`)
Move from `triage.py` Phase 2. Single keypress: 1-6 maps to doc_type taxonomy. `s` = skip, `q` = done.

#### Tags pass (`tags.py`)
Move from `triage.py` Phase 3. Multi-select toggle from presets + `t` for custom. Enter/space = next file.

Preset tags (configurable list):
```python
PRESET_TAGS = [
    "ai", "web-dev", "devops", "python", "react", "typescript",
    "obsidian", "khoj", "infrastructure", "career", "learning",
    "neovim", "git", "api", "database", "design",
]
```

#### Projects pass (`projects.py`)
Move from `triage.py` Phase 4. Same toggle pattern as tags.

Preset projects (configurable list):
```python
PRESET_PROJECTS = [
    "context-refinery", "bdr-project", "water-and-stone",
    "socialxp", "smb-ops-hub", "cim",
]
```

#### Links pass (`links.py`) — NEW
This is the most complex pass. Modeled on `propertiesWizardV2.js` behavior:

1. For each file, show its name + preview
2. Present a list of all OTHER .md files in the working set (numbered)
3. User toggles related notes by number (like tags)
4. Enter/space = done with this file
5. On write:
   - Store selected filenames in frontmatter `related` field as a YAML list
   - Inject/update a `## Related` section at the bottom of the note body:
     ```markdown
     ## Related
     - [[note-title-one]]
     - [[note-title-two]]
     ```
   - If `## Related` section already exists, replace its content
   - Wiki-link format: `[[filename-without-extension]]`

For large file sets (>20 files), show a search/filter prompt before the numbered list:
```
  Type to filter, or press Enter to show all:
```

### Review phase (`review.py`)
Move from `triage.py` Phase 5. Show a Rich table with columns for each active pass. `y` = write, `n` = cancel, `r` = re-edit a file.

The review table columns should be dynamic based on which passes were run. Only show columns for active passes.

### Writer (`writers.py`)
Move `write_frontmatter()` and `parse_file()` from `triage.py`. Add:
- `write_related_section(body, related_filenames) -> str` — injects or replaces `## Related` section
- Field ordering per `docs/02-target-output.md`: id, title, source, created_at, author, status, doc_type, tags, projects, related

### Terminal helpers (`terminal.py`)
Move `getch()`, `getline()`, `getnum()` from `triage.py`. These are shared across all passes.

## Migration
- Delete the monolithic `context_refinery/triage.py` after the module is working
- The entry point should work the same way: `python3 -m context_refinery.triage [directory|files...]`
- All existing functionality must be preserved — this is a refactor, not a rewrite

## Key constraints
- Python 3 stdlib + `rich` + `pyyaml` only (no new dependencies)
- Single keypress input everywhere — never require Enter for option selection
- `q` always means "soft quit, save progress so far"
- `Ctrl+C` always means "hard abort, nothing saved"
- `s` means "skip this file" in single-select passes
- Enter/space means "done with this file" in multi-select passes (tags, projects, links)
- Taxonomy values MUST match `docs/01-taxonomy.md` exactly

## Testing
- Test each pass independently with mock records
- Test the runner dispatches correctly
- Test `write_related_section` injects and replaces correctly
- Test frontmatter round-trip (parse → modify → write → parse gives same result)

## Do NOT
- Change the taxonomy values
- Add dependencies beyond rich and pyyaml
- Use any async/await patterns — this is a synchronous terminal tool
- Move or modify the Obsidian vault scripts (they are reference only)
- Break the `python3 -m context_refinery.triage` entry point
