"""Links pass — relate notes to each other via [[wiki-links]].

NEW pass (not extracted from triage.py). Modeled on propertiesWizardV2.js behavior.
See project-docs/jules-spec-modular-triage-system.md for full requirements.
"""

from context_refinery.triage.passes.base import TriagePass
from context_refinery.triage.terminal import console, getch, getline

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
            "  [bold][number][/bold] toggle link  "
            "[bold][enter/space][/bold] done  "
            "[bold][q][/bold] quit  "
            "[bold][/][/bold] filter\n"
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
        import os
        import sys
        from context_refinery.triage.terminal import console, getch, getline

        name = os.path.basename(record["filepath"])
        name_no_ext = os.path.splitext(name)[0]
        if "related" not in record:
            record["related"] = []
        current = list(record["related"])

        candidates = [os.path.splitext(os.path.basename(r["filepath"]))[0] for r in self._all_records if r["filepath"] != record["filepath"]]
        filtered_candidates = candidates

        console.print(f"[dim][{index+1}/{total}][/dim]  [bold yellow]{name}[/bold yellow]  [dim]related: {current}[/dim]")

        if len(candidates) > 20:
            query = getline("Type to filter, or press Enter to show all:")
            if query:
                filtered_candidates = [c for c in candidates if query.lower() in c.lower()]

        while True:
            console.print()
            for i, cand in enumerate(filtered_candidates):
                color = "green" if cand in record["related"] else "white"
                console.print(f"  [{i+1}] [{color}]{cand}[/{color}]")

            console.print(f"\n[dim]Currently selected: {record['related']}[/dim]")

            while True:
                ch = getch()

                if ch == "\x03":
                    console.print("\n[red]Hard abort — nothing saved.[/red]")
                    sys.exit(0)

                if ch.lower() == "q":
                    console.print(f"\n[dim]Stopping links pass[/dim]")
                    return False

                if ch in ("\n", "\r", " "):
                    console.print(f"         [dim]→ related: {record['related']}[/dim]")
                    return True

                if ch == "/":
                    query = getline("Type to filter, or press Enter to show all:")
                    if query:
                        filtered_candidates = [c for c in candidates if query.lower() in c.lower()]
                    else:
                        filtered_candidates = candidates
                    break

                # Support multi-digit numbers by reading a line if user pressed a digit
                # Wait, terminal.py provides getnum or we can just read chars
                # Let's try reading a full line with getnum? No, the spec says "User types a number to toggle"
                # If there are >9 candidates we must read multiple chars or require enter.
                # Actually, getline might be better here for numbers. Let's capture characters until Enter if they are digits.
                # Or just use getline("Number:") if they type a digit.
                if ch.isdigit():
                    num_str = ch
                    sys.stdout.write(ch)
                    sys.stdout.flush()
                    while True:
                        next_ch = getch()
                        if next_ch in ("\n", "\r", " "):
                            sys.stdout.write("\n")
                            sys.stdout.flush()
                            break
                        if next_ch.isdigit():
                            num_str += next_ch
                            sys.stdout.write(next_ch)
                            sys.stdout.flush()
                        # handle backspace for robust input
                        elif next_ch in ("\x08", "\x7f"):
                            if len(num_str) > 0:
                                num_str = num_str[:-1]
                                sys.stdout.write("\b \b")
                                sys.stdout.flush()

                    if num_str:
                        idx = int(num_str) - 1
                        if 0 <= idx < len(filtered_candidates):
                            cand = filtered_candidates[idx]
                            if cand in record["related"]:
                                record["related"].remove(cand)
                                console.print(f"         [red]- {cand}[/red]")
                            else:
                                record["related"].append(cand)
                                console.print(f"         [green]+ {cand}[/green]")
                        break

    def get_display_value(self, record: dict) -> str:
        related = record.get("related", [])
        return ", ".join(related[:3]) if related else "—"
