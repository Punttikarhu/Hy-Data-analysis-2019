#!/usr/bin/env python3

import pandas as pd

def powers_of_series(s, k):
    a = []
    for i in range(1, k+1):
        #df.append(s.values**i)
        df = pd.DataFrame(s**i, index=s.index, columns=[i])
        a.append(df)

    return pd.concat(a, axis=1)
    
def main():
    s = pd.Series([1, 2, 3, 4], index=list("abcd"))
    print(powers_of_series(s, 3))
    
if __name__ == "__main__":
    main()
