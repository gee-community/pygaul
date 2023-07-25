"""Tests of the continents submanagement."""
import json
from pathlib import Path

import pygaul

continent_file = Path(__file__).parents[1] / "pygaul" / "data" / "gaul_continent.json"


def test_file():
    """Check that the file is present."""
    assert continent_file.is_file()


def test_continent():
    """Check that the continent are working."""
    fc = pygaul.get_items(name="antartica")
    assert fc.aggregate_array("ADM0_CODE").getInfo() == [10]


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
