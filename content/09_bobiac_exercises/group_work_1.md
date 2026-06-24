# Group Work 1

Let's now consolidate what you have learned! These excercises will walk you through how to create your own Jupyter Notebook containing code that segments images with Cellpose!

To go through these exercises, you need to create a new folder on your `Desktop` called `bobiac_uv`.

## Exercise 1

**Create a Python Environment with `uv` and Install `numpy` & `matplotlib`**

1. Open the Terminal or PowerShell and navigate to the `bobiac_uv` folder.
2. Create a new virtual environment with `uv` in the `bobiac_uv_env` folder named `my-env`.
3. Activate the newly created `my-env` virtual environment.
4. Install `numpy` and `matplotlib` in the `my-env` virtual environment.
5. List the installed packages in the `my-env` virtual environment to confirm that `numpy` and `matplotlib` are installed.
6. Deactivate the `my-env` virtual environment.

:::{dropdown} Solution

1. open the Terminal or PowerShell.
2. `cd .../Desktop/bobiac_uv`
3. `uv venv my-env`
4. `source my-env/bin/activate` (Linux/macOS) or `my-env\Scripts\activate` (Windows)
5. `uv pip install numpy matplotlib`
6. `uv pip list`
7. `deactivate`

:::

## Exercise 2

**Create a new `Jupyter Notebook` with `uv`'s `juv` tool**

1. Open the Terminal or PowerShell and navigate to the `bobiac_uv` folder.
2. Inside the `bobiac_uv` folder, create a new folder named `nb_folder` and navigate into it.
3. Inside the `nb_folder`, create a new Jupyter Notebook named `my-first-nb.ipynb` using `uv`'s `juv` tool.
4. Run the `my-first-nb.ipynb` notebook in your browser using `juv`.

:::{dropdown} Solution

1. open the Terminal or PowerShell.
2. `cd .../Desktop/bobiac_uv`
3. `mkdir nb_folder`
4. `cd .../Desktop/nb_folder`
5. `uvx juv init my-first-nb.ipynb`
6. `uvx juv run my-first-nb.ipynb`

:::

## Exercise 3

**Add dependencies to a `Jupyter Notebook` with `juv`**

1. In the `my-first-nb.ipynb` notebook created in [Exercise 2](#exercise-2), add `matplotlib`, `numpy`, and `pandas` as dependencies using `juv`.
2. Run the notebook with `juv` and import the three libraries in the first cell to confirm that they are installed and can be imported without errors.

    :::{note}
    If you have the `my-first-nb.ipynb` notebook open in your browser, you need to stop it from the terminal (`cmd + c` or `ctrl + c`) and close the browser tab before running the notebook again with `juv` or the new dependencies will not be installed.
    :::

:::{dropdown} Solution

1. `cd .../Desktop/nb_folder` (the folder created in [Exercise 2](#exercise-2))
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


