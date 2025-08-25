"""Tests of the ``AdmNames`` object."""

import pytest

import pygaul


def test_empty(dataframe_regression):
    """Empty request, should list the countries."""
    df = pygaul.Names()
    dataframe_regression.check(df)


def test_duplicate_input():
    """Request with too many parameters."""
    with pytest.raises(Exception):
        pygaul.Names(name="Singapore", admin="222")


def test_non_existing():
    """Request non existing area."""
    with pytest.raises(Exception):
        pygaul.Names(name="t0t0")

    with pytest.raises(Exception):
        pygaul.Names(admin="t0t0")


def test_area(dataframe_regression):
    """Request a known."""
    df = pygaul.Names(name="Singapore")
    dataframe_regression.check(df)


def test_sub_content(dataframe_regression):
    """Request a sublevel."""
    df = pygaul.Names(name="Singapore", content_level=1)
    dataframe_regression.check(df)


def test_complete_content(dataframe_regression):
    """Request the complete hierarchy of an area."""
    df = pygaul.Names(name="Singapore", content_level=1, complete=True)
    dataframe_regression.check(df)


def test_too_high(dataframe_regression):
    """Request a sublevel higher than available in the area."""
    with pytest.warns(UserWarning):
        df = pygaul.Names(admin="2968", content_level=0)
        dataframe_regression.check(df)


def test_too_low(dataframe_regression):
    """Request a sublevel lower than available in the area."""
    with pytest.warns(UserWarning):
        df = pygaul.Names(admin="3435", content_level=4)
        dataframe_regression.check(df)


def test_case_insensitive():
    """Request an area without respecting the case."""
    df1 = pygaul.Names(name="Singapore")
    df2 = pygaul.Names(name="singaPORE")

    assert df1.equals(df2)


def test_suggestions():
    """Test that when a wrong name is given 5 options are proposed in the error message."""
    expected_error = 'The requested "Franc" is not part of FAO GAUL 2024. The closest matches are: France, Franca, Ranco, Franciou, Rancul.'
    with pytest.raises(ValueError, match=expected_error):
        pygaul.Names(name="Franc")


def test_get_names():
    """Test that get_names still works."""
    df1 = pygaul.Names(name="Singapore")

    with pytest.warns(DeprecationWarning):
        df2 = pygaul.get_names(name="Singapore")
        assert df1.equals(df2)


def test_adm_names():
    """Test that AdmNames still works."""
    df1 = pygaul.Names(name="Singapore")

    with pytest.warns(DeprecationWarning):
        df2 = pygaul.AdmNames(name="Singapore")
        assert df1.equals(df2)
