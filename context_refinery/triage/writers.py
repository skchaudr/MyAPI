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
    """Read a markdown file and extract frontmatter + body.

    Returns (dict, str) — frontmatter dict and body text.
    """
    raise NotImplementedError("JULES: Copy from triage.py lines 166-186")


def preview(filepath):
    """Return first meaningful line after frontmatter (max 90 chars)."""
    raise NotImplementedError("JULES: Copy from triage.py lines 189-205")


def write_frontmatter(filepath, frontmatter, body):
    """Write updated YAML frontmatter + body back to file.

    Field order per docs/02-target-output.md:
    id, title, source, created_at, author, status, doc_type, tags, projects, related
    """
    raise NotImplementedError("JULES: Copy from triage.py lines 208-229")


def write_related_section(body, related_filenames):
    """Inject or replace a ## Related section at the bottom of the note body.

    Args:
        body: The markdown body text (without frontmatter).
        related_filenames: List of filenames (without .md extension) to link.

    Returns:
        Updated body string with ## Related section containing [[wiki-links]].
        If ## Related already exists, replace its content.
    """
    raise NotImplementedError("JULES: NEW — implement per spec")


def gather_files(directory):
    """Gather all .md files from directory recursively, sorted."""
    raise NotImplementedError("JULES: Copy from triage.py lines 232-236")


def make_record(filepath, frontmatter):
    """Create a triage record dict for a file with current metadata.

    Returns dict with keys: filepath, status, doc_type, tags, projects.
    """
    raise NotImplementedError("JULES: Copy from triage.py lines 241-249")
