import sys
import os
import glob
import uuid
import datetime
from rich.console import Console

from .terminal import getch, getline
from .writers import parse_file, write_frontmatter, write_related_section
from .review import review_phase
from .passes import StatusPass, DocTypePass, TagsPass, ProjectsPass, LinksPass

console = Console()

def gather_files(directory):
    """Find all .md files in directory."""
    path = os.path.join(directory, "*.md")
    return [f for f in glob.glob(path) if os.path.isfile(f)]

def make_record(filepath, frontmatter):
    """Create a working record dictionary for a file."""
    rec = {
        "filepath": filepath,
        "status": frontmatter.get("status", "scratchpad"),
        "doc_type": frontmatter.get("doc_type", "other"),
        "tags": frontmatter.get("tags", []),
        "projects": frontmatter.get("projects", []),
        "related": frontmatter.get("related", []),
    }
    return rec

def print_menu():
    console.print()
    console.print("[bold]Context Refinery — Triage Console[/bold]")
    console.print()
    console.print("  [1] Full pipeline (status → doc_type → tags → projects → links → review)")
    console.print("  [2] Status only")
    console.print("  [3] Doc type only")
    console.print("  [4] Tags only")
    console.print("  [5] Projects only")
    console.print("  [6] Links only")
    console.print("  [7] Custom (pick passes)")
    console.print("  [q] Quit")
    console.print()

def get_passes_from_choice(choice):
    all_passes = [StatusPass(), DocTypePass(), TagsPass(), ProjectsPass(), LinksPass()]
    if choice == "1":
        return all_passes
    elif choice == "2":
        return [StatusPass()]
    elif choice == "3":
        return [DocTypePass()]
    elif choice == "4":
        return [TagsPass()]
    elif choice == "5":
        return [ProjectsPass()]
    elif choice == "6":
        return [LinksPass()]
    elif choice == "7":
        console.print("[dim]Enter pass numbers separated by spaces (e.g. 1 2 5):[/dim]")
        for i, p in enumerate(all_passes, 1):
            console.print(f"  [{i}] {p.name}")
        custom = getline(">").strip().split()
        selected = []
        for c in custom:
            if c.isdigit() and 1 <= int(c) <= len(all_passes):
                selected.append(all_passes[int(c)-1])
        return selected
    return None

def execute_writes(records, active_passes):
    """Write updated metadata back to each file's YAML frontmatter."""
    written = 0
    for rec in records:
        filepath = rec["filepath"]
        try:
            frontmatter, body = parse_file(filepath)

            # Update fields based on what was run
            for p in active_passes:
                if p.name == "MATURITY STATUS":
                    frontmatter["status"] = rec["status"]
                elif p.name == "DOCUMENT TYPE":
                    frontmatter["doc_type"] = rec["doc_type"]
                elif p.name == "TAGS":
                    frontmatter["tags"] = rec["tags"]
                elif p.name == "PROJECTS":
                    frontmatter["projects"] = rec["projects"]
                elif p.name == "RELATED LINKS":
                    frontmatter["related"] = rec["related"]

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

            # Check if links pass was active to update body
            if any(p.name == "RELATED LINKS" for p in active_passes):
                body = write_related_section(body, rec["related"])

            write_frontmatter(filepath, frontmatter, body)
            written += 1
        except Exception as e:
            console.print(f"[red]Failed: {os.path.basename(filepath)}: {e}[/red]")

    console.print(f"\n[bold green]Updated {written} file(s).[/bold green]")

def run():
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

    while True:
        print_menu()
        console.print("Select an option: ", end="")
        ch = getch()
        console.print(ch)

        if ch == "\x03" or ch.lower() == "q":
            return

        passes = get_passes_from_choice(ch)
        if not passes:
            console.print("[red]Invalid selection or no passes chosen.[/red]")
            continue

        console.print(f"\n[dim]Loaded [bold]{len(records)}[/bold] file(s)  •  "
                      f"Ctrl+C = hard abort  •  q = done early  •  s = skip file[/dim]\n")

        # Run selected passes
        for p in passes:
            for i, rec in enumerate(records):
                cont = p.process_file(rec, i, len(records), records)
                if not cont:
                    break

        # Review phase
        confirmed = review_phase(records, passes)
        if confirmed:
            execute_writes(records, passes)

        console.print("\n[bold green]All done.[/bold green]\n")
        return
