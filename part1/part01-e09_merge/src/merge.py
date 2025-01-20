#!/usr/bin/env python3

def merge(L1, L2):
    L = []
    i, j = 0, 0
    while i < len(L1) and j < len(L2):
        if L1[i] <= L2[j]:
            L.append(L1[i])
            i += 1
        else:
            L.append(L2[j])
            j += 1
            
    while i < len(L1):
        L.append(L1[i])
        i += 1
        
    while j < len(L2):
        L.append(L2[j])
        j += 1
        
    return L
    


def main():
    L1 =[1, 5, 9, 12]
    L2 = [2, 6, 10]
    print(merge(L1, L2))
    pass

if __name__ == "__main__":
    main()
