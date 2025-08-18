import impynb


def test_ignoring_cells(clean_imports: None) -> None:
    with impynb.configure(skip_cell_tags=[]):
        from .test_package import contains_ignorable_cells

    assert contains_ignorable_cells is not None
    assert contains_ignorable_cells.NOTEBOOK_WAS_IMPORTED is not None
    assert contains_ignorable_cells.NOTEBOOK_WAS_IMPORTED

    assert not hasattr(
        contains_ignorable_cells, "CELL_WITH_SPECIAL_COMMENT_WAS_IGNORED"
    )

    # without further configuration, the cell with a tag should not be ignored
    assert contains_ignorable_cells.CELL_WITH_TAG_WAS_IGNORED is not None
    assert not contains_ignorable_cells.CELL_WITH_TAG_WAS_IGNORED


def test_ignoring_cells_with_skip_cell_tags(clean_imports: None) -> None:
    # we configure impynb to skip cells with the tag "remove_cell"
    with impynb.configure(skip_cell_tags=["remove_cell"]):
        from .test_package import contains_ignorable_cells

    # now, the cell with a tag should be ignored
    assert not hasattr(contains_ignorable_cells, "CELL_WITH_TAG_WAS_IGNORED")
