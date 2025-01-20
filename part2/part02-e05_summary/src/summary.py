#!/usr/bin/env python3

import sys
import statistics
import re

def summary(filename):
    sum = 0
    num = 0
    l = []
    with open(filename) as f:
        for line in f:
            if re.match(r"[^A-Za-z]", line):
                sum += float(line)
                # print(line)
                num += 1
                l.append(float(line))
        avg = sum / num
        std = statistics.stdev(l)
    #     r = f"File: {filename} Sum: {sum:6f} Average: {avg:6f} Stddev: {std:6f}"
    # return r
    return (sum,avg,std)

def main():
    # print(summary("src/example3.txt"))
    # print(summary("src/example.txt"))
    for f in sys.argv[1:]:
        # print(summary(f))
        s, a, std = summary(f)
        print(f"File: {f} Sum: {s:6f} Average: {a:6f} Stddev: {std:6f}")
    pass

if __name__ == "__main__":
    main()
