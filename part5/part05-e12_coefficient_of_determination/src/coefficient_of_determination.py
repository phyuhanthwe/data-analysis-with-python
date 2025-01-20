#!/usr/bin/env python3

import pandas as pd
from sklearn import linear_model


def coefficient_of_determination():
    df = pd.read_csv('src/mystery_data.tsv', sep='\t')
    x = df[['X1', 'X2', 'X3', 'X4', 'X5']].values
    y = df['Y'].values
    model = linear_model.LinearRegression(fit_intercept=True)
    model.fit(x, y)
    l = []
    l.append(model.score(x, y))
    for i in ['X1', 'X2', 'X3', 'X4', 'X5']:
        model.fit(df[i].values.reshape(-1, 1), y)
        s = model.score(df[i].values.reshape(-1, 1), y)
        l.append(s)
    return l
    
def main():
    # print(coefficient_of_determination())
    score = coefficient_of_determination()
    print(f"R2-score with feature(s) X: {score[0]}")
    for i, s in enumerate(score[1:], start=1):
        print(f"R2-score with feature(s) X{i}: {s}")

if __name__ == "__main__":
    main()
