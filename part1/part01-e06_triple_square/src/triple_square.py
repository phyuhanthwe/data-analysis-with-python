#!/usr/bin/env python3

def triple(num):
        return num * 3
    
def square(num):
    return num ** 2
    
   
def main():
    # for i in range(1, 11):
    #     print(f"triple({i})=={triple(i)} square({i})=={square(i)}")
        
    for i in range(1, 11):
        t = triple(i)
        s = square(i)
        if s > t:
            break
        print(f"triple({i})=={t} square({i})=={s}")
    pass

if __name__ == "__main__":
    main()
