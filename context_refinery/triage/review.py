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
    while True:
        console.print()
        console.print(Rule("[bold cyan]PHASE 5 — REVIEW[/bold cyan]"))

        table = Table(show_header=True, header_style="bold magenta", box=None, padding=(0, 1))
        table.add_column("#", style="dim", width=4, no_wrap=True)
        table.add_column("File", no_wrap=False, max_width=35)

        for p in active_passes:
            table.add_column(p.name, no_wrap=False, max_width=30)

        for idx, rec in enumerate(records, 1):
            name = os.path.basename(rec["filepath"])

            row = [str(idx), name]
            for p in active_passes:
                val = p.get_display_value(rec)

                # Apply colors for StatusPass and DocTypePass
                if p.name == "MATURITY STATUS":
                    from context_refinery.triage.passes.status import STATUSES, STATUS_COLORS
                    status_key = next((k for k, v in STATUSES.items() if v == rec.get("status")), None)
                    s_color = STATUS_COLORS.get(status_key, "white") if status_key else "white"
                    val = f"[{s_color}]{val}[/{s_color}]"

                row.append(val)

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

            if not active_passes:
                console.print("[dim]No passes available to edit.[/dim]")
                continue

            console.print("Which pass to re-edit?")
            for i, p in enumerate(active_passes):
                console.print(f"  [{i+1}] {p.name}")

            p_num = getnum(f"Pass number (1-{len(active_passes)}) or Enter to skip:")
            if p_num is None or not (1 <= p_num <= len(active_passes)):
                continue

            pass_to_run = active_passes[p_num - 1]
            console.print(f"\n[cyan]Editing {pass_to_run.name} for {name}[/cyan]")
            pass_to_run.print_legend()
            pass_to_run.process_file(rec, num - 1, len(records))

def execute_writes(records):
    """Write updated metadata back to each file's YAML frontmatter.

    For each record:
    1. Parse existing frontmatter + body
    2. Update status, doc_type, tags, projects from record
    3. If record has 'related', call write_related_section() on body
    4. Ensure required fields (id, title, source, created_at, author) exist
    5. Call write_frontmatter() with field ordering per taxonomy spec
    """
    written = 0
    for rec in records:
        filepath = rec["filepath"]
        try:
            frontmatter, body = parse_file(filepath)

            # Update fields
            frontmatter["status"] = rec.get("status", frontmatter.get("status", "scratchpad"))
            frontmatter["doc_type"] = rec.get("doc_type", frontmatter.get("doc_type", "note"))
            if "tags" in rec:
                frontmatter["tags"] = rec["tags"]
            if "projects" in rec:
                frontmatter["projects"] = rec["projects"]

            if "related" in rec:
                frontmatter["related"] = rec["related"]
                body = write_related_section(body, rec["related"])

            # Ensure required fields exist
            if "id" not in frontmatter:
                frontmatter["id"] = str(uuid.uuid4())
            if "title" not in frontmatter:
                frontmatter["title"] = os.path.splitext(os.path.basename(filepath))[0]
            if "source" not in frontmatter:
                frontmatter["source"] = "obsidian"
            if "created_at" not in frontmatter:
                frontmatter["created_at"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
            if "author" not in frontmatter:
                frontmatter["author"] = "Unknown"

            write_frontmatter(filepath, frontmatter, body)
            written += 1
        except Exception as e:
            console.print(f"[red]Failed: {os.path.basename(filepath)}: {e}[/red]")

    console.print(f"\n[bold green]Updated {written} file(s).[/bold green]")
