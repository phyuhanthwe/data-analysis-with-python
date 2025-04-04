#!/usr/bin/python3

import numpy as np

def meeting_planes(a1, b1, c1, a2, b2, c2, a3, b3, c3):
    matrix = np.array([[-a1, -b1, 1], [-a2, -b2, 1], [-a3, -b3, 1]])
    constant = np.array([c1, c2, c3])
    y, x , z = np.linalg.solve(matrix, constant)
    
    return x, y, z

def main():
    a1=1
    b1=4
    c1=5
    a2=3
    b2=2
    c2=1
    a3=2
    b3=4
    c3=1

    x, y, z = meeting_planes(a1, b1, c1, a2, b2, c2, a3, b3, c3)
    print(f"Planes meet at x={x}, y={y} and z={z}")

if __name__ == "__main__":
    main()
