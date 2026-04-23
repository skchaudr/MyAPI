"""Project pass — assign singular project wikilink (V4 schema).

V4 uses a singular `project: "[[--Project Name]]"` field.
Optional — Enter/space skips if no project applies.
"""

import sys
import os
from context_refinery.triage.passes.base import TriagePass
from context_refinery.triage.terminal import console, getch, getline
from context_refinery.triage.writers import preview


class ProjectPass(TriagePass):

    @property
    def name(self) -> str:
        return "PROJECT"

    def print_legend(self) -> None:
        console.print(
            "  [bold][t][/bold] type project name  "
            "[bold][c][/bold] clear  "
            "[bold][Enter/Space][/bold] skip (no project)  "
            "[bold][s][/bold] skip file  "
            "[bold][q][/bold] done\n"
        )

    def process_file(self, record: dict, index: int, total: int) -> bool:
        name = os.path.basename(record["filepath"])
        hint = preview(record["filepath"])
        current = record.get("project", "")

        console.print(f"[dim][{index}/{total}][/dim]  [bold yellow]{name}[/bold yellow]  [dim]project: {current or '—'}[/dim]")
        if hint:
            console.print(f"         [dim]{hint}[/dim]")
        self.print_legend()

        while True:
            ch = getch()

            if ch == "\x03":
                sys.exit(0)

            if ch.lower() == "q":
                return False

            if ch.lower() == "s":
                console.print(f"         [dim]→ skipped (keeping {current or '—'})[/dim]")
                return True

            if ch in ("\r", "\n", " "):
                console.print(f"         [dim]→ no project[/dim]")
                return True

            if ch.lower() == "c":
                record["project"] = ""
                console.print(f"         [red]cleared[/red]")
                return True

            if ch.lower() == "t":
                raw = getline("  Project name:").strip()
                if raw:
                    name_clean = raw.strip("[]")
                    if not name_clean.startswith("--"):
                        name_clean = f"--{name_clean}"
                    record["project"] = f"[[{name_clean}]]"
                    console.print(f"         → [green]{record['project']}[/green]")
                    return True

    def get_display_value(self, record: dict) -> str:
        return record.get("project", "") or "—"
