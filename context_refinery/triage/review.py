import sys
import os
from rich.console import Console
from rich.table import Table
from rich.rule import Rule
from .terminal import getch, getnum
from .passes.status import STATUSES
from .passes.doctype import DOC_TYPES

console = Console()

def review_phase(records, active_passes):
    """Show summary table, confirm, write frontmatter."""
    while True:
        console.print()
        console.print(Rule("[bold cyan]PHASE — REVIEW[/bold cyan]"))

        table = Table(show_header=True, header_style="bold magenta", box=None, padding=(0, 1))
        table.add_column("#", style="dim", width=4, no_wrap=True)
        table.add_column("File", no_wrap=False, max_width=35)

        for p in active_passes:
            table.add_column(p.name, no_wrap=False)

        for idx, rec in enumerate(records, 1):
            name = os.path.basename(rec["filepath"])

            row = [str(idx), name]
            for p in active_passes:
                row.append(p.get_display_value(rec))

            table.add_row(*row)

        console.print(table)
        console.print()
        console.print(
            "  [bold green][y][/bold green] Write to files   "
            "[bold red][n][/bold red] Cancel   "
            "[bold yellow][r][/bold yellow] Re-edit a file"
        )
        console.print("[dim]Waiting for y, n, or r...[/dim]", end=" ")

        ch = getch()
        console.print(ch)

        if ch == "\x03" or ch.lower() == "n":
            console.print("\n[red]Cancelled — no files modified.[/red]")
            return False

        if ch.lower() == "y":
            return True

        if ch.lower() == "r":
            num = getnum(f"Re-edit which file? (1–{len(records)})")
            if num is None or not (1 <= num <= len(records)):
                console.print("[dim]Invalid number.[/dim]")
                continue

            rec = records[num - 1]
            name = os.path.basename(rec["filepath"])
            console.print(f"\n[yellow]Re-editing #{num}: {name}[/yellow]")

            for p in active_passes:
                console.print(f"[dim]{p.name}:[/dim]")
                p.print_legend()

                # Custom re-edit loops for status/doctype for brevity like original
                if p.name == "MATURITY STATUS":
                    while True:
                        sch = getch()
                        if sch.lower() == "q" or sch == "\x03":
                            break
                        if sch in STATUSES:
                            rec["status"] = STATUSES[sch]
                            console.print(f"  → {STATUSES[sch]}")
                            break
                elif p.name == "DOCUMENT TYPE":
                    while True:
                        dch = getch()
                        if dch.lower() == "q" or dch == "\x03":
                            break
                        if dch in DOC_TYPES:
                            rec["doc_type"] = DOC_TYPES[dch]
                            console.print(f"  → {DOC_TYPES[dch]}")
                            break
                else:
                    # Rerun the pass for this single file
                    p.process_file(rec, 0, 1, records)

            continue
