#!/usr/bin/env python3

def reverse_dictionary(d):
    dic = {}
    for k, v in d.items():
        for i in v:
            if i not in dic:
               dic[i] = [] 
            dic[i].append(k)
            
    return dic

def main():
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(reverse_dictionary(d))
    pass

if __name__ == "__main__":
    main()
