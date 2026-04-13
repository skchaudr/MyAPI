"""Runner — interactive menu + orchestrator for triage passes.

This is the main entry point. Presents a menu to select passes,
runs them in order, then hands off to review.
"""

import os
import sys

from context_refinery.triage.terminal import console, getch
from context_refinery.triage.writers import parse_file, gather_files, make_record
from context_refinery.triage.passes import StatusPass, DocTypePass, TagsPass, ProjectsPass, LinksPass
from context_refinery.triage.review import review_phase, execute_writes

try:
    from rich.rule import Rule
except ImportError:
    print("Please run: pip install rich")
    exit(1)


def show_menu():
    """Display the triage console menu. Returns list of pass classes to run.

    Menu options:
      [1] Full pipeline (status → doc_type → tags → projects → links → review)
      [2] Status only
      [3] Doc type only
      [4] Tags only
      [5] Projects only
      [6] Links only
      [7] Custom (pick passes)
      [q] Quit
    """
    raise NotImplementedError("JULES: Implement menu per spec")


def run_passes(records, pass_classes):
    """Instantiate and run each pass over the records.

    For each pass class:
    1. Instantiate it (LinksPass needs all_records kwarg)
    2. Print a Rich Rule with the pass name
    3. Call pass.print_legend()
    4. For each record, call pass.process_file(record, index, total)
    5. If process_file returns False (user quit), stop this pass

    Returns list of active TriagePass instances (for dynamic review columns).
    """
    raise NotImplementedError("JULES: Implement per spec")


def main():
    """Entry point — parse args, load files, show menu, run passes, review.

    Usage:
      python3 -m context_refinery.triage [directory]
      python3 -m context_refinery.triage file1.md file2.md ...

    Same CLI interface as the original triage.py.
    """
    raise NotImplementedError("JULES: Adapt from triage.py lines 622-677, add menu dispatch")
