# BoBiAC Book

## How to use it

- Clone this repository.

- Move into the cloned directory.

- Create a fresh environment with uv
  - `uv venv .venv`
  - `source .venv/bin/activate` (on Mac/Linux) or `.venv\Scripts\activate` (on Windows)
- Install the requirements:
  - `uv pip install .`
  - `NOTE`: if to use one of your notebook you require a specific package, add it to the `dependencies` section in the `pyproject.toml` file, or run `uv add package-name` to add it automatically.
  - I added the `pre-commit` package to the dependencies that also checks for typing errors using `typos` and formatting issues, so after installing the dependencies, run `pre-commit install` in the terminal to set it up. I recommend running `uv run pre-commit run --all-files` in the terminal after you stage the changes in VSCode to see what it will do before committing them (it should automatically run when you click on `commit` in VSCode anyway).
  - `NOTE`: if `typos` tries to change words that are not supposed to be changed (e.g. `nd2` -> `and2`), add the word to the `[tool.typos.default.extend-words]` section in the `pyproject.toml` file in the root directory of the repository.

- To build the book (on Mac/Linux):
  - run the command:
    - `./build_local.sh -r`
  - `NOTE`: if you get a permission error, run `chmod +x build_local.sh` one time to make the script executable.
  - `NOTE`: the first time you can also use the `-l` flag (`./build_local.sh -r -l`) and the book will be automatically opened in your browser (otherwise open the `index.html` file in the generated `_build/html` folder)
