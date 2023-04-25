from pandas import Series


def relative_strength_index(win: Series,
                            *,
                            len: int = 14) -> Series:
    delta = win.diff().dropna()
    up = delta.clip(lower=0)
    down = delta.clip(upper=0)
    ma_up = up.ewm(span=len).mean()
    ma_down = down.abs().ewm(span=len).mean()
    rs = ma_up / ma_down
    rsi = 100.0 - (100.0 / (1.0 + rs))
    return rsi
