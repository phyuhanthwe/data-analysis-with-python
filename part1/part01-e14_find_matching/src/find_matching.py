#!/usr/bin/env python3

def find_matching(L, pattern):
    l = []
    for i, v in enumerate(L):
        if pattern in v:
            l.append(i)
    return l

def main():
    print(find_matching(["sensitive", "engine", "rubbish", "comment"], "en"))
    pass

if __name__ == "__main__":
    main()
