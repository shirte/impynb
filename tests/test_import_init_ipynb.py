import impynb  # noqa: F401


def test_import_init_ipynb() -> None:
    from .test_package.submodule_with_init_ipynb import (
        NOTEBOOK_WAS_IMPORTED,
        VARIABLE_WAS_SET,
    )

    assert NOTEBOOK_WAS_IMPORTED is not None
    assert NOTEBOOK_WAS_IMPORTED

    assert VARIABLE_WAS_SET is not None
    assert VARIABLE_WAS_SET
