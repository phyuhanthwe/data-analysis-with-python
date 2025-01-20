#!/usr/bin/env python3

def distinct_characters(L):
    dic = {}
    for i in L:
        dic[i] = len(set(i))
    return dic

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
