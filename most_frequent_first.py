#!/usr/bin/env python3

import numpy as np

def most_frequent_first(a, c):
    print(a)
    C = a[:, c]
    print(f'C column = {C}')
    unique, counts = np.unique(C, return_counts=True)
    print(f'unique = {unique}')
    print(f'counts = {counts}')
    idx = np.argsort(counts)
    idx = np.flip(idx)
    uniqueSorted = unique[idx]
    print(f'uniqueSorted = {uniqueSorted}')
    result = []
    for num in uniqueSorted:
        result.append(a[C == num])
    return np.concatenate(result, axis=0)



def main():
    most_frequent_first(np.random.randint(10, size=(8,8)), -1)

if __name__ == "__main__":
    main()
