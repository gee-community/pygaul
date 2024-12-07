
pyGAUL
======

.. |license| image:: https://img.shields.io/badge/License-MIT-yellow.svg?logo=opensourceinitiative&logoColor=white
    :target: LICENSE
    :alt: License: MIT

.. |commit| image:: https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg?logo=git&logoColor=white
   :target: https://conventionalcommits.org
   :alt: conventional commit

.. |ruff| image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
   :target: https://github.com/astral-sh/ruff
   :alt: ruff badge

.. |prettier| image:: https://img.shields.io/badge/code_style-prettier-ff69b4.svg?logo=prettier&logoColor=white
   :target: https://github.com/prettier/prettier
   :alt: prettier badge

.. |pre-commmit| image:: https://img.shields.io/badge/pre--commit-active-yellow?logo=pre-commit&logoColor=white
    :target: https://pre-commit.com/
    :alt: pre-commit

.. |pypi| image:: https://img.shields.io/pypi/v/pygaul?color=blue&logo=pypi&logoColor=white
    :target: https://pypi.org/project/pygaul/
    :alt: PyPI version

.. |conda| image:: https://img.shields.io/conda/vn/conda-forge/pygaul?logo=condaforge&logoColor=white&color=orange
    :target: https://anaconda.org/conda-forge/pygaul
    :alt: conda distrib

.. |build| image:: https://img.shields.io/github/actions/workflow/status/gee-community/pygaul/unit.yaml?logo=github&logoColor=white
    :target: https://github.com/gee-community/pygaul/actions/workflows/unit.yaml
    :alt: build

.. |coverage| image:: https://img.shields.io/codecov/c/github/gee-community/pygaul?logo=codecov&logoColor=white
    :target: https://codecov.io/gh/gee-community/pygaul
    :alt: Test Coverage

.. |docs| image:: https://img.shields.io/readthedocs/pygaul?logo=readthedocs&logoColor=white
    :target: https://pygaul.readthedocs.io/en/latest/
    :alt: Documentation Status

|license| |commit| |ruff| |prettier| |pre-commmit| |pypi| |conda| |build| |coverage| |docs|

Overview
--------

.. image:: docs/_static/logo.svg
    :width: 20%
    :align: right

Easy access to administrative boundary defined by FAO GAUL 2015 from Python scripts.

This lib provides access to FAO GAUL 2015 datasets from a Python script. it is the best boundary dataset available for GEE at this point. We provide access to The current version (2015) administrative areas till level 2.

install it using either ``pip`` or ``conda``:

.. code-block:: console

   pip install pygaul

and then request area of interest from their name or GADM Id:

.. code-block:: python

   import pygaul

   gdf = pygaul.Items(name="Singapore", content_level=1)

Note
----

the dataset was generated in 2015 by the Food and Alimentation Organization (FAO). It has not been updated on Google Earthengine since then. Use with caution on disputed territories.


Credits
-------

This package was created with `Copier <https://copier.readthedocs.io/en/latest/>`__ and the `@12rambau/pypackage <https://github.com/12rambau/pypackage>`__ 0.1.15 project template.
