# Group Work 1: Building your Own Spot Detection Pipeline

Let's now consolidate what you have learned! These exercises will walk you through how to create your own Jupyter Notebook containing code that segments images with Cellpose and detects spots with Spotiflow.

The images we will use for this exercise can be downloaded from the <a href="https://github.com/bobiac/bobiac-book/releases/download/data-bobiac-2026/group-work-1.zip" download> <i class="fas fa-download"></i> Group Work 1 Dataset</a>.

To go through these exercises, you need to create a new folder named `bobiac_group_work`. In the instruction below, we will assume this folder is on your `Desktop` but you can choose a different location if you prefer.

## Step 1

**Create a new `Jupyter Notebook` with `uv`'s `juv` tool**

1. Open a new Terminal or PowerShell and navigate to the `bobiac_group_work` folder.
2. Inside the `bobiac_group_work` folder, create a new folder named `group_work_1` and navigate into it.
3. Inside the `group_work_1`, create a new Jupyter Notebook named `group_work_1.ipynb` using `uv`'s `juv` tool.
4. Run the notebook in your browser using `juv`.\
5. Close the notebook tab in your browser and stop the notebook from the terminal (`cmd + c` or `ctrl + c`) before proceeding to [Step 2](#step-2).

:::{dropdown} Solution

1. Open the Terminal or PowerShell.
2. `cd .../Desktop/bobiac_group_work`
3. `mkdir group_work_1`
4. `cd .../Desktop/bobiac_group_work/group_work_1`
5. `uvx juv init group_work_1.ipynb`
6. `uvx juv run group_work_1.ipynb`
7. Close the notebook tab in your browser and stop the notebook from the terminal (`cmd + c` or `ctrl + c`)

:::

## Step 2

**Add dependencies to the `Jupyter Notebook` with `juv`**

1. In your notebook created in [Step 1](#step-1), add your dependencies using `juv`.
    :::{note}
    It is up to you which dependencies you want to add based on what we covered during the course. If you forget a dependency, you can always close the notebook in both the browser and the terminal, add the dependency, and re-run the notebook.
    :::
2. Run the notebook with `juv`.
3. Import the libraries in the first cell.
4. Run the cell to confirm that they are installed and can be imported without errors.

:::{dropdown} Solution

1. `cd .../Desktop/bobiac_group_work/group_work_1` (the folder created in [Step 1](#step-1))
2. `uvx juv add group_work_1.ipynb cellpose tqdm tifffile spotiflow`
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

## Step 3

**Run Cellpose on the full dataset**

In this step you need to add the code that **segments nuclei and cytoplasm** of all the images in the dataset using **Cellpose** and **saves the segmentation as a `.tif` file**.

You need to segment both the *nuclei* and *cytoplasm* of the images. The nuclei are in channel 0 and the cytoplasm is in channel 1.

:::{tip}
To get the nuclei segmentation, you can pass only the nuclei channel (channel 0) to the `Cellpose` `eval` method. To get the cytoplasm segmentation, you can pass both channels (0 and 1).
:::

1. For each step, create a new `code` cell in the notebook (`+` button).
2. Within the cell, add the necessary code.

:::{dropdown} Solution

See [Solution Notebook](group_work_1_solution.ipynb)

:::

## Step 4

**Run Spotiflow on the full dataset**

In this step you need to add the code that **detects spots in the 4th channels** of all the images in the dataset using **Spotiflow** and **saves a `.csv` file of their coordinates**.

1. For each step, create a new `code` cell in the notebook (`+` button).
2. Within the cell, add the necessary code.

:::{dropdown} Solution

See [Solution Notebook](group_work_1_solution.ipynb)

:::
