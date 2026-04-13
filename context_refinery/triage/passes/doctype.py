"""Doc type pass — classify document type via single keypress.

Extracted from context_refinery/triage.py lines 350-387 (doctype_phase).
"""

from context_refinery.triage.passes.base import TriagePass
from context_refinery.triage.terminal import console, getch

# Taxonomy from docs/01-taxonomy.md
DOC_TYPES = {
    "1": "note",
    "2": "conversation",
    "3": "spec",
    "4": "log",
    "5": "article",
    "6": "other",
}

DOC_TYPE_COLORS = {
    "1": "green",
    "2": "magenta",
    "3": "cyan",
    "4": "yellow",
    "5": "blue",
    "6": "dim",
}


class DocTypePass(TriagePass):

    @property
    def name(self) -> str:
        return "DOC TYPE"

    def print_legend(self) -> None:
        """Print the doc type keypress legend."""
        raise NotImplementedError("JULES: Copy from triage.py lines 266-276")

    def process_file(self, record: dict, index: int, total: int) -> bool:
        """Assign doc_type to one file. s=skip, q=done, 1-6=set type.

        Returns True to continue, False if user pressed q.
        """
        raise NotImplementedError("JULES: Adapt from triage.py lines 360-387")

    def get_display_value(self, record: dict) -> str:
        return record.get("doc_type", "note")
