"""Tests of the continents submanagement."""
import pygaul


def test_continent(data_regression):
    """Check that the continent are working."""
    fc = pygaul.Items(name="Africa")
    data_regression.check(fc.aggregate_array("gaul0_name").getInfo())
