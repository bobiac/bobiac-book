# Group Work 1: Building your Own Spot Detection Pipeline

Let's now consolidate what you have learned! These exercises will walk you through how to create your own Jupyter Notebook containing code that segments images with Cellpose!

To go through these exercises, you need to create a new folder on your `Desktop` called `bobiac_uv_env`.

## Exercise 1

**Create a new `Jupyter Notebook` with `uv`'s `juv` tool**

1. Open the Terminal or PowerShell and navigate to the `bobiac_uv_env` folder.
2. Inside the `bobiac_uv_env` folder, create a new folder named `nb_folder` and navigate into it.
3. Inside the `nb_folder`, create a new Jupyter Notebook named `group_work_1.ipynb` using `uv`'s `juv` tool.
4. Run the notebook in your browser using `juv`.

:::{dropdown} Solution

1. Open the Terminal or PowerShell.
2. `cd .../Desktop/bobiac_uv_env`
3. `mkdir nb_folder`
4. `cd .../Desktop/nb_folder`
5. `uvx juv init group_work_1.ipynb`
6. `uvx juv run group_work_1.ipynb`

:::

## Exercise 2

**Add dependencies to the `Jupyter Notebook` with `juv`**

1. In your notebook created in [Exercise 1](#exercise-1), add your dependencies using `juv`.
2. Run the notebook with `juv` and import the libraries in the first cell to confirm that they are installed and can be imported without errors.

    :::{note}
    If you have the notebook open in your browser, you need to stop it from the terminal (`cmd + c` or `ctrl + c`) and close the browser tab before running the notebook again with `juv` or the new dependencies will not be installed.
    :::

:::{dropdown} Solution

1. `cd .../Desktop/nb_folder` (the folder created in [Exercise 1](#exercise-1))
2. `uvx juv add group_work_1.ipynb cellpose tqdm tifffile spotiflow numpy`
3. `uvx juv run group_work_1.ipynb`  
4. Add a new `code` cell in the notebook (`+` button)
5. Within this cell, import the necessary libraries:

    ```python
    from pathlib import Path

    from cellpose import core, io, models, plot
    from cellpose.models import MODEL_DIR
    from tqdm import tqdm

    import csv

    import tifffile
    from spotiflow.model import Spotiflow
    import numpy as np
    ```

6. Run the cell to confirm that the libraries are imported without errors.

:::

## Exercise 3

**Add code that segments the first two channels of many image files using Cellpose and saves the segmentation result as a tif file**
1. For each step, create a new `code` cell in the notebook (`+` button).
2. Within the cell, add the necessary code.


:::{dropdown} Solution

See [Solution Notebook](group_work_1_solution.ipynb)

:::

## Exercise 4

**Add code that uses Spotiflow to detect spots in the 3rd and 4th channels of the images and saves a .csv file of their coordinates.**
1. For each step, create a new `code` cell in the notebook (`+` button).
2. Within the cell, add the necessary code.


:::{dropdown} Solution

See [Solution Notebook](group_work_1_solution.ipynb)

:::

