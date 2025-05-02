import sys

import pytest


@pytest.fixture
def clean_imports() -> None:
    to_remove = [k for k in sys.modules if k.startswith("tests.test_package")]
    for k in to_remove:
        del sys.modules[k]
