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


class TagsPass(TriagePass):

    @property
    def name(self) -> str:
        return "TAGS"

    def print_legend(self) -> None:
        """Print the tag keypress legend with numbered/lettered presets."""
        parts = []
        for i, tag in enumerate(PRESET_TAGS):
            if i < len(KEYS):
                key = KEYS[i]
                parts.append(f"[bold][{key}][/bold] {tag}")
        console.print("  " + "  ".join(parts))
        console.print(
            "\n  [bold][t][/bold] type custom  "
            "[bold][enter/space][/bold] done with tags  "
            "[bold][q][/bold] done with all files\n"
        )

    def process_file(self, record: dict, index: int, total: int) -> bool:
        """Toggle tags for one file. t=custom, enter/space=done, q=quit all.

        Returns True to continue, False if user pressed q.
        """
        name = os.path.basename(record["filepath"])
        current_tags = list(record["tags"])

        console.print(f"[dim][{index}/{total}][/dim]  [bold yellow]{name}[/bold yellow]  [dim]tags: {current_tags}[/dim]")

        while True:
            ch = getch()

            if ch == "\x03":
                console.print("\n[red]Hard abort — nothing saved.[/red]")
                sys.exit(0)

            if ch.lower() == "q":
                return False

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
            idx = None
            if ch in KEYS:
                idx = KEYS.index(ch)

            if idx is not None and 0 <= idx < len(PRESET_TAGS):
                tag = PRESET_TAGS[idx]
                if tag in record["tags"]:
                    record["tags"].remove(tag)
                    console.print(f"         [red]- {tag}[/red]")
                else:
                    record["tags"].append(tag)
                    console.print(f"         [green]+ {tag}[/green]")

    def get_display_value(self, record: dict) -> str:
        tags = record.get("tags", [])
        return ", ".join(tags[:5]) if tags else "—"
