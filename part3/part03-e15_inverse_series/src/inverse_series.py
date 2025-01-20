#!/usr/bin/env python3

import pandas as pd

def inverse_series(s):
    return pd.Series(s.index, index=s.values)

def main():
    s = pd.Series({2001: "Bush", 2005: "Bush", 2009: "Obama", 2013: "Obama", 2017: "Trump"})
    print("Original Series:")
    print(s)

    inverted_s = inverse_series(s)
    print("\nInverted Series:")
    print(inverted_s)
    return

if __name__ == "__main__":
    main()
