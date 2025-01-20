#!/usr/bin/env python3

import pandas as pd

def cyclists():
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';')
    df = df.dropna(how='all')
    clean_df = df.dropna(axis=1, how='all')
    # print(clean_df.shape)
    return clean_df


def main():
    print(cyclists())
    return
    
if __name__ == "__main__":
    main()
