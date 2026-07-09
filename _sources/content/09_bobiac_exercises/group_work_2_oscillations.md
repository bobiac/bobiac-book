# Group Work 2: Analysing Oscillations in Time-Series Images

In this exercise, you will build a small analysis workflow in a Jupyter Notebook to investigate whether the expression of a gene oscillates over time. The notebook is based on the example in <a href="group_work_2_oscillations_solution.html" target="_blank">Solution Notebook</a>, and it uses time-resolved microscopy images together with cell and nucleus label masks.

The images we will use for this exercise can be downloaded from the <a href="https://github.com/bobiac/bobiac-book/releases/download/data-bobiac-2026/bobiac_exercises_oscillations.zip" download> <i class="fas fa-download"></i> Group Work 2 Dataset</a>.

To go through this exercise, create a new folder named `bobiac_group_work`. In the instructions below, we assume this folder is on your `Desktop`, but you can choose a different location if you prefer.

## Step 1

**Create a new Jupyter Notebook with `uv`'s `juv` tool**

1. Open a new terminal or PowerShell and navigate to the `bobiac_group_work` folder.
2. Inside the `bobiac_group_work` folder, create a new folder named `group_work_2` and navigate into it.
3. Inside `group_work_2`, create a new Jupyter Notebook named `oscillations.ipynb` using `juv`.
4. Run the notebook in your browser with `juv`.
5. Close the notebook tab in your browser and stop the notebook from the terminal (`cmd + c` or `ctrl + c`) before continuing to [Step 2](#step-2).

:::{dropdown} Solution

1. Open the terminal or PowerShell.
2. `cd .../Desktop/bobiac_group_work`
3. `mkdir group_work_2`
4. `cd .../Desktop/bobiac_group_work/group_work_2`
5. `uvx juv init oscillations.ipynb`
6. `uvx juv run oscillations.ipynb`
7. Close the notebook tab in your browser and stop the notebook from the terminal (`cmd + c` or `ctrl + c`)

:::

## Step 2

**Add dependencies to the notebook with `juv`**

1. In your notebook created in [Step 1](#step-1), add the dependencies you need for the analysis.
2. Run the notebook with `juv`.
3. Import the libraries in the first code cell.
4. Run the cell to confirm that the imports work without errors.

The analysis in the example notebook uses the following packages:

- `matplotlib`
- `numpy`
- `pandas`
- `seaborn`
- `scikit-image`
- `scipy`
- `tifffile`
- `imagecodecs`
- `bobiac_tools`

:::{note}
If you prefer to work in Google Colab instead of locally, copy the `.ipynb` file to your Google Drive and open it from the Colab website. In that case, you will need to add a `!pip install <package_name>` cell for each dependency before importing the libraries.
:::

:::{dropdown} Solution

1. `cd .../Desktop/bobiac_group_work/group_work_2`
2. Add the dependencies:

   ```bash
   uvx juv add oscillations.ipynb matplotlib numpy pandas seaborn scikit-image scipy tifffile imagecodecs
   uvx juv add oscillations.ipynb "bobiac_tools @ git+https://github.com/bobiac/bobiac-tools.git"
   ```

3. `uvx juv run oscillations.ipynb`
4. In the first code cell, add imports such as:

   ```python
   from pathlib import Path

   import matplotlib.pyplot as plt
   import pandas as pd
   import seaborn as sns
   import skimage
   import tifffile
   from bobiac_tools import overlay_labels
   ```

5. Run the cell to confirm that the libraries import without errors.

:::

## Step 3

**Load and inspect the time-series images**

In this step, you will load the image files and the segmentation masks and inspect the data visually.

1. Create a new code cell in the notebook.
2. Download the dataset folder that contains the time-lapse file `F01_1615_tcyx.tif`.
3. For the `F01_1615_tcyx.tif` file, display the first eight time points of the last channel in the as a grid of images.
4. In the same dataset folder, there is a `F01_1615_tcyx_cell_labels.tif` file (labeled mask of the cells) and a `F01_1615_tcyx_nuclei_labels.tif` file (labeled mask of the nuclei). Visualize these masks as an overlay

The example notebook uses the data in the course repository under the `images/` and `masks/` folders for the time-series example.

:::{dropdown} Solution

See <a href="group_work_2_oscillations_solution.html" target="_blank">Solution Notebook</a> for a worked example.

:::

## Step 4

**Measure nuclear intensity for the first time point**

In this step, you will analyse the first image and quantify the intensity of each nucleus.

1. Load the first time point of the last channel in the `F01_1615_tcyx.tif` file.
2. Remove objects touching the border of the image.
3. Measure the intensity of each nucleus with `skimage.measure.regionprops_table`.
4. Subtract the background intensity from the measurements and inspect the resulting values.

:::{tip}
You can use the same workflow as in the earlier measurement notebooks: load the image, apply a mask, extract region measurements, and store the results in a `pandas.DataFrame`.
:::

:::{dropdown} Solution

See <a href="group_work_2_oscillations_solution.html" target="_blank">Solution Notebook</a> for a worked example.

:::

## Step 5

**Perform quality control and analyse all time points**

Now you will turn the workflow into a batch analysis over all 16 images.

1. Check the measurements for artifacts, for example by plotting the distribution of background-corrected intensities.
2. Overlay the measured values on the image and inspect whether any nuclei look suspicious.
3. Loop through all time points, measure the intensity of each nucleus, and add a `time` column.
4. Combine all measurements into a single `DataFrame`.

:::{dropdown} Solution

See <a href="group_work_2_oscillations_solution.html" target="_blank">Solution Notebook</a> for a worked example.

:::

## Step 6

**Visualise the oscillations and estimate the frequency**

In this final step, you will answer the main question: what is the frequency of the oscillations?

1. Use `sns.lineplot` to visualise the intensity of each nucleus over time.
2. Add a second plot showing the average signal across cells.
3. Estimate the oscillation frequency from the pattern you observe.
4. Write a short conclusion in a markdown cell.

:::{dropdown} Solution

See <a href="group_work_2_oscillations_solution.html" target="_blank">Solution Notebook</a> for a worked example.

:::

## Bonus

**Try a nuclear/cytoplasmic ratio**

If you want an extra challenge, replace the nuclear intensity measurement with a ratio of nuclear intensity divided by cytoplasmic intensity. This can sometimes make the oscillation easier to interpret.
