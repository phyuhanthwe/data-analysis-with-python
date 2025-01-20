#!/usr/bin/env python3

import pandas as pd


def bicycle_timeseries():
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';')
    pattern = r'\w+\s(\d+)\s(\w+)\s(\d+)\s(\d+:\d+)'
    df1 = df.Päivämäärä.str.extract(pattern)    
    df1.columns = ['Day', 'Month', 'Year', 'Hour']
    month_map = {'tammi': '1', 'helmi': '2', 'maalis': '3', 'huhti': '4', 'touko': '5', 'kesä': '6', 'heinä': '7', 'elo': '8', 'syys': '9', 'loka': '10', 'marras': '11', 'joulu': '12'}
    df1.Month = df1['Month'].map(month_map)
    df2 = pd.concat([df1, df], axis=1)
    df2 = df2.dropna(how='all')
    df2['DateTime'] = pd.to_datetime(df2[['Year', 'Month', 'Day']].astype(str).agg('-'.join, axis=1) + ' ' + df2['Hour'])
    df2.drop(columns=['Päivämäärä', 'Unnamed: 21', 'Day', 'Month', 'Year', 'Hour'], inplace=True)
    df2 = df2.set_index('DateTime')
    return df2


def main():
    df = bicycle_timeseries()
    print(df.head())
    print(df.shape)
    return None

if __name__ == "__main__":
    main()
