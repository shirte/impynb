from __future__ import annotations

import importlib
import importlib.util
from asyncio import AbstractEventLoop
from collections.abc import Sequence
from importlib.machinery import ModuleSpec
from pathlib import Path
from types import ModuleType
from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from .notebook_loader import NotebookLoader

if TYPE_CHECKING:
    from _typeshed.importlib import MetaPathFinderProtocol
else:
    MetaPathFinderProtocol = object


class NotebookFinderConfig(TypedDict, total=False):
    skip_cell_tags: list[str] | None
    event_loop: AbstractEventLoop | None


class NotebookFinder(MetaPathFinderProtocol):
    #
    # Singleton
    #
    _instance: NotebookFinder | None = None

    def __new__(cls) -> NotebookFinder:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    #
    # Constructor
    #
    def __init__(self) -> None:
        self._config = NotebookFinderConfig(
            skip_cell_tags=[],
            event_loop=None,
        )

    #
    # Configuration
    #
    @property
    def config(self) -> NotebookFinderConfig:
        return self._config

    @config.setter
    def config(self, value: NotebookFinderConfig) -> None:
        self._config.update(value)

    #
    # Find Spec
    #
    def find_spec(
        self,
        fullname: str,
        path: Sequence[str] | None,
        target: ModuleType | None = None,
        /,
    ) -> ModuleSpec | None:
        if path is None:
            return None

        name = fullname.rsplit(".", 1)[-1]

        notebook_path = None
        is_package = False
        for d in path:
            # Check for a package (directory with __init__.ipynb)
            # BUT: if the package contains a __init__.py AND a __init__.ipynb file,
            # we prefer the __init__.py file and skip loading the notebook.
            pkg_dir = Path(d) / name
            init_nb = pkg_dir / "__init__.ipynb"
            init_py = pkg_dir / "__init__.py"
            if init_nb.is_file() and not init_py.is_file():
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

        loader = NotebookLoader(
            notebook_path,
            skip_cell_tags=self._config["skip_cell_tags"],
            event_loop=self._config["event_loop"],
        )
        spec = importlib.util.spec_from_loader(
            fullname, loader, origin=str(notebook_path), is_package=is_package
        )
        return spec
