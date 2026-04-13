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
    tty_in = None
    if sys.stdin.isatty():
        stream = sys.stdin
    else:
        try:
            tty_in = open("/dev/tty", encoding="utf-8")
            stream = tty_in
        except OSError:
            stream = sys.stdin

    if not stream.isatty():
        console.print("[red]This script needs an interactive terminal.[/red]")
        sys.exit(1)

    fd = stream.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setcbreak(fd)
        ch = stream.read(1)
    finally:
        try:
            termios.tcsetattr(fd, termios.TCSAFLUSH, old)
        except termios.error:
            pass
        if tty_in is not None:
            tty_in.close()
    return ch


def getline(prompt):
    """Read a line from the user (normal line mode)."""
    console.print(f"[bold]{prompt}[/bold] ", end="")
    tty_in = None
    try:
        if sys.stdin.isatty():
            stream = sys.stdin
        else:
            try:
                tty_in = open("/dev/tty", encoding="utf-8")
                stream = tty_in
            except OSError:
                stream = sys.stdin

        return stream.readline().strip()
    except (EOFError, OSError):
        return ""
    finally:
        if tty_in is not None:
            tty_in.close()


def getnum(prompt):
    """Read a number from the user."""
    console.print(f"\n[bold]{prompt}[/bold] ", end="")
    tty_in = None
    try:
        if sys.stdin.isatty():
            stream = sys.stdin
        else:
            try:
                tty_in = open("/dev/tty", encoding="utf-8")
                stream = tty_in
            except OSError:
                stream = sys.stdin

        return int(stream.readline().strip())
    except (ValueError, EOFError, OSError):
        return None
    finally:
        if tty_in is not None:
            tty_in.close()
