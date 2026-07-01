# juv Exercises

To go through these exercises, you need to create a new folder on your `Desktop` called `bobiac_juv`.

## Exercise 1

**Create a new `Jupyter Notebook` with `uv`'s `juv` tool**

1. Open the Terminal or PowerShell and navigate to the `bobiac_juv` folder.
2. Inside the `bobiac_juv` folder, create a new folder named `nb_folder` and navigate into it.
3. Inside the `nb_folder`, create a new Jupyter Notebook named `bobiac_nb.ipynb` using `uv`'s `juv` tool.
4. Run the `bobiac_nb.ipynb` notebook in your browser using `juv`.

:::{dropdown} Solution

1. open the Terminal or PowerShell.
2. `cd .../Desktop/bobiac_juv`
3. `mkdir nb_folder`
4. `cd .../Desktop/bobiac_juv/nb_folder`
5. `uvx juv init bobiac_nb.ipynb`
6. `uvx juv run bobiac_nb.ipynb`

:::

## Exercise 2

**Add dependencies to a `Jupyter Notebook` with `juv`**

1. In the `bobiac_nb.ipynb` notebook created in [Exercise 1](#exercise-1), add `matplotlib`, `numpy`, and `pandas` as dependencies using `juv`.
2. Run the notebook with `juv` and import the three libraries in the first cell to confirm that they are installed and can be imported without errors.

    :::{note}
    If you have the `bobiac_nb.ipynb` notebook open in your browser, you need to stop it from the terminal (`cmd + c` or `ctrl + c`) and close the browser tab before running the notebook again with `juv` or the new dependencies will not be installed.
    :::

:::{dropdown} Solution

1. `cd .../Desktop/bobiac_juv/nb_folder` (the folder created in [Exercise 1](#exercise-1))
2. `uvx juv add bobiac_nb.ipynb numpy pandas matplotlib`
3. `uvx juv run bobiac_nb.ipynb`  
4. add a new `code` cell in the notebook (`+` button)
5. within this cell, import the three libraries:

    ```python
    import matplotlib
    import numpy as np
    import pandas as pd
    ```

6. Run the cell to confirm that the libraries are imported without errors.

:::
