import sys
import os
from rich.console import Console
from rich.rule import Rule
from .base import TriagePass
from ..terminal import getch, getline

console = Console()

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
        console.print("[dim]Toggle tags by number/letter, press [t] for custom, [Enter/Space] when done[/dim]")
        for i, tag in enumerate(PRESET_TAGS):
            key = str(i + 1) if i < 9 else chr(ord('a') + i - 9)
            console.print(f"  [{key}] {tag}", end="")
            if (i + 1) % 6 == 0:
                console.print()
        if len(PRESET_TAGS) % 6 != 0:
            console.print()

    def process_file(self, record: dict, index: int, total: int, all_records: list = None) -> bool:
        if index == 0:
            console.print()
            console.print(Rule(f"[bold cyan]PHASE — {self.name}[/bold cyan]"))
            self.print_legend()

        name = os.path.basename(record["filepath"])
        if "tags" not in record:
            record["tags"] = []

        current_tags = list(record["tags"])

        console.print(f"[dim][{index+1}/{total}][/dim]  [bold yellow]{name}[/bold yellow]  [dim]tags: {current_tags}[/dim]")

        while True:
            ch = getch()

            if ch == "\x03":
                console.print("\n[red]Hard abort — nothing saved.[/red]")
                sys.exit(0)

            if ch.lower() == "q":
                console.print(f"\n[dim]Stopping {self.name.lower()} pass[/dim]")
                return False

            if ch in ("\n", "\r", " "):
                console.print(f"         [dim]→ tags: {record['tags']}[/dim]")
                return True

            if ch.lower() == "t":
                custom = getline("  Tag:")
                if custom:
                    tag = custom.lower().strip()
                    if tag and tag not in record["tags"]:
                        record["tags"].append(tag)
                        console.print(f"         [green]+ {tag}[/green]")
                continue

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
        return ", ".join(tags[:5]) or "[dim]—[/dim]"
