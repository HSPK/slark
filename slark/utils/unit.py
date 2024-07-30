from typing import List

import pandas as pd

from slark.types.spreadsheets.data import CellTypes


def values_to_dataframe(
    values: List[List[CellTypes]], *, has_header: bool = True, dropna: bool = True
) -> pd.DataFrame:
    values = [[cell.text if hasattr(cell, "text") else cell for cell in row] for row in values]
    if has_header:
        df = pd.DataFrame(values[1:], columns=values[0])
    else:
        df = pd.DataFrame(values)
    if dropna:
        df = df.dropna(axis=0, how="all").dropna(axis=1, how="all")
    return df


def dataframe_to_values(df: pd.DataFrame, *, has_header: bool = True) -> List[List[CellTypes]]:
    if has_header:
        values = [df.columns.tolist()] + df.values.tolist()
    else:
        values = df.values.tolist()
    return values
