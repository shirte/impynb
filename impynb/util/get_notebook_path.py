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

    if ipython is None:
        return None

    #
    # vscode notebooks
    #
    vsc_ipynb_file = ipython.user_ns.get("__vsc_ipynb_file__")
    if vsc_ipynb_file is not None and os.path.isfile(vsc_ipynb_file):
        return cast(str, vsc_ipynb_file)

    #
    # Jupyter lab / notebook
    #
    jupyter_notebook_path = os.environ.get("JPY_SESSION_NAME")
    if jupyter_notebook_path is not None and os.path.isfile(jupyter_notebook_path):
        return jupyter_notebook_path

    session = cast(Optional[str], globals().get("__session__"))
    if session is not None and os.path.isfile(session):
        return session

    #
    # Others (e.g. Google Colab)
    #
    paths = ipython.user_ns.get("_dh", [])
    if len(paths) > 0:
        path = ipython.user_ns["_dh"][0]

        # Notebooks on Google Colab are not stored as files, but they are executed in
        # the context directory given by the `_dh` variable (usually /content/).
        # -> we pretend that there is a notebook with the colab notebook ID as its name
        #    in the context directory
        colab_notebook_id = os.environ.get("COLAB_NOTEBOOK_ID")
        if colab_notebook_id is not None:
            filename = f"{colab_notebook_id}.ipynb"
        else:
            return None

        return os.path.join(path, filename)

    return None
