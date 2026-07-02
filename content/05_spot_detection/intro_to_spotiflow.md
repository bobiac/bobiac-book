# Introduction to Spotiflow

[**Spotiflow**](https://weigertlab.org/spotiflow/index.html) is a **free**, **open-source**, **deep learning**-based tool for **spot detection** in **fluorescence microscopy** images. It is designed to accurately and robustly localize **spot-like structures** (such as individual transcripts in FISH and smFISH experiments, or any diffraction-limited puncta) without the manual threshold tuning required by classical methods.

At its core, **Spotiflow** uses a **pretrained U-Net** that jointly predicts a **probability heatmap** (spots appear as Gaussian blobs; candidates are found as local maxima) and a **stereographic flow field** (each pixel points toward the nearest spot center) for **subpixel refinement**. It is **threshold-agnostic** and works on both **2D** and **3D datasets**. Several **pretrained models** are available for different imaging modalities (e.g. `general`, `hybiss`, `synth_complex`, `fluo_live`, `synth_3d`, `smfish_3d`), and users can also **fine-tune or train custom models** on their own data when the pretrained models do not fit their needs.

A prediction returns the **spot coordinates** together with intermediate outputs (e.g. `heatmap`).

The project has **documentation, tutorials, and example datasets** available on the [official documentation](https://weigertlab.org/spotiflow/index.html), the [GitHub repository](https://github.com/weigertlab/spotiflow), and the [paper](https://www.nature.com/articles/s41592-025-02662-x).

## Download and Install Spotiflow

**Spotiflow** is available via:

* A **Python package** (recommended for scripting and integration into pipelines)
* A **Command-Line Interface (CLI)** (`spotiflow-predict`) for quick inference ([see the documentation](https://weigertlab.org/spotiflow/cli.html))
* A **napari plugin** for interactive use

Below are the instructions to install **Spotiflow** using [`uv`](https://docs.astral.sh/uv/).

You can use `uv` to use/install **Spotiflow** in three ways:

1. **Direct execution (napari plugin)**: Use `uv` to automatically handle environment creation and launch the napari GUI with the **Spotiflow** plugin
2. **Manual environment setup**: Create a virtual environment first, then install **Spotiflow** within that environment
3. **Jupyter Notebook Integration**: Use `uvx juv` with the Jupyter notebooks from this course to run the **Spotiflow** notebooks directly in the browser

<p class="alert alert-warning">
    <strong>⚠️ Note:</strong> If you want to use <code>Spotiflow</code> efficiently, make sure to run it using GPU or it will be very slow. If you have an Apple Silicon Mac, you can take advantage of the built-in GPU (no need of a particular installation). See the instructions below for more details on how to run <code>Spotiflow</code> with GPU support on Windows/Linux.
</p>

### 1. Direct Execution with uv (napari plugin)

**Spotiflow** ships a [napari](https://napari.org) plugin ([`napari-spotiflow`](https://github.com/weigertlab/napari-spotiflow)) that lets you run spot detection interactively inside the napari viewer. Similarly to how you can launch napari with `uvx "napari[all]"`, you can launch napari **together with** the **Spotiflow** plugin in a single command (it might take a little while the first time you run this command, but after that it will be very quick):

```bash
uvx --with "napari-spotiflow" "napari[all]"
```

Once napari opens, go to `Plugins > napari-spotiflow` to run the plugin.

:::{dropdown} NVIDIA GPU (CUDA - Windows/Linux)

To launch the napari plugin with NVIDIA GPU support:

1. you need to have the [NVIDIA drivers](https://www.nvidia.com/en-us/drivers/) installed on your system.
2. you can run `nvidia-smi` in the terminal to check your CUDA version (shown in the top-right of the output, e.g. `CUDA Version: 13.0.0`).
3. run the following command, replacing `cu130` with your CUDA version. The `--index-strategy unsafe-best-match` flag is needed so that `uv` resolves the other packages from PyPI rather than only from the PyTorch index:

```bash
uvx --index-strategy unsafe-best-match --with torch --with torchvision --with "napari-spotiflow" --index https://download.pytorch.org/whl/cu130 "napari[all]"
```

:::

### 2. Manual Environment Setup

If you need to use **Spotiflow** for scripting and integration into pipelines, it is useful to set up a virtual environment manually. Here are the steps:

**1.1. Create a new virtual environment:**

When using `uv`, you can create a virtual environment with the following command:

```bash
uv venv spotiflow-env
```

**1.2. Activate the virtual environment:**

```bash
# On Linux or macOS
source spotiflow-env/bin/activate
# On Windows use 
spotiflow-env\Scripts\activate
```

**1.3. Install Spotiflow:**

```bash
uv pip install spotiflow
```

If you also want to use the napari plugin from within this environment, install it together with napari:

```bash
uv pip install "napari[all]" napari-spotiflow
```

and then launch napari with:

```bash
napari
```

:::{dropdown} NVIDIA GPU (CUDA - Windows/Linux)

To use Spotiflow with an NVIDIA GPU in your virtual environment:

1. you need to have the [NVIDIA drivers](https://www.nvidia.com/en-us/drivers/) installed on your system.
2. you can run `nvidia-smi` in the terminal to check your CUDA version (shown in the top-right of the output, e.g. `CUDA Version: 13.0.0`).
3. before installing Spotiflow, install `torch` and `torchvision` with CUDA support, replacing `cu130` with your CUDA version:

```bash
uv pip install torch torchvision --index-url https://download.pytorch.org/whl/cu130
```

4. then install Spotiflow as described above:

```bash
uv pip install spotiflow
```

<p class="alert alert-warning">
    <strong>⚠️ Note:</strong> On Windows you also need the <a href="https://visualstudio.microsoft.com/visual-cpp-build-tools/">Visual Studio Build Tools</a> with the C++ components installed before installing Spotiflow.
</p>

:::

### 3. Jupyter Notebook Integration

To run for example the [Spotiflow Notebook](spotiflow_notebook.ipynb) locally in your browser, you can use the following command:

```bash
# for the spotiflow notebook
uvx juv run path/to/spotiflow_notebook.ipynb # (or simply juv run spotiflow_notebook.ipynb if you have the tool)
```

:::{dropdown} NVIDIA GPU (CUDA - Windows/Linux)

In order to use Spotiflow in the notebooks with an NVIDIA GPU:

1. you need to have the [NVIDIA drivers](https://www.nvidia.com/en-us/drivers/) installed on your system.
2. you can run `nvidia-smi` in the terminal to check your CUDA version (shown in the top-right of the output, e.g. `CUDA Version: 13.0.0`).
3. update the `# /// script` block at the top of the `spotiflow_notebook.ipynb` to install the appropriate version of [PyTorch with CUDA support](https://pytorch.org/get-started/locally/) (replace `cu130` with your CUDA version):

   ```python
    # /// script
    # requires-python = ">=3.12"
    # dependencies = [
    #     "matplotlib",
    #     "tifffile",
    #     "spotiflow",
    #     "ndv[jupyter,pygfx]",
    #     "jupyter-rfb<=0.5.4",
    #     "torch",
    #     "torchvision",
    # ]
    #
    # [tool.uv.sources]
    # torch = { index = "pytorch-cu130" }
    # torchvision = { index = "pytorch-cu130" }
    #
    # [[tool.uv.index]]
    # name = "pytorch-cu130"
    # url = "https://download.pytorch.org/whl/cu130"
    # explicit = true
    # ///
   ```

4. re-run the notebook using `uvx juv run`.

:::

## What's Next?

In the next sections, we will focus on how to use [Spotiflow in scripts and pipelines](spotiflow_notebook.ipynb) to automatically detect spots in both 2D and 3D images using the pretrained models. We will also show how to [train a Spotiflow custom model](spotiflow_retraining.ipynb) on annotated data if the pretrained models do not fit your specific needs.
