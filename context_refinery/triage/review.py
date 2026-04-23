"""Review phase — summary table, confirm, re-edit, execute writes.

Extracted from context_refinery/triage.py lines 500-617.
"""

import os
import uuid
import datetime

from context_refinery.triage.terminal import console, getch, getnum
from context_refinery.triage.writers import parse_file, write_frontmatter, write_related_section
from context_refinery.triage.passes.base import TriagePass

try:
    from rich.table import Table
    from rich.rule import Rule
except ImportError:
    print("Please run: pip install rich")
    exit(1)


def review_phase(records, active_passes: list[TriagePass]):
    """Show summary table, confirm, write frontmatter.

    The table columns should be DYNAMIC — only show columns for passes
    that were actually run.

    Args:
        records: List of triage record dicts.
        active_passes: List of TriagePass instances that were run.

    Returns True if user confirmed, False if cancelled.

    Supports: y=write, n=cancel, r=re-edit a specific file.
    """
    actions = ["y", "n", "r"]
    selected = 0

    while True:
        console.print()
        console.print(Rule("[bold cyan]PHASE 5 — REVIEW[/bold cyan]"))

        table = Table(show_header=True, header_style="bold magenta", box=None, padding=(0, 1))
        table.add_column("#", style="dim", width=4, no_wrap=True)
        table.add_column("File", no_wrap=False, max_width=35)

        # Dynamic columns based on active passes
        for p in active_passes:
            table.add_column(p.name.title(), no_wrap=False, max_width=30)

        for idx, rec in enumerate(records, 1):
            name = os.path.basename(rec["filepath"])

            row = [str(idx), name]
            for p in active_passes:
                val = p.get_display_value(rec)
                if p.name == "MATURITY STATUS":
                    from context_refinery.triage.passes.status import STATUSES, STATUS_COLORS
                    status_key = next((k for k, v in STATUSES.items() if v == rec.get("status")), None)
                    s_color = STATUS_COLORS.get(status_key, "white") if status_key else "white"
                    val = f"[{s_color}]{val}[/{s_color}]"
                elif p.name == "TYPE":
                    from context_refinery.triage.passes.doctype import TYPE_VALUES, TYPE_COLORS
                    type_key = next((k for k, v in TYPE_VALUES.items() if v == rec.get("type")), None)
                    t_color = TYPE_COLORS.get(type_key, "white") if type_key else "white"
                    val = f"[{t_color}]{val}[/{t_color}]"
                elif p.name == "FORMAT":
                    from context_refinery.triage.passes.format import FORMAT_VALUES, FORMAT_COLORS
                    fmt_key = next((k for k, v in FORMAT_VALUES.items() if v == rec.get("format")), None)
                    f_color = FORMAT_COLORS.get(fmt_key, "white") if fmt_key else "white"
                    val = f"[{f_color}]{val}[/{f_color}]"
                row.append(val)

            table.add_row(*row)

        console.print(table)
        console.print()
        console.print("[dim]Use arrows or y/n/r, then Enter to choose. r re-edits one file by number.[/dim]")
        console.print(
            "  [bold green]y[/bold green] Write to files   "
            "[bold red]n[/bold red] Cancel   "
            "[bold yellow]r[/bold yellow] Re-edit a file"
        )
        for idx, label in enumerate(("Write", "Cancel", "Re-edit")):
            prefix = "[bold green]>[/bold green] " if idx == selected else "  "
            console.print(f"{prefix}{label}")
        console.print("[dim]Waiting for y, n, r, arrows, or Enter...[/dim]", end=" ")

        ch = getch()

        if ch == "\x03":
            console.print("\n[red]Cancelled — no files modified.[/red]")
            return False

        if ch in ("UP", "LEFT"):
            selected = (selected - 1) % len(actions)
            continue
        if ch in ("DOWN", "RIGHT"):
            selected = (selected + 1) % len(actions)
            continue

        if ch in ("\r", "\n", " "):
            ch = actions[selected]

        if ch.lower() == "n":
            console.print("\n[red]Cancelled — no files modified.[/red]")
            return False

        if ch.lower() == "y":
            return True

        if ch.lower() == "r":
            console.print("[dim]Re-edit means: choose a file number, then run the active passes again on that file.[/dim]")
            num = getnum(f"Re-edit which file? (1–{len(records)})")
            if num is None or not (1 <= num <= len(records)):
                console.print("[dim]Invalid number.[/dim]")
                continue

            rec = records[num - 1]
            name = os.path.basename(rec["filepath"])
            console.print(f"\n[yellow]Re-editing #{num}: {name}[/yellow]")

            # Re-run ALL active passes on this single file sequentially
            for p in active_passes:
                console.print(f"[dim]{p.name.title()}:[/dim]")
                p.print_legend()
                p.process_file(rec, num, len(records))

            continue


def execute_writes(records):
    """Write updated metadata back to each file's YAML frontmatter."""
    written = 0
    for rec in records:
        filepath = rec["filepath"]
        try:
            frontmatter, body = parse_file(filepath)

            # V4 fields
            frontmatter["type"] = rec.get("type", "resource")

            # status only for project/event
            if rec.get("type") in ("project", "event"):
                frontmatter["status"] = rec.get("status", "active")
            else:
                frontmatter.pop("status", None)

            # remove deprecated format field
            frontmatter.pop("format", None)

            if rec.get("area"):
                frontmatter["area"] = rec["area"]
            if rec.get("project"):
                frontmatter["project"] = rec["project"]
            elif "project" in frontmatter and not rec.get("project"):
                pass  # preserve existing if not explicitly cleared
            if rec.get("concepts"):
                frontmatter["concepts"] = rec["concepts"]

            frontmatter["tags"] = rec.get("tags", [])

            if "related" in rec:
                frontmatter["related"] = rec["related"]
                body = write_related_section(body, rec["related"])

            if rec.get("review_flags"):
                frontmatter["review_flags"] = rec["review_flags"]
            else:
                frontmatter.pop("review_flags", None)

            # Ensure required fields exist
            if "id" not in frontmatter:
                frontmatter["id"] = str(uuid.uuid4())
            if "title" not in frontmatter:
                frontmatter["title"] = os.path.splitext(os.path.basename(filepath))[0]
            if "created_at" not in frontmatter:
                frontmatter["created_at"] = datetime.datetime.now(datetime.timezone.utc).isoformat()

            write_frontmatter(filepath, frontmatter, body)
            written += 1
        except Exception as e:
            console.print(f"[red]Failed: {os.path.basename(filepath)}: {e}[/red]")

    console.print(f"\n[bold green]Updated {written} file(s).[/bold green]")
