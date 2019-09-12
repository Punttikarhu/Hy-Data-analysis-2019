#!/usr/bin/env python3
from typing import List, Any

import numpy as np

def get_row_vectors(a):
    parts = np.split(a, 4)
    return parts

def get_column_vectors(a):
    parts = np.hsplit(a, 4)
    return parts

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print('Row vectors:')
    rows = get_row_vectors(a)
    print(rows)
    print('Column vectors:')
    columns = get_column_vectors(a)
    print(columns)
    print(np.shape(rows), np.shape(columns))


if __name__ == "__main__":
    main()
