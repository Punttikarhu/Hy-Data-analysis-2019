#!/usr/bin/env python3
import re


def file_extensions(filename):
    noFileExtensions = []
    D = {}
    with open(filename) as f:
        for line in f:
            fname = line.split()
            parts = re.findall(r"\w+", line)
            if len(parts) == 1:
                noFileExtensions.append(*parts)
                continue
            if parts[-1] in D.keys():
                D[parts[-1]].append(*fname)
            else:
                D[parts[-1]] = fname

    return noFileExtensions, D

def main():
    noFileExtensions, D = file_extensions('filenames.txt')
    print(f'{len(noFileExtensions)} files with no extension')
    for key in sorted(D.keys()):
        print(f'{key} {len(D[key])}')

if __name__ == "__main__":
    main()
