from __future__ import annotations

import importlib
import importlib.util
from collections.abc import Sequence
from importlib.machinery import ModuleSpec
from pathlib import Path
from types import ModuleType
from typing import TYPE_CHECKING

from .notebook_loader import NotebookLoader

if TYPE_CHECKING:
    from _typeshed.importlib import MetaPathFinderProtocol
else:
    MetaPathFinderProtocol = object


class NotebookFinder(MetaPathFinderProtocol):
    def __init__(self, skip_cell_tags: list[str] = []) -> None:
        self._skip_cell_tags = skip_cell_tags

    def find_spec(
        self,
        fullname: str,
        path: Sequence[str] | None,
        target: ModuleType | None = None,
        /,
    ) -> ModuleSpec | None:
        print("FIND_SPEC", fullname, path, target)

        if path is None:
            return None

        name = fullname.rsplit(".", 1)[-1]

        notebook_path = None
        is_package = False
        for d in path:
            # Check for a package (directory with __init__.ipynb)
            pkg_dir = Path(d) / name
            init_nb = pkg_dir / "__init__.ipynb"
            if init_nb.is_file():
                notebook_path = init_nb
                is_package = True
                break

            tmp = Path(d) / f"{name}.ipynb"
            if tmp.is_file():
                notebook_path = tmp
                is_package = False  # for clarity
                break

        if notebook_path is None:
            return None

        loader = NotebookLoader(notebook_path, skip_cell_tags=self._skip_cell_tags)
        print("SPEC_FROM_LOADER", fullname, notebook_path, is_package)
        spec = importlib.util.spec_from_loader(
            fullname, loader, origin=str(notebook_path), is_package=is_package
        )
        return spec

    def __repr__(self) -> str:
        return f"NotebookFinder(skip_cell_tags={self._skip_cell_tags})"
