#!/usr/bin/env python3

import numpy as np

# def diamond(n):
#     size = 2 * n - 1
#     matrix = np.zeros((size, size), dtype=int)
#     # for i in range(n):
#     #     matrix[i, n - i - 1 : n+i] = 1
#     #     matrix[size - i - 1, n - i - 1 : n+i] = 1
#     # return matrix
#     # upper = np.eye(size, dtype=int, k=n-1) + np.eye(size, dtype=int, k=-(n-1))
#     # matrix[:n, :] = upper[:n, :]
#     # matrix[n-1:, :] = upper[n-1:, :]
#     upper = np.eye(size, dtype=int, k=n-1)
#     lower = np.eye(size, dtype=int, k=-(n-1))
#     matrix = upper + lower
    
#     return matrix

def diamond(n):
    size = 2 * n - 1
    result = np.zeros((size, size), dtype=int)
    
    # upper = np.eye(size, dtype=int, k=n-1)  
    # upper += np.fliplr(np.eye(size, dtype=int, k=(n-1))) 

    # lower = np.eye(size, dtype=int, k=-(n-1))  
    # lower += np.fliplr(np.eye(size, dtype=int, k=-(n-1)))  

    # result[:n, :] = np.clip(upper[:n, :], 0, 1)
    # result[n-1:, :] = np.clip(lower[n-1:, :], 0, 1)
    
    upper = np.eye(size, dtype=int, k=n-1)  
    upper += np.fliplr(np.eye(size, dtype=int, k=(n-1)))
    upper = np.clip(upper[:n, :], 0, 1)  
    lower = np.flipud(upper[:-1, :])
    
    result = np.concatenate((upper, lower), axis=0)

    
    return result

def main():
    print(diamond(3))
    print(diamond(1))
    pass

if __name__ == "__main__":
    main()
