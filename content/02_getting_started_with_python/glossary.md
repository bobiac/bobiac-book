
# Glossary

A quick reference for the key terms and concepts used throughout this course.

| Term | aka | Definition |
| ---- | ------------- | ---------- |
| **Alias** | | A shorter nickname given to a package when importing it (e.g. `import numpy as np` makes `np` an alias for `numpy`). Conventional aliases (like `np`, `pd`, `plt`) are widely recognized and should be preferred. |
| **API** | | **A**pplication **P**rogramming **I**nterface. A defined set of functions and rules that lets you interact with a library, service, or program. When you call `numpy.mean(...)`, you are using `numpy`'s API. |
| **Cell** | | The basic unit of a `Jupyter Notebook`. Each cell contains either `Python` code or text (Markdown) and can be run independently. |
| **conda-forge** | | A community-maintained package repository, common in scientific computing. Packages hosted there cannot be installed with `uv` — use `conda`, `mamba`, or `pixi` instead. |
| **Dependencies** | Packages, Libraries | The external packages that a script or notebook needs in order to run. |
| **IDE** | | **I**ntegrated **D**evelopment **E**nvironment. A code editor with extras like syntax highlighting, autocomplete, error detection, and AI tools. [VS Code](https://code.visualstudio.com) is a popular free choice. |
| **Import** | | A statement (`import package_name`) that makes a package's functionality available inside a script or notebook cell. Packages must be imported before they can be used, even if they are already installed. |
| **Interpreter** | Python Interpreter | The program installed on your computer that reads and executes `Python` code. When you run `python script.py`, the interpreter is what actually runs the instructions. |
| **Jupyter Notebook** | `.ipynb` file | An interactive file format (`.ipynb` — **i**nteractive **py**thon **n**ote**b**ook) that lets you write and run `Python` code in small chunks called _cells_, and mix code with text, images, and equations. |
| **JupyterLab** | | The browser-based application used to open and work with `Jupyter Notebooks`. Launched automatically by `uvx juv run`. |
| **juv** | | A command-line tool built on top of `uv`, specifically designed for `Jupyter Notebooks`. It reads the `///script` block of a notebook and automatically sets up the environment before launching `JupyterLab`. |
| **Kernel** | | The `Python` process running behind a `Jupyter Notebook`. All cells in a notebook share the same kernel. If something goes wrong (stale state, infinite loop), you can restart it with the ⟳ button. |
| **Library** | Package, Dependency | See **Package**. |
| **Module** | | A single `.py` file containing `Python` code (functions, classes, variables) that can be imported. A **package** is a collection of modules grouped together. For example, `matplotlib.pyplot` is the `pyplot` module inside the `matplotlib` package. |
| **Package** | Library, Dependency | A collection of `Python` code grouped together to provide a specific set of functionality (e.g. `numpy` for numerical computing). Packages must be installed before they can be imported. |
| **PEP** | | **P**ython **E**nhancement **P**roposal. A document that describes a new feature or convention for the `Python` language. See [peps.python.org](https://peps.python.org/). |
| **PEP 723** | | A `PEP` that defines a standard way to declare a script's dependencies directly inside the file itself, using a `///script` comment block. Both `uv` and `juv` use this standard. |
| **`///script` block** | inline script metadata | The special comment block defined by `PEP 723`, placed at the top of a `.py` or `.ipynb` file to declare its `Python` version and package dependencies. |
| **pip** | | The standard `Python` package installer. `uv pip install` mimics and replaces it. Packages are downloaded from `PyPI`. |
| **Python** | | Both the **programming language** (the rules and syntax for writing instructions) and the **interpreter** (the program that reads and executes those instructions). |
| **Python Version** | | The specific release of `Python` in use (e.g. `3.11`, `3.12`, `3.13`). Different projects may require different versions; `uv` can install and manage multiple versions side by side. |
| **PyPI** | Python Package Index | The central online repository at [pypi.org](https://pypi.org/) from which `pip` and `uv pip install` download packages. |
| **Standard Library** | | The collection of packages that come bundled with `Python` and are available by default, without any installation (e.g. packages for working with files, dates, or CSV data). |
| **Terminal** | Command line, Shell | A text-based interface for interacting with your computer's operating system. On macOS/Linux it is called the **Terminal**; on Windows, use **PowerShell**. |
| **uv** | | A modern, extremely fast tool for managing `Python` versions, virtual environments, and packages — all in one. Used via the `uv` command in the terminal. |
| **uvx** | `uv tool run` | A shortcut for `uv tool run`. Runs a command-line tool from a package on the fly, installing it into a temporary isolated environment without any manual install step. |
| **Virtual Environment** | `.venv`, env | An isolated workspace (a folder on your computer) containing its own `Python` interpreter and its own installed packages, completely separate from other environments. Prevents package conflicts between projects. |

<br>

# `uv` ↔️ `conda` Translation Table

If you are already familiar with `conda`, here is a quick translation table to help you understand how `uv` commands map to `conda` commands:

| <span style="display: inline-block; width:245px;">`uv` command</span> | <span style="display: inline-block; width:140px;">`conda` equivalent</span> | Description |
| -------- | ------------------ | ----------- |
| **`uv venv`** | **`conda create`** | Create a new virtual environment. |
| <i class="fab fa-apple"></i> `source .venv/bin/activate`<br><i class="fab fa-windows"></i> `.venv\Scripts\activate` | **`conda activate`** | Activate the virtual environment. |
| **`uv pip install [PACKAGE]`** | **`conda install`** | Install a package into the active environment. |
| **`uv pip uninstall [PACKAGE]`** | **`conda remove`** | Remove a package from the active environment. |
| **`uv pip list`** | **`conda list`** | List all packages in the active environment. |
