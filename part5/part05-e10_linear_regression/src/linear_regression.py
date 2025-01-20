#!/usr/bin/env python3

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def fit_line(x, y):
    model = LinearRegression(fit_intercept=True)
    model.fit(x[:, np.newaxis], y)
    s = model.coef_[0]
    i = model.intercept_
    return s, i
    
def main():
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([2, 4, 5, 4, 5])
    s, i = (fit_line(x, y))
    print("Slope:", s)
    print("Intercept:", i)
    plt.scatter(x,y, color="blue", label="Original Data")
    plt.plot(x, s * x + i, color="red", label="Fitted Line")
    plt.show()
   
    
if __name__ == "__main__":
    main()
