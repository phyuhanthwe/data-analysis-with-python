#!/usr/bin/env python3

def is_positive(x):
    return x > 0

def positive_list(L):
    l = list(filter(is_positive, L)) 
    return l

def main():
    print(positive_list([2,-2,0,1,-7]))
    pass

if __name__ == "__main__":
    main()
