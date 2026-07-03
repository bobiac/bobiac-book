# Group Work 3: Does a Protein Localize to a Cellular Compartment?

In this exercise, you will build an analysis workflow in a Jupyter Notebook to investigate whether a protein localizes to a cellular compartment; in this example, the cell membrane. The notebook is based on the example in [membrane_enrichment.ipynb](membrane_enrichment.ipynb), and it uses fluorescence images together with cell label masks and a table of detected spots.

The dataset consists of fluorescence images with five channels:

| Channel | Staining | Staining Description |
|---------|---------|----------------|
| 0 | Hoechst | Nuclear stain |
| 1 | Phalloidin | F-actin stain; whole cell marker |
| 2 | Protein A | Spot pattern |
| 3 | Protein B | Spot pattern |
| 4 | Protein C | Spot pattern |

To go through this exercise, create a new folder named `bobiac_group_work`. In the instructions below, we assume this folder is on your `Desktop`, but you can choose a different location if you prefer.

## Step 1

**Create a new Jupyter Notebook with `uv`'s `juv` tool**

1. Open a new terminal or PowerShell and navigate to the `bobiac_group_work` folder.
2. Inside the `bobiac_group_work` folder, create a new folder named `group_work_3` and navigate into it.
3. Inside `group_work_3`, create a new Jupyter Notebook named `membrane_enrichment.ipynb` using `juv`.
4. Run the notebook in your browser with `juv`.
5. Close the notebook tab in your browser and stop the notebook from the terminal (`cmd + c` or `ctrl + c`) before continuing to [Step 2](#step-2).

:::{dropdown} Solution

1. Open the terminal or PowerShell.
2. `cd .../Desktop/bobiac_group_work`
3. `mkdir group_work_3`
4. `cd .../Desktop/bobiac_group_work/group_work_3`
5. `uvx juv init membrane_enrichment.ipynb`
6. `uvx juv run membrane_enrichment.ipynb`
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

1. `cd .../Desktop/bobiac_group_work/group_work_3`
2. Add the dependencies:

   ```bash
   uvx juv add membrane_enrichment.ipynb matplotlib numpy pandas seaborn scikit-image scipy tifffile imagecodecs
   uvx juv add "bobiac_tools @ git+https://github.com/bobiac/bobiac-tools.git"
   ```

3. `uvx juv run membrane_enrichment.ipynb`
4. In the first code cell, add imports such as:

   ```python
   import matplotlib.pyplot as plt
   import numpy as np
   import pandas as pd
   import seaborn as sns
   import skimage
   import tifffile
   from bobiac_tools import overlay_labels
   from scipy.spatial import KDTree
   ```

5. Run the cell to confirm that the libraries import without errors.

:::

## Step 3

**Load and inspect the image, mask and spot table**

In this step, you will load the fluorescence image, the segmentation mask and the table of detected spots, and inspect the data visually.

:::{dropdown} Solution

1. Create a new code cell in the notebook.
2. Load the image, the cell mask and the spot table.
3. Remove cells that touch the border of the image with `skimage.segmentation.clear_border`.
4. Visualise the image channels, the mask and the spots to confirm the data is correct. You can use `overlay_labels` and its `focus_object` attribute to zoom in on a single cell.

See [membrane_enrichment.ipynb](membrane_enrichment.ipynb) for a worked example.

:::

## Step 4

**Make an analysis plan**

Before writing any analysis code, write down a plan in a markdown cell. This is the central question of the exercise:

### Question

**Does Protein C localize to the cell membrane?**

### Approach

Asking whether a distribution of objects is close to a cellular compartment (here, the cell membrane) is just a variation of the co-localisation analysis. The key idea is to **transform the cell membrane region into a set of points** and then measure how close the Protein C spots are to those membrane points, compared to a random reference.

### Workflow

:::{dropdown} Solution

1. **Generate a reference for comparison.** A randomly distributed set of points inside each cell's cytoplasm. We call this the **random dataset**, which we compare to our **protein dataset**.
2. **Measure the nearest neighbour distance.** For every Protein C spot, identify the closest point on the cell membrane and measure the distance.
3. **Calculate the average nearest neighbour distance.** Average this distance across all spots in the cell.
4. **Calculate the Clark-Evans Index.** The ratio of the average C-to-membrane distance compared to the C-to-random distance:
   - **Ratio = 1:** Protein C is distributed independently of the membrane.
   - **Ratio < 1:** Protein C co-localises with (is enriched near) the membrane.
   - **Ratio > 1:** Protein C and the membrane avoid each other.
5. **Calculate the p-value of the Clark-Evans Index** using a comparison against multiple random patterns.

:::

:::{tip}
Because we only ask whether Protein C is closer *than random* to the membrane, you only need the nearest neighbour distance **from Protein C spots to the membrane**, not the reverse. Randomise the position of the Protein C spots (the null distribution), not the membrane points.
:::

## Step 5

**Assemble the datasets**

In this step, you will build a cell-level dataframe and map each spot to the cell it belongs to.

:::{dropdown} Solution

1. Create a `df_cell` dataframe with the `area` and `label` of each cell using `skimage.measure.regionprops_table`.
2. Map the cell label to each spot, and remove spots that fall in the background.
3. Count the number of spots per cell and add this count to `df_cell`.

:::

## Step 6

**Turn the cell membrane into a set of points**

The key step of this analysis is converting the cell membrane into a list of coordinates (points) so that it can be compared to the Protein C spots, exactly like a cross nearest neighbour analysis between two spot populations.

The code snippet below shows how the boolean mask of a single cell can be turned into its boundary and then into a list of boundary coordinates:

```python
from skimage.segmentation import find_boundaries

cell_id = 11

# identify the spots that belong to cell with index 11
spots_C = df_spots.loc[
    (df_spots["channel"] == 2) & (df_spots["label_cell"] == cell_id)
][["y", "x"]].to_numpy()

# Identify the boundary of cell 11 and turn it into a list of coordinates (spots)
boundary = find_boundaries(
    mask == cell_id
)  # create a binary mask of just the cell boundary
coords = np.argwhere(
    boundary
)  # create a list of coordinates (y, x) for each boundary pixel

overlay_labels(label_mask=boundary, coordinates=[spots_C, coords], focus_object=True)
```

:::{tip}
1. Pick a single cell and extract its Protein C spots (channel 2).
2. Compute the boundary of that cell and convert it into a list of coordinates.
3. Overlay the Protein C spots and the boundary points to confirm the transformation worked.
:::

## Step 7

**Perform the analysis for one cell**

Focus on one cell, calculate the distances between Protein C and the membrane and compare to a null distribution.

:::{dropdown} Solution

1. Calculate the distance of every Protein C point to the nearest membrane point and average over all distances.
2. Generate a random point distribution inside the cell that has the same number of points as Protein C.
3. Calculate the distance of every random ponint to the nearest membrane point and average over all distances.
4. Calculate the Clark-Evans index and the p-value as previously.
5. Check if your results make sense.

See [membrane_enrichment.ipynb](membrane_enrichment.ipynb) for a worked example.

:::

## Step 8

**Set up batch processing**

Perform the same analysis for all cells in the image.

:::{dropdown} Solution

1. Use a for loop to iterate over all cell labels.
2. Store individual cell results (CE-index, p-val, average distance to membrane) in `df_cell`.
3. Perform quality control and check for outliers by overlaying results on the image and by histogram analysis.

See [membrane_enrichment.ipynb](membrane_enrichment.ipynb) for a worked example.

:::

## Step 8

**Visualise the results and draw a conclusion**

In this final step, you will answer the main question: does Protein C localize to the cell membrane?

:::{dropdown} Solution

1. Plot the distribution of the observed nearest neighbour distances (`nn_observed`) and mark the mean observed and mean random distances.
2. Plot the distribution of the Clark-Evans index (`ce`) and mark its mean.
3. Interpret the result: if the mean Clark-Evans index is clearly below 1, Protein C localises close to the membrane.
4. Write a short conclusion in a markdown cell.

Protein C localises close to the cell membrane, with an average distance of ~4.5 pixels and a mean Clark-Evans index well below 1.

:::

## Bonus

**Test the other proteins**

If you want an extra challenge, repeat the analysis for Protein A (channel 0) and Protein B (channel 1) instead of Protein C. Do they also localise to the cell membrane, or are they distributed randomly within the cell?
