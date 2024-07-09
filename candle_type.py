def candle_type(o, h, l, c):

    diff = abs(c - o)     # body size
    o1, c1 = np.roll(o, 1), np.roll(c, 1)  # previous day open and close
    min_oc = np.where(o < c, o, c)  # smallest of open and close is used .
    max_oc = np.where(o > c, o, c)  # greatest of open and close is used .

    pattern = np.where(
      np.logical_and( min_oc - l > diff, h - max_oc < diff), ' Hammer',
      np.where(np.logical_and( h - max_oc > diff, min_oc - l < diff),
      ' Inverted Hammer', np.where(np.logical_and(np.logical_and(c > o, c1 < o1), np.logical_and(c > o1, o < c1)),
        ' Bullish Engulfing', np.where( min_oc - l > diff, ' Hanging Man',
                      np.where(np.logical_and( h - max_oc > diff,
                  min_oc - l < diff),
                      ' Shooting Star', np.where(np.logical_and(np.logical_and(c > o, c1 < o1), np.logical_and(c > o1, o < c1)),
                      ' Bearish Engulfing', ' None'))))))
    return pattern
