#!/usr/bin/env python3

import pandas as pd

def below_zero():
    df = pd.read_csv('src/kumpula-weather-2017.csv')
    filter_df = df[df['Air temperature (degC)'] < 0]
    # print(filter_df.head())
    num = filter_df['Air temperature (degC)'].count()
    return num

def main():
    num = below_zero()
    # print(num)
    print(f"Number of days below zero: {num}")
    return
    
if __name__ == "__main__":
    main()
