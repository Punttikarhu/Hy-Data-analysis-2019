#!/usr/bin/env python3
from functools import reduce


def sum_equation(L):
    if (len(L) == 0):
        return "0 = 0"
    else:
        str = ""
        for i in range(len(L) - 1):
            str += "".join(f"{L[i]} + ")

        str += f"{L[-1]} = {sum(L)}"
        return str


def main():
    sum_equation([1,5,7])

if __name__ == "__main__":
    main()
