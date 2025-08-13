import impynb


def test_async() -> None:
    from .test_package import async_cells

    assert async_cells is not None
    assert async_cells.NOTEBOOK_WAS_EXECUTED is not None
    assert async_cells.NOTEBOOK_WAS_EXECUTED
