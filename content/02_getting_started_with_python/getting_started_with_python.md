# 02 - <i class="fab fa-python"></i> Getting Started with `Python` and `uv`

Before we start writing code, let's take a few minutes to understand what `Python` actually is and how we will use it in this course.

This is not an extensive introduction to Python, but rather a brief overview of minimal concepts and ideas that will help you get started.

TODO: ADD TABLE WITH TOC

## 1. What is Python?

When people say `Python`, they can mean two things:

1. **The Programming Language**: a way that allows us to write instructions that a computer can understand and carry out based on specific **rules** and **syntax**.
2. **The Interpreter**: the actual program (also called `Python`) installed on your computer that is able to **read** the instructions and **execute** them.

:::{note}
🍕 **Analogy**: Think of the **Programming Language rules** and **syntax** as the **grammar** and **vocabulary** we use to write **a pizza recipe**, and the **Interpreter** as the **cook** who **reads**, **understands**, and **executes** the instructions to make a wonderful pizza.
:::

## 2. What is `uv`?

Now that we know what `Python` is, we need a way to **install it** and to **manage everything around it**. For this course we will use a single tool called [`uv`](https://docs.astral.sh/uv/).

`uv` is a **modern, extremely fast tool** that takes care of (almost) everything you need to work with `Python`. Instead of learning many different tools, you only have to learn **one**.

In particular, `uv` can act as three things at once:

1. **A package manager**: it installs and keeps track of the **packages** (libraries) your code needs.
2. **A virtual environment manager**: it creates **isolated workspaces** so that each project has its own packages without interfering with the others.
3. **A Python interpreter manager**: it can **download and install `Python` itself**, in whatever version you need.

:::{note}
🍕 **Analogy**: If `Python` is the **cook**, then `uv` is the **kitchen manager**: it hires the right cook (the **interpreter**), sets up a dedicated kitchen for each recipe (the **environment**), and makes sure all the **ingredients** (the **packages**) are stocked and ready.
:::

Let's look at these three roles one at a time, starting from the packages, then the environments, and finally the interpreter manager.

### 2.1. `uv` as a Package Manager

Out of the box, `Python` can already do a lot. But its real power comes from **packages** (also called **libraries**).

A **package** is simply a collection of `Python` code that **someone else has already written** and made available for you to reuse. Instead of writing everything from scratch, you can install a package and immediately use its functionality. For example, in this course we will use packages to **read images**, **do calculations**, and **make plots**.

`uv` makes installing a package as simple as:

```bash
uv add <package-name>
```

When you do this, `uv` downloads the package, installs it, and **records** that your project depends on it, so the exact same setup can be **reproduced later** (by you or by someone else).

### 2.2. `uv` as a Virtual Environment Manager

If every package were installed in **one shared place** on your computer, different projects could easily **conflict** with each other (for example, one project needs an old version of a package while another needs a newer one).

To avoid this, `uv` uses **virtual environments**. A **virtual environment** is an **isolated workspace** that contains its **own `Python`** and its **own packages**, completely separate from everything else on your computer.

:::{note}
🍕 **Analogy**: Think of a **virtual environment** as a **separate kitchen** dedicated to a single recipe. Whatever ingredients you bring into that kitchen stay there and don't get mixed up with the ingredients of other recipes in other kitchens.
:::

The great thing is that you usually **don't have to think about this**: when you work on a project with `uv`, it automatically creates and uses the right environment for you.

### 2.3. `uv` as a Python Interpreter Manager

Finally, `uv` can also manage the **`Python` interpreter** itself, the actual `Python` program we talked about in [Section 1](#1-what-is-python).

This means `uv` can **download and install any version of `Python`** you need, directly inside your project's environment. If a project requires a specific version of `Python`, `uv` can fetch exactly that one for you, without you having to install it manually.

:::{note}
💡 **You don't need to install Python yourself**: In principle, you *can* download `Python` directly from the [official Python website](https://www.python.org/downloads/), and it will be installed **system-wide** on your computer. However, this is **not ideal**: installing packages directly into that system `Python` can quickly become messy and lead to conflicts. By letting `uv` manage the interpreter and its packages inside isolated environments, you keep everything **clean**, **reproducible**, and **easy to remove**.
:::

## 3. Python Files and the `.py` Extension

`Python` instructions (`Python` *code*/*script*) are usually saved in plain text files ending in **`.py`**. For example, a file called `bobiac.py`.

As mentioned above, this `.py` text file **must** follow specific **rules** and **syntax** in order to be correctly executed, otherwise, `Python` will throw an **error**.

:::{note}
😁 **Don't worry**: Coming across an **error** in your `Python` code is completely normal, it happens even to experienced programmers! **Errors are a natural part of the learning process and often help you understand the language better**.
:::

You will start learning the **rules** and **syntax** of `Python` by writing your own `Python` code in the next sessions of this course.

## 4. Jupyter Notebooks

Running full `.py` files is great once you are familiar with `Python` and you are comfortable with the workflow, but for **learning** and **experimenting** it's a bit clunky: you have to write the whole file, save it, run it, look at the output, then go back and edit.

In this course we will use `Jupyter Notebooks` and its particular file types with the extension **`.ipynb`** (short for **i**nteractive **py**thon **n**ote**b**ook). For example, a file called `bobiac.ipynb`.

`Jupyter Notebooks` allow us to:

- write and run `Python` code in **small chunks** (called *cells*) and execute them one at a time.
- The output of each cell is displayed **immediately** below the cell, so you can see the results of your code as you go.
- Mix **`Python` code** with **text**, **images**, and **equations** in the same document, which is great for **learning** purposes.

:::{note}
💡 **`marimo`**: A new and very valid alternative to `Jupyter Notebooks` is [`marimo`](https://marimo.io), which uses plain `.py` files. We encourage you to have a look at it in the future, once you get more familiar with Python.
:::

## 5. Python and `uv`

