"""Tests of the ``get_name`` function."""

import pytest

import pygaul


def test_empty():
    """Empty request."""
    with pytest.raises(Exception):
        pygaul.get_names()


def test_duplicate_input():
    """Request with too many parameters."""
    with pytest.raises(Exception):
        pygaul.get_names(name="Singapore", admin="222")


def test_non_existing():
    """Request non existing area."""
    with pytest.raises(Exception):
        pygaul.get_names(name="t0t0")

    with pytest.raises(Exception):
        pygaul.get_names(admin="t0t0")


def test_area():
    """Request a known."""
    sublevels = ["Singapore"]
    df = pygaul.get_names(name="Singapore")
    assert sorted(df.ADM0_NAME.to_list()) == sublevels


def test_sub_content():
    """Request a sublevel."""
    sublevels = ["2658", "2659", "2660", "2661", "2662", "2663", "2664", "2665", "2666"]
    df = pygaul.get_names(name="Singapore", content_level=1)
    assert sorted(df.ADM1_CODE.to_list()) == sublevels
    assert len(df) == 9


def test_too_high():
    """Request a sublevel higher than available in the area."""
    with pytest.warns(UserWarning):
        df = pygaul.get_names(admin="2658", content_level=0)
        assert len(df) == 1
        assert df.ADM1_NAME.to_list() == ["Ang Mo Kio-cheng San"]


def test_too_low():
    """Request a sublevel lower than available in the area."""
    with pytest.warns(UserWarning):
        df = pygaul.get_names(admin="2658", content_level=4)
        assert len(df) == 1
        assert df.ADM1_NAME.to_list() == ["Ang Mo Kio-cheng San"]


def test_case_insensitive():
    """Request an area without respecting the case."""
    df1 = pygaul.get_names(name="Singapore")
    df2 = pygaul.get_names(name="singaPORE")

    assert df1.equals(df2)


def test_suggestions():
    """Test that when a wrong name is given 5 options are proposed in the error message."""
    expected_error = 'The requested "Franc" is not part of FAO GAUL 2015. The closest matches are: France, Franca, Ranco, Rancul, Ranchi.'
    with pytest.raises(ValueError, match=expected_error):
        pygaul.get_names(name="Franc")
