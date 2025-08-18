import traceback

import impynb  # noqa: F401


def test_exceptions_from_notebooks() -> None:
    try:
        from .test_package import raises_an_exception  # noqa: F401
    except Exception as e:
        tb = e.__traceback__
        extracted = traceback.extract_tb(tb)
        last_frame = extracted[-1]

        filename = last_frame.filename.rsplit("/", 1)[1]

        assert filename == "raises_an_exception.ipynb[cell-1]"
        assert last_frame.lineno == 2

        # check that the code line is not empty (would be displayed as ???)
        assert last_frame.line is not None
        assert last_frame.line.strip() != ""
