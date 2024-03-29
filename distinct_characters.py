#!/usr/bin/env python3

def distinct_characters(L):
    d = {}
    for i, k in enumerate(L):
        d[k] = len(set(k))

    return d


def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
