#!/usr/bin/env python3

import pandas as pd

def main():
    file = pd.read_csv('src/municipal.tsv', sep='\t')
    # print('Shape:',file.shape[0], ',', file.shape[1])
    print(f"Shape: {file.shape[0]},{file.shape[1]}")
    print('Columns:')
    # print(type(file.columns))
    for i in (file.columns):
        print(i)
    return


if __name__ == "__main__":
    main()
