import impynb


def test_import_from_submodule() -> None:
    from .test_package.submodule import is_in_a_submodule

    assert is_in_a_submodule is not None
    assert is_in_a_submodule.NOTEBOOK_WAS_IMPORTED is not None
    assert is_in_a_submodule.NOTEBOOK_WAS_IMPORTED
