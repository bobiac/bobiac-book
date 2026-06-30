# Python and uv

## 1. What is Python?

When people say `Python`, they can mean two things:

1. **The Programming Language**: a way that allows us to write instructions that a computer can understand and carry out based on specific **rules** and **syntax**.
2. **The Interpreter**: the actual program (also called `Python`) installed on your computer that is able to **read** the instructions and **execute** them.

:::{note}
{{pizza}} **Analogy**: Think of the **Programming Language rules** and **syntax** as the **grammar** and **vocabulary** we use to write **a pizza recipe**, and the **Interpreter** as the **cook** who **reads**, **understands**, and **executes** the instructions to make a wonderful pizza.
:::

## 2. Python Packages

On its own, `Python` can already do a lot: it can do **calculations**, **work with text**, **read and write different file types**, **repeat tasks**, and much more.

These capabilities are organized into **packages** (also referred to as **libraries** or **dependencies**). A **package** is simply a **collection of `Python` code** grouped together to provide a specific set of functionality.

Some packages are **already included** with `Python` and are available **by default**, without you having to do anything. Together they form what is called the **standard library** (for example, `Python` already comes with packages to work with `.csv` files, dates, or the file system).

But the **real power** of `Python` comes from the **hundreds of thousands** of additional packages written by people all around the world, which are **not** included by default and must be **installed** before you can use them. Instead of writing everything from scratch, you can simply **install** one of these packages and immediately reuse all the functionality it provides.

For example, in this course we will use packages to:

- **read** (e.g. `tifffile`, `bffile`)
- **manipulate** images and perform **numerical calculations** efficiently (e.g. `numpy`, `scikit-image`)
- use **deep learning** models (e.g. `cellpose`, `spotiflow`)
- create **plots** and **visualizations** (e.g. `matplotlib`, `ndv`)

Each of these would take an enormous amount of work to build ourselves, but thanks to packages we can simply **reuse** code that experts have already written, tested, and shared.

:::{note}
{{pizza}} **Analogy**: To put the **mozzarella** (the **package**) on our pizza, we don't have to buy a cow, milk it, and make the cheese ourselves. We can simply get **mozzarella that someone else has already made beautifully** for us. Sure, we *could* try to make it from scratch (i.e. write the code ourselves), but it can be **quite hard** and time-consuming. **Packages** are exactly that: ready-made ingredients we can reuse instead of preparing everything from scratch.
:::

Most of these installable packages are published on a central repository called the [Python Package Index (PyPI)](https://pypi.org/), from which they can be downloaded and installed.

:::{note}
📦 **Other repositories**: `PyPI` is probably the most common place packages come from, but it is not the only one. In **scientific programming** you might also come across [conda-forge](https://conda-forge.org/), which is another place where packages can be stored for download and installation.
:::

## 3. Virtual Environments

Once we start installing packages, a new problem appears. Imagine you are working on **two different projects** at the same time:

- **Project A** needs **version 1.0** of a package.
- **Project B** needs **version 2.0** of that same package.

If all packages were installed in **one single shared place** on your computer, these two requirements would **conflict** with each other: installing the version needed for Project B would **break** Project A.

To avoid this, we use **virtual environments**.

A **virtual environment** is an **isolated workspace** (imagine a folder on your computer) that contains its **own packages** (and, as we will see, its own `Python`), completely **separate** from everything else on your computer. Each project gets its **own environment**, so the packages of one project can **never interfere** with the packages of another.

:::{note}
{{pizza}} **Analogy**: Imagine a kitchen that prepares **pizza** and **hot dogs** (Project A and Project B). Pizza needs **tomato sauce**, while hot dogs need **ketchup** (two different packages). If both recipes shared the same kitchen space, the sauces could get mixed up, and you might end up with ketchup on a pizza 😱! This does not work! By giving each recipe its **own dedicated space in the kitchen** (virtual environment), the ingredients of one **do not mix** with the ingredients of the other.
:::

A key idea is that virtual environments are **disposable**. An environment is **not precious**: if something goes wrong, or you no longer need a project, you can simply **delete the environment and recreate it from scratch**, without affecting `Python` itself or any of your other projects. This makes experimenting **safe**, you can always throw an environment away and start fresh.

## 4. Python Versions

Now that each project has its **own environment**, there is one more thing we may want to control: the **version of `Python`** itself.

Just like packages, `Python` evolves over time and comes in **different versions** (for example `Python 3.10`, `Python 3.11`, `Python 3.12`, ...). Sometimes a package only works with a **specific** version of `Python`, while another project might need a **newer** one.

For this reason, it is useful to be able to **install a specific version of `Python` inside each environment**. This way, Project A can use an older `Python` while Project B uses a newer one, again **without any conflict**.

## 5. Putting It All Together with uv

So far we have introduced three things we need to manage:

1. **Packages**, the libraries (or dependencies) our code depends on.
2. **Virtual environments**, the isolated and disposable workspaces for each project.
3. **Python versions**, the specific version of `Python` each environment uses.

How do we handle **all of this** easily? With a single tool called [`uv`](https://docs.astral.sh/uv/)!

`uv` is a **modern, extremely fast tool** that takes care of **everything** we just described. Instead of learning many different tools, you only have to learn **one**. With `uv` you can:

- **install and manage packages** in your project,
- **create and manage virtual environments** automatically,
- **download and install any version of `Python`** you need.

:::{note}
🔧 **Other tools**: `uv` is not the only tool that can manage packages, virtual environments, and `Python` versions together. Other popular options include [conda](https://docs.conda.io/) and [pixi](https://pixi.sh/), which are also common in scientific computing. In this course we will use `uv`, but the concepts you learn here apply to these other tools as well.
:::

:::{note}
💡 **NOTE**: In principle, you *can* download `Python` directly from the [official Python website](https://www.python.org/downloads/), and it will be installed **system-wide** on your computer. However, this is **not ideal**: installing packages directly into that system `Python` can quickly become messy and lead to the conflicts we described above. By letting `uv` manage the `Python` versions, the environments, and the packages for us, we keep everything **clean**, **reproducible**, and **easy to throw away** and recreate.
:::
