"""Links pass — relate notes to each other via [[wiki-links]].

NEW pass (not extracted from triage.py). Modeled on propertiesWizardV2.js behavior.
See project-docs/jules-spec-modular-triage-system.md for full requirements.
"""

from context_refinery.triage.passes.base import TriagePass
from context_refinery.triage.terminal import console, getch, getline

class LinksPass(TriagePass):
    """Link related notes to each other.

    For each file:
    1. Show filename + preview
    2. Present numbered list of all OTHER .md files in the working set
    3. User toggles related notes by number
    4. Enter/space = done with this file
    5. On write: store in frontmatter `related` field + inject ## Related section

    For large file sets (>20 files), show a filter prompt before the list.
    """

    def __init__(self, all_records: list[dict]):
        """Store reference to all records for cross-linking.

        Args:
            all_records: The full list of triage records (used to show link candidates).
        """
        self._all_records = all_records

    @property
    def name(self) -> str:
        return "RELATED LINKS"

    def print_legend(self) -> None:
        """Print the links legend — number to toggle, enter/space to confirm."""
        raise NotImplementedError("JULES: Implement per spec")

    def process_file(self, record: dict, index: int, total: int) -> bool:
        """Link related notes for one file. Number=toggle, enter/space=done, q=quit.

        Should:
        - Show candidates (all records except current)
        - If >20 candidates, show filter prompt first
        - Toggle by number, show current selections
        - Store selected filenames (without .md) in record["related"]

        Returns True to continue, False if user pressed q.
        """
        raise NotImplementedError("JULES: Implement per spec")

    def get_display_value(self, record: dict) -> str:
        related = record.get("related", [])
        return ", ".join(related[:3]) if related else "—"
