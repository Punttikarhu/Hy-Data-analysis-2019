#!/usr/bin/env python3

import pandas as pd

def municipalities_of_finland():
    df = pd.read_csv('src\municipal.tsv', sep='\t')
    df2 = pd.DataFrame(df[1:], index=df['Region 2018'][1:], columns=df.columns[1:])
    print(df['Region 2018'][1:])
    return df2
    
def main():
    municipalities_of_finland()
    
if __name__ == "__main__":
    main()
