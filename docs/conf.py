"""Configuration file for the Sphinx documentation builder.

This file only contains a selection of the most common options. For a full
list see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

# -- Path setup ----------------------------------------------------------------
import os
import re
from datetime import datetime
from pathlib import Path

import ee
import httplib2

# -- Project information -------------------------------------------------------
project = "pyGAUL"
author = "Pierrick Rambaud"
copyright = f"2023-{datetime.now().year}, {author}"
release = "0.3.4"

# -- General configuration -----------------------------------------------------
extensions = [
    "sphinx_copybutton",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx_design",
    "autoapi.extension",
    "sphinxcontrib.icon",
    "jupyter_sphinx",
]
exclude_patterns = ["**.ipynb_checkpoints"]
templates_path = ["_template"]

# -- Options for HTML output ---------------------------------------------------
html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]
html_logo = "_static/logo.png"
html_theme_options = {
    "logo": {
        "text": project,
    },
    "use_edit_page_button": True,
    "footer_end": ["theme-version", "pypackage-credit"],
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/gee-community/pygaul",
            "icon": "fa-brands fa-github",
        },
        {
            "name": "Pypi",
            "url": "https://pypi.org/project/pygaul/",
            "icon": "fa-brands fa-python",
        },
        {
            "name": "Conda",
            "url": "https://anaconda.org/conda-forge/pygaul",
            "icon": "fa-custom fa-conda",
            "type": "fontawesome",
        },
    ],
}
html_context = {
    "github_user": "gee-community",
    "github_repo": "pygaul",
    "github_version": "main",
    "doc_path": "docs",
}
html_css_files = ["custom.css"]

# -- Options for autosummary/autodoc output ------------------------------------
autodoc_typehints = "description"
autoapi_dirs = ["../pygaul"]
autoapi_python_class_content = "init"
autoapi_member_order = "groupwise"


# -- Script to authenticate to Earthengine using a token -----------------------
def gee_configure() -> None:
    """Initialize earth engine according to the environment.

    It will use the creddential file if the EARTHENGINE_TOKEN env variable exist.
    Otherwise it use the simple Initialize command (asking the user to register if necessary).
    """
    # only do the initialization if the credential are missing
    if not ee.data._credentials:
        # if the credentials token is asved in the environment use it
        if "EARTHENGINE_TOKEN" in os.environ:
            # get the token from environment variable
            ee_token = os.environ["EARTHENGINE_TOKEN"]

            # as long as RDT quote the token, we need to remove the quotes before writing
            # the string to the file
            pattern = r"^'[^']*'$"
            if re.match(pattern, ee_token) is not None:
                ee_token = ee_token[1:-1]

            # write the token to the appropriate folder
            credential_folder_path = Path.home() / ".config" / "earthengine"
            credential_folder_path.mkdir(parents=True, exist_ok=True)
            credential_file_path = credential_folder_path / "credentials"
            credential_file_path.write_text(ee_token)

        # if the user is in local development the authentication should
        # already be available
        ee.Initialize(http_transport=httplib2.Http())


gee_configure()

# -- Options for intersphinx output --------------------------------------------
intersphinx_mapping = {}
