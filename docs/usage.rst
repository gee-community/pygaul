Usage
=====

Get admininstrative items
-------------------------

The PyGAUL lib can be used to extract information from the FAO GAUL dataset as :code:`ee.FeatureCollection`.

.. note::

    :code:`ee.FeatureCollection` can easily be converted to :code:`GeoDataFrame` but if interacting with Earthengine is not the chore of your usage, have a look to `pygadm <https://github.com/12rambau/pygadm>`__. It will provide accès to smaller administrative boundaries and return directly a gdf.

.. important::

    **PyGAUL** is not managing the connection to Google Earth Engine API. The user is responsible to set up the Initialization as he see fit.
    This is a feature to allow users with exotic GEE connection (e.g. service accounts) to continue use the lib without any modification.

Countries
^^^^^^^^^

Using the :code:`Items` class, you can access an administrative area using either its name or its GAUL identification code.

For example to extract the France geometry you can use the following code:

.. jupyter-execute::

    import pygaul
    from geemap import Map
    import ee

    ee.Initialize()

    fc = pygaul.Items(name="France")

    # display it in a map
    m = Map(zoom=5, center=[46.21, 2.21])
    m.addLayer(fc, {"color": "red"}, "")
    m

If you know the code of the area you try to use, you can use the GADM code instead of the name.

.. jupyter-execute::

    import pygaul
    from geemap import Map
    import ee

    ee.Initialize()

    fc = pygaul.Items(admin="85")

    # display it in a map
    m = Map(zoom=5, center=[46.21, 2.21])
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

    fc = pygaul.Items(name="Corse-du-Sud")

    # display it in a map
    m = Map(zoom=8, center=[41.86, 8.97])
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

    fc = pygaul.Items(admin="85", content_level=2)

    # display it in a map
    m = Map(zoom=5, center=[46.21, 2.21])
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

    fc = pygaul.Items(name=["France", "Germany"], content_level=1)

    # display it in a map
    m = Map(zoom=5, center=[48.83, 5.17])
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

    fc = pygaul.Items(name="europe")

    # display it in a map
    m = Map(zoom=4, center = [49.38237278700955, 31.464843750000004])
    m.addLayer(fc, {"color": "red"}, "")
    m

Find administrative names
-------------------------

To get the available name and GAUL code in a administrative layer you can use the :code:`Names` class with the same parameters. Use then these names in a :code:`Items` request to get the geometry.

For example to get the names and codes of all the departments in France you can run:

.. jupyter-execute::

    import pygaul

    pygaul.Names(admin="85", content_level=2)

.. note::

    If needed, one can get the names of the upper administrative layers by setting the ``complete`` parameter to ``True``.

    .. jupyter-execute::

        import pygaul

        pygaul.Names(admin="1270", content_level=2, complete=True)

.. note::

    You can also get the list of all the country names by omitting admin and name parameters. If a level is not provided the table will only show country names but other parameters remain availables.

    .. code-block:: python

        pygaul.Names()


Suggestion
----------

If you make an error when writing the name of your input, the error message will suggest 5 potential candidates in the existing names of the GADM dataset:


.. jupyter-execute::
    :raises: ValueError

    import pygaul
    import ee

    ee.Initialize()

    fc = pygaul.Items(name="Franc")
