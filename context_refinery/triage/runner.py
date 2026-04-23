"""Runner — interactive menu + orchestrator for triage passes.

This is the main entry point. Presents a menu to select passes,
runs them in order, then hands off to review.
"""

import json
import os
import sys
from pathlib import Path

from context_refinery.triage.terminal import console, getch, getnum
from context_refinery.triage.writers import parse_file, gather_files, make_record
from context_refinery.triage.passes import TypePass, StatusPass, ConceptsPass, TagsPass, LinksPass
from context_refinery.triage.passes.project import ProjectPass
from context_refinery.triage.passes.v4schema import V4SchemaPass
from context_refinery.triage.review import review_phase, execute_writes

try:
    from rich.rule import Rule
except ImportError:
    print("Please run: pip install rich")
    exit(1)


MENU_ITEMS = [
    ("1", "V4 Owner Pass (type → project/status → area → concepts → tags → related)", [V4SchemaPass]),
    ("2", "Type only", [TypePass]),
    ("3", "Project only", [ProjectPass]),
    ("4", "Status only", [StatusPass]),
    ("5", "Concepts only", [ConceptsPass]),
    ("6", "Tags only", [TagsPass]),
    ("7", "Related only", [LinksPass]),
    ("9", "Custom pipeline", None),
]

PREFILL_FIELDS = {"type", "status", "area", "project", "tags"}


def load_queue_files(queue_json: str, vault_root: str, confidences: set[str]) -> list[str]:
    """Load file paths from a normalizer JSON report."""
    root = Path(vault_root).expanduser()
    data = json.loads(Path(queue_json).read_text(encoding="utf-8"))
    files = []
    for item in data:
        if item.get("confidence") not in confidences:
            continue
        rel_path = item.get("path")
        if not rel_path:
            continue
        path = root / rel_path
        if path.exists() and path.suffix == ".md":
            files.append(str(path))
    return files


def load_queue_suggestions(queue_json: str, vault_root: str, confidences: set[str]) -> dict[str, dict]:
    """Load normalizer suggestions keyed by absolute file path."""
    root = Path(vault_root).expanduser()
    data = json.loads(Path(queue_json).read_text(encoding="utf-8"))
    suggestions = {}
    for item in data:
        if item.get("confidence") not in confidences:
            continue
        rel_path = item.get("path")
        if not rel_path:
            continue
        path = root / rel_path
        if path.exists() and path.suffix == ".md":
            suggestions[str(path)] = item.get("suggested") or {}
    return suggestions


def prefill_record_from_suggestion(record: dict, suggestion: dict) -> list[str]:
    """Apply safe normalizer suggestions to the in-memory review record."""
    changed = []
    for field in PREFILL_FIELDS:
        if field not in suggestion:
            continue
        value = suggestion[field]
        if value in (None, "", []):
            continue
        if record.get(field) != value:
            record[field] = value
            changed.append(field)
    return sorted(changed)


def parse_args(argv: list[str]) -> tuple[list[str], str | None, str | None, set[str]]:
    """Parse the small CLI surface while preserving positional file support."""
    positional = []
    queue_json = None
    vault_root = None
    confidences = {"medium", "review"}

    i = 0
    while i < len(argv):
        arg = argv[i]
        if arg == "--queue-json" and i + 1 < len(argv):
            queue_json = argv[i + 1]
            i += 2
        elif arg == "--vault-root" and i + 1 < len(argv):
            vault_root = argv[i + 1]
            i += 2
        elif arg == "--confidence" and i + 1 < len(argv):
            confidences = {part.strip() for part in argv[i + 1].split(",") if part.strip()}
            i += 2
        else:
            positional.append(arg)
            i += 1

    return positional, queue_json, vault_root, confidences


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
    selected = 0

    while True:
        console.print(Rule("[bold cyan]CONTEXT REFINERY — TRIAGE TOOL[/bold cyan]"))
        console.print("[dim]Use arrow keys or 1-8, then Enter to choose.[/dim]\n")
        for idx, (key, label, _) in enumerate(MENU_ITEMS):
            prefix = "[bold green]>[/bold green] " if idx == selected else "  "
            console.print(f"{prefix}[bold][{key}][/bold] {label}")
        console.print("  [bold][q][/bold] Quit\n")

        ch = getch()

        if ch == "\x03" or ch.lower() == "q":
            return []

        if ch in ("UP", "LEFT"):
            selected = (selected - 1) % len(MENU_ITEMS)
            continue
        if ch in ("DOWN", "RIGHT"):
            selected = (selected + 1) % len(MENU_ITEMS)
            continue

        if ch in ("\r", "\n", " "):
            key, _, passes = MENU_ITEMS[selected]
            if key == "9":
                ch = "9"
            elif passes is not None:
                return passes

        if ch == "1":
            return MENU_ITEMS[0][2]
        elif ch == "2":
            return MENU_ITEMS[1][2]
        elif ch == "3":
            return MENU_ITEMS[2][2]
        elif ch == "4":
            return MENU_ITEMS[3][2]
        elif ch == "5":
            return MENU_ITEMS[4][2]
        elif ch == "6":
            return MENU_ITEMS[5][2]
        elif ch == "7":
            return MENU_ITEMS[6][2]
        elif ch == "8":
            return MENU_ITEMS[7][2]
        elif ch == "9":
            console.print("\n[yellow]Select passes (e.g., 246 for type+concepts+tags):[/yellow]")
            console.print("  1=V4OwnerPass  2=Type  3=Project  4=Status  5=Concepts  6=Tags  7=Related")

            custom_passes = []
            while True:
                c = getch()
                if c == "\r" or c == "\n":
                    break
                if c == "1" and V4SchemaPass not in custom_passes:
                    custom_passes.append(V4SchemaPass)
                    console.print("1", end="", style="bold green")
                elif c == "2" and TypePass not in custom_passes:
                    custom_passes.append(TypePass)
                    console.print("2", end="", style="bold green")
                elif c == "3" and ProjectPass not in custom_passes:
                    custom_passes.append(ProjectPass)
                    console.print("3", end="", style="bold green")
                elif c == "4" and StatusPass not in custom_passes:
                    custom_passes.append(StatusPass)
                    console.print("4", end="", style="bold green")
                elif c == "5" and ConceptsPass not in custom_passes:
                    custom_passes.append(ConceptsPass)
                    console.print("5", end="", style="bold green")
                elif c == "6" and TagsPass not in custom_passes:
                    custom_passes.append(TagsPass)
                    console.print("6", end="", style="bold green")
                elif c == "7" and LinksPass not in custom_passes:
                    custom_passes.append(LinksPass)
                    console.print("7", end="", style="bold green")

            console.print("\n")
            if custom_passes:
                return custom_passes


def run_passes(records, pass_classes, vault_root=None):
    """Instantiate and run each pass over the records.

    For each pass class:
    1. Instantiate it (LinksPass needs all_records kwarg; V3SchemaPass needs vault_root)
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
        elif cls == V4SchemaPass:
            instance = cls(vault_root)
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
    if any(arg in ("-h", "--help") for arg in sys.argv[1:]):
        console.print("[bold]Usage:[/bold]")
        console.print("  python3 -m context_refinery.triage [directory]")
        console.print("  python3 -m context_refinery.triage file1.md file2.md ...")
        console.print("  python3 -m context_refinery.triage --queue-json report.json --vault-root /path/to/vault --confidence medium,review")
        console.print("\n[dim]Pass a directory to triage every .md file under it recursively.[/dim]")
        return

    positional, queue_json, vault_root_arg, confidences = parse_args(sys.argv[1:])

    # Accept file paths as args, or a directory as first arg
    if queue_json:
        vault_root = vault_root_arg or os.getcwd()
        files = load_queue_files(queue_json, vault_root, confidences)
        queue_suggestions = load_queue_suggestions(queue_json, vault_root, confidences)
        target = vault_root
    elif positional:
        queue_suggestions = {}
        target = positional[0]
        if os.path.isdir(target):
            files = gather_files(target)
        else:
            files = [f for f in positional if f.endswith(".md") and os.path.exists(f)]
    else:
        queue_suggestions = {}
        console.print("[bold]Usage:[/bold]")
        console.print("  python3 -m context_refinery.triage [directory]")
        console.print("  python3 -m context_refinery.triage file1.md file2.md ...")
        console.print("  python3 -m context_refinery.triage --queue-json report.json --vault-root /path/to/vault --confidence medium,review")
        return

    if not files:
        console.print("[bold green]No .md files found — nothing to triage.[/bold green]")
        return

    console.print(f"\n[dim]Loaded [bold]{len(files)}[/bold] file(s)  •  "
                  f"Ctrl+C = hard abort  •  q = done early  •  s = skip file[/dim]\n")

    # Build records from existing frontmatter
    records = []
    prefilled_count = 0
    for f in files:
        try:
            fm, _ = parse_file(f)
            record = make_record(f, fm)
            changed = prefill_record_from_suggestion(record, queue_suggestions.get(f, {}))
            if changed:
                record["_prefilled_fields"] = changed
                prefilled_count += 1
            records.append(record)
        except Exception as e:
            console.print(f"[red]Skipping {os.path.basename(f)}: {e}[/red]")

    if not records:
        console.print("[dim]No valid files to triage.[/dim]")
        return

    if prefilled_count:
        console.print(f"[dim]Prefilled normalizer suggestions for {prefilled_count} file(s).[/dim]\n")

    pass_classes = show_menu()
    if not pass_classes:
        console.print("\n[dim]Exiting.[/dim]")
        return

    vault_root = target if os.path.isdir(target) else os.path.dirname(os.path.abspath(files[0]))
    active_instances = run_passes(records, pass_classes, vault_root=vault_root)

    confirmed = review_phase(records, active_instances)
    if not confirmed:
        return

    execute_writes(records)
    console.print("\n[bold green]All done.[/bold green]\n")
