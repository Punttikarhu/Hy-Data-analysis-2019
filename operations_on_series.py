#!/usr/bin/env python3
import pandas as pd


def create_series(L1, L2):
    s1 = pd.Series(L1, index=list('abc'))
    s2 = pd.Series(L2, index=list('abc'))
    return (s1, s2)
    
def modify_series(s1, s2):
    s1['d'] = s2['b']
    del s2['b']
    print(s1, s2)
    return (s1, s2)
    
def main():
    s1, s2 = create_series([1, 2, 3], [4, 5, 6])
    modify_series(s1, s2)
    print(s1 + s2)
    
if __name__ == "__main__":
    main()
