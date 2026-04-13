import sys
import os
from rich.console import Console
from rich.rule import Rule
from .base import TriagePass
from ..terminal import getch, getline

console = Console()

class LinksPass(TriagePass):
    @property
    def name(self) -> str:
        return "RELATED LINKS"

    def print_legend(self) -> None:
        console.print("[dim]Toggle related notes by number, [Enter/Space] when done[/dim]")

    def process_file(self, record: dict, index: int, total: int, all_records: list = None) -> bool:
        if index == 0:
            console.print()
            console.print(Rule(f"[bold cyan]PHASE — {self.name}[/bold cyan]"))

        name = os.path.basename(record["filepath"])
        if "related" not in record:
            record["related"] = []

        # Get all other files
        all_other_records = [r for r in (all_records or []) if r["filepath"] != record["filepath"]]
        if not all_other_records:
            console.print(f"[dim][{index+1}/{total}][/dim]  [bold yellow]{name}[/bold yellow]  [dim]No other files to link.[/dim]")
            return True

        console.print(f"\n[dim][{index+1}/{total}][/dim]  [bold yellow]{name}[/bold yellow]")

        # Show search/filter prompt for >20 files
        filtered_records = all_other_records
        if len(all_other_records) > 20:
            filter_query = getline("  Type to filter, or press Enter to show all:").lower()
            if filter_query:
                filtered_records = [r for r in all_other_records if filter_query in os.path.basename(r["filepath"]).lower()]

        if not filtered_records:
            console.print("  [dim]No files matched filter.[/dim]")
            return True

        # Present the list
        self.print_legend()
        for i, r in enumerate(filtered_records):
            other_name = os.path.splitext(os.path.basename(r["filepath"]))[0]
            console.print(f"  [{i+1}] {other_name}")

        console.print(f"  [dim]current related: {record['related']}[/dim]")

        # We keep track of number strings being typed
        num_str = ""

        while True:
            ch = getch()

            if ch == "\x03":
                console.print("\n[red]Hard abort — nothing saved.[/red]")
                sys.exit(0)

            if ch.lower() == "q":
                console.print(f"\n[dim]Stopping {self.name.lower()} pass[/dim]")
                return False

            if ch in ("\n", "\r", " "):
                if num_str:
                    # process the number that was typed
                    idx = int(num_str) - 1
                    num_str = ""
                    if 0 <= idx < len(filtered_records):
                        other_name = os.path.splitext(os.path.basename(filtered_records[idx]["filepath"]))[0]
                        if other_name in record["related"]:
                            record["related"].remove(other_name)
                            console.print(f"         [red]- {other_name}[/red]")
                        else:
                            record["related"].append(other_name)
                            console.print(f"         [green]+ {other_name}[/green]")
                    continue
                else:
                    console.print(f"         [dim]→ related: {record['related']}[/dim]")
                    return True

            if ch.isdigit():
                num_str += ch

    def get_display_value(self, record: dict) -> str:
        related = record.get("related", [])
        return f"{len(related)} links" if related else "[dim]—[/dim]"
