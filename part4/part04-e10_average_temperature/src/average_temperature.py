#!/usr/bin/env python3

import pandas as pd

def average_temperature():
    df = pd.read_csv('src/kumpula-weather-2017.csv')
    filter_df = df[df['m'] == 7]
    avg_temperature = filter_df['Air temperature (degC)'].mean()
    return avg_temperature

def main():
    avg_temperature = average_temperature()
    # print(avg_temperature)
    print(f'Average temperature in July: {avg_temperature:.1f}')
    return

if __name__ == "__main__":
    main()
