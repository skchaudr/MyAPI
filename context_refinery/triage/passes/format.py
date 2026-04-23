"""Format pass — classify how the note is used via single keypress (V3 schema).

V3 formats: note / reference / howto / log
"""

import sys
import os
from context_refinery.triage.passes.base import TriagePass
from context_refinery.triage.terminal import console, getch

FORMAT_VALUES = {
    "1": "note",
    "2": "reference",
    "3": "howto",
    "4": "log",
}

FORMAT_COLORS = {
    "1": "green",
    "2": "blue",
    "3": "cyan",
    "4": "yellow",
}


class FormatPass(TriagePass):

    @property
    def name(self) -> str:
        return "FORMAT"

    def print_legend(self) -> None:
        console.print(
            "  [bold][1][/bold] [green]note[/green]  "
            "[bold][2][/bold] [blue]reference[/blue]  "
            "[bold][3][/bold] [cyan]howto[/cyan]  "
            "[bold][4][/bold] [yellow]log[/yellow]  "
            "[bold][s][/bold] skip  "
            "[bold][q][/bold] done\n"
        )

    def process_file(self, record: dict, index: int, total: int) -> bool:
        name = os.path.basename(record["filepath"])
        current = record["format"]

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

            if ch in FORMAT_VALUES:
                fmt = FORMAT_VALUES[ch]
                color = FORMAT_COLORS[ch]
                record["format"] = fmt
                console.print(f"         → [{color}]{fmt}[/{color}]")
                return True

    def get_display_value(self, record: dict) -> str:
        return record.get("format", "note")
