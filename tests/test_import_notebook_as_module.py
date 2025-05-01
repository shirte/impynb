import impynb


def test_relative_import_of_notebook_as_module() -> None:
    from .test_package import some_notebook_to_import

    assert some_notebook_to_import is not None
    assert some_notebook_to_import.NOTEBOOK_WAS_IMPORTED is not None
    assert some_notebook_to_import.NOTEBOOK_WAS_IMPORTED
