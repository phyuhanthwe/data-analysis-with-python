#!/usr/bin/env python3

import re



def file_listing(filename="src/listing.txt"):
    r = []
    pattern = (r'^[^\s]+\s+\d+\s+[^\s]+\s+[^\s]+\s+(\d+)\s+(\w{3})\s+(\d{1,2})\s+(\d{2}):(\d{2})\s+(.+)$')
    with open (filename, 'r') as f:
        for line in f:
            match = re.match(pattern, line)
            if match:
                size = int(match.group(1))
                month = match.group(2)
                day = int(match.group(3))
                hour = int(match.group(4))
                minute = int(match.group(5))
                file_name = match.group(6)
                r.append((size, month, day, hour, minute, file_name))
    return r

def main():
    print(file_listing())
    pass

if __name__ == "__main__":
    main()
