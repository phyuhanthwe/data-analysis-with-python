#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

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


# def cycling_weather_continues():
def cycling_weather_continues(station):
    wdf = pd.read_csv('src/kumpula-weather-2017.csv', sep= ',')
    wdf.rename(columns={'m': 'month', 'd': 'day'}, inplace=True)
    wdf['Date'] = pd.to_datetime(wdf[['Year', 'month', 'day']])
    wdf = wdf.set_index('Date')[['Precipitation amount (mm)', 'Snow depth (cm)', 'Air temperature (degC)']]
    # print(wdf.head())
    
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';')
    cdf = split_date(df)
    cdf = pd.concat([cdf, df], axis=1)
    cdf['Date'] = pd.to_datetime(cdf[['Year', 'Month', 'Day']], dayfirst=True)
    cdf = cdf.set_index('Date')

    cdf = cdf[cdf['Year'] == '2017']

    cdf.drop(columns=['Weekday', 'Day', 'Month', 'Year', 'Hour', 'Päivämäärä', 'Unnamed: 21'], inplace=True)
    cdf = cdf[cdf.index.notna()]
    # print(cdf.head())

    # cdf_2017 = cdf.index.year == 2017
    daily = cdf.resample('D').sum()
    # print(daily.head())

    combined_data = pd.merge(wdf, daily, left_index=True, right_index=True, how='inner')
    combined_data.fillna(method='ffill', inplace=True)
    # print(combined_data.head())

    x = combined_data[['Precipitation amount (mm)', 'Snow depth (cm)', 'Air temperature (degC)']]
    y = combined_data[station]
    model = LinearRegression(fit_intercept=True)
    model.fit(x, y)
    coef = model.coef_
    score = model.score(x, y)

    return (coef, score)

    
def main():
    station = 'Baana'
    coef, score = (cycling_weather_continues(station))
    print(f"Measuring station: {station}")
    print(f"Regression coefficient for variable 'precipitation': {coef[0]:.1f}")
    print(f"Regression coefficient for variable 'snow depth': {coef[1]:.1f}")
    print(f"Regression coefficient for variable 'temperature': {coef[2]:.1f}")
    print(f"Score: {score:.2f}")
    return

if __name__ == "__main__":
    main()
