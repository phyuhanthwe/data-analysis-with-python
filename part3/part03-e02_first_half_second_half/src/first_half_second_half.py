#!/usr/bin/env python3

import numpy as np

def first_half_second_half(a):
    m, n = a.shape
    first = a[:, 0:n//2]
    second = a[:, n//2:]
    # print(first)
    # print(second)
    mask = np.sum(first, axis=1) > np.sum(second, axis=1)
    return (a[mask])
    # return np.array([])

def main():
    a = np.array([
    [1, 2, 3, 4, 5, 6],  
    [7, 8, 9, 4, 5, 6],  
    [3, 1, 2, 9, 8, 7]   
    ])
    print(first_half_second_half(a))
    pass

if __name__ == "__main__":
    main()
