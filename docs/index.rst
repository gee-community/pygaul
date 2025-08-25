:html_theme.sidebar_secondary.remove:


pyGAUL
======

.. toctree::
   :hidden:

   usage
   contribute

Easy access to administrative boundary defined by FAO GAUL 2015 from Python scripts.

This lib provides access to FAO GAUL 2015 datasets from a Python script. it is the best boundary dataset available for GEE at this point. We provide access to The current version (2015) administrative areas till level 2.

.. note::

   the dataset was generated in 2015 by the Food and Alimentation Organization (FAO). It has not been updated on Google Earthengine since then. Use with caution on disputed territories.

install it using either ``pip`` or ``conda``:

.. code-block:: console

   pip install pygaul

and then request area of interest from their name or GADM Id:

.. code-block:: python

   import pygaul

   fc = pygaul.Items(name="Singapore", content_level=1)

Documentation contents
----------------------

The documentation contains 3 main sections:

.. grid:: 1 2 3 3

   .. grid-item::

      .. card:: Usage
         :link: usage.html

         Usage and installation

   .. grid-item::

      .. card:: Contribute
         :link: contribute.html

         Help us improve the lib.

   .. grid-item::

      .. card:: API
         :link: autoapi/index.html

         Discover the lib API.
