from __future__ import annotations

from collections.abc import Generator
from contextlib import contextmanager
from types import TracebackType

from typing_extensions import Unpack

from .notebook_finder import NotebookFinder, NotebookFinderConfig

__all__ = ["NotebookImportContext", "configure"]

notebook_finder = NotebookFinder()


class NotebookImportContext:
    """
    Context manager for temporarily configuring notebook import settings.
    """

    def __init__(self, **kwargs: Unpack[NotebookFinderConfig]) -> None:
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
    **kwargs: Unpack[NotebookFinderConfig],
) -> Generator[None, None, None]:
    """
    Context manager for temporarily configuring notebook import settings.

    Parameters
    ----------
    skip_cell_tags : list[str]
        List of cell tags to skip during notebook import
    event_loop : AbstractEventLoop
        Custom asyncio event loop to use during import

    Yields
    -------
    None
        This context manager yields no value.

    See Also
    --------
    NotebookImportContext : The class that handles the actual configuration.

    Examples
    --------

    Using custom cell tags:
    >>> with configure(skip_cell_tags=['test', 'debug']):
    ...     import my_notebook  # Will skip cells tagged with 'test' or 'debug'

    Using a custom event loop:
    >>> import asyncio
    >>> my_event_loop = asyncio.new_event_loop()
    >>> with configure(event_loop=my_event_loop):
    ...    import my_notebook  # Will use the specified event loop for async operations
    """
    with NotebookImportContext(**kwargs):
        yield
