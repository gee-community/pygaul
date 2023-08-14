"""Tests of the ``get_items`` function."""


import pytest

import pygaul


def test_empty():
    """Empty request."""
    with pytest.raises(Exception):
        pygaul.get_items()


def test_duplicate_intput():
    """Request with too many parameters."""
    # request with too many things
    with pytest.raises(Exception):
        pygaul.get_items(name="Singapore", admin="222")


def test_non_existing():
    """Request non existing area."""
    with pytest.raises(Exception):
        pygaul.get_items(name="t0t0")

    with pytest.raises(Exception):
        pygaul.get_items(admin="t0t0")


def test_area(data_regression):
    """Request a known geometry."""
    fc = pygaul.get_items(name="Singapore")
    assert fc.size().getInfo() == 1
    assert fc.first().get("ADM0_CODE").getInfo() == 222
    data_regression.check(fc.geometry().bounds().coordinates().get(0).getInfo())


def test_sub_content(data_regression):
    """Request a sublevel."""
    fc = pygaul.get_items(name="Singapore", content_level=1)
    assert all([i == 222 for i in fc.aggregate_array("ADM0_CODE").getInfo()])
    data_regression.check(fc.aggregate_array("ADM1_CODE").getInfo())


def test_too_high():
    """Request a sublevel higher than available in the area."""
    with pytest.warns(UserWarning):
        fc = pygaul.get_items(admin="2658", content_level=0)
        assert fc.size().getInfo() == 1
        assert fc.aggregate_array("ADM1_CODE").getInfo() == [2658]


def test_too_low():
    """Request a sublevel lower than available in the area."""
    # request a level too low
    with pytest.warns(UserWarning):
        fc = pygaul.get_items(admin="2658", content_level=3)
        assert fc.size().getInfo() == 1
        assert fc.aggregate_array("ADM1_CODE").getInfo() == [2658]


def test_case_insensitive():
    """Request an area without respecting the case."""
    fc1 = pygaul.get_items(name="Singapore")
    fc2 = pygaul.get_items(name="singaPORE")

    assert fc1.getInfo() == fc2.getInfo()


def test_multiple_input(data_regression):
    """Test when several geometries are requested at once."""
    fc1 = pygaul.get_items(name=["france", "germany"])
    data_regression.check(fc1.getInfo())

    fc2 = pygaul.get_items(admin=["85", "93"])
    assert fc1.getInfo() == fc2.getInfo()
