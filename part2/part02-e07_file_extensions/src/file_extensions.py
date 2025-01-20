#!/usr/bin/env python3
import re

def file_extensions(filename):
    l = []
    d = {}
    with open(filename, 'r') as f:
        for line in f:
            line = re.sub(r"\n", "",line)
            # if "." in line:
            #     index = (line.index("."))
            #     if "." not in line[index+1:]:
            #         k.append(line[index+1:])
            #     else:
            #         print(line[index+1:])
            l1 =(line.split("."))
            if len(l1) > 1:
                if l1[-1] in d.keys():
                    d[l1[-1]].append(line)
                else:
                    d[l1[-1]] = [line]
            else:
                l.append(l1[-1])
    # print(d)
    # # print(l)
    return (l, d)

def main():
    l, d = (file_extensions("src/filenames.txt"))
    print(f"{len(l)} files with no extension")
    for k in sorted(d):
        print(f"{k} {len(d[k])}")

    pass

if __name__ == "__main__":
    main()
