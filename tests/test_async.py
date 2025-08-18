import asyncio
from unittest.mock import Mock

import impynb


def test_async(clean_imports: None) -> None:
    from .test_package import async_cells

    assert async_cells is not None
    assert async_cells.NOTEBOOK_WAS_EXECUTED is not None
    assert async_cells.NOTEBOOK_WAS_EXECUTED


def test_custom_event_loop(clean_imports: None) -> None:
    mock_loop = Mock(spec=asyncio.AbstractEventLoop)
    with impynb.configure(event_loop=mock_loop):
        from .test_package import async_cells  # noqa: F401

    mock_loop.run_until_complete.assert_called_once()
