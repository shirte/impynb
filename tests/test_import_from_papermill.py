import os
import tempfile

import papermill as pm


def test_import_from_notebook_env_vars() -> None:
    with tempfile.TemporaryDirectory() as tmpdir:
        relative_notebook_path = (
            "./tests/test_package/import_from_papermill_env_vars.ipynb"
        )

        # set an environment variable to point to the notebook path
        os.environ["NOTEBOOK_PATH"] = os.path.abspath(relative_notebook_path)

        # Test that the notebook can be run with papermill
        pm.execute_notebook(
            relative_notebook_path,
            os.path.join(tmpdir, "result_import_from_papermill_env_vars.ipynb"),
            kernel_name="python3",
            language="python",
        )


def test_import_from_notebook_parameters() -> None:
    with tempfile.TemporaryDirectory() as tmpdir:
        relative_notebook_path = (
            "./tests/test_package/import_from_papermill_parameters.ipynb"
        )

        # Test that the notebook can be run with papermill
        pm.execute_notebook(
            relative_notebook_path,
            os.path.join(tmpdir, "result_import_from_papermill_parameters.ipynb"),
            kernel_name="python3",
            language="python",
            parameters={"NOTEBOOK_PATH": os.path.abspath(relative_notebook_path)},
        )
