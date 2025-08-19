import impynb  # noqa: F401


def test_import_from_submodule() -> None:
    from .test_package.submodule import is_in_a_submodule

    assert is_in_a_submodule is not None
    assert is_in_a_submodule.NOTEBOOK_WAS_IMPORTED is not None
    assert is_in_a_submodule.NOTEBOOK_WAS_IMPORTED


def test_relative_import_of_notebook_with_from() -> None:
    from .test_package import import_some_local_module

    assert import_some_local_module is not None
    assert import_some_local_module.NOTEBOOK_WAS_IMPORTED_CORRECTLY is not None
    assert import_some_local_module.NOTEBOOK_WAS_IMPORTED_CORRECTLY


def test_relative_import_of_notebook() -> None:
    from .test_package import import_notebook_relative_path

    assert import_notebook_relative_path is not None
    assert import_notebook_relative_path.NOTEBOOK_WAS_IMPORTED is not None
    assert import_notebook_relative_path.NOTEBOOK_WAS_IMPORTED
