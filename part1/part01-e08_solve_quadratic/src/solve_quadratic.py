#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):
    plus_x =(-b + (math.sqrt((b ** 2) - (4 * a  * c)))) / (2 * a)
    minus_x =(-b - (math.sqrt((b ** 2) - (4 * a  * c)))) / (2 * a)
    return (plus_x, minus_x)


def main():
    print(solve_quadratic(1,-3,2))
    print(solve_quadratic(1,2,1))
    pass

if __name__ == "__main__":
    main()
