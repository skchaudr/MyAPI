import sys
import os
from rich.console import Console
from rich.rule import Rule
from .base import TriagePass
from ..terminal import getch

console = Console()

STATUSES = {
    "1": "mature",
    "2": "incubating",
    "3": "scratchpad",
    "4": "deprecated",
    "5": "reference"
}

STATUS_COLORS = {
    "1": "bold green",
    "2": "bold yellow",
    "3": "bold red",
    "4": "dim",
    "5": "bold blue"
}

class StatusPass(TriagePass):
    @property
    def name(self) -> str:
        return "MATURITY STATUS"

    def print_legend(self) -> None:
        console.print(
            "  [1] [bold green]mature[/bold green]       "
            "[2] [bold yellow]incubating[/bold yellow]   "
            "[3] [bold red]scratchpad[/bold red]   "
            "[4] [dim]deprecated[/dim]   "
            "[5] [bold blue]reference[/bold blue]"
        )

    def process_file(self, record: dict, index: int, total: int, all_records: list = None) -> bool:
        if index == 0:
            console.print()
            console.print(Rule(f"[bold cyan]PHASE — {self.name}[/bold cyan]"))
            self.print_legend()

        name = os.path.basename(record["filepath"])
        current = record.get("status", "scratchpad")

        status_key = next((k for k, v in STATUSES.items() if v == current), None)
        c_color = STATUS_COLORS.get(status_key, "white") if status_key else "white"

        console.print(f"[dim][{index+1}/{total}][/dim]  [bold yellow]{name}[/bold yellow]  [dim]current: [{c_color}]{current}[/{c_color}][/dim]", end=" ")

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
                if "status" not in record:
                    record["status"] = current
                return True

            if ch in STATUSES:
                val = STATUSES[ch]
                color = STATUS_COLORS[ch]
                record["status"] = val
                console.print(f"  → [{color}]{val}[/{color}]")
                return True

    def get_display_value(self, record: dict) -> str:
        current = record.get("status", "scratchpad")
        status_key = next((k for k, v in STATUSES.items() if v == current), None)
        s_color = STATUS_COLORS.get(status_key, "white") if status_key else "white"
        return f"[{s_color}]{current}[/{s_color}]"
