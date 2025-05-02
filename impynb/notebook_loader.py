from __future__ import annotations

import linecache
from importlib.abc import Loader
from pathlib import Path
from pprint import pp
from types import ModuleType

import nbformat
from IPython.core.interactiveshell import InteractiveShell

from .util import is_runnable_cell


class NotebookLoader(Loader):
    def __init__(self, path: Path, skip_cell_tags: list[str] = []) -> None:
        self._shell = InteractiveShell.instance()
        self._path = path
        self._skip_cell_tags = skip_cell_tags

    def exec_module(self, mod: ModuleType) -> None:
        if mod.__spec__ is None:
            raise ImportError(f"Module {mod.__name__} has no spec")

        if mod.__spec__.origin is None:
            raise ImportError(f"Module {mod.__name__} has no origin")

        # load the notebook object
        with open(mod.__spec__.origin, encoding="utf-8") as f:
            nb = nbformat.read(f, 4)

        # check
        assert nb["metadata"]["language_info"]["name"] == "python"

        # extra work to ensure that magics that would affect the user_ns
        # actually affect the notebook module's ns
        save_user_ns = self._shell.user_ns
        self._shell.user_ns = mod.__dict__

        mod.__dict__["__file__"] = mod.__spec__.origin
        mod.__path__ = [str(self._path.parent)]  # necessary for __init__.ipynb files

        try:
            for i, cell in enumerate(nb.cells):
                if is_runnable_cell(cell, self._skip_cell_tags):
                    # transform the input to executable Python
                    code = self._shell.input_transformer_manager.transform_cell(cell.source)

                    # create a pseudo filename for the code object
                    pseudo_filename = f"{mod.__spec__.origin}[cell-{i}]"

                    # add the code to linecache so that traceback are correct
                    linecache.cache[pseudo_filename] = (
                        len(code),
                        None,
                        code.splitlines(keepends=True),
                        pseudo_filename,
                    )

                    # compile the code to a code object
                    code_obj = compile(
                        code,
                        pseudo_filename,
                        "exec",
                        dont_inherit=True,
                    )

                    # run the code
                    exec(code_obj, mod.__dict__)
        finally:
            self._shell.user_ns = save_user_ns
