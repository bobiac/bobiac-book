# `uv` and `juv`

## Exercise 1

**Create a Python Environment with `uv` and Install `numpy` & `matplotlib`**

1. Create a new folder on your `Desktop` named `bobiac_uv_env`.
2. Open the Terminal or PowerShell and navigate to the `bobiac_uv_env` folder.
3. Create a new virtual environment with `uv` in the `bobiac_uv_env` folder named `my-env`.
4. Activate the newly created `my-env` virtual environment.
5. Install `numpy` and `matplotlib` in the `my-env` virtual environment.
6. List the installed packages in the `my-env` virtual environment to confirm that `numpy` and `matplotlib` are installed.
7. Deactivate the `my-env` virtual environment.

:::{dropdown} Solution

1. create a new folder on your `Desktop` called `bobiac_uv_env` (e.g. `cd .../Desktop` then `mkdir bobiac_uv_env` if you are using Terminal or PowerShell).
2. open the Terminal or PowerShell (if you haven't already).
3. `cd .../Desktop/bobiac_uv_env`
4. `uv venv my-env`
5. `source my-env/bin/activate` (Linux/macOS) or `my-env\Scripts\activate` (Windows)
6. `uv pip install numpy matplotlib`
7. `uv pip list`
8. `deactivate`

:::

## Exercise 2

**Create a new `Jupyter Notebook` with `uv`'s `juv` tool**

1. Create a new folder on your `Desktop` named `bobiac_uv_nb`.
2. Open the Terminal or PowerShell and navigate to the `bobiac_uv_nb` folder.
3. Create a new Jupyter Notebook named `my-first-nb.ipynb` using `uv`'s `juv` tool.
4. Run the `my-first-nb.ipynb` notebook in your browser using `juv`.

:::{dropdown} Solution

1. create a new folder on your `Desktop` called `bobiac_uv_nb` (e.g. `cd .../Desktop` then `mkdir bobiac_uv_nb` if you are using Terminal or PowerShell).
2. open the Terminal or PowerShell (if you haven't already).
3. `cd .../Desktop/bobiac_uv_nb`
4. `uvx juv init my-first-nb.ipynb`
5. `uvx juv run my-first-nb.ipynb`

:::

## Exercise 3

**Add dependencies to a `Jupyter Notebook` with `juv`**

1. In the `my-first-nb.ipynb` notebook created in [Exercise 2](#exercise-2), add `matplotlib`, `numpy`, and `pandas` as dependencies using `juv`.
2. Run the notebook with `juv` and import the three libraries in the first cell to confirm that they are installed and can be imported without errors.

    :::{note}
    If you have the `my-first-nb.ipynb` notebook open in your browser, you need to stop it from the terminal (`cmd + c` or `ctrl + c`) and close the browser tab before running the notebook again with `juv` or the new dependencies will not be installed.
    :::

:::{dropdown} Solution

1. `cd .../Desktop/bobiac_uv_nb` (the folder created in [Exercise 2](#exercise-2))
2. `uvx juv add my-first-nb.ipynb numpy pandas matplotlib`
3. `uvx juv run my-first-nb.ipynb`  
4. add a new `code` cell in the notebook (`+` button)
5. within this cell, import the three libraries:

    ```python
    import matplotlib
    import numpy as np
    import pandas as pd
    ```

6. Run the cell to confirm that the libraries are imported without errors.

:::

## Exercise 4

**Create a `.py` file with the PEP723 `///script` header using `uv`**

1. Create a new folder on your `Desktop` named `bobiac_uv_py`.
2. Open the Terminal or PowerShell and navigate to the `bobiac_uv_py` folder.
3. Use `uv` to create a new Python file named `my_script.py` with the PEP723 `///script` header and Python `3.13`.
4. Add `numpy` and `matplotlib` as dependencies to the `my_script.py` file using `uv`.
5. Run the `my_script.py` file using `uv` to verify that the dependencies are installed and the script runs without errors.
6. Optional: show the dependencies of the `my_script.py` file using `uv tree`.
7. Optional: show the python version used for the `my_script.py` file using `uv python`.

:::{dropdown} Solution

1. create a new folder on your `Desktop` called `bobiac_uv_py` (e.g. `cd .../Desktop` then `mkdir bobiac_uv_py` if you are using Terminal or PowerShell).
2. open the Terminal or PowerShell (if you haven't already).
3. `cd .../Desktop/bobiac_uv_py`
4. `uv init --script my_script.py -p 3.13`
5. `uv add --script my_script.py numpy matplotlib`
6. `uv run my_script.py`
7. Optional: `uv tree --script my_script.py`
8. Optional: `uv python find --script my_script.py --show-version`

:::
