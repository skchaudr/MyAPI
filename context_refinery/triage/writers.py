"""
File parsing and frontmatter writing utilities.

Extracted from context_refinery/triage.py lines 166-249.
"""

import os
import glob
import yaml
import uuid
import datetime
import re

try:
    from rich.console import Console
except ImportError:
    print("Please run: pip install rich")
    exit(1)

console = Console()


def parse_file(filepath):
    """Read a markdown file and extract frontmatter + body.

    Returns (dict, str) — frontmatter dict and body text.
    """
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
    """Return first meaningful line after frontmatter (max 90 chars)."""
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
    """Write updated YAML frontmatter + body back to file.

    Field order per docs/02-target-output.md:
    id, title, source, created_at, author, status, doc_type, tags, projects, related
    """
    # Field order per docs/02-target-output.md
    ordered = {}
    field_order = [
        "id", "title", "source", "created_at", "author",
        "status", "doc_type", "tags", "projects", "related"
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
    if not related_filenames:
        return body

    related_content = "## Related\n" + "\n".join(f"- [[{filename}]]" for filename in related_filenames)

    # Try to find existing ## Related section
    # Note: we should replace its content, but NOT consume preceding/following sections under different headers.

    # Let's split by lines to handle this cleanly
    lines = body.split('\n')
    new_lines = []
    in_related = False
    replaced = False

    for line in lines:
        if line.startswith("## Related"):
            in_related = True
            replaced = True
            new_lines.append(related_content)
            continue

        if in_related:
            if line.startswith("#"):
                # We reached another header, stop ignoring lines
                in_related = False
                new_lines.append(line)
        else:
            new_lines.append(line)

    if not replaced:
        # Need to append
        if new_lines and new_lines[-1].strip() != "":
            new_lines.append("")
        new_lines.append(related_content)

    return "\n".join(new_lines).strip() + "\n" # Add trailing newline for formatting


def gather_files(directory):
    """Gather all .md files from directory recursively, sorted."""
    pattern = os.path.join(directory, "**", "*.md")
    files = sorted(glob.glob(pattern, recursive=True))
    return files


def make_record(filepath, frontmatter):
    """Create a triage record dict for a file with current metadata.

    Returns dict with keys: filepath, status, doc_type, tags, projects, related.
    """
    return {
        "filepath": filepath,
        "status": frontmatter.get("status", "scratchpad"),
        "doc_type": frontmatter.get("doc_type", "note"),
        "tags": [str(t) for t in (frontmatter.get("tags") or [])],
        "projects": [str(p) for p in (frontmatter.get("projects") or [])],
        "related": [str(r) for r in (frontmatter.get("related") or [])]
    }
