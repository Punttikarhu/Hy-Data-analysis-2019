#!/usr/bin/env python3
import pandas as pd


def read_series():
    a = {}
    while True:
        pair = input('Enter index value pair separated by whitespace: ')
        if pair == '':
            break
        parts = pair.split()
        if len(parts) != 2:
            raise Exception()
        a[parts[0]] = parts[1]
    s = pd.Series(a)
    return s

def main():
    read_series()

if __name__ == "__main__":
    main()
