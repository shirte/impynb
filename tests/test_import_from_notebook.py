import impynb


def test_relative_import_of_notebook_as_module() -> None:
    from .test_package import import_some_local_module

    assert import_some_local_module is not None
    assert import_some_local_module.NOTEBOOK_WAS_IMPORTED_CORRECTLY is not None
    assert import_some_local_module.NOTEBOOK_WAS_IMPORTED_CORRECTLY
