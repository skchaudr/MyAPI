#!/usr/bin/env python3
"""
Context Refinery — CLI Triage Tool

Keyboard-driven metadata assignment for Obsidian notes before
deploying to Khoj. Modeled on triage_inbox.py interaction pattern.

Phases:
  1. Status   — assign maturity level (single keypress)
  2. Doc Type — classify document type (single keypress)
  3. Tags     — quick-add from presets or type custom
  4. Projects — assign to project from presets or type custom
  5. Review   — table summary, confirm, write YAML frontmatter
"""

import os
import sys
import glob
import tty
import termios
import yaml
import uuid
import datetime
import copy

try:
    from rich.console import Console
    from rich.table import Table
    from rich.rule import Rule
except ImportError:
    print("Please run: pip install rich")
    exit(1)

console = Console()


# ── Taxonomy (from docs/01-taxonomy.md) ──────────────────────────────────────

STATUSES = {
    "1": "mature",
    "2": "incubating",
    "3": "scratchpad",
    "4": "deprecated",
    "5": "reference",
}

STATUS_COLORS = {
    "1": "green",
    "2": "cyan",
    "3": "yellow",
    "4": "red",
    "5": "blue",
}

DOC_TYPES = {
    "1": "note",
    "2": "conversation",
    "3": "spec",
    "4": "log",
    "5": "article",
    "6": "other",
}

DOC_TYPE_COLORS = {
    "1": "green",
    "2": "magenta",
    "3": "cyan",
    "4": "yellow",
    "5": "blue",
    "6": "dim",
}

# Common tags — extend as your vault grows
PRESET_TAGS = [
    "ai", "web-dev", "devops", "python", "react", "typescript",
    "obsidian", "khoj", "infrastructure", "career", "learning",
    "neovim", "git", "api", "database", "design",
]

# Known projects — extend as needed
PRESET_PROJECTS = [
    "context-refinery", "bdr-project", "water-and-stone",
    "socialxp", "smb-ops-hub", "cim",
]


# ── Terminal helpers (from triage_inbox.py) ──────────────────────────────────

def getch():
    """Read one keypress without Enter."""
    tty_in = None
    if sys.stdin.isatty():
        stream = sys.stdin
    else:
        try:
            tty_in = open("/dev/tty", encoding="utf-8")
            stream = tty_in
        except OSError:
            stream = sys.stdin

    if not stream.isatty():
        console.print("[red]This script needs an interactive terminal.[/red]")
        sys.exit(1)

    fd = stream.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setcbreak(fd)
        ch = stream.read(1)
    finally:
        try:
            termios.tcsetattr(fd, termios.TCSAFLUSH, old)
        except termios.error:
            pass
        if tty_in is not None:
            tty_in.close()
    return ch


def getline(prompt):
    """Read a line from the user (normal line mode)."""
    console.print(f"[bold]{prompt}[/bold] ", end="")
    tty_in = None
    try:
        if sys.stdin.isatty():
            stream = sys.stdin
        else:
            try:
                tty_in = open("/dev/tty", encoding="utf-8")
                stream = tty_in
            except OSError:
                stream = sys.stdin

        return stream.readline().strip()
    except (EOFError, OSError):
        return ""
    finally:
        if tty_in is not None:
            tty_in.close()


def getnum(prompt):
    """Read a number from the user."""
    console.print(f"\n[bold]{prompt}[/bold] ", end="")
    tty_in = None
    try:
        if sys.stdin.isatty():
            stream = sys.stdin
        else:
            try:
                tty_in = open("/dev/tty", encoding="utf-8")
                stream = tty_in
            except OSError:
                stream = sys.stdin

        return int(stream.readline().strip())
    except (ValueError, EOFError, OSError):
        return None
    finally:
        if tty_in is not None:
            tty_in.close()


# ── File helpers ─────────────────────────────────────────────────────────────

def parse_file(filepath):
    """Read a markdown file and extract frontmatter + body."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    frontmatter = {}
    body = content

    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            try:
                frontmatter = yaml.safe_load(parts[1]) or {}
                body = parts[2].strip()
            except yaml.YAMLError:
                pass

    if not isinstance(frontmatter, dict):
        frontmatter = {}

    return frontmatter, body


def preview(filepath):
    """Return first meaningful line after frontmatter."""
    try:
        with open(filepath, encoding="utf-8") as f:
            in_fm = False
            for line in f:
                s = line.strip()
                if s == "---":
                    in_fm = not in_fm
                    continue
                if in_fm:
                    continue
                if s and not s.startswith("#"):
                    return s[:90]
    except Exception:
        pass
    return ""


def write_frontmatter(filepath, frontmatter, body):
    """Write updated YAML frontmatter + body back to file."""
    # Field order per docs/02-target-output.md
    ordered = {}
    field_order = [
        "id", "title", "source", "created_at", "author",
        "status", "doc_type", "tags", "projects",
    ]
    for key in field_order:
        if key in frontmatter:
            ordered[key] = frontmatter[key]
    # Preserve any extra fields not in the standard order
    for key in frontmatter:
        if key not in ordered:
            ordered[key] = frontmatter[key]

    yaml_str = yaml.dump(ordered, default_flow_style=False, sort_keys=False, allow_unicode=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("---\n")
        f.write(yaml_str)
        f.write("---\n\n")
        f.write(body)


def gather_files(directory):
    """Gather all .md files from directory."""
    pattern = os.path.join(directory, "**", "*.md")
    files = sorted(glob.glob(pattern, recursive=True))
    return files


# ── Triage record ────────────────────────────────────────────────────────────

def make_record(filepath, frontmatter):
    """Create a triage record for a file with current metadata."""
    return {
        "filepath": filepath,
        "status": frontmatter.get("status", "scratchpad"),
        "doc_type": frontmatter.get("doc_type", "note"),
        "tags": [str(t) for t in (frontmatter.get("tags") or [])],
        "projects": [str(p) for p in (frontmatter.get("projects") or [])],
    }


# ── UI legends ───────────────────────────────────────────────────────────────

def print_status_legend():
    console.print(
        "  [bold][1][/bold] [green]mature[/green]  "
        "[bold][2][/bold] [cyan]incubating[/cyan]  "
        "[bold][3][/bold] [yellow]scratchpad[/yellow]  "
        "[bold][4][/bold] [red]deprecated[/red]  "
        "[bold][5][/bold] [blue]reference[/blue]  "
        "[bold][s][/bold] skip  "
        "[bold][q][/bold] done\n"
    )


def print_doctype_legend():
    console.print(
        "  [bold][1][/bold] [green]note[/green]  "
        "[bold][2][/bold] [magenta]conversation[/magenta]  "
        "[bold][3][/bold] [cyan]spec[/cyan]  "
        "[bold][4][/bold] [yellow]log[/yellow]  "
        "[bold][5][/bold] [blue]article[/blue]  "
        "[bold][6][/bold] [dim]other[/dim]  "
        "[bold][s][/bold] skip  "
        "[bold][q][/bold] done\n"
    )


def print_tags_legend():
    parts = []
    for i, tag in enumerate(PRESET_TAGS):
        key = str(i + 1) if i < 9 else chr(ord("a") + i - 9)
        parts.append(f"[bold][{key}][/bold] {tag}")
    console.print("  " + "  ".join(parts))
    console.print(
        "\n  [bold][t][/bold] type custom  "
        "[bold][enter/space][/bold] done with tags  "
        "[bold][q][/bold] done with all files\n"
    )


def print_projects_legend():
    parts = []
    for i, proj in enumerate(PRESET_PROJECTS):
        parts.append(f"[bold][{i+1}][/bold] {proj}")
    console.print("  " + "  ".join(parts))
    console.print(
        "\n  [bold][t][/bold] type custom  "
        "[bold][enter/space][/bold] done with projects  "
        "[bold][q][/bold] done with all files\n"
    )


# ── Phase 1: Status assignment ───────────────────────────────────────────────

def status_phase(records):
    """Assign maturity status to each file. Returns (triaged, remaining)."""
    total = len(records)
    triaged = []

    console.print(Rule("[bold cyan]PHASE 1 — MATURITY STATUS[/bold cyan]"))
    print_status_legend()

    for i, rec in enumerate(records):
        name = os.path.basename(rec["filepath"])
        hint = preview(rec["filepath"])
        current = rec["status"]

        console.print(f"[dim][{i+1}/{total}][/dim]  [bold yellow]{name}[/bold yellow]  [dim]({current})[/dim]")
        if hint:
            console.print(f"         [dim]{hint}[/dim]")

        while True:
            ch = getch()

            if ch == "\x03":
                console.print("\n[red]Hard abort — nothing saved.[/red]")
                sys.exit(0)

            if ch.lower() == "q":
                console.print(f"\n[dim]Stopping after {len(triaged)} files[/dim]")
                return triaged, records[i:]

            if ch.lower() == "s":
                console.print("         [dim]→ skipped (keeping {current})[/dim]")
                triaged.append(rec)
                break

            if ch in STATUSES:
                status = STATUSES[ch]
                color = STATUS_COLORS[ch]
                rec["status"] = status
                console.print(f"         → [{color}]{status}[/{color}]")
                triaged.append(rec)
                break

    return triaged, []


# ── Phase 2: Doc type assignment ─────────────────────────────────────────────

def doctype_phase(records):
    """Assign doc_type to each file."""
    total = len(records)

    console.print()
    console.print(Rule("[bold cyan]PHASE 2 — DOC TYPE[/bold cyan]"))
    print_doctype_legend()

    for i, rec in enumerate(records):
        name = os.path.basename(rec["filepath"])
        current = rec["doc_type"]

        console.print(f"[dim][{i+1}/{total}][/dim]  [bold yellow]{name}[/bold yellow]  [dim]({current})[/dim]")

        while True:
            ch = getch()

            if ch == "\x03":
                console.print("\n[red]Hard abort — nothing saved.[/red]")
                sys.exit(0)

            if ch.lower() == "q":
                console.print(f"\n[dim]Stopping doc type pass[/dim]")
                return

            if ch.lower() == "s":
                console.print(f"         [dim]→ skipped (keeping {current})[/dim]")
                break

            if ch in DOC_TYPES:
                dtype = DOC_TYPES[ch]
                color = DOC_TYPE_COLORS[ch]
                rec["doc_type"] = dtype
                console.print(f"         → [{color}]{dtype}[/{color}]")
                break


# ── Phase 3: Tag assignment ──────────────────────────────────────────────────

def tags_phase(records):
    """Assign tags to each file. Multi-select with toggle."""
    total = len(records)

    console.print()
    console.print(Rule("[bold cyan]PHASE 3 — TAGS[/bold cyan]"))
    print_tags_legend()

    for i, rec in enumerate(records):
        name = os.path.basename(rec["filepath"])
        current_tags = list(rec["tags"])

        console.print(f"[dim][{i+1}/{total}][/dim]  [bold yellow]{name}[/bold yellow]  [dim]tags: {current_tags}[/dim]")

        while True:
            ch = getch()

            if ch == "\x03":
                console.print("\n[red]Hard abort — nothing saved.[/red]")
                sys.exit(0)

            if ch.lower() == "q":
                console.print(f"\n[dim]Stopping tags pass[/dim]")
                return

            # Enter or space = done with this file's tags
            if ch in ("\n", "\r", " "):
                console.print(f"         [dim]→ tags: {rec['tags']}[/dim]")
                break

            # Custom tag
            if ch.lower() == "t":
                custom = getline("  Tag:")
                if custom:
                    tag = custom.lower().strip()
                    if tag and tag not in rec["tags"]:
                        rec["tags"].append(tag)
                        console.print(f"         [green]+ {tag}[/green]")
                continue

            # Preset tag toggle
            idx = None
            if ch.isdigit() and ch != "0":
                idx = int(ch) - 1
            elif ch.isalpha() and ord(ch.lower()) >= ord("a"):
                idx = ord(ch.lower()) - ord("a") + 9

            if idx is not None and 0 <= idx < len(PRESET_TAGS):
                tag = PRESET_TAGS[idx]
                if tag in rec["tags"]:
                    rec["tags"].remove(tag)
                    console.print(f"         [red]- {tag}[/red]")
                else:
                    rec["tags"].append(tag)
                    console.print(f"         [green]+ {tag}[/green]")


# ── Phase 4: Project assignment ──────────────────────────────────────────────

def projects_phase(records):
    """Assign projects to each file."""
    total = len(records)

    console.print()
    console.print(Rule("[bold cyan]PHASE 4 — PROJECTS[/bold cyan]"))
    print_projects_legend()

    for i, rec in enumerate(records):
        name = os.path.basename(rec["filepath"])
        current = list(rec["projects"])

        console.print(f"[dim][{i+1}/{total}][/dim]  [bold yellow]{name}[/bold yellow]  [dim]projects: {current}[/dim]")

        while True:
            ch = getch()

            if ch == "\x03":
                console.print("\n[red]Hard abort — nothing saved.[/red]")
                sys.exit(0)

            if ch.lower() == "q":
                console.print(f"\n[dim]Stopping projects pass[/dim]")
                return

            if ch in ("\n", "\r", " "):
                console.print(f"         [dim]→ projects: {rec['projects']}[/dim]")
                break

            if ch.lower() == "t":
                custom = getline("  Project:")
                if custom:
                    proj = custom.strip()
                    if proj and proj not in rec["projects"]:
                        rec["projects"].append(proj)
                        console.print(f"         [green]+ {proj}[/green]")
                continue

            if ch.isdigit() and ch != "0":
                idx = int(ch) - 1
                if 0 <= idx < len(PRESET_PROJECTS):
                    proj = PRESET_PROJECTS[idx]
                    if proj in rec["projects"]:
                        rec["projects"].remove(proj)
                        console.print(f"         [red]- {proj}[/red]")
                    else:
                        rec["projects"].append(proj)
                        console.print(f"         [green]+ {proj}[/green]")


# ── Phase 5: Review & write ──────────────────────────────────────────────────

def review_phase(records):
    """Show summary table, confirm, write frontmatter."""
    while True:
        console.print()
        console.print(Rule("[bold cyan]PHASE 5 — REVIEW[/bold cyan]"))

        table = Table(show_header=True, header_style="bold magenta", box=None, padding=(0, 1))
        table.add_column("#", style="dim", width=4, no_wrap=True)
        table.add_column("File", no_wrap=False, max_width=35)
        table.add_column("Status", width=12, no_wrap=True)
        table.add_column("Type", width=14, no_wrap=True)
        table.add_column("Tags", no_wrap=False, max_width=30)
        table.add_column("Projects", no_wrap=False, max_width=20)

        for idx, rec in enumerate(records, 1):
            name = os.path.basename(rec["filepath"])
            # Color the status
            status_key = next((k for k, v in STATUSES.items() if v == rec["status"]), None)
            s_color = STATUS_COLORS.get(status_key, "white") if status_key else "white"

            table.add_row(
                str(idx),
                name,
                f"[{s_color}]{rec['status']}[/{s_color}]",
                rec["doc_type"],
                ", ".join(rec["tags"][:5]) or "[dim]—[/dim]",
                ", ".join(rec["projects"][:3]) or "[dim]—[/dim]",
            )

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

            # Quick re-assignment
            console.print("[dim]Status:[/dim]")
            print_status_legend()
            while True:
                sch = getch()
                if sch.lower() == "q" or sch == "\x03":
                    break
                if sch in STATUSES:
                    rec["status"] = STATUSES[sch]
                    console.print(f"  → {STATUSES[sch]}")
                    break

            console.print("[dim]Doc type:[/dim]")
            print_doctype_legend()
            while True:
                dch = getch()
                if dch.lower() == "q" or dch == "\x03":
                    break
                if dch in DOC_TYPES:
                    rec["doc_type"] = DOC_TYPES[dch]
                    console.print(f"  → {DOC_TYPES[dch]}")
                    break

            continue


def execute_writes(records):
    """Write updated metadata back to each file's YAML frontmatter."""
    written = 0
    for rec in records:
        filepath = rec["filepath"]
        try:
            frontmatter, body = parse_file(filepath)

            # Update fields
            frontmatter["status"] = rec["status"]
            frontmatter["doc_type"] = rec["doc_type"]
            frontmatter["tags"] = rec["tags"]
            frontmatter["projects"] = rec["projects"]

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


# ── Entry point ──────────────────────────────────────────────────────────────

def main():
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

    # Phase 1: Status
    triaged, remaining = status_phase(records)
    if not triaged:
        console.print("[dim]Nothing triaged.[/dim]")
        return

    # Phase 2: Doc type
    doctype_phase(triaged)

    # Phase 3: Tags
    tags_phase(triaged)

    # Phase 4: Projects
    projects_phase(triaged)

    # Phase 5: Review & write
    confirmed = review_phase(triaged)
    if not confirmed:
        return

    execute_writes(triaged)
    console.print("\n[bold green]All done.[/bold green]\n")


if __name__ == "__main__":
    main()
