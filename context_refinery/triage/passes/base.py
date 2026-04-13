"""Abstract base class for all triage passes."""

from abc import ABC, abstractmethod


class TriagePass(ABC):
    """All passes share the same interaction contract."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Display name for the pass (e.g., 'MATURITY STATUS')."""

    @abstractmethod
    def print_legend(self) -> None:
        """Print the keypress legend for this pass."""

    @abstractmethod
    def process_file(self, record: dict, index: int, total: int) -> bool:
        """Process a single file. Returns True to continue, False to stop (q pressed).

        Mutates record in-place.
        """

    @abstractmethod
    def get_display_value(self, record: dict) -> str:
        """Return the current value for this pass (shown in review table)."""
