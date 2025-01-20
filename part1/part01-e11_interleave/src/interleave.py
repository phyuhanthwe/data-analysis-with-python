#!/usr/bin/env python3

def interleave(*lists):
    # l = []
    # for t in zip(*lists):
    #     l.append(t)
    l1 = [t for t in zip(*lists)]
    l = [i for tup in l1 for i in tup]        
    return l

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
