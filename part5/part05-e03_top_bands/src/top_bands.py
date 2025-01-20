#!/usr/bin/env python3

import pandas as pd

def top_bands():
    df = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep='\t')
    df1 = pd.read_csv('src/bands.tsv', sep='\t')
    # print(df.dtypes)
    # print(df1.dtypes)
    df1['Band'] = df1['Band'].str.upper()
    print(df1['Band'].head())
    merge_df = pd.merge(df, df1, left_on='Artist', right_on='Band', how='inner')
    return merge_df

def main():
    # print(top_bands())
    df = top_bands()
    print(df.dtypes)
    print(df.shape)
    return

if __name__ == "__main__":
    main()
