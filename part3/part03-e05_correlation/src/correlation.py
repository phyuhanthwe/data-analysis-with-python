#!/usr/bin/env python3

import scipy.stats
import numpy as np

def load():
    import pandas as pd
    return pd.read_csv("src/iris.csv").drop('species', axis=1).values

def lengths():
    file = load()
    x = file[:, 0]
    y = file[:, 2]
    print(x.shape, y.shape)
    c, p = scipy.stats.pearsonr(x, y)
    return c

def correlations():
    file = load()
    x = file[:, 0]
    y = file[:, 1]
    a = file[:, 2]
    b = file[:, 3]
    data = np.stack([x, y, a, b])
    r = np.corrcoef(data)
    print(r.shape)
    return r

def main():
    print(lengths())
    print(correlations())

if __name__ == "__main__":
    main()
