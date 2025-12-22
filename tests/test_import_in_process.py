from multiprocessing import Process, Queue


def test_import_in_process() -> None:
    import impynb

    result_queue: Queue = Queue()

    def run_import() -> None:
        try:
            import sys

            # check that NotebookFinder is already registered because this process
            # is a fork of the main process (which has imported impynb)
            found = False
            for loader in sys.meta_path:
                if isinstance(loader, impynb.NotebookFinder):
                    found = True

            result_queue.put(found)

            from .test_package import (  # type: ignore[attr-defined]
                some_notebook_to_import,
            )

            result_queue.put(some_notebook_to_import is not None)
            result_queue.put(some_notebook_to_import.NOTEBOOK_WAS_IMPORTED is not None)
            result_queue.put(some_notebook_to_import.NOTEBOOK_WAS_IMPORTED)
        except Exception as e:
            result_queue.put(str(e))

    p = Process(target=run_import)
    p.start()
    p.join()

    expected_length = 4
    assert result_queue.qsize() == expected_length

    for i in range(expected_length):
        assert result_queue.get() is True

    assert p.exitcode == 0
