#!/usr/bin/env python3

import pandas as pd

def powers_of_series(s, k):
    l = []
    # df = pd.DataFrame(s, index=s.index, columns=['1'])
    for i in range(k):
        df1 = pd.DataFrame({(i+1): s**(i+1)})
        l.append(df1)
    df = pd.concat(l, axis=1)
    return df
    
def main():
    s = pd.Series([1,2,3,4], index=list("abcd"))
    print(powers_of_series(s, 3))
    return
    
if __name__ == "__main__":
    main()
