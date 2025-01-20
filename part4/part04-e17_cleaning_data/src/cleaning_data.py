#!/usr/bin/env python3

import pandas as pd
import numpy as np


def cleaning_data():
    df = pd.read_csv('src/presidents.tsv', sep='\t')
    cleaned_df = df.copy()
    p = {'Bush, George': 'George Bush', 'Clinton, Bill': 'Bill Clinton'}
    cleaned_df.President = cleaned_df.President.replace(p).str.title()

    cleaned_df['ExtractedYear'] = cleaned_df.Start.str.extract(r"(\d{4})")
    cleaned_df.Start = cleaned_df['Start'].where(cleaned_df['Start'].str.isnumeric(), cleaned_df['ExtractedYear'])
    cleaned_df.Start = pd.to_numeric(cleaned_df['Start'], errors='coerce', downcast='integer')
    cleaned_df.drop(columns=['ExtractedYear'], inplace=True)

    cleaned_df.Last = pd.to_numeric(cleaned_df['Last'], errors='coerce', downcast='integer')

    objto_int ={'two' : '2'}
    cleaned_df.Seasons = cleaned_df.Seasons.replace(objto_int).astype(int)

    v ={'Cheney, dick': 'Dick Cheney', 'gore, Al': 'Al Gore'}
    cleaned_df['Vice-president'] = cleaned_df['Vice-president'].replace(v).str.title()
    # cleaned_df['Vice-president'] = cleaned_df['Vice-president'].str.title()

    # print(cleaned_df.dtypes)
    cleaned_df['President'] = cleaned_df['President'].astype(object)
    cleaned_df['Vice-president'] = cleaned_df['Vice-president'].astype(object)
    cleaned_df['Seasons'] = cleaned_df['Seasons'].astype(int)
    cleaned_df['Start'] = cleaned_df['Start'].astype(int)
    cleaned_df['Last'] = cleaned_df['Last'].astype(float)
    return cleaned_df

def main():
    print(cleaning_data())
    return

if __name__ == "__main__":
    main()
