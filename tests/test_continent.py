"""Tests of the continents submanagement."""

import json
from pathlib import Path

import pandas as pd

import pygaul

continent_file = Path(__file__).parents[1] / "pygaul" / "data" / "gaul_continent.json"
database_file = Path(__file__).parents[1] / "pygaul" / "data" / "gaul_database.parquet"


def test_file():
    """Check that the file is present."""
    assert continent_file.is_file()


def test_continent(data_regression):
    """Check that the continent are working."""
    fc = pygaul.Items(name="antartica")
    data_regression.check(fc.aggregate_array("ADM0_CODE").getInfo())


def test_duplication():
    """Make sure there are no duplicates in the continent database."""
    continent_dict = json.loads(continent_file.read_text())
    duplicates = {}
    for continent in continent_dict:
        duplicates[continent] = set()
        current_set = set(continent_dict[continent])
        for other in continent_dict:
            if other == continent:
                continue
            other_list = continent_dict[other]
            intersection = current_set.intersection(other_list)
            duplicates[continent] = duplicates[continent].union(intersection)

    assert all([len(duplicates[c]) == 0 for c in duplicates])


def test_orphan():
    """Check that all countries are in a continent."""
    data = pd.read_parquet(database_file)
    continent_dict = json.loads(continent_file.read_text())
    countries = data.ADM0_CODE.unique()
    orphan = []
    for country in countries:
        exist = False
        for continent in continent_dict:
            if country in continent_dict[continent]:
                exist = True
                break
        if exist is False:
            orphan.append(country)
    assert len(orphan) == 0
