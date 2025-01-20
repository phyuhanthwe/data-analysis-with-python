#!/usr/bin/env python3
import string

def word_frequencies(filename="src/alice.txt"):
    dic = {}
    with open(filename) as f:
        for line in f:
            # line = line.strip("""!"#$%&'()*,-./:;?@[]_\n""")
            line = line.split(" ")
            for k in line:
                k = k.strip("""!"#$%&'()*,-./:;?@[]_\n""")
                if k in dic:
                    dic[k] = dic[k] + 1
                else:
                    dic[k] = 1
    # print(dic['creating'])
    print(len(dic))
    return dic

def main():
    (word_frequencies())
    pass

if __name__ == "__main__":
    main()
