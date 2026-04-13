"""Runner — interactive menu + orchestrator for triage passes.

This is the main entry point. Presents a menu to select passes,
runs them in order, then hands off to review.
"""

import os
import sys

from context_refinery.triage.terminal import console, getch
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
    console.print()
    console.print(Rule("[bold cyan]CONTEXT REFINERY — TRIAGE[/bold cyan]"))
    console.print("  [bold][1][/bold] Full pipeline")
    console.print("  [bold][2][/bold] Status only")
    console.print("  [bold][3][/bold] Doc type only")
    console.print("  [bold][4][/bold] Tags only")
    console.print("  [bold][5][/bold] Projects only")
    console.print("  [bold][6][/bold] Links only")
    console.print("  [bold][7][/bold] Custom (pick passes)")
    console.print("  [bold][q][/bold] Quit")

    while True:
        ch = getch()
        if ch == "\x03" or ch.lower() == "q":
            return []

        if ch == "1": return [StatusPass, DocTypePass, TagsPass, ProjectsPass, LinksPass]
        if ch == "2": return [StatusPass]
        if ch == "3": return [DocTypePass]
        if ch == "4": return [TagsPass]
        if ch == "5": return [ProjectsPass]
        if ch == "6": return [LinksPass]

        if ch == "7":
            available_passes = [StatusPass, DocTypePass, TagsPass, ProjectsPass, LinksPass]
            selected = set()
            while True:
                console.print()
                console.print("[cyan]Toggle passes to run:[/cyan]")
                for i, cls in enumerate(available_passes):
                    status = "[green][x][/green]" if i in selected else "[dim][ ][/dim]"
                    console.print(f"  [{i+1}] {status} {cls().name}")

                console.print("\n[dim]Press number to toggle, Enter to confirm, q to cancel[/dim]")

                ch2 = getch()
                if ch2 == "\x03" or ch2.lower() == "q":
                    return []

                if ch2 in ("\n", "\r"):
                    if not selected:
                        console.print("[dim]No passes selected, returning to main menu...[/dim]")
                        break
                    return [available_passes[i] for i in sorted(list(selected))]

                if ch2.isdigit():
                    idx = int(ch2) - 1
                    if 0 <= idx < len(available_passes):
                        if idx in selected:
                            selected.remove(idx)
                        else:
                            selected.add(idx)


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
            instance = cls(all_records=records)
        else:
            instance = cls()

        active_instances.append(instance)

        console.print()
        console.print(Rule(f"[bold cyan]PHASE — {instance.name}[/bold cyan]"))
        instance.print_legend()

        for index, record in enumerate(records):
            cont = instance.process_file(record, index, len(records))
            if not cont:
                break

    return active_instances


def main():
    """Entry point — parse args, load files, show menu, run passes, review.

    Usage:
      python3 -m context_refinery.triage [directory]
      python3 -m context_refinery.triage file1.md file2.md ...

    Same CLI interface as the original triage.py.
    """
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
        console.print("[dim]Nothing to do.[/dim]")
        return

    active_passes = run_passes(records, pass_classes)

    if not active_passes:
        return

    confirmed = review_phase(records, active_passes)
    if not confirmed:
        return

    execute_writes(records)
    console.print("\n[bold green]All done.[/bold green]\n")
