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
3. `uv venv .venv` (or simply `uv venv`)
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

:::{dropdown} Solution

1. open the Terminal or PowerShell.
2. `cd .../Desktop/bobiac_uv`
3. `source .venv/bin/activate` (Linux/macOS) or `.venv\Scripts\activate` (Windows)
4. `uv pip install scikit-image`
5. `uv pip list`
6. `deactivate`

:::

## Exercise 3

**Create a `.py` file with the PEP723 `///script` header using `uv`**

1. Open the Terminal or PowerShell and navigate to the `bobiac_uv` folder.
2. Inside the `bobiac_uv` folder, create a new folder named `py_folder` and navigate into it.
3. Use `uv` to create a new Python file named `bobiac_script.py` with the PEP723 `///script` header and Python `3.13`.
4. Add `numpy` and `matplotlib` as dependencies to the `bobiac_script.py` file using `uv`.
5. Run the `bobiac_script.py` file using `uv` to verify that the dependencies are installed and the script runs without errors.
6. Optional: show the dependencies of the `bobiac_script.py` file using `uv tree`.
7. Optional: show the python version used for the `bobiac_script.py` file using `uv python`.

:::{dropdown} Solution

1. open the Terminal or PowerShell.
2. `cd .../Desktop/bobiac_uv`
3. `mkdir py_folder`
4. `cd .../Desktop/bobiac_uv/py_folder`
5. `uv init --script bobiac_script.py -p 3.13`
6. `uv add --script bobiac_script.py numpy matplotlib`
7. `uv run bobiac_script.py`
8. Optional: `uv tree --script bobiac_script.py`
9. Optional: `uv python find --script bobiac_script.py --show-version`

:::