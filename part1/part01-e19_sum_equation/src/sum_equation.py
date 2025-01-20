#!/usr/bin/env python3
from functools import reduce
def sum_equation(L):
    if not L:
        return "0 = 0"
    s = reduce(lambda x, y: x + y, L, 0)
    st = ""
    for x,i in enumerate(L):
        if x != len(L) - 1:
            st = st + str(i) + " + "
        else:
            st = st + str(i)
    
    st = st + " = " + str(s)
    return st
    

def main():
    print(sum_equation([1,5,7]))
    print(sum_equation([]))
    pass

if __name__ == "__main__":
    main()
