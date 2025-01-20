#!/usr/bin/env python3

import pandas as pd

def snow_depth():
    df = pd.read_csv('src/kumpula-weather-2017.csv')
    max_snow = df['Snow depth (cm)'].max()
    return max_snow

def main():
    max_snow = snow_depth()
    print(f'Max snow depth: {max_snow:.1f}')
    return

if __name__ == "__main__":
    main()
