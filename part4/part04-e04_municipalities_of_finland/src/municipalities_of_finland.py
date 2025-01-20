#!/usr/bin/env python3

import pandas as pd

def municipalities_of_finland():
    df = pd.read_csv('src/municipal.tsv', sep='\t', index_col='Region 2018')
    muni_df = df.loc['Akaa' : 'Äänekoski']
    return muni_df
    
def main():
    print(municipalities_of_finland())
    return
    
if __name__ == "__main__":
    main()

