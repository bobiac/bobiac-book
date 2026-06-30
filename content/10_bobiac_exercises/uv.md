# uv Exercises

To go through these exercises, you need to create a new folder on your `Desktop` called `bobiac_uv`.

## Exercise 1

**Create a Python Environment with `uv` and Install `numpy` & `matplotlib`**

1. Open the Terminal or PowerShell and navigate to the `bobiac_uv` folder.
2. Create a new virtual environment with `uv` in the `bobiac_uv_env` folder named `.venv`.
3. Activate the newly created `.venv` virtual environment.
4. Install `numpy` and `matplotlib` in the `.venv` virtual environment.
5. List the installed packages in the `.venv` virtual environment to confirm that `numpy` and `matplotlib` are installed.
6. Deactivate the `.venv` virtual environment.

:::{dropdown} Solution

1. open the Terminal or PowerShell.
2. `cd .../Desktop/bobiac_uv`
3. `uv venv .venv`
4. `source .venv/bin/activate` (Linux/macOS) or `.venv\Scripts\activate` (Windows)
5. `uv pip install numpy matplotlib`
6. `uv pip list`
7. `deactivate`

:::

## Exercise 2

**Add to the environment created in [Exercise 1](#exercise-1) the `scikit-image` package**

1. Open the Terminal or PowerShell and navigate to the `bobiac_uv` folder.
2. Activate the `.venv` virtual environment created in [Exercise 1](#exercise-1).
3. Add the `scikit-image` package to the `.venv` virtual environment.
4. List the installed packages in the `.venv` virtual environment to confirm that `scikit-image` is installed.
5. Deactivate the `.venv` virtual environment.
