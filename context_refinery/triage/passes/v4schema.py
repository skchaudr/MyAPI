"""V4 owner-pass — fill missing/invalid schema fields, file-by-file.

UX model (from vault-doctor/src/normalize.py):
  type / status  →  single letter key, Enter accepts default
  area / project →  numbered vault suggestions or [m] manual
  concepts / tags →  numbered picks, [m] manual, Enter done

Status is only prompted when type is project or event.
Format field is gone in V4 — handled by topic/log and topic/howto tags.
"""

import os
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Optional

from context_refinery.triage.passes.base import TriagePass
from context_refinery.triage.passes.doctype import TYPE_VALUES, TYPE_COLORS
from context_refinery.triage.passes.status import STATUSES, STATUS_COLORS
from context_refinery.triage.terminal import console, getch
from context_refinery.triage.writers import parse_file, preview

try:
    from rich.panel import Panel
    from rich.prompt import Prompt
except ImportError:
    print("Please run: pip install rich")
    sys.exit(1)

VALID_TYPES    = set(TYPE_VALUES.values())
VALID_STATUSES = set(STATUSES.values())
VALID_TAG_PREFIXES = ("topic/", "tool/", "lang/", "scope/")
MIN_CONCEPTS = 1
MAX_TAGS = 8
PAGE_SIZE = 10
CONCEPT_PRESETS = [
    "AI Tooling",
    "Agent Collaboration",
    "Automation",
    "Benchmarking",
    "CLI Workflow",
    "Context Engineering",
    "Data Migration",
    "Developer Workflow",
    "Editor Workflow",
    "Failure Analysis",
    "Human-in-the-Loop",
    "Infrastructure",
    "Knowledge Graph",
    "Multi-Agent Workflow",
    "Note Refinement",
    "Obsidian Workflow",
    "Operational Runbook",
    "Project Architecture",
    "Prompt Engineering",
    "RAG Pipeline",
    "Remote Development",
    "Retrieval Quality",
    "Schema Design",
    "Service Deployment",
    "Source of Truth",
    "Terminal Workflow",
    "Tooling Ergonomics",
    "Vault Taxonomy",
    "VM Operations",
]
TAG_ALIASES = {
    "tterm": "topic/terminal",
    "uterm": "tool/terminal",
}
SECRET_PATTERNS = (
    re.compile(r"sk-[A-Za-z0-9_-]{16,}"),
    re.compile(r"AIza[0-9A-Za-z_-]{16,}"),
    re.compile(r"[A-Za-z0-9_-]{32,}"),
)

STATUS_REQUIRED_TYPES = {"project", "event"}

CORE_FIELDS = ["type", "area", "concepts", "tags"]


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


def _normalize_tag_input(tag: str) -> str:
    tag = tag.strip()
    return TAG_ALIASES.get(tag, tag)


def _looks_like_tag(value: str) -> bool:
    return _unwrap(value).startswith(VALID_TAG_PREFIXES)


def _looks_like_secret(value: str) -> bool:
    return any(pattern.search(str(value)) for pattern in SECRET_PATTERNS)


def _dedupe_preserving_order(values: list[str]) -> list[str]:
    seen = set()
    result = []
    for value in values:
        if value and value not in seen:
            result.append(value)
            seen.add(value)
    return result


def _iter_scalar_values(value) -> list[str]:
    """Flatten frontmatter values so malformed nested lists stay out of prompts."""
    if value is None:
        return []
    if isinstance(value, list):
        flattened = []
        for item in value:
            flattened.extend(_iter_scalar_values(item))
        return flattened
    return [str(value).strip()]


def collect_suggestions(vault_root: str) -> dict[str, list[str]]:
    """Scan vault for top existing area/concept/tag values."""
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
                for c in _iter_scalar_values(fm.get("concepts")):
                    concept = _unwrap(c)
                    if concept and not concept.startswith("[") and not _looks_like_tag(concept):
                        concept_counts[concept] += 1
                for t in _iter_scalar_values(fm.get("tags")):
                    tag = t.strip()
                    if _valid_tag(tag):
                        tag_counts[tag] += 1
            except Exception:
                pass

    return {
        "area":     [v for v, _ in area_counts.most_common(50)],
        "concepts": _dedupe_preserving_order(CONCEPT_PRESETS + [v for v, _ in concept_counts.most_common(50)]),
        "tags":     [v for v, _ in tag_counts.most_common(50)],
    }


def _missing_fields(record: dict) -> list[str]:
    missing = []
    if record.get("type") not in VALID_TYPES:
        missing.append("type")
    if record.get("type") in STATUS_REQUIRED_TYPES and record.get("status") not in VALID_STATUSES:
        missing.append("status")
    if not record.get("area") and not record.get("project"):
        missing.append("area")
    if not record.get("concepts"):
        missing.append("concepts")
    if not record.get("tags"):
        missing.append("tags")
    return missing


def _invalid_fields(record: dict) -> dict[str, str]:
    issues = {}
    if record.get("type") and record["type"] not in VALID_TYPES:
        issues["type"] = f"old value: {record['type']}"
    if record.get("area") and not _is_wikilink(str(record["area"])):
        issues["area"] = "needs [[wikilink]]"
    if record.get("concepts"):
        cs = record["concepts"] if isinstance(record["concepts"], list) else [record["concepts"]]
        bad = [c for c in cs if not _is_wikilink(str(c))]
        secretish = [c for c in cs if _looks_like_secret(str(c))]
        if secretish:
            issues["concepts"] = "contains secret-shaped text"
        elif bad:
            issues["concepts"] = f"non-wikilinks: {bad}"
        elif any(_looks_like_tag(str(c)) for c in cs):
            issues["concepts"] = "concepts should be idea wikilinks, not tag-shaped values"
    if record.get("tags"):
        ts = record["tags"] if isinstance(record["tags"], list) else [record["tags"]]
        bad = [t for t in ts if not _valid_tag(str(t))]
        secretish = [t for t in ts if _looks_like_secret(str(t))]
        if secretish:
            issues["tags"] = "contains secret-shaped text"
        elif bad:
            issues["tags"] = f"replace legacy tags: {bad}"
    return issues


def _compact_path(path: str, limit: int = 72) -> str:
    if len(path) <= limit:
        return path
    return f"...{path[-(limit - 3):]}"


def _note_label(index: int, total: int, rel_path: str, title: Optional[str] = None) -> str:
    display = (title or Path(rel_path).stem).strip()
    return f"[{index}/{total}] {_compact_path(display, 86)}"


def _print_note_label(note: Optional[str]) -> None:
    if note:
        console.print(f"\n[dim]Note {note}[/dim]")


def _clear_interactive_screen() -> None:
    if console.is_terminal:
        console.clear()


def _page_items(options: list[str], page: int, page_size: int = PAGE_SIZE) -> list[tuple[str, str]]:
    labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    start = page * page_size
    return list(zip(labels, options[start:start + page_size]))


def _page_count(options: list[str], page_size: int = PAGE_SIZE) -> int:
    return max(1, (len(options) + page_size - 1) // page_size)


def _compact_value(value) -> str:
    if value in (None, "", []):
        return "[dim]empty[/dim]"
    if isinstance(value, list):
        cleaned = [str(v) for v in value if str(v).strip()]
        return ", ".join(cleaned[:3]) or "[dim]empty[/dim]"
    return str(value)


def _selected_display(selected: list[str]) -> str:
    if not selected:
        return "[dim]none[/dim]"
    return "  ".join(f"[green]✓[/green] {value}" for value in selected)


def _mark_needs_title(record: dict) -> None:
    flags = list(record.get("review_flags") or [])
    if "needs_title" not in flags:
        flags.append("needs_title")
    record["review_flags"] = flags


def _show_card(index: int, total: int, rel_path: str, record: dict, missing: list[str], issues: dict[str, str]):
    title = (record.get("title") or Path(rel_path).stem).strip()
    needs = []
    for field in ["type", "status", "area", "project", "concepts", "tags"]:
        if field in issues:
            needs.append(f"[yellow]{field}[/yellow]: {issues[field]}  [dim]current: {_compact_value(record.get(field))}[/dim]")
        elif field in missing:
            needs.append(f"[yellow]{field}[/yellow]: missing")

    if not needs:
        body = "[green]V4 fields look good.[/green]"
    else:
        body = "[bold]Needs[/bold]\n" + "\n".join(f"  {line}" for line in needs)
    body = f"[dim]File: {_compact_path(rel_path, 92)}[/dim]\n\n{body}"

    console.print(Panel(
        body,
        title=f"[bold][{index}/{total}] {_compact_path(title, 86)}[/bold]",
        subtitle="[dim]s skip file  q quit pass[/dim]",
        border_style="blue",
        expand=False,
    )) 


def _show_many_picker(
    label: str,
    visible: list[tuple[str, str]],
    selected: list[str],
    max_n: Optional[int],
    min_n: int,
    page: int,
    total_pages: int,
    note: Optional[str],
    rel_path: Optional[str] = None,
    review_flags: Optional[list[str]] = None,
    notice: Optional[str] = None,
) -> None:
    _clear_interactive_screen()
    clean_label = label.strip()
    if max_n is None:
        count_display = f"{len(selected)} selected, min {min_n}"
    else:
        count_display = f"{len(selected)}/{max_n}"
    help_line = "Concepts are reusable idea links: workflows, systems, patterns, decisions, failure modes."
    if clean_label == "tags":
        help_line = "Tags are flexible clustering/search labels; concepts are the stronger graph links."
    body = (
        f"[bold cyan]{clean_label}[/bold cyan]\n"
        f"Selected ({count_display}): {_selected_display(selected)}\n"
        f"[dim]{help_line}[/dim]\n"
        f"[dim]File: {_compact_path(rel_path, 92) if rel_path else 'unknown'}[/dim]\n"
        f"[dim]Flags: {', '.join(review_flags or []) if review_flags else 'none'}[/dim]\n"
        "[dim]Enter done  ·  m manual  ·  t needs title  ·  s skip field  ·  q quit[/dim]"
    )
    console.print(Panel(
        body,
        title=f"[bold]Note {note}[/bold]" if note else None,
        border_style="cyan",
        expand=False,
    ))
    if notice:
        console.print(f"  [yellow]{notice}[/yellow]")
    if visible:
        if total_pages > 1:
            console.print(f"  [dim]page {page + 1}/{total_pages}  ←/→ or ↑/↓ changes page[/dim]")
        for key, value in visible:
            marker = "[green]✓[/green]" if value in selected else " "
            style = "green" if value in selected else "white"
            console.print(f"  [bold]{key}[/bold] {marker} [{style}]{value}[/{style}]")
    console.print("\n[bold]>[/bold] ", end="")


# ── terminal helpers ──────────────────────────────────────────────────────────

def _getch_or_signal():
    ch = getch()
    if ch == "\x03":
        sys.exit(0)
    return ch


def _pick_one(label: str, options: list[str], note: Optional[str] = None) -> Optional[str]:
    if not options:
        return _manual_text(label)
    _print_note_label(note)
    console.print(f"  [bold cyan]{label.strip()}[/bold cyan]")
    for i, value in enumerate(options, start=1):
        console.print(f"    [bold]{i}[/bold] {value}")
    console.print("    [bold]m[/bold] manual    [dim]Enter skip[/dim]", end="  ")
    while True:
        ch = _getch_or_signal()
        if ch.lower() == "q":
            console.print(); return "quit"
        if ch.lower() == "s" or ch in ("\r", "\n"):
            console.print("[dim]skipped[/dim]"); return None
        if ch.lower() == "m":
            console.print("[dim]manual[/dim]"); return _manual_text(label)
        if ch.isdigit() and 1 <= int(ch) <= len(options):
            chosen = options[int(ch) - 1]
            console.print(f"[dim]{chosen}[/dim]"); return chosen


def _pick_many(
    label: str,
    options: list[str],
    current: list[str],
    max_n: Optional[int],
    min_n: int = 0,
    note: Optional[str] = None,
    rel_path: Optional[str] = None,
    record: Optional[dict] = None,
) -> Optional[list[str]]:
    selected = list(current)
    page = 0
    notice = None
    while True:
        total_pages = _page_count(options)
        visible = _page_items(options, page)
        _show_many_picker(
            label,
            visible,
            selected,
            max_n,
            min_n,
            page,
            total_pages,
            note,
            rel_path=rel_path,
            review_flags=list((record or {}).get("review_flags") or []),
            notice=notice,
        )
        notice = None
        ch = _getch_or_signal()
        if ch.lower() == "q":
            console.print(); return "quit"
        if ch.lower() == "t" and record is not None:
            _mark_needs_title(record)
            notice = "Marked review_flags: needs_title"
            continue
        if ch in ("RIGHT", "DOWN") and total_pages > 1:
            page = (page + 1) % total_pages
            continue
        if ch in ("LEFT", "UP") and total_pages > 1:
            page = (page - 1) % total_pages
            continue
        if ch.lower() == "s":
            console.print("[dim]skip[/dim]"); return "skip"
        if ch in ("\r", "\n"):
            if len(selected) < min_n:
                needed = min_n - len(selected)
                notice = f"Add {needed} more {label.strip()} before finishing."
                continue
            summary = ", ".join(selected) if selected else "none"
            console.print(f"[dim]{label.strip()}: {summary}[/dim]")
            break
        if ch.lower() == "m":
            console.print("[dim]manual[/dim]")
            val = _manual_text(f"add {label}") or ""
            if label.strip() == "tags":
                val = _normalize_tag_input(val)
            if val and _looks_like_secret(val):
                notice = "Secret-shaped text ignored."
            elif max_n is not None and len(selected) >= max_n:
                notice = f"{label.strip()} is full."
            elif val and val not in selected:
                selected.append(val)
                notice = f"Added {val}"
            elif val:
                notice = f"{val} is already selected."
        elif ch.isdigit() and visible:
            picked = dict(visible).get(ch)
            if picked is None:
                continue
            val = picked
            if _looks_like_secret(val):
                notice = "Secret-shaped text ignored."
            elif max_n is not None and len(selected) >= max_n:
                notice = f"{label.strip()} is full."
            elif val not in selected:
                selected.append(val)
                notice = f"Added {val}"
            else:
                notice = f"{val} is already selected."
        else:
            notice = "Key not mapped here."
    return selected


def _manual_text(label: str) -> Optional[str]:
    console.print(f"\n  [cyan]{label.strip()}:[/cyan] ", end="")
    try:
        stream = None
        if not sys.stdin.isatty():
            stream = open("/dev/tty")
        val = (stream or sys.stdin).readline().strip()
        if stream:
            stream.close()
        return val or None
    except Exception:
        return Prompt.ask(f"  {label.strip()}").strip() or None


# ── pass ──────────────────────────────────────────────────────────────────────

class V4SchemaPass(TriagePass):

    def __init__(self, vault_root: str = None):
        self._vault_root = vault_root
        self._suggestions: Optional[dict] = None

    def _get_suggestions(self, filepath: str) -> dict:
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
        return "V4 OWNER PASS"

    def print_legend(self) -> None:
        console.print(
            "  Fills missing/invalid V4 fields one note at a time.\n"
            "  Numbers for area/concepts/tags  •  1-6 for type  •  1-4 for status\n"
            "  [bold]\\[s][/bold] skip file  [bold]\\[q][/bold] quit pass\n"
        )

    def process_file(self, record: dict, index: int, total: int) -> bool:
        missing = _missing_fields(record)
        issues  = _invalid_fields(record)

        name = os.path.basename(record["filepath"])

        if not missing and not issues:
            console.print(f"[dim][{index}/{total}][/dim]  {name}  [dim]✓ V4[/dim]")
            return True

        rel = record["filepath"]
        if self._vault_root:
            try:
                rel = str(Path(record["filepath"]).relative_to(self._vault_root))
            except ValueError:
                pass

        note = _note_label(index, total, rel, record.get("title"))
        _show_card(index, total, rel, record, missing, issues)
        suggestions = self._get_suggestions(record["filepath"])
        needs = set(missing) | set(issues)

        # type
        if "type" in needs:
            _print_note_label(note)
            console.print("  [bold cyan]type[/bold cyan]  [dim]Enter = resource[/dim]")
            console.print("    [bold]1[/bold] project")
            console.print("    [bold]2[/bold] area")
            console.print("    [bold]3[/bold] resource")
            console.print("    [bold]4[/bold] concept")
            console.print("    [bold]5[/bold] event")
            console.print("    [bold]6[/bold] periodic")
            console.print("    [bold]s[/bold] skip file    [bold]q[/bold] quit", end="  ")
            while True:
                ch = _getch_or_signal()
                if ch.lower() == "q": return False
                if ch.lower() == "s": return True
                if ch in ("\r", "\n", " "):
                    record["type"] = "resource"
                    console.print("  → [blue]resource[/blue] (default)")
                    break
                if ch in TYPE_VALUES:
                    record["type"] = TYPE_VALUES[ch]
                    console.print(f"  → [{TYPE_COLORS[ch]}]{TYPE_VALUES[ch]}[/{TYPE_COLORS[ch]}]")
                    break

        # status — only for project/event
        if record.get("type") in STATUS_REQUIRED_TYPES and "status" in needs:
            _print_note_label(note)
            console.print("  [bold cyan]status[/bold cyan]  [dim]Enter = active[/dim]")
            console.print("    [bold]1[/bold] active")
            console.print("    [bold]2[/bold] backlog")
            console.print("    [bold]3[/bold] blocked")
            console.print("    [bold]4[/bold] done")
            console.print("    [bold]s[/bold] skip field    [bold]q[/bold] quit", end="  ")
            while True:
                ch = _getch_or_signal()
                if ch.lower() == "q": return False
                if ch.lower() == "s": break
                if ch in ("\r", "\n", " "):
                    record["status"] = "active"
                    console.print("  → [green]active[/green] (default)")
                    break
                if ch in STATUSES:
                    record["status"] = STATUSES[ch]
                    console.print(f"  → [{STATUS_COLORS[ch]}]{STATUSES[ch]}[/{STATUS_COLORS[ch]}]")
                    break

        # area
        if "area" in needs:
            result = _pick_one("area  ", suggestions.get("area", []), note=note)
            if result == "quit": return False
            if result is not None:
                record["area"] = _wrap(result)

        # concepts
        if "concepts" in needs:
            current = [_unwrap(c) for c in (record.get("concepts") or [])]
            while True:
                result = _pick_many(
                    "concepts",
                    suggestions.get("concepts", []),
                    current,
                    max_n=None,
                    min_n=MIN_CONCEPTS,
                    note=note,
                    rel_path=rel,
                    record=record,
                )
                if result == "quit": return False
                if result == "skip": break
                if isinstance(result, list):
                    tag_like = [v for v in result if _looks_like_tag(v)]
                    if tag_like:
                        console.print(f"  [red]✗ concepts are ideas, tags go in tags: {tag_like}[/red]")
                        console.print("  [dim]Examples: AI Tooling, Infrastructure, Developer Workflow[/dim]")
                        current = [v for v in result if not _looks_like_tag(v)]
                        continue
                    record["concepts"] = [_wrap(v) for v in result]
                    break

        # tags
        if "tags" in needs:
            raw_tags = _iter_scalar_values(record.get("tags"))
            legacy_tags = [t for t in raw_tags if t and not _valid_tag(t)]
            current = [t for t in raw_tags if _valid_tag(t)]
            if legacy_tags:
                console.print(f"  [dim]Legacy tags ignored for this prompt: {', '.join(legacy_tags)}[/dim]")
            while True:
                result = _pick_many(
                    "tags  ",
                    suggestions.get("tags", []),
                    current,
                    max_n=MAX_TAGS,
                    min_n=0,
                    note=note,
                    rel_path=rel,
                    record=record,
                )
                if result == "quit": return False
                if result == "skip": break
                if isinstance(result, list):
                    bad = [t for t in result if not _valid_tag(t)]
                    if bad:
                        console.print(f"  [yellow]Tags need a prefix: {bad}[/yellow]")
                        console.print("  [dim]Use topic/, tool/, lang/, or scope/.[/dim]")
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
