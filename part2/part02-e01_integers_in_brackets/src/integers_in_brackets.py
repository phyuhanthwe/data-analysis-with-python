#!/usr/bin/env python3
import re

def integers_in_brackets(s):
    l = re.findall(r'\[\s*([+-]?\d+)\s*]', s)
    return [int(i) for i in l]

def main():
    print(integers_in_brackets(" afd [asd] [12 ] [a34] [ -43 ]tt [+12]xxx"))
    print(integers_in_brackets("  afd [128+] [47 ] [a34]  [ +-43 ]tt [+12]xxx"))    
    pass

if __name__ == "__main__":
    main()
