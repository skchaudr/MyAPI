"""
Terminal input helpers shared across all triage passes.

Extracted from context_refinery/triage.py lines 89-161.
"""

import sys
import tty
import termios

try:
    from rich.console import Console
except ImportError:
    print("Please run: pip install rich")
    exit(1)

console = Console()


def getch():
    """Read one keypress without Enter."""
    raise NotImplementedError("JULES: Copy from triage.py lines 89-117")


def getline(prompt):
    """Read a line from the user (normal line mode)."""
    raise NotImplementedError("JULES: Copy from triage.py lines 120-139")


def getnum(prompt):
    """Read a number from the user."""
    raise NotImplementedError("JULES: Copy from triage.py lines 142-161")
