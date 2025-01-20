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

def cycling_weather():
    df = split_date_continues()
    df1 = pd.read_csv('src/kumpula-weather-2017.csv', sep=',')
    df1.rename(columns={'m': 'Month', 'd':'Day'}, inplace=True)
    merge_df = pd.merge(df1, df, how='left')
    merge_df.drop(columns=['Time', 'Time zone'], inplace=True)
    return merge_df

def main():
    df = cycling_weather()
    print(df.dtypes)
    print(df.shape)
    return

if __name__ == "__main__":
    main()
