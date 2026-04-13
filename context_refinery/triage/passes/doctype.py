import sys
import os
from rich.console import Console
from rich.rule import Rule
from .base import TriagePass
from ..terminal import getch

console = Console()

DOC_TYPES = {
    "1": "conversation",
    "2": "note",
    "3": "spec",
    "4": "log",
    "5": "article",
    "6": "other"
}

class DocTypePass(TriagePass):
    @property
    def name(self) -> str:
        return "DOCUMENT TYPE"

    def print_legend(self) -> None:
        console.print(
            "  [1] conversation  [2] note  [3] spec  [4] log  [5] article  [6] other"
        )

    def process_file(self, record: dict, index: int, total: int, all_records: list = None) -> bool:
        if index == 0:
            console.print()
            console.print(Rule(f"[bold cyan]PHASE — {self.name}[/bold cyan]"))
            self.print_legend()

        name = os.path.basename(record["filepath"])
        current = record.get("doc_type", "other")

        console.print(f"[dim][{index+1}/{total}][/dim]  [bold yellow]{name}[/bold yellow]  [dim]current: {current}[/dim]", end=" ")

        while True:
            ch = getch()

            if ch == "\x03":
                console.print("\n[red]Hard abort — nothing saved.[/red]")
                sys.exit(0)

            if ch.lower() == "q":
                console.print(f"\n[dim]Stopping {self.name.lower()} pass[/dim]")
                return False

            if ch.lower() == "s":
                console.print(f"  [dim]→ skipped (kept {current})[/dim]")
                if "doc_type" not in record:
                    record["doc_type"] = current
                return True

            if ch in DOC_TYPES:
                val = DOC_TYPES[ch]
                record["doc_type"] = val
                console.print(f"  → {val}")
                return True

    def get_display_value(self, record: dict) -> str:
        return record.get("doc_type", "other")
