def is_running_in_notebook() -> bool:
    """
    Check if the code is running in a Jupyter Notebook environment.

    Returns:
        bool: True if running in a Jupyter Notebook, False otherwise.
    """
    from IPython import get_ipython

    ipython = get_ipython()
    if ipython is None:
        return False

    if "IPKernelApp" in ipython.config:
        return True

    return False
