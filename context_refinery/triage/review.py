"""Review phase — summary table, confirm, re-edit, execute writes.

Extracted from context_refinery/triage.py lines 500-617.
"""

import os
import uuid
import datetime

from context_refinery.triage.terminal import console, getch, getnum
from context_refinery.triage.writers import parse_file, write_frontmatter, write_related_section
from context_refinery.triage.passes.base import TriagePass

try:
    from rich.table import Table
    from rich.rule import Rule
except ImportError:
    print("Please run: pip install rich")
    exit(1)


def review_phase(records, active_passes: list[TriagePass]):
    """Show summary table, confirm, write frontmatter.

    The table columns should be DYNAMIC — only show columns for passes
    that were actually run.

    Args:
        records: List of triage record dicts.
        active_passes: List of TriagePass instances that were run.

    Returns True if user confirmed, False if cancelled.

    Supports: y=write, n=cancel, r=re-edit a specific file.
    """
    raise NotImplementedError("JULES: Adapt from triage.py lines 502-583, make columns dynamic based on active_passes")


def execute_writes(records):
    """Write updated metadata back to each file's YAML frontmatter.

    For each record:
    1. Parse existing frontmatter + body
    2. Update status, doc_type, tags, projects from record
    3. If record has 'related', call write_related_section() on body
    4. Ensure required fields (id, title, source, created_at, author) exist
    5. Call write_frontmatter() with field ordering per taxonomy spec
    """
    raise NotImplementedError("JULES: Adapt from triage.py lines 586-617, add related support")
