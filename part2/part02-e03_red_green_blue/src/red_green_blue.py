#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    res = []
    pattern =(r"(\d+)\s+(\d+)\s+(\d+)\s+(.+)")
    with open(filename) as f:
        next(f)
        for line in f:
            match = re.search(pattern, line)
            if match:
                r = match.group(1)
                g = match.group(2)
                b = match.group(3)
                name = match.group(4)
                formated_string = f"{r}\t{g}\t{b}\t{name}"
                res.append(formated_string)
            else:
                print(f"Line not matched: {line}")
    print(f"length of result list: {len(res)}")
    return res

def main():
    (red_green_blue())
    pass

if __name__ == "__main__":
    main()
