#!/usr/bin/env python3

import math


def main():
    # enter you solution here
    shapes = ['triangle', 'rectangle', 'circle']
    def triangle():
        w = int(input("Give base of the triangle: "))
        h = int(input("Give height of the triangle: "))
        area = 0.5 * w * h
        print(f"The area is {area:.6f}")
    
    def rectangle():
        w = int(input("Give width of the rectangle: "))
        h = int(input("Give height of the rectangle: "))
        area = w * h
        print(f"The area is {area:.6f}")
    
    def circle():
        r = int(input("Give radius of the circle: "))
        area = math.pi * r * r
        print(f"The area is {area:.6f}")
    
    while True:
        shape = input("Choose a shape (triangle, rectangle, circle): ")
        if shape == 'triangle':
            triangle()
        elif shape == 'rectangle':
            rectangle()
        elif shape == "circle":
            circle()
        elif shape == "":
            break
        else:
            print("Unknown shape!")
            

if __name__ == "__main__":
    main()
