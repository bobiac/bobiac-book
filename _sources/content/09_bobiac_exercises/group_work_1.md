# Group Work 1

Let's now consolidate what you have learned! These exercises will walk you through how to create your own Jupyter Notebook containing code that segments images with Cellpose!

To go through these exercises, you need to create a new folder on your `Desktop` called `bobiac_uv_env`.

## Exercise 1

**Create a Python Environment with `uv` and Install Dependencies**

1. Open the Terminal or PowerShell and navigate to the `bobiac_uv_env` folder.
2. Create a new virtual environment with `uv` in the `bobiac_uv_env` folder named `group-work-1`.
3. Activate the newly created `group-work-1` virtual environment.
4. Install the necessary dependencies for Cellpose and Spotiflow segmentation in the `group-work-1` virtual environment.
5. List the installed packages in the `group-work-1` virtual environment to confirm that everything is installed.
6. Deactivate the `group-work-1` virtual environment.

:::{dropdown} Solution

1. open the Terminal or PowerShell.
2. `cd .../Desktop/bobiac_uv_env`
3. `uv venv group-work-1`
4. `source group-work-1/bin/activate` (Linux/macOS) or `group-work-1\Scripts\activate` (Windows)
5. `uv pip install cellpose tqdm`
6. `uv pip list`
7. `deactivate`

:::

## Exercise 2

**Create a new `Jupyter Notebook` with `uv`'s `juv` tool**

1. Open the Terminal or PowerShell and navigate to the `bobiac_uv_env` folder.
2. Inside the `bobiac_uv_env` folder, create a new folder named `nb_folder` and navigate into it.
3. Inside the `nb_folder`, create a new Jupyter Notebook named `cellpose-segmentation.ipynb` using `uv`'s `juv` tool.
4. Run the notebook in your browser using `juv`.

:::{dropdown} Solution

1. Open the Terminal or PowerShell.
2. `cd .../Desktop/bobiac_uv_env`
3. `mkdir nb_folder`
4. `cd .../Desktop/nb_folder`
5. `uvx juv init cellpose-segmentation.ipynb`
6. `uvx juv run cellpose-segmentation.ipynb`

:::

## Exercise 3

**Add dependencies to the `Jupyter Notebook` with `juv`**

1. In your notebook created in [Exercise 2](#exercise-2), add your dependencies using `juv`.
2. Run the notebook with `juv` and import the libraries in the first cell to confirm that they are installed and can be imported without errors.

    :::{note}
    If you have the notebook open in your browser, you need to stop it from the terminal (`cmd + c` or `ctrl + c`) and close the browser tab before running the notebook again with `juv` or the new dependencies will not be installed.
    :::

:::{dropdown} Solution

1. `cd .../Desktop/nb_folder` (the folder created in [Exercise 2](#exercise-2))
2. `uvx juv add cellpose-segmentation.ipynb cellpose tqdm`
3. `uvx juv run my-first-nb.ipynb`  
4. Add a new `code` cell in the notebook (`+` button)
5. Within this cell, import the necessary libraries:

    ```python
    from pathlib import Path

    from cellpose import core, io, models, plot
    from tqdm import tqdm
    ```

6. Run the cell to confirm that the libraries are imported without errors.

:::

## Exercise 4

**Add code that segments the first two channels of many image files using Cellpose and saves the segmentation result as a tif file**
1. For each step, create a new `code` cell in the notebook (`+` button).
2. Within the cell, add the necessary code.


:::{dropdown} Solution

```python
#setup
io.logger_setup()  # to get printing of progress
use_gpu = core.use_gpu()
print("GPU available:", use_gpu)

# Path to the folder containing the images to segment
folder_path = Path("data/04_segmentation_cellpose")

# Get the sorted list of all .tif images in the folder
images_path = sorted(folder_path.glob("*.tif"))

# Initialize the model once before the loop
model_path = str(MODEL_DIR / "cpsam_v2")  # or "cpdino" / "cpdino-vitb" or "cpsam"
model = models.CellposeModel(pretrained_model=model_path, gpu=use_gpu)

# Run Cellpose on each image one by one
# NOTE: tqdm is used to show a progress bar, but you can remove it if you don't want it
for image_path in tqdm(images_path, desc="Processing images"):
    # Load the image
    image = io.imread(image_path)
    # select the channels to segement from the multichannel image
    cp_image = image[[0, 1]]
    # Run Cellpose on the image
    masks, flows, styles = model.eval(cp_image)
    # Save the segmentation results as a TIFF file
    output_path = folder_path / f"{image_path.stem}_labels.tif"
    io.imsave(output_path, masks)  # or tifffile.imwrite(output_path, masks)

```

:::
