#!/usr/bin/env python3

import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

def mystery_data():
    df = pd.read_csv('src/mystery_data.tsv', sep='\t')
    x = df[['X1', 'X2', 'X3', 'X4', 'X5']].values
    y = df['Y'].values
    # print(x.T.shape)
    # print(y.shape)
    model = LinearRegression(fit_intercept=False)
    model.fit(x, y)
    return model.coef_

def main():
    # print(mystery_data())
    # print the coefficients here
    coefficients = mystery_data()
    for i, coef in enumerate(coefficients, start=1):
        print(f"Cofficient of X{i} is {coef}")
    
if __name__ == "__main__":
    main()
