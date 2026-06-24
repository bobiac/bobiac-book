# A Gentle Introduction to Python

Welcome! Before we start writing code, let's take a few minutes to understand
*what* Python actually is, *how* a computer runs it, and the tools we'll use in
this course. Don't worry if some of this feels abstract right now — it will all
click once you start typing.

---

## 1. What is Python?

**Python is a programming language.** A programming language is just a way for
*us* (humans) to write instructions that a *computer* can understand and carry
out.

A few things that make Python special:

- **It reads like English.** Compared to many other languages, Python code is
  clean and easy to read. This is why it's one of the best languages to learn
  first.
- **It's everywhere.** Scientists, web developers, data analysts, and AI
  researchers all use Python.
- **It's free and open source.** Anyone can download and use it.

When people say "Python," they can mean two things:

1. **The language** — the rules and syntax for writing instructions.
2. **The interpreter** — the actual program (also called `python`) installed on
   your computer that *reads* your instructions and *executes* them.

> 💡 **Analogy:** Think of the language as the grammar and vocabulary, and the
> interpreter as the person who reads your sentences out loud and does what they
> say.

---

## 2. Python reads `.py` files (written with a specific syntax)

Python instructions are usually saved in plain text files ending in **`.py`**.
For example, a file called `hello.py` might contain:

```python
# This is a comment — Python ignores it
name = "World"
print("Hello, " + name + "!")
```

To run it, you would type this in a terminal:

```bash
python hello.py
```

…and Python would print:

```
Hello, World!
```

### Why "a specific syntax"?

The interpreter is *very picky*. It only understands code written following
Python's rules — its **syntax**. For example:

- Indentation (the spaces at the start of a line) actually matters in Python.
- Words like `print`, `if`, and `for` have special meanings.
- A misplaced symbol or typo will cause an **error** instead of running.

This is normal! Everyone — even experts — sees error messages constantly.
Learning to read them is part of learning to code.

---

## 3. Where you actually write code: editors and IDEs

We now know Python code lives in text files. But what do you *use* to write
those files?

In principle, any plain text editor (even Notepad) would work — but that would
be painful, like writing an essay with no spell-check, no formatting, and no
help at all.

Instead, programmers use an **IDE**: an **I**ntegrated **D**evelopment
**E**environment. That's a fancy name for *one program that bundles together
everything you need to write, run, and fix code*:

- A smart **code editor** with **syntax highlighting** (colors that make code
  easier to read).
- **Autocomplete** — it suggests function names and finishes your typing.
- **Error squiggles** — underlines mistakes *before* you even run the code.
- A built-in **terminal** to run commands without leaving the window.
- **Debugging** tools, search, file management, and add-on **extensions**.

> 💡 **Analogy:** A plain text editor is like writing with a single pencil. An
> IDE is a fully equipped workshop — the pencil, plus a ruler, eraser, good
> lighting, and a helper looking over your shoulder.

### We'll use VS Code

In this course we'll use **Visual Studio Code** (usually just called
**VS Code**):

- It's **free**, hugely popular, and runs on Windows, macOS, and Linux.
- It edits `.py` files *and* opens and runs **Jupyter Notebooks** — all in one
  place.
- With the Python extension installed, it gives you autocomplete, error
  checking, and one-click "Run" buttons.

So VS Code will be our home base: it's *where* we write code, and Python is
*what* runs it.

---

## 4. Why we'll use Jupyter Notebooks in this course

Running full `.py` files is great for real programs, but for *learning* and
*experimenting* it's a bit clunky: you have to write the whole file, save it,
run it, look at the output, then go back and edit.

Instead, we'll mostly use **Jupyter Notebooks** (files ending in `.ipynb`),
which we can open right inside VS Code.

A notebook lets you:

- Write code in small **cells** and run them one at a time.
- See the output (numbers, text, plots, images) *right below* each cell.
- Mix code with **text, notes, and images** — like a digital lab notebook.

```
┌─────────────────────────────────┐
│  [Cell 1]                       │
│  2 + 2                          │
├─────────────────────────────────┤
│  Output: 4                      │
└─────────────────────────────────┘
┌─────────────────────────────────┐
│  [Cell 2]                       │
│  print("Hello from a notebook") │
├─────────────────────────────────┤
│  Output: Hello from a notebook  │
└─────────────────────────────────┘
```

It's the same Python underneath — we're just running it in a friendlier,
interactive way that's perfect for teaching and exploring.

---

## 5. Packages: standing on the shoulders of others

Out of the box, Python can do a lot. But its real power comes from **packages**
(also called **libraries**).

A package is a bundle of code that *someone else has already written* so you
don't have to. Want to:

- Do scientific math? → `numpy`
- Work with tables of data? → `pandas`
- Make plots and charts? → `matplotlib`

Instead of writing thousands of lines yourself, you just **install** the package
and **import** it:

```python
import numpy as np

print(np.mean([1, 2, 3, 4]))   # prints 2.5
```

There are hundreds of thousands of packages available — this huge ecosystem is a
big reason Python is so popular.

---

## 6. What's an "API"?

You'll hear the word **API** a lot. It stands for **A**application
**P**rogramming **I**nterface, which sounds intimidating but means something
simple: **the set of commands a piece of software offers you so you can use it**
— without needing to know how it works inside.

> 💡 **Analogy:** A restaurant menu is an API. You order from the menu; you don't
> walk into the kitchen. The menu defines *what* you can ask for, and the
> kitchen handles *how* it's made.

You'll meet APIs in two main flavors:

1. **A package's API** — when you write `np.mean([...])`, that `mean` function is
   part of `numpy`'s API: the list of functions and tools the package makes
   available to you. A package's **documentation** is basically a description of
   its API.
2. **A web API** — many online services (weather data, maps, even AI models like
   Claude) expose an API so your Python code can *ask them for things* over the
   internet and get answers back.

So when someone says "use the `pandas` API" or "call the weather API," they just
mean: *use the official set of commands that thing provides.*

---

## 7. Environments: keeping projects tidy

Here's a common problem. Imagine:

- **Project A** needs version 1 of a package.
- **Project B** needs version 2 of the same package.

If everything is installed in one big shared pile, these projects can conflict
and break each other. 😫

The solution is a **virtual environment**: an isolated little "box" that holds a
specific version of Python *plus* exactly the packages a given project needs.

> 💡 **Analogy:** Think of environments as separate toolboxes. Each project gets
> its own toolbox with exactly the right tools, so nothing gets mixed up.

Benefits:

- Different projects don't interfere with each other.
- You can share your project and others can recreate the *exact* same setup.
- Your computer's main Python install stays clean.

---

## 8. The tools we'll use: `uv`, `uvx`, and `juv`

Managing environments and packages used to be fiddly. We'll use modern tools
that make it almost effortless.

- **`uv`** — a fast, all-in-one tool for managing Python, environments, and
  packages.
- **`uvx`** — runs a tool *without permanently installing it*, in a temporary
  environment. Great for one-off commands.
- **`juv`** — a helper built for Jupyter notebooks that handles the environment
  *for* you, so a notebook can declare its own dependencies and "just work."

### The magic part: notebooks that carry their own recipe

Thanks to a Python standard called **PEP 723**, a script (or notebook) can
include a small block at the top that lists everything it needs to run. It looks
something like this:

```python
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "numpy",
#     "matplotlib",
# ]
# ///
```

When we launch a notebook with a command like:

```bash
uvx juv run my_notebook.ipynb
```

`juv` reads that block, automatically builds the right environment, installs the
listed packages, and opens the notebook — all in one step. **No manual setup
required on your end.** 🎉

This is why we can focus on *learning Python* instead of fighting with
installation.

---

## 9. Putting it all together

Here's the big picture of what's happening in this course:

1. **Python** is the language; the **interpreter** runs our instructions.
2. We write code in an **IDE** — **VS Code** — our home base for editing and
   running everything.
3. We *could* write `.py` files, but for teaching we'll use **Jupyter
   Notebooks** — interactive, cell-by-cell, with output shown inline.
4. **Packages** give us powerful, ready-made tools we just import and use, and
   each exposes an **API** — the set of commands we call.
5. **Environments** keep each project's tools isolated and reproducible.
6. **`uvx juv`** + the **PEP 723** header at the top of each notebook handle all
   the environment setup automatically — so you can just open it and start
   coding.

---

## Quick glossary

| Term | What it means |
|------|---------------|
| **Python** | The programming language (and its interpreter). |
| **`.py` file** | A plain text file containing Python code. |
| **Syntax** | The strict rules for how Python code must be written. |
| **IDE** | "Integrated Development Environment" — one program that bundles an editor, a runner, error checking, and more. |
| **VS Code** | The IDE we'll use; free, popular, edits `.py` files and notebooks. |
| **Jupyter Notebook** (`.ipynb`) | An interactive document mixing code, output, and notes. |
| **Cell** | A small block of code (or text) in a notebook that you run individually. |
| **Package / Library** | Reusable code written by others that you can import. |
| **Import** | Bringing a package into your code so you can use it. |
| **API** | "Application Programming Interface" — the set of commands a package or service offers you to use. |
| **Environment** | An isolated "box" with a specific Python + packages for one project. |
| **`uv` / `uvx`** | Modern, fast tools for managing Python and running tools. |
| **`juv`** | A tool that runs notebooks and sets up their environment automatically. |
| **PEP 723** | A standard for declaring a script's dependencies at the top of the file. |

---

*Don't try to memorize all of this — it's here for reference. The best way to
learn is to start running cells and experimenting. Let's go! 🐍*
