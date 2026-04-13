"""Tags pass — multi-select tag assignment with toggle.

Extracted from context_refinery/triage.py lines 389-446 (tags_phase).
"""

from context_refinery.triage.passes.base import TriagePass
from context_refinery.triage.terminal import console, getch, getline

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
            key = str(i + 1) if i < 9 else chr(ord("a") + i - 9)
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
        import os
        import sys
        from context_refinery.triage.terminal import console, getch, getline

        name = os.path.basename(record["filepath"])
        current_tags = list(record["tags"])

        console.print(f"[dim][{index+1}/{total}][/dim]  [bold yellow]{name}[/bold yellow]  [dim]tags: {current_tags}[/dim]")

        while True:
            ch = getch()

            if ch == "\x03":
                console.print("\n[red]Hard abort — nothing saved.[/red]")
                sys.exit(0)

            if ch.lower() == "q":
                console.print(f"\n[dim]Stopping tags pass[/dim]")
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
            if ch.isdigit() and ch != "0":
                idx = int(ch) - 1
            elif ch.isalpha() and ord(ch.lower()) >= ord("a"):
                idx = ord(ch.lower()) - ord("a") + 9

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
