from nbformat import NotebookNode


def is_runnable_cell(cell: NotebookNode, skip_cell_tags: list[str] = []) -> bool:
    """
    Check if a cell is runnable in a Jupyter notebook.

    Args:
        cell: A cell from a Jupyter notebook.
        skip_cell_tags: A list of tags for cells that should be skipped.

    Returns:
        bool: True if the cell is runnable, False otherwise.
    """

    # check if the cell is a code cell
    if not hasattr(cell, "cell_type") or cell.cell_type != "code":
        return False

    if cell.source.strip().startswith("#!ignore"):
        return False

    for tag in skip_cell_tags:
        if tag in cell.metadata.get("tags", []):
            return False

    return True
