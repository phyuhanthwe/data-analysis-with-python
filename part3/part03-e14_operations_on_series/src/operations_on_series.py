#!/usr/bin/env python3

import pandas as pd

def create_series(L1, L2):
    if len(L1) == 3 and len(L2) == 3:
        s1 = pd.Series(L1, index=['a', 'b', 'c'])
        s2 = pd.Series(L2, index=['a', 'b', 'c'])
    return (s1, s2)
    
def modify_series(s1, s2):
    s1['d'] = s2['b']
    del s2['b']
    return (s1, s2)
    
def main():
    L1 = [1, 2, 3]
    L2 = [4, 5, 6]
    s1, s2 = create_series(L1, L2)
    print(modify_series(s1, s2))
    r = s1 + s2
    print(r)
    return r
    
if __name__ == "__main__":
    main()
