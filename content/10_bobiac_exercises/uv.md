# uv Exercises

To go through these exercises, you need to create a new folder on your `Desktop` called `bobiac_uv`.

## Exercise 1

**Create a Python Environment with `uv` and Install `numpy` & `matplotlib`**

1. Open the Terminal or PowerShell and navigate to the `bobiac_uv` folder.
2. Create a new virtual environment with `uv` in the `bobiac_uv_env` folder named `bobiac-env`.
3. Activate the newly created `bobiac-env` virtual environment.
4. Install `numpy` and `matplotlib` in the `bobiac-env` virtual environment.
5. List the installed packages in the `bobiac-env` virtual environment to confirm that `numpy` and `matplotlib` are installed.
6. Deactivate the `bobiac-env` virtual environment.

:::{dropdown} Solution

1. open the Terminal or PowerShell.
2. `cd .../Desktop/bobiac_uv`
3. `uv venv bobiac-env`
4. `source bobiac-env/bin/activate` (Linux/macOS) or `bobiac-env\Scripts\activate` (Windows)
5. `uv pip install numpy matplotlib`
6. `uv pip list`
7. `deactivate`

:::

## Exercise 2

**Add to the environment created in [Exercise 1](#exercise-1) the `scikit-image` package**

1. Open the Terminal or PowerShell and navigate to the `bobiac_uv` folder.
2. Activate the `bobiac-env` virtual environment created in [Exercise 1](#exercise-1).
3. Add the `scikit-image` package to the `bobiac-env` virtual environment.
4. List the installed packages in the `bobiac-env` virtual environment to confirm that `scikit-image` is installed.
5. Deactivate the `bobiac-env` virtual environment.
