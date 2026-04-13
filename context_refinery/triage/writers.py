import re
import os
import yaml
from rich.console import Console

console = Console()

def parse_file(filepath):
    """Parse a markdown file into (frontmatter_dict, body_string)."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            try:
                fm = yaml.safe_load(parts[1]) or {}
                body = parts[2].lstrip()
                return fm, body
            except yaml.YAMLError:
                pass
    return {}, content

def write_frontmatter(filepath, frontmatter, body):
    """Write YAML frontmatter and body back to the file."""
    # Ensure correct ordering
    ordered = {}
    ordered_keys = ["id", "title", "source", "created_at", "author", "status", "doc_type", "tags", "projects", "related"]

    for key in ordered_keys:
        if key in frontmatter:
            ordered[key] = frontmatter[key]

    for key, val in frontmatter.items():
        if key not in ordered:
            ordered[key] = val

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("---\n")
        yaml.dump(ordered, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
        f.write("---\n")

        # Don't add extra newline if title starts immediately
        if body.startswith("# "):
            f.write(body)
        else:
            f.write(f"# {ordered.get('title', 'Untitled')}\n\n{body}")

def write_related_section(body: str, related_filenames: list) -> str:
    """Injects or replaces the `## Related` section at the bottom of the note body."""
    if not related_filenames:
        return body

    related_block = "\n\n## Related\n"
    for name in related_filenames:
        related_block += f"- [[{name}]]\n"

    related_pattern = re.compile(r'\n*## Related\n(?:- \[\[.*?\]\]\n?)*', re.IGNORECASE)

    if related_pattern.search(body):
        body = related_pattern.sub(related_block, body)
    else:
        body = body.rstrip() + related_block

    return body
