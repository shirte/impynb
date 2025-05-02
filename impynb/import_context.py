from collections.abc import Generator
from contextlib import contextmanager
from types import TracebackType
from typing import Optional

from .notebook_finder import NotebookFinder

__all__ = ["NotebookImportContext", "configure"]

notebook_finder = NotebookFinder()


class NotebookImportContext:
    """
    Context manager for temporarily configuring notebook import settings.
    """

    def __init__(self, skip_cell_tags: Optional[list[str]] = None):
        self.skip_cell_tags = skip_cell_tags or []
        self._original_skip_cell_tags: Optional[list[str]] = None

    def __enter__(self) -> "NotebookImportContext":
        # Store original settings
        self._original_skip_cell_tags = notebook_finder._skip_cell_tags.copy()

        # Apply new settings
        notebook_finder._skip_cell_tags = self.skip_cell_tags.copy()

        return self

    def __exit__(
        self,
        exc_type: Optional[type],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None:
        # Restore original settings
        if self._original_skip_cell_tags is not None:
            notebook_finder._skip_cell_tags = self._original_skip_cell_tags


@contextmanager
def configure(skip_cell_tags: Optional[list[str]] = None) -> Generator[None, None, None]:
    """
    Context manager for temporarily configuring notebook import settings.

    Args:
        skip_cell_tags: List of cell tags to skip during notebook import

    Example:
        with configure(skip_cell_tags=['test', 'debug']):
            import my_notebook  # Will skip cells tagged with 'test' or 'debug'
    """
    with NotebookImportContext(skip_cell_tags):
        yield
