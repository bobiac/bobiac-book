# juv Exercises

To go through these exercises, you need to create a new folder on your `Desktop` called `bobiac_juv`.

## Exercise 1

**Create a new `Jupyter Notebook` with `uv`'s `juv` tool**

1. Open the Terminal or PowerShell and navigate to the `bobiac_juv` folder.
2. Inside the `bobiac_juv` folder, create a new folder named `nb_folder` and navigate into it.
3. Inside the `nb_folder`, create a new Jupyter Notebook named `my-first-nb.ipynb` using `uv`'s `juv` tool.
4. Run the `my-first-nb.ipynb` notebook in your browser using `juv`.

:::{dropdown} Solution

1. open the Terminal or PowerShell.
2. `cd .../Desktop/bobiac_juv`
3. `mkdir nb_folder`
4. `cd .../Desktop/bobiac_juv/nb_folder`
5. `uvx juv init my-first-nb.ipynb`
6. `uvx juv run my-first-nb.ipynb`

:::

## Exercise 2

**Add dependencies to a `Jupyter Notebook` with `juv`**

1. In the `my-first-nb.ipynb` notebook created in [Exercise 1](#exercise-1), add `matplotlib`, `numpy`, and `pandas` as dependencies using `juv`.
2. Run the notebook with `juv` and import the three libraries in the first cell to confirm that they are installed and can be imported without errors.

    :::{note}
    If you have the `my-first-nb.ipynb` notebook open in your browser, you need to stop it from the terminal (`cmd + c` or `ctrl + c`) and close the browser tab before running the notebook again with `juv` or the new dependencies will not be installed.
    :::

:::{dropdown} Solution

1. `cd .../Desktop/bobiac_juv/nb_folder` (the folder created in [Exercise 1](#exercise-1))
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

## Exercise 3

**Create a `.py` file with the PEP723 `///script` header using `uv`**

1. Open the Terminal or PowerShell and navigate to the `bobiac_juv` folder.
2. Inside the `bobiac_juv` folder, create a new folder named `py_folder` and navigate into it.
3. Use `uv` to create a new Python file named `my_script.py` with the PEP723 `///script` header and Python `3.13`.
4. Add `numpy` and `matplotlib` as dependencies to the `my_script.py` file using `uv`.
5. Run the `my_script.py` file using `uv` to verify that the dependencies are installed and the script runs without errors.
6. Optional: show the dependencies of the `my_script.py` file using `uv tree`.
7. Optional: show the python version used for the `my_script.py` file using `uv python`.

:::{dropdown} Solution

1. open the Terminal or PowerShell.
2. `cd .../Desktop/bobiac_juv`
3. `mkdir py_folder`
4. `cd .../Desktop/bobiac_juv/py_folder`
5. `uv init --script my_script.py -p 3.13`
6. `uv add --script my_script.py numpy matplotlib`
7. `uv run my_script.py`
8. Optional: `uv tree --script my_script.py`
9. Optional: `uv python find --script my_script.py --show-version`

:::
