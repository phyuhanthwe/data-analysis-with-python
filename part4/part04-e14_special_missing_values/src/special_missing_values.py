#!/usr/bin/env python3

import pandas as pd
import numpy as np

def special_missing_values():
    df = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep='\t')
    df.LW = df['LW'].replace(['Re', 'New'], None)
    df = df.dropna(subset=['LW'])
    df = df.astype({'LW':int})
    # print(df.dtypes)
    filter_df = df[df.LW < df.Pos]
    return filter_df

def main():
    print(special_missing_values())
    return

if __name__ == "__main__":
    main()
