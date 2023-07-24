Usage
=====

Get items
---------

The PyGAUL lib can be used to extract information from the FAO GAUL dataset as :code:`ee.FeatureCollection`.

.. important::

    **PyGAUL** is not managing the connection to Google Earth Engine API. The user is responsible to set up the Initialization as he see fit.
    This is a feature to allow users with exotic GEE connection (e.g. service accounts) to continue use the lib without any modification.

Countries
^^^^^^^^^

Using the :code:`get_items` methods, you can access an administrative area using either its name or its GAUL identification code.

For example to extract the France geometry you can use the following code:

.. jupyter-execute::

    import pygaul
    from geemap import Map
    import ee

    ee.Initialize()

    fc = pygaul.get_items(name="France")

    # display it in a map
    m = Map()
    m.centerObject(fc)
    m.addLayer(fc, {"color": "red"}, "")
    m

If you know the code of the area you try to use, you can use the GADM code instead of the name.

.. jupyter-execute::

    import pygaul
    from geemap import Map
    import ee

    ee.Initialize()

    fc = pygaul.get_items(admin="85")

    # display it in a map
    m = Map()
    m.centerObject(fc)
    m.addLayer(fc, {"color": "red"}, "")
    m

Smaller admin levels
^^^^^^^^^^^^^^^^^^^^

One is not bind to only request a country, any level can be accessed using both names and/or GADM code.

.. jupyter-execute::

    import pygaul
    from geemap import Map
    import ee

    ee.Initialize()

    fc = pygaul.get_items(name="Corse-du-Sud")

    # display it in a map
    m = Map()
    m.centerObject(fc)
    m.addLayer(fc, {"color": "red"}, "")
    m

.. warning::

    The names of countries are all unique but not the smaller administrative layers. If you request a small area using name, make sure it's the one you are looking for before running your workflow. follow :ref:`usage:Duplication issue` for more information.

Content of an admin layer
^^^^^^^^^^^^^^^^^^^^^^^^^

Using the :code:`content_level` option, one can require smaller administrative layer than the one setup in the name. For example when you request France, by setting up the :code:`content_level` option to 2, the geodataframe will include all the department geometries.

.. jupyter-execute::

    import pygaul
    from geemap import Map
    import ee

    ee.Initialize()

    fc = pygaul.get_items(admin="85", content_level=2)

    # display it in a map
    m = Map()
    m.centerObject(fc)
    m.addLayer(fc, {"color": "red"}, "")
    m

Request multiple areas at once
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To perform regional analysis that aggregate multiple boundaries, you can now request them at once using a list of ``name`` or a list of ``admin``. In this example we request both germany and France at once:

.. jupyter-execute::

    import pygaul
    from geemap import Map
    import ee

    ee.Initialize()

    fc = pygaul.get_items(name=["France", "Germany"], content_level=1)

    # display it in a map
    m = Map()
    m.centerObject(fc)
    m.addLayer(fc, {"color": "red"}, "")
    m

Continents
^^^^^^^^^^

It's possible to request all countries from one single continent using one of the following names:

-   North America
-   South America
-   Antartica
-   Europe
-   Asia
-   Oceania
-   Africa

.. jupyter-execute::

    import pygaul
    from geemap import Map
    import ee

    ee.Initialize()

    fc = pygaul.get_items(name="europe")

    # display it in a map
    m = Map()
    m.centerObject(fc)
    m.addLayer(fc, {"color": "red"}, "")
    m

Find names
----------

To get the available name and GAUL code in a administrative layer you can use the :code:`get_names` method with the same parameters. Use then these names in a :code:`get_items` request to get the geometry.

For example to get the name and codes of all the departments in France you can run:

.. jupyter-execute::

    import pygaul

    pygaul.get_names(admin="85", content_level=2)

Suggestion
----------

If you make an error when writing the name of your input, the error message will suggest 5 potential candidates in the existing names of the GADM dataset:


.. jupyter-execute::
    :raises: ValueError

    import pygaul
    import ee

    ee.Initialize()

    fc = pygaul.get_items(name="Franc")

