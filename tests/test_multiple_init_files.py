import impynb  # noqa: F401


def test_import_from_submodule() -> None:
    from .test_package import submodule_with_multiple_init

    assert submodule_with_multiple_init is not None
    assert submodule_with_multiple_init.MODULE_WAS_IMPORTED is not None
    assert submodule_with_multiple_init.MODULE_WAS_IMPORTED
