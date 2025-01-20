#!/usr/bin/env python3

def transform(s1, s2):
    try:
        l1 = map(int, s1.split(" "))    
        l2 = map(int, s2.split(" "))
        l3 = list(zip(l1, l2))
        l = []
        for tup in l3:
            t = 1
            for i in tup:
                t *= i
            l.append(t)
    except:
        l = []
    return l

    
def main():
    print(transform("1 5 3", "2 6 -1"))
    pass

if __name__ == "__main__":
    main()
