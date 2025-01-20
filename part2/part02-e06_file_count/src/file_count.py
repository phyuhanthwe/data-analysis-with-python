#!/usr/bin/env python3

import sys

def file_count(filename):
    # count = []
    # word = 0
    # cha = 0
    with open(filename, 'r') as f:
        lines = f.readlines()
        count = len(lines)
        word = sum(len(line.split()) for line in lines)
        cha = sum(len(line) for line in lines)
        return count, word, cha
        # for line in f:
        #     count.append(line)
            # word += len(line.split(" "))
            # for l in line:
            #     cha += len(l)
    # print(count)
    # print(len(count)) 
    # print(word) 
    # print(cha)     
    # return (len(count), word, cha)

def main():
    # print(file_count("src/test.txt"))
    for file in sys.argv[1:]:
        c, w, ch = file_count(file)
        print(f"{c}\t{w}\t{ch}\t{file}")
    pass

if __name__ == "__main__":
    main()
