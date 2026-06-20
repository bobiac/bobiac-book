# 02 - <i class="fab fa-python"></i> Getting Started with Python and `uv`

## Lesson Overview

The goal of this section is to gain a basic understanding of:

1. What Python is.
2. How to install it (we will use `uv`) and where it "lives" on your computer.
3. How to run Python code.
4. What packages are and how to install them.
5. What virtual environments are, why they are useful, and how to create them.

We will focus on using [`uv`](#uv-cheat-sheet) to manage Python versions,
create virtual environments, and install packages.

## Slides

<a
    class="custom-button custom-download-button" href="../../pdfs/02_getting_started_with_python/getting_started_python_uv.pdf" download> <i class="fas fa-download"></i> Download the Slides
</a>

<div align="center">
  <iframe class="custom-pdf-frame-34" src="../../pdfs/02_getting_started_with_python/getting_started_python_uv.pdf"> </iframe>
</div>

## Notes

Here is a summary of some of the most useful commands and concepts that we cover
in the lecture for this section.

### Terminal commands

Here are some basic terminal commands that will help you use the
command line effectively.  These commands work for macOS,
Linux, and the Windows PowerShell terminal (but not the windows `cmd` Prompt).

```{tip}
Reminder, To open the terminal:

- On macOS, you can use the `Command + Space` shortcut to
open Spotlight, then type "Terminal" and hit `Enter`.
- On Windows, you can use the `Windows + R` shortcut to open the Run dialog,
then type "powershell" and hit `Enter`.
```

| <span style="display: inline-block; width:100px;">Command</span>  | Description |
| -------- | ----------- |
| **`ls`** | List directory contents. |
| **`cd [DIR]`** | Change directory to `[DIR]`. <br><small>_If `[DIR]` is not provided, defaults to the home directory._</small> |
| **`pwd`** | Print the current working directory. |
| **`mkdir [DIR]`** | Create a new directory named `[DIR]`. |

```{tip}
When using relative paths, you can use `..` to refer to the parent directory,
and `.` to refer to the current directory.
```

### `uv` cheat sheet

[`uv`]((https://docs.astral.sh/uv/)) is a fast, one-stop-shop for managing
Python versions, virtual environments, and packages.  It is an _excellent_ tool
to learn if you want to get started quickly with Python.

Here are some common `uv` commands that will help you get started using Python
with `uv`.  We will use them throughout this book.

| <span style="display: inline-block; width:275px;">Command</span>  | Description |
| -------- | ----------- |
| **`uv help <COMMAND>`** | Useful way to get help on a specific `<COMMAND>`. |
| **`uv venv [ENV_PATH]`** | Create a virtual environment at the specified `ENV_PATH`.<br><small>👍 _If `[ENV_PATH]` is not provided, defaults to `.venv` in the current directory_.</small> |
| <i class="fab fa-apple"></i> `source .venv/bin/activate`<br><i class="fab fa-windows"></i> `.venv\Scripts\activate` | Activate the virtual environment in the path `.venv` |
| **`uv pip install   [PACKAGE]`**<br>**`uv pip uninstall [PACKAGE]`** | Install or uninstall `PACKAGE` in the current virtual environment.  May use multiple packages separated by space. |
| **`uv pip list`** | List all installed packages in the current virtual environment. |
| <hr> | <hr> |
| **`uv run script.py`** | Run a Python script `script.py` in an on-demand virtual environment. See details [below](#uv-run) |
| <a name="uvx"></a>**`uvx <COMMAND>`**<br>_short for:_<br>**`uv tool run <COMMAND>`**<br>  | Run a `<COMMAND>` provided by a Python package _of the same name_. <br>✨ _This creates an environment, installs the package, and then invokes the command all in one step!_</small> |
| **`uv <COMMAND> -p <PYTHON>`** | Use the specified version of python (e.g. `-p 3.10`).<br><small>_This flag works with `uv tool run`, and `uv venv` commands._</small> |

<small>_... For complete docs, see [Getting started with
uv](https://docs.astral.sh/uv/getting-started/)._</small>

```{note}
While we will not be covering it here, `uv` is also frequently used for
[**project management**](https://docs.astral.sh/uv/guides/projects/).  If you
see references to commands like `uv init`, `uv sync`, `uv add`, or `uv remove`,
these are only relevant in the context of using `uv` for project management.
```

### `uv` ↔️ `conda` translation table

```{tip}
If you are already familiar with `conda`, here is a quick translation table to
help you understand how `uv` commands map to `conda` commands:

| <span style="display: inline-block; width:245px;">`uv` command</span> | <span style="display: inline-block; width:140px;">`conda` equivalent</span>  | Description |
| -------- | ------------------ | ----------- |
| **`uv venv`** | **`conda create`** | Create a new env |
| **<i class="fab fa-apple"></i> `source .venv/bin/activate`**<br> <i class="fab fa-windows"></i> **`.venv\Scripts\activate`** | **`conda activate`** | Activate the virtual environment in the path `.venv` |
| **`uv pip install`** | **`conda install`** | Install a package into the env |
| **`uv pip uninstall`** | **`conda remove`** | Remove a package from the env |
| **`uv pip list`** | **`conda list`** | List all packages in the env |
```

### `uv run`

`uv run` is a command that allows you to run a command or script in an on-demand
virtual environment.

If you have a simple python script named `hello.py`, that has _no_ dependencies:

```python
print("Hello, world!")
```

You can run it with:

```bash
uv run hello.py
```

... which is shorthand for `uv run python hello.py`.

<small>_... For complete docs, see
[Running scripts](https://docs.astral.sh/uv/guides/scripts/)._</small>

### `uv run` with additional dependencies

A particulary useful feature of `uv run` is that you can specify dependencies
_in your script_ using a special syntax in a comment at the top of the file.

For example, the following `example_script.py` uses _two_ packages, `requests`
and `rich`, to download and print a JSON file downloaded from the internet in a
nice format:

```python
# /// script
# dependencies = ["requests<3", "rich"]
# ///

import requests
from rich import print

resp = requests.get("https://jsonplaceholder.typicode.com/posts")
print(resp.json())
```

With `uv` you can run this script _without_ having to first create an
environment and install the necessary dependencies, simply
by running:

```bash
uv run example_script.py
```

<small>_... For complete docs, see [Declaring script
dependencies](https://docs.astral.sh/uv/guides/scripts/#declaring-script-dependencies)._</small>

### Running Jupyter notebooks with `juv`

💡 _Think of `juv` as `uv run` for Jupyter notebooks._

`juv` is a command line tool built on top of `uv` that provides a
convenient way to run a Jupyter notebook, with all the necessary
dependencies, in an on-demand virtual environment.

It is built on the following concepts:

1. As we saw [above](#uvx): `uvx juv` is shorthand for "run the
   command `juv` from the package `juv`.
2. As we saw [above](#uv-run-with-additional-dependencies): `uv` can read
   dependencies specified inside of a script.
3. `juv` just brings along the necessary Jupyter notebook dependencies and
   parses the dependencies from the top of your notebook for `uv`.

| <span style="display: inline-block; width:310px;">Command</span>  | Description |
| -------- | ----------- |
| **`uvx juv init <name.ipynb>`** | Initialize a new Jupyter notebook named `<name.ipynb>`. |
| **`uvx juv add <name.ipynb> <PACKAGE>`** | Add a new dependency to the comment at the top of `<name.ipynb>`. |
| **`uvx juv run <name.ipynb>`** | Launch a Jupyter notebook server and run the notebook `<name.ipynb>`. |

<small>_... For complete docs, see the [`juv` repository](https://github.com/manzt/juv)._</small>

## FROM PYTHON FOR BIOIMAGE ANALYSIS NOTEBOOK
## 0. Importing Libraries
### Concept

Python is powerful in part because of its wide array of *external libraries*. An **external Python library (also called a Python package)** is a publicly available code base containing functions and other tools not already included internally in Python. While you could write your own Python code to conduct tasks, you can save significant time and effort by using other developers' libraries. 

We are going to be using a few external Python libraries in this lesson, so we will start by learning how to specify them in our code. This practice is called specifying or importing our **dependencies**. It's standard practice to import all dependencies at the very beginning of your code.

<p class="alert alert-info">
    <strong>Note:</strong> In Python, there is an important distinction between <i><b>installing</b></i> a library and <i><b>importing</b></i> a library. Installing a library means downloading it onto your computer so that it is available for use. Importing a library means telling Python to make that library's functionality available in your current code. In this lesson setup, uv has installed all necessary libraries already for you, so you only need to worry about importing!
</p>

### How to import a library
First, it's important to review a library's information to learn how to import and use it correctly. The website [pypi.org](https://pypi.org) allows you to easily search external Python libraries and learn how to install them. This webpage will also give a brief description of the library, and typically will contain a link to access its documentation. The documentation will then contain detailed information about how to use the library. 

Below is an example of an external library, its PyPi page, and its documentation. 

| Library Name | PyPi Link | Documentation Link | 
|---------|----------------|----------------|
| `ndv` | [ndv](https://pypi.org/project/ndv/) | [ndv](https://pyapp-kit.github.io/ndv/latest/) |

In reviewing this pypi page, we see that `ndv` is an n-dimensional array viewer that can be used to view images. We can import it to use in our code with the line:
```python
import ndv
```
### Importing with an alias
Sometimes libraries will have long names that can be prone to typos. To simplify code, you can create an alias for a library when you import them.

```python
# importing a library without alias
import tifffile

# importing a library with alias
import tifffile as tiff
```
### Only importing a portion of a library
Sometimes, you will only need to use a small portion of a large library. You can import only certain modules from a library in two different ways: 

```python
from matplotlib import pyplot # option 1
import matplotlib.pyplot # option 2
```

Here, `pyplot` is a module within the library `matplotlib`. 

### Combining approaches: importing a portion of a library with an alias
```python
import matplotlib.pyplot as plt
```