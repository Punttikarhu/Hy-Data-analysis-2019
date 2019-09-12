#!/usr/bin/env python3

import sys

def file_count(filename):
    with open(filename) as f:
        data = f.read()
        numberOfLines = len(data.strip().split('\n'))
        numberOfWords = len(data.split())
        numberOfChars = len(data)
    return numberOfLines, numberOfWords, numberOfChars

def main():

    for filename in sys.argv[1:]:
        numberOfLines, numberOfWords, numberOfChars = file_count(filename)
        print(f'{numberOfLines}\t{numberOfWords}\t{numberOfChars}\t{filename}')

if __name__ == "__main__":
    main()
