"""Status pass — assign maturity level via single keypress.

Extracted from context_refinery/triage.py lines 304-347 (status_phase).
"""

from context_refinery.triage.passes.base import TriagePass
from context_refinery.triage.terminal import console, getch

# Taxonomy from docs/01-taxonomy.md
STATUSES = {
    "1": "mature",
    "2": "incubating",
    "3": "scratchpad",
    "4": "deprecated",
    "5": "reference",
}

STATUS_COLORS = {
    "1": "green",
    "2": "cyan",
    "3": "yellow",
    "4": "red",
    "5": "blue",
}


class StatusPass(TriagePass):

    @property
    def name(self) -> str:
        return "MATURITY STATUS"

    def print_legend(self) -> None:
        """Print the status keypress legend."""
        raise NotImplementedError("JULES: Copy from triage.py lines 254-263")

    def process_file(self, record: dict, index: int, total: int) -> bool:
        """Assign status to one file. s=skip, q=done, 1-5=set status.

        Returns True to continue, False if user pressed q.
        """
        raise NotImplementedError("JULES: Adapt from triage.py lines 314-347")

    def get_display_value(self, record: dict) -> str:
        return record.get("status", "scratchpad")
