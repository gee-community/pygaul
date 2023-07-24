"""Tests of the ``get_items`` function."""

import math

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


def test_area():
    """Request a known."""
    bounds = [
        103.63828400206005,
        1.1640393937452072,
        104.09003995172597,
        1.4712714973692553,
    ]
    fc = pygaul.get_items(name="Singapore")
    coords = fc.geometry().bounds().coordinates().get(0).getInfo()
    assert fc.first().get("ADM0_CODE").getInfo() == 222
    assert all([math.isclose(b, t) for b, t in zip([*coords[0], *coords[2]], bounds)])


def test_sub_content():
    """Request a sublevel."""
    sublevels = [2658, 2659, 2660, 2661, 2662, 2663, 2664, 2665, 2666]
    fc = pygaul.get_items(name="Singapore", content_level=1)
    assert all([i == 222 for i in fc.aggregate_array("ADM0_CODE").getInfo()])
    assert fc.aggregate_array("ADM1_CODE").getInfo() == sublevels


def test_too_high():
    """Request a sublevel higher than available in the area."""
    with pytest.warns(UserWarning):
        fc = pygaul.get_items(admin="2658", content_level=0)
        assert fc.aggregate_array("ADM1_CODE").getInfo() == [2658]


def test_too_low():
    """Request a sublevel lower than available in the area."""
    # request a level too low
    with pytest.warns(UserWarning):
        fc = pygaul.get_items(admin="2658", content_level=3)
        assert fc.aggregate_array("ADM1_CODE").getInfo() == [2658]


def test_case_insensitive():
    """Request an area without respecting the case."""
    fc1 = pygaul.get_items(name="Singapore")
    fc2 = pygaul.get_items(name="singaPORE")

    assert fc1.getInfo() == fc2.getInfo()


def test_multiple_input():
    """Test when several geometries are requested at once."""
    bounds = [
        -5.142230921252722,
        41.33878298628808,
        15.039879038982702,
        55.05564675594154,
    ]
    fc1 = pygaul.get_items(name=["france", "germany"])
    coords = fc1.geometry().bounds().coordinates().get(0).getInfo()
    assert all([math.isclose(b, t) for b, t in zip([*coords[0], *coords[2]], bounds)])

    fc2 = pygaul.get_items(admin=["85", "93"])
    assert fc1.getInfo() == fc2.getInfo()


def test_continent():
    """Check that the continent are working."""
    fc = pygaul.get_items(name="antartica")
    assert fc.aggregate_array("ADM0_CODE").getInfo() == [10]
