#!/usr/bin/env python3

import numpy as np

def diamond(n):
    a = np.eye(n, dtype = int)
    b = np.flip(a, axis = 1)
    c = np.concatenate((b, a[:,1:]), axis = 1)
    d = np.flip(c)
    e = np.concatenate((c, d[1:,:]))
    return e


def main():
    diamond(3)

if __name__ == "__main__":
    main()
