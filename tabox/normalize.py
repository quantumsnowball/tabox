from typing import TypeVar

from pandas import DataFrame, Series

T_Pandas = TypeVar('T_Pandas', Series, DataFrame)


def normalize(win: T_Pandas) -> T_Pandas:
    if isinstance(win, Series):
        sr = (win - win.min()) / (win.max() - win.min())
        return sr
    elif isinstance(win, DataFrame):
        df = (win - win.min()) / (win.max() - win.min())
        return df
    else:
        raise TypeError('Only support Series or DataFrame')
