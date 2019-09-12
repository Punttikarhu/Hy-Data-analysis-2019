#!/usr/bin/env python3

import numpy as np

def multiplication_table(n):
    a = np.arange(n)
    b = a * a.reshape(n, 1)

    return b

def main():
    print(multiplication_table(4))

if __name__ == "__main__":
    main()
