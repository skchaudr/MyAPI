import sys
import os
from rich.console import Console
from rich.rule import Rule
from .base import TriagePass
from ..terminal import getch, getline

console = Console()

PRESET_PROJECTS = [
    "context-refinery", "bdr-project", "water-and-stone",
    "socialxp", "smb-ops-hub", "cim",
]

class ProjectsPass(TriagePass):
    @property
    def name(self) -> str:
        return "PROJECTS"

    def print_legend(self) -> None:
        console.print("[dim]Toggle projects by number, press [t] for custom, [Enter/Space] when done[/dim]")
        for i, proj in enumerate(PRESET_PROJECTS):
            console.print(f"  [{i+1}] {proj}", end="")
            if (i + 1) % 4 == 0:
                console.print()
        if len(PRESET_PROJECTS) % 4 != 0:
            console.print()

    def process_file(self, record: dict, index: int, total: int, all_records: list = None) -> bool:
        if index == 0:
            console.print()
            console.print(Rule(f"[bold cyan]PHASE — {self.name}[/bold cyan]"))
            self.print_legend()

        name = os.path.basename(record["filepath"])
        if "projects" not in record:
            record["projects"] = []

        current = list(record["projects"])

        console.print(f"[dim][{index+1}/{total}][/dim]  [bold yellow]{name}[/bold yellow]  [dim]projects: {current}[/dim]")

        while True:
            ch = getch()

            if ch == "\x03":
                console.print("\n[red]Hard abort — nothing saved.[/red]")
                sys.exit(0)

            if ch.lower() == "q":
                console.print(f"\n[dim]Stopping {self.name.lower()} pass[/dim]")
                return False

            if ch in ("\n", "\r", " "):
                console.print(f"         [dim]→ projects: {record['projects']}[/dim]")
                return True

            if ch.lower() == "t":
                custom = getline("  Project:")
                if custom:
                    proj = custom.strip()
                    if proj and proj not in record["projects"]:
                        record["projects"].append(proj)
                        console.print(f"         [green]+ {proj}[/green]")
                continue

            if ch.isdigit() and ch != "0":
                idx = int(ch) - 1
                if 0 <= idx < len(PRESET_PROJECTS):
                    proj = PRESET_PROJECTS[idx]
                    if proj in record["projects"]:
                        record["projects"].remove(proj)
                        console.print(f"         [red]- {proj}[/red]")
                    else:
                        record["projects"].append(proj)
                        console.print(f"         [green]+ {proj}[/green]")

    def get_display_value(self, record: dict) -> str:
        projects = record.get("projects", [])
        return ", ".join(projects[:3]) or "[dim]—[/dim]"
