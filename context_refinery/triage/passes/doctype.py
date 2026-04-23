"""Type pass — classify note type via single keypress (V3 schema).

V3 types: project / area / resource / concept / log (+ rare: task, utility)
Default: resource (the safe fallback per schema spec).
"""

import sys
import os
from context_refinery.triage.passes.base import TriagePass
from context_refinery.triage.terminal import console, getch

TYPE_VALUES = {
    "1": "project",
    "2": "area",
    "3": "resource",
    "4": "concept",
    "5": "event",
    "6": "periodic",
}

TYPE_COLORS = {
    "1": "green",
    "2": "cyan",
    "3": "blue",
    "4": "magenta",
    "5": "yellow",
    "6": "dim",
}

# Backward-compat alias so old imports don't break
DOC_TYPES = TYPE_VALUES
DOC_TYPE_COLORS = TYPE_COLORS


class TypePass(TriagePass):

    @property
    def name(self) -> str:
        return "TYPE"

    def print_legend(self) -> None:
        console.print(
            "  [bold][1][/bold] [green]project[/green]  "
            "[bold][2][/bold] [cyan]area[/cyan]  "
            "[bold][3][/bold] [blue]resource[/blue]  "
            "[bold][4][/bold] [magenta]concept[/magenta]  "
            "[bold][5][/bold] [yellow]event[/yellow]  "
            "[bold][6][/bold] [dim]periodic[/dim]  "
            "[bold][s][/bold] skip  "
            "[bold][q][/bold] done\n"
        )

    def process_file(self, record: dict, index: int, total: int) -> bool:
        """Assign type to one file. s=skip, q=done, 1-7=set type.

        Returns True to continue, False if user pressed q.
        """
        name = os.path.basename(record["filepath"])
        current = record["type"]

        console.print(f"[dim][{index}/{total}][/dim]  [bold yellow]{name}[/bold yellow]  [dim]({current})[/dim]")
        self.print_legend()

        while True:
            ch = getch()

            if ch == "\x03":
                console.print("\n[red]Hard abort — nothing saved.[/red]")
                sys.exit(0)

            if ch.lower() == "q":
                return False

            if ch.lower() == "s":
                console.print(f"         [dim]→ skipped (keeping {current})[/dim]")
                return True

            if ch in TYPE_VALUES:
                t = TYPE_VALUES[ch]
                color = TYPE_COLORS[ch]
                record["type"] = t
                console.print(f"         → [{color}]{t}[/{color}]")
                return True

    def get_display_value(self, record: dict) -> str:
        return record.get("type", "resource")


# Keep old name as alias so runner/tests that still reference DocTypePass don't break
DocTypePass = TypePass
