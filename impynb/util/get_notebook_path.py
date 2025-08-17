import os
from typing import Optional, cast


def get_notebook_path() -> Optional[str]:
    """
    Get the path of the current Jupyter Notebook.

    Returns:
        str: The path to the current notebook.
    """
    from IPython import get_ipython

    ipython = get_ipython()

    #
    # vscode notebooks
    #
    if ipython is not None:
        vsc_ipynb_file = ipython.user_ns.get("__vsc_ipynb_file__")
        if vsc_ipynb_file is not None:
            return cast(str, vsc_ipynb_file)

    #
    # Jupyter lab / notebook
    #
    if "JPY_SESSION_NAME" in os.environ:
        jupyter_notebook_path = os.environ.get("JPY_SESSION_NAME")
        if jupyter_notebook_path is not None and os.path.isfile(jupyter_notebook_path):
            return jupyter_notebook_path

    if "__session__" in globals():
        session = cast(Optional[str], globals()["__session__"])
        if session is not None and os.path.isfile(session):
            return session

    return None
