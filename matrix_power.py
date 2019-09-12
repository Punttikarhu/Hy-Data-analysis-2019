#!/usr/bin/env python3
from functools import reduce

import numpy as np

def matrix_power(a, n):
    if n == 0:
     return np.eye(len(a), dtype=int)

    if n == -1:
        return np.linalg.inv(a)

    if n > 0:
        b = reduce((lambda x, y: x @ y), [a] * (n - 1), a)
        return b

    if n < -1:
        b = reduce((lambda x, y: x @ y), [np.linalg.inv(a)] * abs(n + 1), np.linalg.inv(a))
        return b

def main():
    np.random.seed(0)
    a = np.random.randint(1, 10, (4, 4))
    print(f'a = {a}')
    print(matrix_power(a, 0))


if __name__ == "__main__":
    main()
