#!/usr/bin/env python3

import numpy as np

def get_rows(a):
    rows = []
    for i in range(a.shape[0]):
        rows.append(a[i,:])
    return rows

def get_columns(a):
    columns = []
    for i in range(a.shape[1]):
        columns.append(a[:,i])
    return columns

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Rows:", get_rows(a))
    print("Columns:", get_columns(a))

if __name__ == "__main__":
    main()
