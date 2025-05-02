from impynb import NotebookImportContext, configure, notebook_finder


def test_context_manager_function() -> None:
    """Test the configure() context manager function."""
    # Set initial state
    original_tags = ["original"]
    notebook_finder.config = {"skip_cell_tags": original_tags.copy()}

    # Test the context manager
    test_tags = ["test", "debug"]
    with configure(skip_cell_tags=test_tags):
        # Within context, should have test tags
        assert notebook_finder.config["skip_cell_tags"] == test_tags

    # After context, should be restored to original
    assert notebook_finder.config["skip_cell_tags"] == original_tags


def test_context_manager_class() -> None:
    """Test the NotebookImportContext class directly."""
    # Set initial state
    original_tags = ["initial"]
    notebook_finder.config = {"skip_cell_tags": original_tags.copy()}

    # Test the context manager class
    test_tags = ["class_test"]
    with NotebookImportContext(skip_cell_tags=test_tags):
        # Within context, should have test tags
        assert notebook_finder.config["skip_cell_tags"] == test_tags

    # After context, should be restored to original
    assert notebook_finder.config["skip_cell_tags"] == original_tags


def test_context_manager_exception_safety() -> None:
    """Test that context manager restores settings even when exceptions occur."""
    # Set initial state
    original_tags = ["exception_test"]
    notebook_finder.config = {"skip_cell_tags": original_tags.copy()}

    test_tags = ["should_be_restored"]

    # Test exception handling
    try:
        with configure(skip_cell_tags=test_tags):
            # Within context, should have test tags
            assert notebook_finder.config["skip_cell_tags"] == test_tags
            # Raise an exception
            raise ValueError("Test exception")
    except ValueError:
        pass  # Expected exception

    # After exception, should be restored to original
    assert notebook_finder.config["skip_cell_tags"] == original_tags


def test_context_manager_nested() -> None:
    """Test nested context managers."""
    # Set initial state
    original_tags = ["outer"]
    notebook_finder.config = {"skip_cell_tags": original_tags.copy()}

    outer_tags = ["outer_context"]
    inner_tags = ["inner_context"]

    with configure(skip_cell_tags=outer_tags):
        assert notebook_finder.config["skip_cell_tags"] == outer_tags

        with configure(skip_cell_tags=inner_tags):
            assert notebook_finder.config["skip_cell_tags"] == inner_tags

        # Should restore to outer context
        assert notebook_finder.config["skip_cell_tags"] == outer_tags

    # Should restore to original
    assert notebook_finder.config["skip_cell_tags"] == original_tags


def test_context_manager_default_empty() -> None:
    """Test context manager with default empty skip_cell_tags."""
    # Set initial state
    original_tags = ["some_tags"]
    notebook_finder.config = {"skip_cell_tags": original_tags.copy()}

    with configure():
        assert notebook_finder.config["skip_cell_tags"] == ["some_tags"]

    # Should restore to original
    assert notebook_finder.config["skip_cell_tags"] == original_tags


def test_context_manager_none_input() -> None:
    """Test context manager with None input."""
    # Set initial state
    original_tags = ["some_tags"]
    notebook_finder.config = {"skip_cell_tags": original_tags.copy()}

    with configure(skip_cell_tags=[]):
        assert notebook_finder.config["skip_cell_tags"] == []

    # Should restore to original
    assert notebook_finder.config["skip_cell_tags"] == original_tags
