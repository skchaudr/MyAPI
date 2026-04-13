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
        """Print the project keypress legend with numbered presets."""
        parts = []
        for i, proj in enumerate(PRESET_PROJECTS):
            parts.append(f"[bold][{i+1}][/bold] {proj}")
        console.print("  " + "  ".join(parts))
        console.print(
            "\n  [bold][t][/bold] type custom  "
            "[bold][enter/space][/bold] done with projects  "
            "[bold][q][/bold] done with all files\n"
        )

    def process_file(self, record: dict, index: int, total: int) -> bool:
        """Toggle projects for one file. t=custom, enter/space=done, q=quit all.

        Returns True to continue, False if user pressed q.
        """
        import os
        import sys
        from context_refinery.triage.terminal import console, getch, getline

        name = os.path.basename(record["filepath"])
        current = list(record["projects"])

        console.print(f"[dim][{index+1}/{total}][/dim]  [bold yellow]{name}[/bold yellow]  [dim]projects: {current}[/dim]")

        while True:
            ch = getch()

            if ch == "\x03":
                console.print("\n[red]Hard abort — nothing saved.[/red]")
                sys.exit(0)

            if ch.lower() == "q":
                console.print(f"\n[dim]Stopping projects pass[/dim]")
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
        return ", ".join(projects[:3]) if projects else "—"
