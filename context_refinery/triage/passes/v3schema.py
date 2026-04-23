"""V3 normalize pass — fill missing/invalid schema fields, file-by-file.

UX model (from vault-doctor/src/normalize.py):
  type / format / status  →  single letter key, Enter accepts default
  area                    →  numbered vault suggestions, or [m] manual
  concepts / tags         →  numbered picks, [m] manual, Enter done
"""

import os
import sys
from collections import Counter
from pathlib import Path
from typing import Optional

from context_refinery.triage.passes.base import TriagePass
from context_refinery.triage.terminal import console, getch
from context_refinery.triage.writers import parse_file, preview

try:
    from rich.table import Table
    from rich.panel import Panel
    from rich import box
    from rich.prompt import Prompt
except ImportError:
    print("Please run: pip install rich")
    sys.exit(1)

# ── schema constants ──────────────────────────────────────────────────────────

VALID_TYPES    = ["project", "area", "resource", "concept", "log"]
VALID_FORMATS  = ["note", "reference", "howto", "log"]
VALID_STATUSES = ["active", "backlog", "blocked", "done"]
VALID_TAG_PREFIXES = ("topic/", "tool/", "lang/", "scope/")
CORE_FIELDS = ["type", "format", "status", "area", "concepts", "tags"]

TYPE_KEYS   = {"p": "project", "a": "area",      "r": "resource", "c": "concept", "l": "log"}
FORMAT_KEYS = {"n": "note",    "e": "reference",  "h": "howto",   "l": "log"}
STATUS_KEYS = {"a": "active",  "b": "backlog",    "x": "blocked", "d": "done"}


# ── wikilink helpers ──────────────────────────────────────────────────────────

def _unwrap(val: str) -> str:
    val = val.strip()
    if val.startswith("[["):
        val = val[2:]
    if val.endswith("]]"):
        val = val[:-2]
    return val.strip()


def _wrap(val: str) -> str:
    val = val.strip()
    if not val.startswith("[["):
        val = f"[[{val}"
    if not val.endswith("]]"):
        val = f"{val}]]"
    return val


def _is_wikilink(val: str) -> bool:
    s = val.strip()
    return s.startswith("[[") and s.endswith("]]")


def _valid_tag(tag: str) -> bool:
    return any(tag.startswith(p) for p in VALID_TAG_PREFIXES)


# ── vault suggestions ─────────────────────────────────────────────────────────

def collect_suggestions(vault_root: str) -> dict[str, list[str]]:
    """Scan vault for top existing area/concept/tag values (top 9 each)."""
    area_counts: Counter = Counter()
    concept_counts: Counter = Counter()
    tag_counts: Counter = Counter()

    for root, dirs, files in os.walk(vault_root):
        dirs[:] = [d for d in dirs if d != ".obsidian"]
        for file in files:
            if not file.endswith(".md"):
                continue
            try:
                fm, _ = parse_file(os.path.join(root, file))
                if fm.get("area"):
                    area_counts[_unwrap(str(fm["area"]))] += 1
                for c in (fm.get("concepts") or []):
                    concept_counts[_unwrap(str(c))] += 1
                for t in (fm.get("tags") or []):
                    tag_counts[str(t).strip()] += 1
            except Exception:
                pass

    return {
        "area":     [v for v, _ in area_counts.most_common(9)],
        "concepts": [v for v, _ in concept_counts.most_common(9)],
        "tags":     [v for v, _ in tag_counts.most_common(9)],
    }


# ── validation ────────────────────────────────────────────────────────────────

def _missing_fields(record: dict) -> list[str]:
    return [
        f for f in CORE_FIELDS
        if not record.get(f) and record.get(f) != 0
    ]


def _invalid_fields(record: dict) -> dict[str, str]:
    issues = {}
    if record.get("type") and record["type"] not in VALID_TYPES:
        issues["type"] = f"'{record['type']}' not valid"
    if record.get("format") and record["format"] not in VALID_FORMATS:
        issues["format"] = f"'{record['format']}' not valid"
    if record.get("status") and record["status"] not in VALID_STATUSES:
        issues["status"] = f"'{record['status']}' not valid"
    if record.get("area") and not _is_wikilink(str(record["area"])):
        issues["area"] = "needs [[wikilink]]"
    if record.get("concepts"):
        cs = record["concepts"] if isinstance(record["concepts"], list) else [record["concepts"]]
        bad = [c for c in cs if not _is_wikilink(str(c))]
        if bad:
            issues["concepts"] = f"non-wikilinks: {bad}"
        elif len(cs) > 3:
            issues["concepts"] = f"max 3 (got {len(cs)})"
    if record.get("tags"):
        ts = record["tags"] if isinstance(record["tags"], list) else [record["tags"]]
        bad = [t for t in ts if not _valid_tag(str(t))]
        if bad:
            issues["tags"] = f"bad prefix: {bad}"
        elif len(ts) > 2:
            issues["tags"] = f"max 2 (got {len(ts)})"
    return issues


# ── terminal helpers ──────────────────────────────────────────────────────────

def _single_key(label: str, key_map: dict[str, str], default_key: str) -> Optional[str]:
    """Show inline options, highlight default. Returns value or None for skip/quit."""
    parts = []
    for k, v in key_map.items():
        if k == default_key:
            parts.append(f"[bold cyan]\\[{k}]{v}[/bold cyan]")
        else:
            parts.append(f"[dim]\\[{k}][/dim]{v}")
    console.print(f"  [cyan]{label}[/cyan]  {'  '.join(parts)}  [dim]\\[s]skip  \\[q]quit[/dim]", end="  ")

    while True:
        ch = getch()
        if ch == "\x03":
            sys.exit(0)
        if ch.lower() == "q":
            console.print()
            return "quit"
        if ch.lower() == "s":
            console.print("[dim]skip[/dim]")
            return "skip"
        if ch in ("\r", "\n"):
            chosen = key_map[default_key]
            console.print(f"[dim]{chosen}[/dim]")
            return chosen
        if ch in key_map:
            console.print(f"[dim]{key_map[ch]}[/dim]")
            return key_map[ch]


def _pick_one(label: str, options: list[str]) -> Optional[str]:
    """Number-key pick from suggestions, m=manual, s=skip, q=quit, Enter=skip."""
    if not options:
        return _manual_text(label)

    parts = [f"[dim]\\[{i+1}][/dim]{v}" for i, v in enumerate(options)]
    console.print(f"  [cyan]{label}[/cyan]  {'  '.join(parts)}  [dim]\\[m]manual  \\[s]skip  ↵ skip[/dim]", end="  ")

    while True:
        ch = getch()
        if ch == "\x03":
            sys.exit(0)
        if ch.lower() == "q":
            console.print()
            return "quit"
        if ch.lower() == "s" or ch in ("\r", "\n"):
            console.print("[dim]skipped[/dim]")
            return None
        if ch.lower() == "m":
            console.print("[dim]manual[/dim]")
            return _manual_text(label)
        if ch.isdigit() and 1 <= int(ch) <= len(options):
            chosen = options[int(ch) - 1]
            console.print(f"[dim]{chosen}[/dim]")
            return chosen


def _pick_many(label: str, options: list[str], current: list[str], max_n: int) -> Optional[list[str]]:
    """Number-key multi-pick, m=manual add, Enter=done, s=skip, q=quit."""
    selected = list(current)

    while len(selected) < max_n:
        remaining = max_n - len(selected)
        sel_display = ", ".join(selected) if selected else "[dim]none[/dim]"
        if options:
            parts = [f"[dim]\\[{i+1}][/dim]{v}" for i, v in enumerate(options)]
            row = "  ".join(parts)
            console.print(
                f"  [cyan]{label}[/cyan]  [{sel_display}]  {remaining} left  "
                f"{row}  [dim]\\[m]add  \\[s]skip  ↵ done[/dim]",
                end="  "
            )
        else:
            console.print(
                f"  [cyan]{label}[/cyan]  [{sel_display}]  {remaining} left  "
                f"[dim]\\[m]add  \\[s]skip  ↵ done[/dim]",
                end="  "
            )

        ch = getch()
        if ch == "\x03":
            sys.exit(0)
        if ch.lower() == "q":
            console.print()
            return "quit"
        if ch.lower() == "s":
            console.print("[dim]skip[/dim]")
            return "skip"
        if ch in ("\r", "\n"):
            console.print()
            break
        if ch.lower() == "m":
            console.print("[dim]manual[/dim]")
            val = _manual_text(f"add {label}").strip()
            if val and val not in selected:
                selected.append(val)
        elif ch.isdigit() and options and 1 <= int(ch) <= len(options):
            val = options[int(ch) - 1]
            if val not in selected:
                selected.append(val)
                console.print(f"[dim]+{val}[/dim]")
            else:
                console.print(f"[dim](already added)[/dim]")
        else:
            console.print()

    return selected


def _manual_text(label: str) -> Optional[str]:
    console.print(f"\n  [cyan]{label.strip()}:[/cyan] ", end="")
    try:
        import tty, termios
        fd = sys.stdin.fileno() if sys.stdin.isatty() else open("/dev/tty").fileno()
        old = termios.tcgetattr(fd)
        termios.tcsetattr(fd, termios.TCSAFLUSH, old)
        val = sys.stdin.readline().strip() if sys.stdin.isatty() else open("/dev/tty").readline().strip()
        return val or None
    except Exception:
        return Prompt.ask(f"  {label.strip()}").strip() or None


# ── note header ───────────────────────────────────────────────────────────────

def _show_header(rel_path: str, record: dict, missing: list[str], issues: dict[str, str]):
    table = Table(box=box.SIMPLE, show_header=False, padding=(0, 1))
    table.add_column("field",   style="cyan",  width=10)
    table.add_column("current", style="white")
    table.add_column("",        width=25)

    for f in CORE_FIELDS:
        val = record.get(f, "")
        if f in issues:
            flag = f"[red]{issues[f]}[/red]"
        elif f in missing:
            flag = "[yellow]missing[/yellow]"
        else:
            flag = "[green]✓[/green]"
        display = str(val) if val else "[dim]—[/dim]"
        table.add_row(f, display, flag)

    subtitle = (
        "[dim]type:[/dim] \\[p]roject \\[a]rea \\[r]esource \\[c]oncept \\[l]og  "
        "[dim]fmt:[/dim] \\[n]ote \\[e]ref \\[h]owto \\[l]og  "
        "[dim]status:[/dim] \\[a]ctive \\[b]acklog \\[x]blocked \\[d]one"
    )
    console.print(Panel(
        table,
        title=f"[bold]{rel_path}[/bold]",
        subtitle=subtitle,
        border_style="blue",
        expand=False,
    ))


# ── pass ──────────────────────────────────────────────────────────────────────

class V3SchemaPass(TriagePass):

    def __init__(self, vault_root: str = None):
        self._vault_root = vault_root
        self._suggestions: Optional[dict] = None

    def _suggestions_for(self, filepath: str) -> dict:
        if self._suggestions is None:
            root = self._vault_root or str(Path(filepath).parent)
            console.print("[dim]Scanning vault for suggestions…[/dim]")
            self._suggestions = collect_suggestions(root)
            a = len(self._suggestions["area"])
            c = len(self._suggestions["concepts"])
            t = len(self._suggestions["tags"])
            console.print(f"[dim]  areas: {a}  concepts: {c}  tags: {t}[/dim]\n")
        return self._suggestions

    @property
    def name(self) -> str:
        return "V3 NORMALIZE"

    def print_legend(self) -> None:
        console.print(
            "  Fills missing/invalid V3 fields one note at a time.\n"
            "  Letter keys for type/format/status  •  numbers for area/concepts/tags\n"
            "  [bold][s][/bold] skip file  [bold][q][/bold] quit pass\n"
        )

    def process_file(self, record: dict, index: int, total: int) -> bool:
        missing = _missing_fields(record)
        issues  = _invalid_fields(record)

        name = os.path.basename(record["filepath"])

        if not missing and not issues:
            console.print(f"[dim][{index}/{total}][/dim]  {name}  [dim]✓ V3[/dim]")
            return True

        rel = record["filepath"]
        if self._vault_root:
            try:
                rel = str(Path(record["filepath"]).relative_to(self._vault_root))
            except ValueError:
                pass

        _show_header(rel, record, missing, issues)

        suggestions = self._suggestions_for(record["filepath"])

        needs = {f for f in missing} | {f for f in issues}

        # type
        if "type" in needs:
            default_key = next((k for k, v in TYPE_KEYS.items() if v == record.get("type")), "r")
            result = _single_key("type  ", TYPE_KEYS, default_key)
            if result == "quit":  return False
            if result == "skip":  return True
            record["type"] = result

        # format
        if "format" in needs:
            default_key = next((k for k, v in FORMAT_KEYS.items() if v == record.get("format")), "n")
            result = _single_key("format", FORMAT_KEYS, default_key)
            if result == "quit":  return False
            if result == "skip":  return True
            record["format"] = result

        # status
        if "status" in needs:
            default_key = next((k for k, v in STATUS_KEYS.items() if v == record.get("status")), "a")
            result = _single_key("status", STATUS_KEYS, default_key)
            if result == "quit":  return False
            if result == "skip":  return True
            record["status"] = result

        # area
        if "area" in needs:
            result = _pick_one("area  ", suggestions.get("area", []))
            if result == "quit":  return False
            if result is not None:
                record["area"] = _wrap(result)

        # concepts
        if "concepts" in needs:
            current = [_unwrap(c) for c in (record.get("concepts") or [])]
            result = _pick_many("concepts", suggestions.get("concepts", []), current, max_n=3)
            if result == "quit":  return False
            if result != "skip" and isinstance(result, list):
                record["concepts"] = [_wrap(v) for v in result]

        # tags
        if "tags" in needs:
            current = list(record.get("tags") or [])
            while True:
                result = _pick_many("tags  ", suggestions.get("tags", []), current, max_n=2)
                if result == "quit":  return False
                if result == "skip":  break
                if isinstance(result, list):
                    bad = [t for t in result if not _valid_tag(t)]
                    if bad:
                        console.print(f"  [red]✗ bad prefix: {bad} — use topic/ tool/ lang/ scope/[/red]")
                        current = [t for t in result if _valid_tag(t)]
                        continue
                    record["tags"] = result
                    break

        return True

    def get_display_value(self, record: dict) -> str:
        missing = _missing_fields(record)
        issues  = _invalid_fields(record)
        if not missing and not issues:
            return "✓"
        parts = []
        if missing:
            parts.append(f"missing: {', '.join(missing)}")
        if issues:
            parts.append(f"invalid: {', '.join(issues)}")
        return "  ".join(parts)
