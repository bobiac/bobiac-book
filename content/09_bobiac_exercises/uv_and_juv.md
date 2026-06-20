# `uv` and `juv`

To go through these exercises, you need to create a new folder on your `Desktop` called `bobiac_uv`.

## Exercise 1

**Create a Python Environment with `uv` and Install `numpy` & `matplotlib`**

1. Open the Terminal or PowerShell and navigate to the `bobiac_uv` folder.
2. Create a new virtual environment with `uv` in the `bobiac_uv` folder named `my-env`.
3. Activate the newly created `my-env` virtual environment.
4. Install `numpy` and `matplotlib` in the `my-env` virtual environment.
5. List the installed packages in the `my-env` virtual environment to confirm that `numpy` and `matplotlib` are installed.

:::{dropdown} Solution

1. `cd .../Desktop/bobiac_uv`
2. `uv venv my-env`
3. `source my-env/bin/activate` (Linux/macOS) or `my-env\Scripts\activate` (Windows)
4. `uv pip install numpy matplotlib`
5. `uv pip list`

:::

## Exercise 2

**Create a new `Jupyter Notebook` with `uv`'s `juv` tool**

1. In the`bobiac_uv` folder, create a new Jupyter Notebook named `my-first-nb.ipynb` using ``uv`'s`juv` tool.
2. Run the `my-first-nb.ipynb` notebook in your browser using `juv`.

:::{dropdown} Solution

1. `cd .../Desktop/bobiac_uv`
2. `uvx juv init my-first-nb.ipynb`
3. `uvx juv run my-first-nb.ipynb`

:::

## Exercise 3

**Add dependencies to a `Jupyter Notebook` with `juv`**

1. In the `my-first-nb.ipynb` notebook created in [Exercise 2](#exercise-2), add `matplotlib`, `numpy`, and `pandas` as dependencies using `juv`.
2. Run the notebook with `juv` and import the three libraries in the first cell to confirm that they are installed and can be imported without errors.

    :::{note}
    If you have the `my-first-nb.ipynb` notebook open in your browser, you need to stop it from the terminal (`cmd + c` or `ctrl + c`) and close the browser tab before running the notebook again with `juv` or the new dependencies will not be installed.
    :::

:::{dropdown} Solution

1. `cd .../Desktop/bobiac_uv`
2. `uvx juv add matplotlib numpy pandas -n my-first-nb.ipynb`
3. `uvx juv run my-first-nb.ipynb`  
4. add a new `code` cell in the notebook (`+` button)
5. within this cell, import the three libraries:

    ```python
    import matplotlib
    import numpy as np
    import pandas as pd
    ```

6. Run the cell to confirm that the libraries are imported without errors.
