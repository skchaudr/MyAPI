"""Runner — interactive menu + orchestrator for triage passes.

This is the main entry point. Presents a menu to select passes,
runs them in order, then hands off to review.
"""

import os
import sys

from context_refinery.triage.terminal import console, getch, getnum
from context_refinery.triage.writers import parse_file, gather_files, make_record
from context_refinery.triage.passes import StatusPass, DocTypePass, TagsPass, ProjectsPass, LinksPass
from context_refinery.triage.review import review_phase, execute_writes

try:
    from rich.rule import Rule
except ImportError:
    print("Please run: pip install rich")
    exit(1)


def show_menu():
    """Display the triage console menu. Returns list of pass classes to run.

    Menu options:
      [1] Full pipeline (status → doc_type → tags → projects → links → review)
      [2] Status only
      [3] Doc type only
      [4] Tags only
      [5] Projects only
      [6] Links only
      [7] Custom (pick passes)
      [q] Quit
    """
    while True:
        console.print(Rule("[bold cyan]CONTEXT REFINERY — TRIAGE TOOL[/bold cyan]"))
        console.print("  [bold][1][/bold] Full pipeline (status → doc type → tags → projects → links)")
        console.print("  [bold][2][/bold] Status only")
        console.print("  [bold][3][/bold] Doc type only")
        console.print("  [bold][4][/bold] Tags only")
        console.print("  [bold][5][/bold] Projects only")
        console.print("  [bold][6][/bold] Links only")
        console.print("  [bold][7][/bold] Custom pipeline")
        console.print("  [bold][q][/bold] Quit\n")

        ch = getch()

        if ch == "\x03" or ch.lower() == "q":
            return []

        if ch == "1":
            return [StatusPass, DocTypePass, TagsPass, ProjectsPass, LinksPass]
        elif ch == "2":
            return [StatusPass]
        elif ch == "3":
            return [DocTypePass]
        elif ch == "4":
            return [TagsPass]
        elif ch == "5":
            return [ProjectsPass]
        elif ch == "6":
            return [LinksPass]
        elif ch == "7":
            console.print("\n[yellow]Select passes to run (e.g., 134 for status, tags, projects):[/yellow]")
            console.print("  1=Status, 2=DocType, 3=Tags, 4=Projects, 5=Links")

            custom_passes = []
            while True:
                c = getch()
                if c == "\r" or c == "\n":
                    break
                if c == "1" and StatusPass not in custom_passes:
                    custom_passes.append(StatusPass)
                    console.print("1", end="", style="bold green")
                elif c == "2" and DocTypePass not in custom_passes:
                    custom_passes.append(DocTypePass)
                    console.print("2", end="", style="bold green")
                elif c == "3" and TagsPass not in custom_passes:
                    custom_passes.append(TagsPass)
                    console.print("3", end="", style="bold green")
                elif c == "4" and ProjectsPass not in custom_passes:
                    custom_passes.append(ProjectsPass)
                    console.print("4", end="", style="bold green")
                elif c == "5" and LinksPass not in custom_passes:
                    custom_passes.append(LinksPass)
                    console.print("5", end="", style="bold green")

            console.print("\n")
            if custom_passes:
                return custom_passes


def run_passes(records, pass_classes):
    """Instantiate and run each pass over the records.

    For each pass class:
    1. Instantiate it (LinksPass needs all_records kwarg)
    2. Print a Rich Rule with the pass name
    3. Call pass.print_legend()
    4. For each record, call pass.process_file(record, index, total)
    5. If process_file returns False (user quit), stop this pass

    Returns list of active TriagePass instances (for dynamic review columns).
    """
    active_instances = []

    for cls in pass_classes:
        if cls == LinksPass:
            instance = cls(records)
        else:
            instance = cls()

        active_instances.append(instance)

        console.print()
        console.print(Rule(f"[bold cyan]PHASE — {instance.name}[/bold cyan]"))
        instance.print_legend()

        total = len(records)
        for i, rec in enumerate(records, 1):
            if not instance.process_file(rec, i, total):
                console.print(f"\n[dim]Stopping {instance.name} pass early.[/dim]")
                break

    return active_instances


def main():
    """Entry point — parse args, load files, show menu, run passes, review.

    Usage:
      python3 -m context_refinery.triage [directory]
      python3 -m context_refinery.triage file1.md file2.md ...

    Same CLI interface as the original triage.py.
    """
    # Accept file paths as args, or a directory as first arg
    if len(sys.argv) > 1:
        target = sys.argv[1]
        if os.path.isdir(target):
            files = gather_files(target)
        else:
            files = [f for f in sys.argv[1:] if f.endswith(".md") and os.path.exists(f)]
    else:
        console.print("[bold]Usage:[/bold]")
        console.print("  python3 -m context_refinery.triage [directory]")
        console.print("  python3 -m context_refinery.triage file1.md file2.md ...")
        return

    if not files:
        console.print("[bold green]No .md files found — nothing to triage.[/bold green]")
        return

    console.print(f"\n[dim]Loaded [bold]{len(files)}[/bold] file(s)  •  "
                  f"Ctrl+C = hard abort  •  q = done early  •  s = skip file[/dim]\n")

    # Build records from existing frontmatter
    records = []
    for f in files:
        try:
            fm, _ = parse_file(f)
            records.append(make_record(f, fm))
        except Exception as e:
            console.print(f"[red]Skipping {os.path.basename(f)}: {e}[/red]")

    if not records:
        console.print("[dim]No valid files to triage.[/dim]")
        return

    pass_classes = show_menu()
    if not pass_classes:
        console.print("\n[dim]Exiting.[/dim]")
        return

    active_instances = run_passes(records, pass_classes)

    confirmed = review_phase(records, active_instances)
    if not confirmed:
        return

    execute_writes(records)
    console.print("\n[bold green]All done.[/bold green]\n")
