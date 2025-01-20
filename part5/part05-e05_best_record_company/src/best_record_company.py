#!/usr/bin/env python3

import pandas as pd

def best_record_company():
    df = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep='\t')
    woc_by_publisher = df.groupby('Publisher')['WoC'].sum()
    best_publisher = woc_by_publisher.idxmax()
    best_df = df[df['Publisher'] == best_publisher]
    return best_df

def main():
    print(best_record_company())
    return
    

if __name__ == "__main__":
    main()
