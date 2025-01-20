#!/usr/bin/env python3

import numpy as np

def vector_lengths(a):
    return np.sqrt(np.sum(a**2, axis=1))
    
    # return np.array([])

def main():
    np.random.seed(0)
    a = np.random.randint(0, 10, (3,2))
    print(a)
    print(vector_lengths(a))
    pass

if __name__ == "__main__":
    main()
