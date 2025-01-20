#!/usr/bin/env python3

import numpy as np
# import scipy.linalg

def vector_angles(X, Y):
    matrix = np.sum(X * Y, axis=1)
    norm_x = np.sqrt(np.sum(X**2, axis=1))
    norm_y = np.sqrt(np.sum(Y**2, axis=1))
    angle = matrix / (norm_x * norm_y)
    angle = np.clip(angle, -1.0, 1.0)
    radian = np.arccos(angle)
    degree = np.degrees(radian)
    return degree
    # np.array([])

def main():
    X=np.array([[0,0,1], [-1,1,0]])
    Y=np.array([[0,1,0], [1,1,0]])
    print(vector_angles(X, Y))

if __name__ == "__main__":
    main()
