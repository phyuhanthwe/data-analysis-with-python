#!/usr/bin/env python3

import pandas as pd
import numpy as np


def split_date():
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';')
    # df1 = pd.DataFrame(df.Päivämäärä.str.split(" ", expand=True), columns=['Weekday','Day', 'Month', 'Year', 'Hour'])
    pattern = r"(\w+)\s(\d+)\s(\w+)\s(\d+)\s(\d+):\d+"
    df1 = df['Päivämäärä'].str.extract(pattern)
    df1.columns = ['Weekday','Day', 'Month', 'Year', 'Hour']
    df1 = df1.dropna(how='all')
    weekday_map = {'ma': 'Mon', 'ti': 'Tue', 'ke': 'Wed', 'to': 'Thu', 'pe': 'Fri', 'la': 'Sat', 'su': 'Sun'}
    month_map = {'tammi': '1', 'helmi': '2', 'maalis': '3', 'huhti': '4', 'touko': '5', 'kesä': '6', 'heinä': '7', 'elo': '8', 'syys': '9', 'loka': '10', 'marras': '11', 'joulu': '12'}
    df1.Weekday = df1.Weekday.map(weekday_map)
    df1.Month = df1.Month.map(month_map).astype(int)
    # df1.Year = df1.Year.astype(int)
    # df1.Day = df1.Day.astype(int)
    # df1.Hour = df1.Hour.astype(int)
    df1[['Year', 'Day', 'Hour']] = df1[['Year', 'Day', 'Hour']].astype(int)
    print(df1.dtypes)
    return df1

def main():
    print(split_date())
    return
       
if __name__ == "__main__":
    main()
