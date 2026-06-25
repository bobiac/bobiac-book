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

## 2. Installing Python

The `Python` interpreter, as most of any computer program, has different **versions** (e.g. **3.13**, **3.14**, etc). We could pick the version we want from the [official Python website](https://www.python.org/downloads/) and install it on our computer. However, this is might not the best way to install `Python`.





## 2. Installing Python and Python Packages

Out of the box, `Python` can do a lot. But its real power comes from **packages** (also called **libraries**).

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

