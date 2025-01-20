#!/usr/bin/env python3

import pandas as pd

def growing_municipalities(df):
    df_subset = df.dropna(subset=['Population change from the previous year, %'])
    growing_municipalities = df_subset[df_subset['Population change from the previous year, %'] > 0]
    growing_count = len(growing_municipalities)
    print("Number of growing municipalities:", growing_count)

    total_count = len(df_subset)
    print("Total number of municipalities in subset:", total_count)

    proportion = (growing_count / total_count) 
    print("Calculated proportion:", proportion)

    return proportion

def main():
    df = pd.read_csv('src/municipal.tsv', sep='\t', index_col='Region 2018')
    # print(df.columns)
    df1 = df.loc['Akaa':'Äänekoski']
    proportion = growing_municipalities(df1)
    print(f"Proportion of growing municipalities: {proportion:.1f}%")
    return

if __name__ == "__main__":
    main()
