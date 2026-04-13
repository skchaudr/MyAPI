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
        console.print(
            "  [bold][1][/bold] [green]note[/green]  "
            "[bold][2][/bold] [magenta]conversation[/magenta]  "
            "[bold][3][/bold] [cyan]spec[/cyan]  "
            "[bold][4][/bold] [yellow]log[/yellow]  "
            "[bold][5][/bold] [blue]article[/blue]  "
            "[bold][6][/bold] [dim]other[/dim]  "
            "[bold][s][/bold] skip  "
            "[bold][q][/bold] done\n"
        )

    def process_file(self, record: dict, index: int, total: int) -> bool:
        """Assign doc_type to one file. s=skip, q=done, 1-6=set type.

        Returns True to continue, False if user pressed q.
        """
        import os
        import sys
        from context_refinery.triage.terminal import console, getch
        from context_refinery.triage.writers import preview

        name = os.path.basename(record["filepath"])
        snippet = preview(record["filepath"])
        current = record["doc_type"]

        console.print(f"[dim][{index+1}/{total}][/dim]  [bold yellow]{name}[/bold yellow]  [dim]({current})[/dim]")
        if snippet:
            console.print(f"         [italic dim]{snippet}[/italic dim]")

        while True:
            ch = getch()

            if ch == "\x03":
                console.print("\n[red]Hard abort — nothing saved.[/red]")
                sys.exit(0)

            if ch.lower() == "q":
                console.print(f"\n[dim]Stopping doc type pass[/dim]")
                return False

            if ch.lower() == "s":
                console.print(f"         [dim]→ skipped (kept {current})[/dim]")
                return True

            if ch in DOC_TYPES:
                val = DOC_TYPES[ch]
                color = DOC_TYPE_COLORS[ch]
                record["doc_type"] = val
                console.print(f"         [dim]→[/dim] [{color}]{val}[/{color}]")
                return True

    def get_display_value(self, record: dict) -> str:
        return record.get("doc_type", "note")
