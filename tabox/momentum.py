from typing import TypeVar

from pandas import DataFrame, Series

T_Pandas = TypeVar('T_Pandas', Series, DataFrame)


def price_percentile(win: T_Pandas) -> T_Pandas:
    if isinstance(win, Series):
        sr = Series(win.rank(pct=True))
        return sr
    elif isinstance(win, DataFrame):
        df = DataFrame(win.rank(axis=0, pct=True))
        return df
    else:
        raise TypeError('Only support Series or DataFrame')
