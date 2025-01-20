#!/usr/bin/env python3

def detect_ranges(numbers):
    # Sort the numbers list
    numbers = sorted(numbers)
    result = []
    start = numbers[0]
    
    for i in range(1, len(numbers)):
        if numbers[i] != numbers[i - 1] + 1:
            if start == numbers[i - 1]:
                result.append(start)
            else:
                result.append((start, numbers[i - 1] + 1))
            start = numbers[i]
    
    if start == numbers[-1]:
        result.append(start)
    else:
        result.append((start, numbers[-1] + 1))
    
    return result

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
