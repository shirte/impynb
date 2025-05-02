from __future__ import annotations

from collections.abc import Generator
from contextlib import contextmanager
from types import TracebackType

from typing_extensions import Unpack

from .notebook_finder import NotebookFinder, NotebookFinderConfigUpdate

__all__ = ["NotebookImportContext", "configure"]

notebook_finder = NotebookFinder()


class NotebookImportContext:
    """
    Context manager for temporarily configuring notebook import settings.
    """

    def __init__(self, **kwargs: Unpack[NotebookFinderConfigUpdate]) -> None:
        self._new_config = kwargs

    def __enter__(self) -> NotebookImportContext:
        # Store original settings
        self._original_config = notebook_finder.config.copy()

        # Apply new settings
        notebook_finder.config = self._new_config

        return self

    def __exit__(
        self,
        exc_type: type | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        # Restore original settings
        notebook_finder.config = self._original_config


@contextmanager
def configure(
    **kwargs: Unpack[NotebookFinderConfigUpdate],
) -> Generator[None, None, None]:
    """
    Context manager for temporarily configuring notebook import settings.

    Args:
        skip_cell_tags: List of cell tags to skip during notebook import

    Example:
        with configure(skip_cell_tags=['test', 'debug']):
            import my_notebook  # Will skip cells tagged with 'test' or 'debug'
    """
    with NotebookImportContext(**kwargs):
        yield
