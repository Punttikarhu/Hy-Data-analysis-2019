#!/usr/bin/env python3

def find_matching(L, pattern):
    L2 = []
    for i, item in enumerate(L):
        if pattern in item:
            L2.append(i)
    return L2

def main():
    find_matching(["sensitive", "engine", "rubbish", "comment"], "en")

if __name__ == "__main__":
    main()
