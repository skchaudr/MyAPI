"""
File parsing and frontmatter writing utilities.

Extracted from context_refinery/triage.py lines 166-249.
"""

import os
import glob
import yaml
import uuid
import datetime

try:
    from rich.console import Console
except ImportError:
    print("Please run: pip install rich")
    exit(1)

console = Console()


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
        "status", "doc_type", "tags", "projects", "related",
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


def write_related_section(body, related_filenames):
    """Inject or replace a ## Related section at the bottom of the note body.

    Args:
        body: The markdown body text (without frontmatter).
        related_filenames: List of filenames (without .md extension) to link.

    Returns:
        Updated body string with ## Related section containing [[wiki-links]].
        If ## Related already exists, replace its content.
    """
    import re
    if not related_filenames:
        return body

    links = "\n".join(f"- [[{fn}]]" for fn in related_filenames)
    section = f"\n## Related\n{links}"

    # Match the ## Related section up to the next section or end of string
    pattern = r"\n## Related\b.*?(?=\n\n## |\Z)"

    if re.search(pattern, body, re.DOTALL):
        body = re.sub(pattern, section, body, count=1, flags=re.DOTALL)
    else:
        body = body.rstrip() + "\n" + section

    return body

def gather_files(directory):
    """Gather all .md files from directory."""
    pattern = os.path.join(directory, "**", "*.md")
    files = sorted(glob.glob(pattern, recursive=True))
    return files


def make_record(filepath, frontmatter):
    """Create a triage record for a file with current metadata."""
    return {
        "filepath": filepath,
        "status": frontmatter.get("status", "scratchpad"),
        "doc_type": frontmatter.get("doc_type", "note"),
        "tags": [str(t) for t in (frontmatter.get("tags") or [])],
        "projects": [str(p) for p in (frontmatter.get("projects") or [])],
        "related": [str(r) for r in (frontmatter.get("related") or [])],
    }
