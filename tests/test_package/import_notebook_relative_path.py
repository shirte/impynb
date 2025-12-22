from . import some_notebook_to_import  # type: ignore[attr-defined]

assert some_notebook_to_import is not None

NOTEBOOK_WAS_IMPORTED = some_notebook_to_import.NOTEBOOK_WAS_IMPORTED
