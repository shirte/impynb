import inspect
import os
import sys

from .notebook_finder import NotebookFinder

__all__ = ["init"]


# Important: we have to insert the NotebookFinder at the beginning of sys.meta_path in order to
# account for __init__.ipynb files. Assume the module structure is like this:
#
# mypackage/
#    __init__.ipynb
#    submodule.py
#
# and we try to import like this:
#
#    from mypackage import something
#
# If we insert the NotebookFinder at the end of sys.meta_path, the default import machinery will
# see a package without __init__.py and interpret it as a namespace package (and return a valid
# ModuleSpec). As a consequence, our finder is skipped and will never get the chance to discover
# __init__.ipynb modules.
notebook_finder = NotebookFinder()
sys.meta_path.insert(0, notebook_finder)


def init(skip_cell_tags: list[str] = []) -> None:
    notebook_finder._skip_cell_tags = skip_cell_tags

    caller_frame = inspect.currentframe().f_back
    caller_module_name = caller_frame.f_globals.get("__name__")
    caller_module = sys.modules[caller_module_name]

    if not hasattr(caller_module, "__file__") or caller_module.__file__ is None:
        caller_module.__file__ = caller_module.__vsc_ipynb_file__

    # figure out root package and module name
    script_name = os.path.basename(caller_module.__file__)
    script_module_name = os.path.splitext(script_name)[0]

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
    root_module_name = parent_dirs[0]

    # assign package name
    if not hasattr(caller_module, "__package__") or caller_module.__package__ is None:
        caller_module.__package__ = ".".join(parent_dirs)

    # if sys.path doesn't contain the package path, add it
    if root_module_path not in sys.path:
        sys.path.insert(0, root_module_path)
