
# Getting started with uv

This is not an extensive tutorial on `uv`, but rather a **brief introduction** to some of the tools that we will use in this course. For a more complete guide, check out the [official uv documentation](https://docs.astral.sh/uv/).

## 1. Terminal Commands

Before we start, let's go over some of the `terminal` commands that could be useful during the course.

First of all, what is a `terminal`? A `terminal` is a text-based interface that allows you to interact with your computer's operating system. You can use it to run commands, navigate the file system, and manage files and directories.

On **macOS** and **Linux**, this program is simply called the **Terminal**. On **Windows**, we suggest using **PowerShell** (instead of the older `cmd` Prompt) since most of the commands we will use behave the same way as on macOS and Linux.

:::{tip}
To open the terminal:

- On **macOS**, use the `Command + Space` shortcut to open Spotlight, then type "Terminal" and hit `Enter`.
- On **Windows**, use the `Windows + R` shortcut to open the Run dialog, then type "powershell" and hit `Enter`.
:::

Here are a few basic commands that work on macOS, Linux, and the Windows PowerShell terminal (but not the Windows `cmd` Prompt):

| <span style="display: inline-block; width:120px;">Command</span> | Description |
| -------- | ----------- |
| **`pwd`** | Print the path of the current working directory. |
| **`ls`** | List the contents of the current directory. |
| **`cd [DIR]`** | Change directory to `[DIR]`. <br><small>_If `[DIR]` is not provided, defaults to the home directory._</small> |
| **`mkdir [DIR]`** | Create a new directory named `[DIR]`. |

:::{note}
💡 **Relative paths**: when navigating with `cd`, you can use `.` to refer to the current directory and `..` to refer to the parent directory (for example, `cd ..` moves you up one level).

For example, if you are in `Desktop/bobiac` and want to move to a sibling folder `Desktop/data`, you don't need to type the full path, you can instead go up one level and then into `data`:

```bash
cd ../data
```

:::

## 2. Installing `uv`

To install `uv` you can follow this [uv instruction](https://bobiac.github.io/uv_instruction.html) or follow the [uv documentation](https://docs.astral.sh/uv/getting-started/installation).

## 3. Virtual Environments with uv

As we saw in the [previous section](python_and_uv.md#3-virtual-environments), a **virtual environment** is an isolated workspace with its own `Python` and its own packages. With `uv`, creating one is a single command:

```bash
uv venv
```

By default, this creates a virtual environment in a folder named `.venv` inside your current directory. If you want to give it a different name or location, you can pass a path:

```bash
uv venv my-env
```

### 3.1. Choosing a Python Version with the `-p` Flag

You can also tell `uv` which **version of `Python`** to use inside the new environment with the `-p` (`--python`) flag. If that version isn't already installed on your computer, `uv` will **automatically download and install it** for you.

```bash
uv venv -p 3.13
```

### 3.2. Activating and Deactivating the Environment

Creating an environment doesn't put you "inside" it, you also need to **activate** it. Activation tells your terminal to use the `Python` and packages from that environment instead of any others on your computer. The command differs slightly between operating systems:

| <span style="display: inline-block; width:200px;">OS</span> | Command |
| -------- | ----------- |
| <i class="fab fa-apple"></i> macOS / Linux | `source .venv/bin/activate` |
| <i class="fab fa-windows"></i> Windows (PowerShell) | `.venv\Scripts\activate` |

Once activated, you should see the environment's name appear at the beginning of your terminal prompt (e.g. `(.venv)`), this is `uv` (and your terminal) telling you that the environment is now active. From here, any package you install with `uv pip install` (see below) will be installed **inside this environment only**.

To leave the environment and go back to your computer's normal terminal, simply run:

```bash
deactivate
```

:::{note}
💡 **Remember**: environments are disposable. If anything feels broken, you can always delete the `.venv` folder and recreate it from scratch with `uv venv`.

In order to see folder starting with a dot (like `.venv`), on mac you can use the keyboard shortcut `Command + Shift + .` to toggle hidden files. On Windows, you can go to the `View` tab in the file explorer and check the `Hidden items` box.
:::

### 3.3. Installing Packages with `uv`

Once your virtual environment is **activated**, you can install **packages** into it with `uv pip install`:

```bash
uv pip install numpy
```

You can install **multiple packages** at once by separating them with a space, and even pin a **specific version** of a package:

```bash
uv pip install numpy matplotlib "scikit-image==0.24"
```

To remove a package you no longer need, use `uv pip uninstall`:

```bash
uv pip uninstall matplotlib
```

And to see everything that is currently installed in the active environment, use `uv pip list`:

```bash
uv pip list
```

:::{note}
📦 **What is `pip`?**: `pip` is the standard `Python` package installer, it's what `uv pip install` mimics (and replaces) under the hood. Both `pip` and `uv pip install` download packages from [PyPI](https://pypi.org/), the **Python Package Index**.

Not all packages are published on `PyPI` though. Some, especially in **scientific programming**, are instead only available on [conda-forge](https://conda-forge.org/). `uv` **cannot** install packages from `conda-forge`, if you need one of those, you'll have to use `conda` (or its faster reimplementation `mamba`) or `pixi` instead of `uv`.
:::

## 4. The Python Files and `uv`

`Python` code is usually saved in plain text files ending in **`.py`** (for example `bobiac.py`). Each of these files contains a list of instructions that the `Python` interpreter reads and executes, one after the other, from top to bottom.

### 4.1. Importing Packages in a Python File

As we saw earlier, **packages** give us access to functionality that we don't have to write ourselves. But before we can actually use a package inside a `.py` file, we need to **import** it:

```python
import numpy

print(numpy.mean([1, 2, 3, 4]))
> 2.5
```

This makes everything inside the `numpy` package available, and you access its functions with the `numpy.` prefix.

:::{tip}
✅ **Best practice**: it's good practice to put **all your imports at the very top** of a `.py` file, before any other code. This makes it immediately clear, just by glancing at the first few lines, which packages a script depends on.
:::

Since typing the full package name every time can get tedious, especially for packages with long names, it's common to import a package with a shorter **alias** instead:

```python
import numpy as np

print(np.mean([1, 2, 3, 4]))
> 2.5
```

Here, `np` is just a "nickname" for `numpy`, both refer to the exact same package, but `np` is much quicker to type. This is such a common convention that you'll see `import numpy as np` (and similar aliases, like `import pandas as pd`) at the top of almost every script that uses them.

:::{note}
💡 You can technically choose any alias you like, but it's best to stick to the **conventional ones** (like `np` for `numpy`), since that's what most `Python` programmers will recognize at a glance.
:::

### 4.2. Running Python Files

So far we've created an environment, activated it, and installed packages into it manually. We also created a `.py` file and imported some packages into it. Now we want to **run** that file, which means telling `Python` to read the instructions in the file and execute them.

Once your virtual environment is **activated**, the simplest way to run a `.py` file is with the `python` command, followed by the **path** to the file:

```bash
python path/to/your/script.py
```

This works because, once activated, your terminal's `python` command points to the `Python` interpreter that lives **inside that specific environment**, the one with all the packages you installed in it.

### 4.3. Running Python Files with `uv`

`uv` can also run a `.py` file for you directly, without requiring you to manually create and activate an environment first.

The `uv run` command runs a `Python` script (or any command):

```bash
uv run script.py
```

This is shorthand for `uv run python script.py`. Depending on your situation, this is what actually happens:

1. **No environment was ever created**: if there is no `.venv` folder at all in the current directory, `uv` simply uses (or quickly downloads) a plain `Python` interpreter to run your script, no environment is created on disk for this. If your script only relies on `Python`'s standard library, this works perfectly fine, there is **nothing to install**. But if your script `import`s a third-party package (like `numpy`), it will fail with a `ModuleNotFoundError`, since that package is nowhere to be found.
2. **An environment exists but is _not_ activated**: if you previously created a `.venv` in the current directory with `uv venv` (as we saw [above](#virtual-environments-with-uv)) and installed packages into it, `uv run script.py` will automatically **detect and use that `.venv`**, including everything you installed in it, **even without activating it**. `uv` simply looks for a folder literally named **`.venv`** next to your script.

   :::{note}
   ⚠️ **Custom-named environments**: this auto-detection only works for the **default** `.venv` name. If you created your environment with a custom name (e.g. `uv venv my-env`), `uv run` will **not** find it automatically, you would need to **activate it** first.
   :::

3. **An environment is activated**: if you have **activated** an environment (default-named or not), `uv run script.py` will use that **active environment** and everything installed in it, exactly like running `python script.py` directly.

### 4.4. `uv run --with`

As we just saw, if your `.py` file `import`s a third-party package and there is no environment to provide it, `uv run script.py` fails with a `ModuleNotFoundError`. The `--with` flag fixes exactly that: it tells `uv` to install **extra dependencies**, just for that single run, without needing a `.venv` at all:

```bash
uv run --with numpy script.py
```

You can also pass multiple packages, or even pin a specific version, for example to quickly check that your code still works with an older release of a package:

```bash
uv run --with "numpy==1.26" --with matplotlib script.py
```

### 4.5. The `-p` Flag

You can use the `-p` flag with `uv run` to choose which `Python` version to run the script with, for example if you want to test your code against a version different from the one in your active environment:

```bash
uv run -p 3.11 script.py
```

This is especially handy when you want to quickly check that your code works across different `Python` versions, without having to manually create a new environment for each one.

### 4.6. `uvx` (`uv tool run`)

`uvx` is a shortcut for `uv tool run`: it runs a **command-line tool** provided by a package, installing it into a temporary, isolated environment on the fly, without you ever having to `uv pip install` it yourself.

```bash
uvx ruff check script.py
```

This installs `ruff` into a throwaway environment (if it isn't already cached), then runs the `check` command on `script.py`.

In this course, we will use `uvx` to quickly launch some common tools with a graphical interface, such as `napari` and `cellpose`, without having to install them first:

```bash
uvx "napari[all]"
uvx "cellpose[gui]"
```

:::{note}
💡 `uvx <command>` and `uv tool run <command>` are exactly the same thing, `uvx` is just shorter to type. Notice there is no extra `run` keyword after `uvx`, since `uvx` already means "run".
:::

### 4.7. `uv` and `PEP 723`

A [**PEP**](https://peps.python.org/) (**P**ython **E**nhancement **P**roposal) is a document that describes a new feature or convention for the `Python` language. [**PEP 723**](https://peps.python.org/pep-0723/) is one of these proposals, and it defines a standard way to declare a script's dependencies **directly inside the script itself**, using a special comment block at the top of the file:

```python
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "numpy",
#     "matplotlib",
# ]
# ///

import numpy as np
import matplotlib.pyplot as plt

print(np.mean([1, 2, 3, 4]))
```

This is exactly the kind of block we saw earlier when running `uv run --with`, except now the dependencies travel **with the file**, instead of being typed out on the command line.

This is where `uv` really shines: when you run a `.py` file that contains this `///script` block, `uv` automatically **reads the dependencies**, creates a **temporary environment**, installs everything that's needed, and runs the script, all in one single command:

```bash
uv run script.py
```

No manual environment creation, no `uv pip install`, nothing to set up beforehand. The script is **completely self-contained**: anyone (including future you!) can run it with a single command and get the exact same result, regardless of what is or isn't already installed on their computer.

:::{tip}
🚀 **pyrunner**: if you like the idea of self-contained `Python` scripts, check out [`pyrunner`](https://github.com/fdrgsp/pyrunner), a small **desktop app** (an icon on your computer, just like any other application) built specifically for `PEP 723` scripts. You simply double-click it, select a `.py` (or `.ipynb`) file containing a `///script` block, and it runs the script for you, installing `uv` itself first if it isn't already on your computer.

This is especially useful if you write your own `PEP 723` script and want to share it with **someone who doesn't know how to use `Python` or a terminal**: they can just double-click `pyrunner`, pick your file, and run it, without ever opening a terminal. See the [`pyrunner` repository](https://github.com/fdrgsp/pyrunner) for more details.
:::
