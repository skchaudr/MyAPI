"""Tags pass — multi-select tag assignment with toggle.

Extracted from context_refinery/triage.py lines 389-446 (tags_phase).
"""

import sys
import os
from context_refinery.triage.passes.base import TriagePass
from context_refinery.triage.terminal import console, getch, getline, KEYS

PRESET_TAGS = [
    "ai", "web-dev", "devops", "python", "react", "typescript",
    "obsidian", "khoj", "infrastructure", "career", "learning",
    "neovim", "git", "api", "database", "design",
]

PAGE_SIZE = 9


def normalize_tags(tags):
    """Keep preset tags in a stable order, then preserve custom tags."""
    seen = set()
    normalized = []

    for tag in PRESET_TAGS:
        if tag in tags and tag not in seen:
            normalized.append(tag)
            seen.add(tag)

    for tag in tags:
        if tag not in seen:
            normalized.append(tag)
            seen.add(tag)

    return normalized


def page_items(page_index):
    start = page_index * PAGE_SIZE
    end = start + PAGE_SIZE
    return PRESET_TAGS[start:end]


class TagsPass(TriagePass):

    @property
    def name(self) -> str:
        return "TAGS"

    def print_legend(self, page_index: int = 0) -> None:
        """Print the tag keypress legend with numbered/lettered presets."""
        page = page_items(page_index)
        total_pages = max(1, (len(PRESET_TAGS) + PAGE_SIZE - 1) // PAGE_SIZE)

        parts = []
        for i, tag in enumerate(page):
            key = str(i + 1)
            parts.append(f"[bold][{key}][/bold] {tag}")

        console.print(f"  [dim]page {page_index + 1}/{total_pages}[/dim]")
        for i in range(0, len(parts), 3):
            console.print("  " + "  ".join(parts[i:i + 3]))
        console.print(
            "\n  [bold][t][/bold] type custom  "
            "[bold]s[/bold] skip  "
            "[bold][enter/space][/bold] done with tags  "
            "[bold][q][/bold] done with all files  "
            "[bold][←/→][/bold] prev/next page\n"
        )

    def process_file(self, record: dict, index: int, total: int) -> bool:
        """Toggle tags for one file. t=custom, enter/space=done, q=quit all.

        Returns True to continue, False if user pressed q.
        """
        name = os.path.basename(record["filepath"])
        record["tags"] = normalize_tags(list(record["tags"]))
        current_tags = list(record["tags"])
        page_index = 0

        while True:
            console.print(f"[dim][{index}/{total}][/dim]  [bold yellow]{name}[/bold yellow]  [dim]tags: {record['tags']}[/dim]")
            self.print_legend(page_index)

            ch = getch()

            if ch == "\x03":
                console.print("\n[red]Hard abort — nothing saved.[/red]")
                sys.exit(0)

            if ch.lower() == "q":
                return False

            if ch.lower() == "s":
                console.print(f"         [dim]→ skipped (keeping {record['tags']})[/dim]")
                return True

            if ch == "LEFT":
                page_index = (page_index - 1) % max(1, (len(PRESET_TAGS) + PAGE_SIZE - 1) // PAGE_SIZE)
                continue

            if ch == "RIGHT":
                page_index = (page_index + 1) % max(1, (len(PRESET_TAGS) + PAGE_SIZE - 1) // PAGE_SIZE)
                continue

            # Enter or space = done with this file's tags
            if ch in ("\n", "\r", " "):
                console.print(f"         [dim]→ tags: {record['tags']}[/dim]")
                return True

            # Custom tag
            if ch.lower() == "t":
                custom = getline("  Tag:")
                if custom:
                    tag = custom.lower().strip()
                    if tag and tag not in record["tags"]:
                        record["tags"].append(tag)
                        console.print(f"         [green]+ {tag}[/green]")
                continue

            # Preset tag toggle
            visible_tags = page_items(page_index)
            if ch in {str(i + 1) for i in range(len(visible_tags))}:
                idx = int(ch) - 1
                tag = visible_tags[idx]
                if tag in record["tags"]:
                    record["tags"].remove(tag)
                    console.print(f"         [red]- {tag}[/red]")
                else:
                    record["tags"].append(tag)
                    console.print(f"         [green]+ {tag}[/green]")
                record["tags"] = normalize_tags(record["tags"])

    def get_display_value(self, record: dict) -> str:
        tags = record.get("tags", [])
        return ", ".join(tags[:5]) if tags else "—"
