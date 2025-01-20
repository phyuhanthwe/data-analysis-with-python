#!/usr/bin/env python3
import pandas as pd

def read_series():
    data = {}
    while True:
        word = input("user input: ")
        if word == "":
            break
        l = word.split(maxsplit=1)
        if len(l) == 2:
            i, v = l
            data[i] = v
        else:
            # return pd.Series(data, dtype=object)
            raise ValueError("malformed input") 
    return pd.Series(data, dtype=object)

def main():
    try:
        print(read_series())
    except ValueError as e:
        print(e)
    pass

if __name__ == "__main__":
    main()
