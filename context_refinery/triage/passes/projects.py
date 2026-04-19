"""Projects pass — multi-select project assignment with toggle.

Extracted from context_refinery/triage.py lines 448-498 (projects_phase).
"""

import sys
import os
from context_refinery.triage.passes.base import TriagePass
from context_refinery.triage.terminal import console, getch, getline, KEYS

PRESET_PROJECTS = [
    "context-refinery", "bdr-project", "water-and-stone",
    "socialxp", "smb-ops-hub", "cim",
]

PAGE_SIZE = 9


def normalize_projects(projects):
    """Keep preset projects in a stable order, then preserve custom projects."""
    seen = set()
    normalized = []

    for proj in PRESET_PROJECTS:
        if proj in projects and proj not in seen:
            normalized.append(proj)
            seen.add(proj)

    for proj in projects:
        if proj not in seen:
            normalized.append(proj)
            seen.add(proj)

    return normalized


def page_items(page_index):
    start = page_index * PAGE_SIZE
    end = start + PAGE_SIZE
    return PRESET_PROJECTS[start:end]


class ProjectsPass(TriagePass):

    @property
    def name(self) -> str:
        return "PROJECTS"

    def print_legend(self, page_index: int = 0) -> None:
        """Print the project keypress legend."""
        page = page_items(page_index)
        total_pages = max(1, (len(PRESET_PROJECTS) + PAGE_SIZE - 1) // PAGE_SIZE)
        parts = []
        for i, proj in enumerate(page):
            key = str(i + 1)
            parts.append(f"[bold][{key}][/bold] {proj}")
        console.print(f"  [dim]page {page_index + 1}/{total_pages}[/dim]")
        for i in range(0, len(parts), 3):
            console.print("  " + "  ".join(parts[i:i + 3]))
        console.print(
            "\n  [bold][t][/bold] type custom  "
            "[bold]s[/bold] skip  "
            "[bold][enter/space][/bold] done with projects  "
            "[bold][q][/bold] done with all files  "
            "[bold][←/→][/bold] prev/next page\n"
        )

    def process_file(self, record: dict, index: int, total: int) -> bool:
        """Toggle projects for one file. t=custom, enter/space=done, q=quit all.

        Returns True to continue, False if user pressed q.
        """
        name = os.path.basename(record["filepath"])
        record["projects"] = normalize_projects(list(record["projects"]))
        page_index = 0

        while True:
            console.print(f"[dim][{index}/{total}][/dim]  [bold yellow]{name}[/bold yellow]  [dim]projects: {record['projects']}[/dim]")
            self.print_legend(page_index)

            ch = getch()

            if ch == "\x03":
                console.print("\n[red]Hard abort — nothing saved.[/red]")
                sys.exit(0)

            if ch.lower() == "q":
                return False

            if ch.lower() == "s":
                console.print(f"         [dim]→ skipped (keeping {record['projects']})[/dim]")
                return True

            if ch == "LEFT":
                page_index = (page_index - 1) % max(1, (len(PRESET_PROJECTS) + PAGE_SIZE - 1) // PAGE_SIZE)
                continue

            if ch == "RIGHT":
                page_index = (page_index + 1) % max(1, (len(PRESET_PROJECTS) + PAGE_SIZE - 1) // PAGE_SIZE)
                continue

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

            visible_projects = page_items(page_index)
            if ch in {str(i + 1) for i in range(len(visible_projects))}:
                idx = int(ch) - 1
                proj = visible_projects[idx]
                if proj in record["projects"]:
                    record["projects"].remove(proj)
                    console.print(f"         [red]- {proj}[/red]")
                else:
                    record["projects"].append(proj)
                    console.print(f"         [green]+ {proj}[/green]")
                record["projects"] = normalize_projects(record["projects"])

    def get_display_value(self, record: dict) -> str:
        projects = record.get("projects", [])
        return ", ".join(projects[:3]) if projects else "—"
