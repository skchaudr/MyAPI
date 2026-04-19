"""Links pass — relate notes to each other via [[wiki-links]].

NEW pass (not extracted from triage.py). Modeled on propertiesWizardV2.js behavior.
See project-docs/jules-spec-modular-triage-system.md for full requirements.
"""

import sys
import os
from context_refinery.triage.passes.base import TriagePass
from context_refinery.triage.terminal import console, getch, getline, KEYS

class LinksPass(TriagePass):
    """Link related notes to each other.

    For each file:
    1. Show filename + preview
    2. Present numbered list of all OTHER .md files in the working set
    3. User toggles related notes by number
    4. Enter/space = done with this file
    5. On write: store in frontmatter `related` field + inject ## Related section

    For large file sets (>20 files), show a filter prompt before the list.
    """

    def __init__(self, all_records: list[dict]):
        """Store reference to all records for cross-linking.

        Args:
            all_records: The full list of triage records (used to show link candidates).
        """
        self._all_records = all_records

    @property
    def name(self) -> str:
        return "RELATED LINKS"

    def print_legend(self) -> None:
        """Print the links legend — number to toggle, enter/space to confirm."""
        console.print(
            "  [bold][0-9/a-z][/bold] toggle link  "
            "[bold][/][/bold] filter\n"
            "  [bold]s[/bold] skip  "
            "[bold][enter/space][/bold] done  "
            "[bold][q][/bold] quit\n"
        )

    def process_file(self, record: dict, index: int, total: int) -> bool:
        """Link related notes for one file. Number=toggle, enter/space=done, q=quit.

        Should:
        - Show candidates (all records except current)
        - If >20 candidates, show filter prompt first
        - Toggle by number, show current selections
        - Store selected filenames (without .md) in record["related"]

        Returns True to continue, False if user pressed q.
        """
        name = os.path.basename(record["filepath"])

        candidates = [rec for rec in self._all_records if rec["filepath"] != record["filepath"]]

        # Build candidate list = self._all_records minus current record
        # If >20 candidates, automatically show filter prompt

        filter_str = ""
        if len(candidates) > 20:
            filter_str = getline("  Filter candidates (leave blank for all):").strip().lower()

        filtered_candidates = []
        for cand in candidates:
            cand_name = os.path.basename(cand["filepath"])
            if not filter_str or filter_str in cand_name.lower():
                filtered_candidates.append(cand)

        # Limit to max available keys (36)
        if len(filtered_candidates) > len(KEYS):
            filtered_candidates = filtered_candidates[:len(KEYS)]

        if "related" not in record:
            record["related"] = []

        while True:
            console.print(f"[dim][{index}/{total}][/dim]  [bold yellow]{name}[/bold yellow]  [dim]related: {record['related']}[/dim]")
            self.print_legend()

            for i, cand in enumerate(filtered_candidates):
                cand_name = os.path.splitext(os.path.basename(cand["filepath"]))[0]
                marker = "[green]x[/green]" if cand_name in record["related"] else "[dim] [/dim]"
                console.print(f"  [{KEYS[i]}] {marker} {cand_name}")

            ch = getch()

            if ch == "\x03":
                console.print("\n[red]Hard abort — nothing saved.[/red]")
                sys.exit(0)

            if ch.lower() == "q":
                return False

            if ch.lower() == "s":
                console.print(f"         [dim]→ skipped (keeping {record['related']})[/dim]")
                return True

            if ch in ("\n", "\r", " "):
                console.print(f"         [dim]→ related: {record['related']}[/dim]")
                return True

            if ch == "/":
                filter_str = getline("  Filter candidates (leave blank for all):").strip().lower()
                filtered_candidates = []
                for cand in candidates:
                    cand_name = os.path.basename(cand["filepath"])
                    if not filter_str or filter_str in cand_name.lower():
                        filtered_candidates.append(cand)
                if len(filtered_candidates) > len(KEYS):
                    filtered_candidates = filtered_candidates[:len(KEYS)]
                continue

            idx = None
            if ch in KEYS:
                idx = KEYS.index(ch)
            if idx is not None and 0 <= idx < len(filtered_candidates):
                cand = filtered_candidates[idx]
                cand_name = os.path.splitext(os.path.basename(cand["filepath"]))[0]
                if cand_name in record["related"]:
                    record["related"].remove(cand_name)
                    console.print(f"         [red]- {cand_name}[/red]")
                else:
                    record["related"].append(cand_name)
                    console.print(f"         [green]+ {cand_name}[/green]")

    def get_display_value(self, record: dict) -> str:
        related = record.get("related", [])
        return ", ".join(related[:3]) if related else "—"
