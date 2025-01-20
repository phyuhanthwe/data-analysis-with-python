# Enter you module contents here
"""
This module provides two function to create hypotenuse and area.
"""
__version__ = "1.0"
__author__ = "phyu han"

import math
def hypotenuse(a, b):
    "The hypotenuse is the longest side of a right triangle and is opposite the right angle."
    c = math.sqrt((a**2 + b**2))
    return c

def area(h,w):
    "A right-angled triangle is the same as half of a square or a rectangle."
    return 0.5 * h * w