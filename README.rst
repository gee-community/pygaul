pyGAUL
======

.. image:: https://img.shields.io/badge/License-MIT-yellow.svg?logo=opensourceinitiative&logoColor=white
    :target: LICENSE
    :alt: License: MIT

.. image:: https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg?logo=git&logoColor=white
   :target: https://conventionalcommits.org
   :alt: conventional commit

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Black badge

.. image:: https://img.shields.io/badge/code_style-prettier-ff69b4.svg?logo=prettier&logoColor=white
   :target: https://github.com/prettier/prettier
   :alt: prettier badge

.. image:: https://img.shields.io/badge/pre--commit-active-yellow?logo=pre-commit&logoColor=white
    :target: https://pre-commit.com/
    :alt: pre-commit

.. image:: https://img.shields.io/pypi/v/pygaul?color=blue&logo=pypi&logoColor=white
    :target: https://pypi.org/project/pygaul/
    :alt: PyPI version

.. image:: https://img.shields.io/conda/vn/conda-forge/pygaul?logo=condaforge&logoColor=white&color=orange
    :target: https://anaconda.org/conda-forge/pygaul
    :alt: conda distrib

.. image:: https://img.shields.io/github/actions/workflow/status/12rambau/pygaul/unit.yaml?logo=github&logoColor=white
    :target: https://github.com/12rambau/pygaul/actions/workflows/unit.yaml
    :alt: build

.. image:: https://img.shields.io/codecov/c/github/gee-community/pygaul?logo=codecov&logoColor=white
    :target: https://codecov.io/gh/gee-community/pygaul
    :alt: Test Coverage

.. image:: https://img.shields.io/readthedocs/pygaul?logo=readthedocs&logoColor=white
    :target: https://pygaul.readthedocs.io/en/latest/
    :alt: Documentation Status

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

   fc = pygaul.Items(name="Singapore", content_level=1)

Note
----

the dataset was generated in 2015 by the Food and Alimentation Organization (FAO). It has not been updated on Google Earthengine since then. Use with caution on disputed territories.

Credits
-------

This package was created with `Cookiecutter <https://github.com/cookiecutter/cookiecutter>`__ and the `12rambau/pypackage <https://github.com/12rambau/pypackage>`__ project template.
