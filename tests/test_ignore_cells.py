import impynb


def test_ignoring_cells() -> None:
    from .test_package import contains_ignorable_cells

    assert contains_ignorable_cells is not None
    assert contains_ignorable_cells.NOTEBOOK_WAS_IMPORTED is not None
    assert contains_ignorable_cells.NOTEBOOK_WAS_IMPORTED

    assert not hasattr(contains_ignorable_cells, "CELL_WAS_IGNORED")
