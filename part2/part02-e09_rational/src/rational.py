#!/usr/bin/env python3
from math import gcd

class Rational(object):
    def __init__(self, a, b):
        if b == 0:
            raise ValueError("cannot be zero")
        common_divisor = gcd(a, b)
        self.a = a // common_divisor
        self.b = b // common_divisor
        
        
    def __str__(self):
        if self.b == 1:
            return f"{self.a}"
        else:
            return f"{self.a}/{self.b}"

    def __add__(self, other):
        new_a = (self.a *other.b) +  (self.b * other.a)
        new_b = self.b * other.b
        return(Rational(new_a, new_b))

    def __sub__	(self, other):
        new_a = (self.a *other.b) -  (self.b * other.a)
        new_b = self.b * other.b
        return(Rational(new_a, new_b))

    def __mul__(self, other):
        new_a = self.a * other.a
        new_b = self.b * other.b
        return(Rational(new_a, new_b))
    
    def __truediv__(self, other):
        new_a = self.a * other.b
        new_b = self.b * other.a
        return(Rational(new_a, new_b))
    
    def __eq__(self, other):
        return self.a * other.b == self.b * other.a
    
    def __gt__(self, other):
        return self.a * other.b > self.b * other.a
    
    def __lt__(self, other):
        return self.a * other.b < self.b * other.a
        
def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))

if __name__ == "__main__":
    main()
