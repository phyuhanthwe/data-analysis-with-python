#!/usr/bin/env python3

import pandas as pd

def subsetting_by_positions():
    df = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep='\t')
    df1 = df.iloc[0:10,[2, 3]]
    return df1

def main():
    print(subsetting_by_positions())
    return

if __name__ == "__main__":
    main()
