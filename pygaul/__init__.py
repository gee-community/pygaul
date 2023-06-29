"""
Easy access to administrative boundary defined by FAO GAUL 2015 from Python scripts.

This lib provides access to FAO GAUL 2015 datasets from a Python script. it is the best boundary dataset available for GEE at this point. We provide access to The current version (2015) administrative areas till level 2.
"""
import warnings
from difflib import get_close_matches
from pathlib import Path

import numpy as np
import pandas as pd

__version__ = "0.0.0"
__author__ = "Pierrick Rambaud"
__email__ = "pierrick.rambaud49@gmail.com"

__gaul_data__ = Path(__file__).parent / "data" / "gaul_database.parquet"


def hello_world() -> str:
    """Hello world demo method.

    Returns:
        the hello world string
    """
    return "hello world !"


def get_names(name: str = "", admin: str = "", content_level: int = -1) -> pd.DataFrame:
    """
    Return the list of names available in a administrative layer using the name or the administrative code.

    Return a pandas DataFrame of the names as FAO GAUL codes of and administrative region. The region can be requested either by its "name" or its "admin", the lib will identify the corresponding level on the fly. The user can also request for a specific level for its content e.g. get all admin level 1 of a country. If nothing is set we will infer the level of the item and if the level is higher than the found item, it will be ignored. If Nothing is found the method will raise an error.

    Args:
        name: The name of a administrative area. Cannot be set along with :code:`admin`.
        admin: The id of an administrative area in the FAO GAUL nomenclature. Cannot be set along with :code:`name`.
        content_level: The level to use in the final dataset. Default to -1 (use level of the selected area).

    Returns:
        The list of all the available names.
    """
    # sanitary check on parameters
    if name and admin:
        raise ValueError('"name" and "id" cannot be set at the same time.')
    elif not name and not admin:
        raise ValueError('at least "name" or "admin" need to be set.')

    # set the id we look for and tell the function if its a name or an admin
    is_name = True if name else False
    id = name if name else admin

    # read the data and find if the element exist
    df = pd.read_parquet(__gaul_data__)
    column = "ADM{}_NAME" if is_name else "ADM{}_CODE"
    is_in = (
        df.filter([column.format(i) for i in range(3)])
        .apply(lambda col: col.str.lower())
        .isin([id.lower()])
    )

    if not is_in.any().any():
        # find the 5 closest names/id
        columns = [df[column.format(i)].dropna().str.lower().values for i in range(3)]
        ids = np.unique(np.concatenate(columns))
        close_ids = get_close_matches(id.lower(), ids, n=5)
        if is_name is True:
            close_ids = [i.capitalize() for i in close_ids]
        else:
            close_ids = [i.upper() for i in close_ids]
        raise ValueError(
            f'The requested "{id}" is not part of FAO GAUL 2015. The closest matches are: {", ".join(close_ids)}.'
        )

    # Get the code of the associated country of the identifed area and the associated level
    line = is_in[~((~is_in).all(axis=1))].idxmax(1)
    level = line.iloc[0][3]

    # load the max_level available in the requested area
    sub_df = df[df[column.format(level)].str.fullmatch(id, case=False)]
    max_level = next(
        i for i in reversed(range(3)) if (sub_df[f"ADM{i}_NAME"] != "").any()
    )

    # get the request level from user
    if content_level == -1:
        content_level = level
    elif content_level < int(level):
        warnings.warn(
            f"The requested level ({content_level}) is higher than the area ({level}). Fallback to {level}."
        )
        content_level = level

    if int(content_level) > max_level:
        warnings.warn(
            f"The requested level ({content_level}) is higher than the max level in this country ({max_level}). Fallback to {max_level}."
        )
        content_level = max_level

    # get the columns name to display
    columns = [f"ADM{content_level}_NAME", f"ADM{content_level}_CODE"]

    # the list will contain duplicate as all the smaller admin level will be included
    sub_df = sub_df[columns].drop_duplicates(ignore_index=True)

    # the list will contain NA as all the bigger admin level will be selected as well
    # the database is read as pure string so dropna cannot be used
    # .astype is also a vectorized operation so it goes very fast
    final_df = sub_df[sub_df[columns[0]].astype(bool)]

    return final_df
