"""Status pass — assign maturity level via single keypress.

Extracted from context_refinery/triage.py lines 304-347 (status_phase).
"""

import sys
import os
from context_refinery.triage.passes.base import TriagePass
from context_refinery.triage.terminal import console, getch
from context_refinery.triage.writers import preview

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
        console.print(
            "  [bold][1][/bold] [green]mature[/green]  "
            "[bold][2][/bold] [cyan]incubating[/cyan]  "
            "[bold][3][/bold] [yellow]scratchpad[/yellow]  "
            "[bold][4][/bold] [red]deprecated[/red]  "
            "[bold][5][/bold] [blue]reference[/blue]  "
            "[bold][s][/bold] skip  "
            "[bold][q][/bold] done\n"
        )

    def process_file(self, record: dict, index: int, total: int) -> bool:
        """Assign status to one file. s=skip, q=done, 1-5=set status.

        Returns True to continue, False if user pressed q.
        """
        name = os.path.basename(record["filepath"])
        hint = preview(record["filepath"])
        current = record["status"]

        console.print(f"[dim][{index}/{total}][/dim]  [bold yellow]{name}[/bold yellow]  [dim]({current})[/dim]")
        if hint:
            console.print(f"         [dim]{hint}[/dim]")

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

            if ch in STATUSES:
                status = STATUSES[ch]
                color = STATUS_COLORS[ch]
                record["status"] = status
                console.print(f"         → [{color}]{status}[/{color}]")
                return True

    def get_display_value(self, record: dict) -> str:
        return record.get("status", "scratchpad")
