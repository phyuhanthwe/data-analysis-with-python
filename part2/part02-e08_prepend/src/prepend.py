#!/usr/bin/env python3

class Prepend(object):
    # Add the methods of the class here
    def __init__(self, param1):
        self.a = param1
        # print("Will print")
        pass
    
    def write(self, s):
        print(self.a + s)
        # return self.a, s
    

def main():
    p = Prepend("+++ ")
    p.write("Hello")
    p.write("Goodbye")
    pass

if __name__ == "__main__":
    main()
