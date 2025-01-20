#!/usr/bin/env python3

import numpy as np

def get_row_vectors(a):
    # l = []
    # a = np.array(a)
    # m, n = a.shape
    # for i in range(m) :
    #     l.append(a[i:i+1, :])
    r = [a[i:i+1, :] for i in range(a.shape[0])]
    return r

def get_column_vectors(a):
    l = []
    a = np.array(a)
    m, n = a.shape
    for i in range(n):
        l.append(a[:,i:i+1])
    # r = [a[:, i:i+1] for i in range(a.shape[1])]
    return l

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    # a = np.array([[5, 0, 3], [3, 7, 9]])
    
    print("a:", a)
    print("Row vectors:", get_row_vectors(a))
    print("Column vectors:", get_column_vectors(a))

if __name__ == "__main__":
    main()
