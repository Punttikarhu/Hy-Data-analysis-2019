#!/usr/bin/env python3
import re
import sys
from statistics import mean, stdev

def summary(filename):
    with open(filename) as f:
        nums = f.read()
        nums = re.findall(r"[-\d\s][0-9^\.]+", nums)
        nums = list(map(float, nums))
        print(nums)
        s = sum(nums)
        average = mean(nums)
        std = stdev(nums)

    return (s ,average , std)

def main():
    for filename in sys.argv[1:]:
        stats = summary(filename)
        print('File: {0} Sum: {1:.6f} Average: {2:.6f} Stddev: {3:.6f}'
              .format(filename, *stats))

if __name__ == "__main__":
    main()
