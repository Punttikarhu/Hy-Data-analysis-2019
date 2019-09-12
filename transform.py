#!/usr/bin/env python3

def transform(s1, s2):
    strList1 = s1.split()
    strList2 = s2.split()
    intList1 = list(map(int, strList1))
    intList2 = list(map(int, strList2))

    return([a*b for a, b in zip(intList1, intList2)])

def main():
    transform("1 5 3", "2 6 -1")

if __name__ == "__main__":
    main()
