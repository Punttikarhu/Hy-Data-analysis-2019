#!/usr/bin/env python3

import numpy as np
import scipy.linalg

def vector_angles(X, Y):
    n, m = np.shape(Y)
    print(f'n, m = {n, m}')
    L = []
    for i in range(n):
        p = np.inner(X[i,:], Y[i,:])
        print(X[i,:], Y[i,:])
        print(f'p = {p}')
        normX = (np.inner(X[i,:], X[i,:])) **0.5
        normY = (np.inner(Y[i,:], Y[i,:])) **0.5
        cosa = p/(normX*normY)
        print(cosa)
        a = np.arccos(np.clip(cosa, -1.0, 1.0))
        b = np.rad2deg(a)
        L.append(b)
    c = np.array(L)
    print(c)
    return c

def main():
    n = 10
    A = np.random.randn(n, 3)
    a = vector_angles(A, A)

if __name__ == "__main__":
    main()
