#!/usr/bin/env python3

def extract_numbers(s):
    l = s.split(" ")
    r = []
    s = []
    for i in l:
        try: 
            r.append(int(i))
        except:
            try:
                r.append(float(i))
            except ValueError:
                continue
    return r
        
    
def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
