"""Tags pass — multi-select tag assignment with toggle.

Extracted from context_refinery/triage.py lines 389-446 (tags_phase).
"""

from context_refinery.triage.passes.base import TriagePass
from context_refinery.triage.terminal import console, getch, getline

PRESET_TAGS = [
    "ai", "web-dev", "devops", "python", "react", "typescript",
    "obsidian", "khoj", "infrastructure", "career", "learning",
    "neovim", "git", "api", "database", "design",
]


class TagsPass(TriagePass):

    @property
    def name(self) -> str:
        return "TAGS"

    def print_legend(self) -> None:
        """Print the tag keypress legend with numbered/lettered presets."""
        raise NotImplementedError("JULES: Copy from triage.py lines 279-289")

    def process_file(self, record: dict, index: int, total: int) -> bool:
        """Toggle tags for one file. t=custom, enter/space=done, q=quit all.

        Returns True to continue, False if user pressed q.
        """
        raise NotImplementedError("JULES: Adapt from triage.py lines 399-446")

    def get_display_value(self, record: dict) -> str:
        tags = record.get("tags", [])
        return ", ".join(tags[:5]) if tags else "—"
