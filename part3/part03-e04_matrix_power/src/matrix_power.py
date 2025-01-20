#!/usr/bin/env python3
import numpy as np
from functools import reduce

def matrix_power(a, n):
    # np.eye(2)
    # r = np.eye(a.shape[0])
    if n == 0:
        return np.eye(a.shape[0])
    elif n > 0:
        return reduce(np.matmul, (a for _ in range(n)))
    else: 
        a_inv = np.linalg.inv(a)
        return reduce(np.matmul, (a_inv for _ in range(abs(n))))
    
    

def main():
    a = np.array([[1, 2], [3, 4]])
    print(matrix_power(a, 0))
    return

if __name__ == "__main__":
    main()
