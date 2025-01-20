#!/usr/bin/env python3

import pandas as pd


def split_date(df):
    pattern = r"(\w+)\s(\d+)\s(\w+)\s(\d+)\s(\d+):\d+"
    df1 = df.Päivämäärä.str.extract(pattern)
    df1.columns = ['Weekday','Day', 'Month', 'Year', 'Hour']
    df1.dropna(how='all', inplace=True)
    weekday_map = {'ma': 'Mon', 'ti': 'Tue', 'ke': 'Wed', 'to': 'Thu', 'pe': 'Fri', 'la': 'Sat', 'su': 'Sun'}
    month_map = {'tammi': '1', 'helmi': '2', 'maalis': '3', 'huhti': '4', 'touko': '5', 'kesä': '6', 'heinä': '7', 'elo': '8', 'syys': '9', 'loka': '10', 'marras': '11', 'joulu': '12'}
    df1.Weekday = df1.Weekday.map(weekday_map)
    df1.Month = df1.Month.map(month_map)
    # df1[['Year', 'Day', 'Hour']] = df1[['Year', 'Day', 'Hour']].astype(int)
    return df1

def split_date_continues():
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';')
    # df.drop(columns=['Päivämäärä'], inplace=True)
    # df.dropna(how='all', inplace=True)
    df1 = split_date(df)
    df2 = pd.concat([df1, df], axis=1)
    df2.drop(columns=['Päivämäärä', 'Unnamed: 21'], inplace=True)
    df2.dropna(how='all' , inplace=True)
    df2[['Year', 'Day', 'Hour', 'Month']] = df2[['Year', 'Day', 'Hour', 'Month']].astype(int)
    return df2

def main():
    df = split_date_continues()
    print(df.head())
    print("Shape:", df.shape)
    print("Column names:\n", df.columns)
    print(df.dtypes)
    # print(split_date(df))


if __name__ == "__main__":
    main()
