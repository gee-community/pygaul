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


def test_area(data_regression):
    """Request a known."""
    df = pygaul.get_names(name="Singapore")
    data_regression.check(df.ADM0_NAME.to_list())


def test_sub_content(data_regression):
    """Request a sublevel."""
    df = pygaul.get_names(name="Singapore", content_level=1)
    data_regression.check(df.ADM1_CODE.to_list())


def test_too_high(data_regression):
    """Request a sublevel higher than available in the area."""
    with pytest.warns(UserWarning):
        df = pygaul.get_names(admin="2658", content_level=0)
        data_regression.check(df.ADM1_NAME.to_list())


def test_too_low(data_regression):
    """Request a sublevel lower than available in the area."""
    with pytest.warns(UserWarning):
        df = pygaul.get_names(admin="2658", content_level=4)
        data_regression.check(df.ADM1_NAME.to_list())


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
