#!/usr/bin/env python3

import pandas as pd

def inverse_series(s):
    s2 = pd.Series(s.index, index=s.values)
    return s2

def main():
    s = pd.Series([1,2,3,1], index=list('abcd'))
    inverse_series(s)

if __name__ == "__main__":
    main()
