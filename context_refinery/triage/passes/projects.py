"""Projects pass — multi-select project assignment with toggle.

Extracted from context_refinery/triage.py lines 448-498 (projects_phase).
"""

from context_refinery.triage.passes.base import TriagePass
from context_refinery.triage.terminal import console, getch, getline

PRESET_PROJECTS = [
    "context-refinery", "bdr-project", "water-and-stone",
    "socialxp", "smb-ops-hub", "cim",
]


class ProjectsPass(TriagePass):

    @property
    def name(self) -> str:
        return "PROJECTS"

    def print_legend(self) -> None:
        """Print the project keypress legend."""
        raise NotImplementedError("JULES: Copy from triage.py lines 292-301")

    def process_file(self, record: dict, index: int, total: int) -> bool:
        """Toggle projects for one file. t=custom, enter/space=done, q=quit all.

        Returns True to continue, False if user pressed q.
        """
        raise NotImplementedError("JULES: Adapt from triage.py lines 458-498")

    def get_display_value(self, record: dict) -> str:
        projects = record.get("projects", [])
        return ", ".join(projects[:3]) if projects else "—"
