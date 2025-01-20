#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
from os import path


def commute():
    df = pd.read_csv(path.join(path.dirname(__file__), './Helsingin_pyorailijamaarat.csv'), sep=';')
    df.dropna(how='all', inplace=True)
    pattern = r"\w+\s(\d+)\s(\w+)\s(\d+)\s(\d+):\d+"
    df1 = df.Päivämäärä.str.extract(pattern)
    df1.columns = ['Day', 'Month', 'Year', 'Hour']
    # weekday_map = {'ma': 'Mon', 'ti': 'Tue', 'ke': 'Wed', 'to': 'Thu', 'pe': 'Fri', 'la': 'Sat', 'su': 'Sun'}
    # weekday_map = {'ma': '1', 'ti': '2', 'ke': '3', 'to': '4', 'pe': '5', 'la': '6', 'su': '7'}
    month_map = {'tammi': '1', 'helmi': '2', 'maalis': '3', 'huhti': '4', 'touko': '5', 'kesä': '6', 'heinä': '7', 'elo': '8', 'syys': '9', 'loka': '10', 'marras': '11', 'joulu': '12'}
    # df1.Weekday =df1.Weekday.map(weekday_map)
    df1.Month = df1.Month.map(month_map)
    df1['Datetime'] = pd.to_datetime(df1[['Year', 'Month', 'Day']].astype(str).agg('-'.join, axis=1))

    df = df.drop(columns=['Päivämäärä', 'Unnamed: 21']).join(df1)
    df = df[(df['Datetime'].dt.year == 2017) & (df['Datetime'].dt.month == 8)]
    df['Weekday'] = df['Datetime'].dt.weekday + 1
    # df = df[(df['Year'] == '2017') & (df['Month'] == '8')]
    result = df.groupby('Weekday').sum(numeric_only=True)
    # print(df['Weekday'].unique())
    return result
    
def main():
    df = commute()
    print(df.head())
    # print(df.shape)
    # %matplotlib inline
    plt.plot(df)
    weekdays="mon tue wed thu fri sat sun".title().split()
    plt.gca().set_xticklabels(weekdays)
    plt.show()
    return


if __name__ == "__main__":
    main()
