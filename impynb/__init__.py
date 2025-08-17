import inspect
import logging
import os
import sys
from typing import Optional

from .import_context import NotebookImportContext, configure
from .notebook_finder import NotebookFinder
from .util import get_notebook_path, is_running_in_notebook

__all__ = ["init", "configure", "NotebookImportContext"]

logger = logging.getLogger(__name__)


# Important: we have to insert the NotebookFinder at the beginning of sys.meta_path in
# order to account for __init__.ipynb files. Assume the module structure is like this:
#
# mypackage/
# |- __init__.ipynb
# |- submodule.py
#
# and we try to import like this:
#
#    from mypackage import something
#
# If we insert the NotebookFinder at the end of sys.meta_path, the default import
# machinery will see a package without __init__.py and interpret it as a namespace
# package (and return a valid ModuleSpec). As a consequence, our finder were to be
# skipped and would have never get the chance to discover __init__.ipynb modules.
notebook_finder = NotebookFinder()
sys.meta_path.insert(0, notebook_finder)


def init(notebook_path: Optional[str] = None) -> None:
    if not is_running_in_notebook():
        return

    # get notebook path
    if notebook_path is None:
        notebook_path = get_notebook_path()

        if notebook_path is None:
            return

    # get frame of the code that called this function
    caller_frame = inspect.currentframe()
    while (
        caller_frame is not None
        and caller_frame.f_globals.get("__name__") != "__main__"
    ):
        # move to the next frame
        caller_frame = caller_frame.f_back

    if caller_frame is None:
        raise RuntimeError("Cannot get caller frame")

    # get the module name of the caller
    caller_module_name = caller_frame.f_globals.get("__name__")
    if caller_module_name is None:
        raise RuntimeError("Cannot determine caller module name")

    # get the module object of the caller
    caller_module = sys.modules[caller_module_name]

    # assign notebook path to the caller module
    if not hasattr(caller_module, "__file__") or caller_module.__file__ is None:
        caller_module.__file__ = notebook_path

    # figure out root package and module name
    script_path = caller_module.__file__

    parent_dirs: list[str] = []
    while True:
        script_path = os.path.dirname(script_path)

        dir_name = os.path.basename(script_path)

        # check if dir contains __init__.py
        if os.path.isfile(os.path.join(script_path, "__init__.py")):
            # add dir to the beginning of the list
            parent_dirs.insert(0, dir_name)
        else:
            break

        # arrived at the root of the filesystem
        if script_path == os.path.dirname(script_path):
            break

    assert len(parent_dirs) > 0, "Not a proper package, because no __init__.py found"

    root_module_path = script_path

    # assign package name
    if not hasattr(caller_module, "__package__") or caller_module.__package__ is None:
        caller_module.__package__ = ".".join(parent_dirs)

    # if sys.path doesn't contain the package path, add it
    if root_module_path not in sys.path:
        sys.path.insert(0, root_module_path)


# We call init() here to ensure that impynb is properly initialized when using it
# directly in a notebook file, e.g. my_notebook.ipynb. When init() is called in a Python
# script, it will do nothing, yet. When we import a notebook (e.g. from my_notebook
# import some_function), the NotebookFinder will kick in and initialize the notebook
# import context.
init()
