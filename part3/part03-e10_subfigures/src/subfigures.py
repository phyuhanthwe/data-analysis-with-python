#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def subfigures(a):
    x1 = a[:, 0]
    print(x1)
    y1 = a[:, 1]
    c = a[:, 2]
    s = a[:, 3]
    fig, ax = plt.subplots(1, 2)
    ax[0].plot(x1, y1)
    ax[1].scatter(x1, y1, c=c, s=s)
    plt.show()
    pass

def main():
    a = np.array([[1, 2, 3, 4], [3, 4, 1, 2]])
    subfigures(a)
    pass

if __name__ == "__main__":
    main()
