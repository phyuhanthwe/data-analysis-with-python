#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt


def cyclists_per_day():
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';')
    pattern = r"(\w+)\s(\d+)\s(\w+)\s(\d+)\s(\d+):\d+"
    df1 = df.Päivämäärä.str.extract(pattern)
    df1.columns = ['Weekday','Day', 'Month', 'Year', 'Hour']
    df1.dropna(how='all', inplace=True)
    month_map = {'tammi': '1', 'helmi': '2', 'maalis': '3', 'huhti': '4', 'touko': '5', 'kesä': '6', 'heinä': '7', 'elo': '8', 'syys': '9', 'loka': '10', 'marras': '11', 'joulu': '12'}
    df1.Month = df1.Month.map(month_map)
    df2 = pd.concat([df1, df], axis=1)
    df2.drop(columns=['Hour', 'Weekday', 'Päivämäärä', 'Unnamed: 21'], inplace=True)
    daily_count = df2.groupby(['Year', 'Month', 'Day']).sum()
    return daily_count
    
    
def main():
    daily_count = cyclists_per_day()
    # print(daily_count.index)
    aug_2017 = daily_count.loc[pd.IndexSlice['2017', '8', :], :]
    for col in aug_2017.columns:
        plt.plot(range(1, 32), aug_2017[col].values, label=col)
    # plt.plot(aug_2017)
    plt.show()
    # print(df.dtypes)
    # print(df.shape)
    # print(df.head())
    return

if __name__ == "__main__":
    main()
