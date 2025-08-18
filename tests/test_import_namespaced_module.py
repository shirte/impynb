import impynb  # noqa: F401


def test_relative_import_of_notebook_as_module() -> None:
    from .test_package.namespaced_module import module

    assert module is not None
    assert module.NOTEBOOK_WAS_IMPORTED is not None
    assert module.NOTEBOOK_WAS_IMPORTED
