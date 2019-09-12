#!/usr/bin/env python3

import numpy as np

def first_half_second_half(a):
    m = np.shape(a)[1]
    m = int(m/2)
    mask = np.sum(a[:,:m], axis=1) > np.sum(a[:, m:], axis=1)
    return a[mask]


def main():
    first_half_second_half(np.random.randint(10, size=(3, 4)))

if __name__ == "__main__":
    main()
