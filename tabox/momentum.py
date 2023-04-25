from pandas import Series


def price_percentile(win: Series) -> Series:
    return Series(win.rank(pct=True))
