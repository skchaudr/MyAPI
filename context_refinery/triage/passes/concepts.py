"""Concepts pass — assign reusable [[WikiLink]] concept links.

The concepts field is the graph layer: reusable ideas that link multiple notes.
Stored as a YAML list of strings, e.g. ['[[React]]', '[[Client Work]]'].
"""

import sys
import os
from context_refinery.triage.passes.base import TriagePass
from context_refinery.triage.terminal import console, getch, getline

MIN_CONCEPTS = 1


class ConceptsPass(TriagePass):

    @property
    def name(self) -> str:
        return "CONCEPTS"

    def print_legend(self) -> None:
        console.print(
            "  [bold][t][/bold] add concept  "
            "[bold][1-9][/bold] remove by number  "
            "[bold][s][/bold] skip  "
            "[bold][enter/space][/bold] done  "
            "[bold][q][/bold] quit all\n"
        )

    def process_file(self, record: dict, index: int, total: int) -> bool:
        name = os.path.basename(record["filepath"])

        if "concepts" not in record:
            record["concepts"] = []

        while True:
            concepts = record["concepts"]
            console.print(f"[dim][{index}/{total}][/dim]  [bold yellow]{name}[/bold yellow]  [dim]concepts: {concepts}[/dim]")
            self.print_legend()

            for i, c in enumerate(concepts, 1):
                console.print(f"  [dim][{i}][/dim] [magenta]{c}[/magenta]")

            ch = getch()

            if ch == "\x03":
                console.print("\n[red]Hard abort — nothing saved.[/red]")
                sys.exit(0)

            if ch.lower() == "q":
                return False

            if ch.lower() == "s":
                console.print(f"         [dim]→ skipped (keeping {concepts})[/dim]")
                return True

            if ch in ("\n", "\r", " "):
                if len(concepts) < MIN_CONCEPTS:
                    console.print(f"         [yellow]add at least {MIN_CONCEPTS} concept[/yellow]")
                    continue
                console.print(f"         [dim]→ concepts: {concepts}[/dim]")
                return True

            if ch.lower() == "t":
                raw = getline("  Concept name:").strip()
                if raw:
                    link = f"[[{raw}]]"
                    if link not in concepts:
                        concepts.append(link)
                        console.print(f"         [green]+ {link}[/green]")
                continue

            if ch in {str(i) for i in range(1, len(concepts) + 1)}:
                idx = int(ch) - 1
                removed = concepts.pop(idx)
                console.print(f"         [red]- {removed}[/red]")

    def get_display_value(self, record: dict) -> str:
        concepts = record.get("concepts", [])
        return ", ".join(concepts[:5]) if concepts else "—"
