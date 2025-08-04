author = "Federico Gasparoli - Image Analysis Collaboratory @ Harvard Medical School - federico.gasparoli@gmail.com"
comments_config = {"hypothesis": False, "utterances": False}
copyright = "2025"

extensions = [
    "sphinx_togglebutton",
    "sphinx_copybutton",
    "myst_nb",
    "jupyter_book",
    "sphinx_thebe",
    "sphinx_comments",
    "sphinx_external_toc",
    "sphinx.ext.intersphinx",
    "sphinx_design",
    "sphinx_book_theme",
    "sphinx_jupyterbook_latex",
    "sphinx_multitoc_numbering",
]

external_toc_exclude_missing = False

html_css_files = ["styles/custom.css"]
html_js_files = ["scripts/custom.js"]

html_static_path = ["_static"]

html_theme = "sphinx_book_theme"

html_theme_options = {
    "search_bar_text": "Search this book...",
    "use_download_button": False,
    "launch_buttons": {
        "notebook_interface": "classic",
        # not using directly colab because we want to customise the notebook for colab
        # "colab_url": "https://colab.research.google.com",
    },
    "repository_url": "https://github.com/HMS-IAC/bobiac/",
    "repository_branch": "main",
    "extra_footer": '<p>\nAll content is licensed under <a href="https://creativecommons.org/licenses/by/4.0/" target="_blank">CC-BY 4.0</a>, except where noted otherwise.\n</p>\n',
    "home_page_in_toc": True,
    "use_repository_button": True,
    "use_edit_page_button": False,
    "use_issues_button": False,
    "logo": {
        # "text": "BoBiAC Book",
        # "image_light": "_static/logo/bobiac_logos_svgexport-03.svg",
        # "image_dark": "_static/logo/bobiac_logos_svgexport-04.svg",
        "image_light": "_static/logo/bobiac-landing-black.png",
        "image_dark": "_static/logo/bobiac-landing-white.png",
    },
}

html_title = "BoBiAC Book"

latex_engine = "pdflatex"

myst_enable_extensions = [
    "colon_fence",
    "dollarmath",
    "linkify",
    "substitution",
    "tasklist",
]

myst_url_schemes = ["mailto", "http", "https"]

nb_execution_allow_errors = False
nb_execution_in_temp = False
# nb_execution_mode = "force"
nb_execution_mode = "cache"
nb_execution_timeout = 30
nb_output_stderr = "show"

numfig = True

pygments_style = "sphinx"

suppress_warnings = ["myst.domains"]

use_jupyterbook_latex = True

use_multitoc_numbering = True

exclude_patterns = [
    ".DS_Store",
    ".venv",
    "_internal/**",
    "README.md",
    "update_notebooks.py",
    "build.sh",
    # This is to exclude the specific notebook from the build to speed up the process
    # during development.
    # "content/01_intro_to_bobiac/**",
    # "content/02_getting_started_with_python/**",
    # "content/03_python_basics/**",
    # "content/04_digital_images_intro/**",
    # "content/05_segmentation/**",
    # "content/05_segmentation/classic/**",
    # "content/05_segmentation/deep_learning/**",
    # "content/05_segmentation/machine_learning/**",
    # "content/06_object_classification/**",
    # "content/07_measurement_and_quantification/**",
    # "content/08_colocalization/**",
]
