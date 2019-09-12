#!/usr/bin/env python3

def extract_numbers(s):
    s = s.split()
    L = []
    for item in s:
        try:
            L.append(int(item))
        except ValueError:
            try:
                L.append(float(item))
            except ValueError:
                pass
    return L

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
