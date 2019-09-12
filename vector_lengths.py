#!/usr/bin/env python3

import numpy as np
#import scipy.linalg

def vector_lengths(a):
    a = np.sqrt(np.sum(np.power(a, 2), axis = 1))
    return a


def main():
    a = np.array([[1,1,1,1],[2,2,2,2]])
    vector_lengths(a)
    pass

if __name__ == "__main__":
    main()
