#!/usr/bin/env python3

import pandas as pd

def main():
    df= pd.read_csv('src\municipal.tsv', sep='\t')
    r, c = df.shape
    print(f'Shape: {r}, {c}')
    print('Columns:')
    for column in df.columns:
        print(column)


if __name__ == "__main__":
    main()
