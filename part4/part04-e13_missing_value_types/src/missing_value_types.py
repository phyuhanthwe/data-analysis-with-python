#!/usr/bin/env python3

import pandas as pd
import numpy as np

def missing_value_types():
    data = {
        'State': ['United Kingdom', 'Finland', 'USA', 'Sweden', 'Germany', 'Russia'],
        'Year of independence': [np.nan, 1917, 1776, 1523, np.nan, 1992],
        'President': [None, 'Niinistö', 'Trump', None, 'Steinmeier', 'Putin']
    }
    df = pd.DataFrame(data)
    df.set_index('State', inplace=True)
    return df
               
def main():
    print(missing_value_types())
    return

if __name__ == "__main__":
    main()
