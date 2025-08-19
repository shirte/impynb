# impynb

Import Jupyter notebooks as Python modules!

## Installation

```bash
pip install impynb
```

## Usage

Assume your project looks like this:

```
my-project/
  my_project/
    __init__.py
    my_notebook.ipynb
    my_module.py
    util.py
  pyproject.toml
```

You can import notebooks from Python modules:

```python
# my_module.py
import impynb
from .my_notebook import some_function  # <-- import notebook
some_function(3, 4)
```

Importing local Python modules from notebooks also works:

```python
# cell in my_notebook.ipynb
import impynb
from .util import add_two_numbers  # <-- import local Python module

def some_function(a, b):
  return add_two_numbers(a, b)
```

## Features

* **Understands package initializers**: Module initializers (`__init__.py`) can also be written as
  Python notebooks (`__init__.ipynb`). If a package contains both files, only `__init__.py` will be used and `__init__.ipynb` is ignored for consistency reasons.
  ```python
  # my-package/my_package/my_module/__init__.ipynb (first cell)
  variable = 42

  # my-package/my_package/main.py
  import impynb
  from . import my_module
  my_module.variable  # 42
  ```
* **Async code**: Notebook cells containing async code will be executed in the default event loop:
  ```python
  # my_notebook.ipynb
  from asyncio import sleep
  await sleep(0.1)
  variable = 42

  # my_module.py
  import impynb
  from . import my_notebook
  my_notebook.variable  # 42
  ```
  The event loop can be configured ([see below](#custom-event-loop)).
* **Exception handling**: Exceptions thrown in notebooks are displayed correctly in the stack trace
  ```python
  # my_notebook.ipynb (first cell)
  raise NotImplementedError()

  # my_module.py
  import impynb
  from .my_notebook import *
  # raises an exception containing the problematic cell:
  #
  #   File ".../my_module.py", line 2
  #     from .my_notebook import *
  #     ^^^^^^^^^^^^^^^^^^^^^^^^^^
  #   ...
  #   File ".../my_notebook.ipynb[cell-0]", line 1, in <module>
  #     raise NotImplementedError()
  ```
* **Code Cell Filtering**: Notebook cells marked with a comment `#!ignore` at the top will be
  skipped when importing the notebook.
  ```python
  #!ignore
  # this code will not run when importing the notebook
  some_heavy_computation()
  ```
* **Advanced configuration**: The module can be configured to use different markers for ignorable
  cells or a custom event loop ([see below](#advanced-configuration)).

## Advanced configuration

The package can be configured

```python
import impynb

impynb.init()

# configuration only applies for imports *after* init() call
from .my_notebook import nice_function
```

### Skip tagged cells

Cells in Jupyter notebooks can be tagged. You can configure `impynb` to skip executing cells having
a specific tag on them:

```python
import impynb
impynb.init(skip_cell_tags=['test'])
```

### Custom event loop

Executing async code will run in the default event loop if not specified otherwise. However,
`impynb` can be configured to use a different event loop:
```python
import asyncio
import impynb

my_event_loop = asyncio.new_event_loop()
impynb.init(event_loop=my_event_loop)

# async cells will be run in the custom event loop
from . import my_notebook
```

### Context manager

The package provides a context manager for a temporary reconfiguration of import settings:

```python
import impynb

with impynb.configure(skip_cell_tags=['test']):
  # will ignore cells tagged as "test"
  from . import my_notebook

# will not ignore cells anymore
import . from my_other_notebook
```

All arguments of the `impynb.init` method are also available in `impynb.configure`.

## Compatibility

`impynb` was tested on the following Jupyter platforms:

* ✅ VSCode: via `__vsc_ipynb_file__` variable ([source][vsc_ipynb_file_answer])
* ✅ Jupyter Notebooks: via `JPY_SESSION_NAME` environment variable or `__session__` as fallback
  ([source][jpy_session_name_answer])
* ✅ Jupyter Lab: same as Jupyter Notebooks
* ✅ Google Colab: creates a virtual Python module with a name based on the `COLAB_NOTEBOOK_ID` env
  variable in the working directory (usually /content). Since a valid Python module requires an
  `__init__.py` (or `__init__.ipynb`) file, you need to create one of these files in the working
  directory to import modules from there.
* ⚪ Papermill: provides no indication about the current notebook name or path (as far as I know)
  and the user needs to provide this manually (see above)

## License

This project is licensed under the **BSD 3-Clause "New" or "Revised" License**. See the [LICENSE](LICENSE) file for details.

[vsc_ipynb_file_answer]: https://web.archive.org/web/20250818234724/https://stackoverflow.com/questions/12544056/how-do-i-get-the-current-ipython-jupyter-notebook-name/72498672#72498672
[jpy_session_name_answer]: https://web.archive.org/web/20250818235421/https://stackoverflow.com/questions/12544056/how-do-i-get-the-current-ipython-jupyter-notebook-name/77904549#77904549
