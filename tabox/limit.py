def crop(value: float,
         low: float,
         high: float) -> float:
    ''' clip a value between low and high '''
    return min(max(value, low), high)
