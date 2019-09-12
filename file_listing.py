#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):
    details = []
    with open(filename) as f:
        for line in f:
            size = re.findall(r"(\d+)\s[A-Za-z]{3}\s" , line)
            month = re.findall(r"\s([A-Za-z]{3})\s", line)
            day = re.findall(r"[A-Za-z]{3}\s(\s\d|\d{2})\s", line)
            hour = re.findall(r"\s(\d|\d{2}):", line)
            minute = re.findall(r":(\d|\d{2})\s", line)
            fname = re.findall(r"\d{1,2}:\d{1,2}\s(.*)\s", line)
            details.append((int(*size), *month, int(*day), int(*hour),
                            int(*minute), *fname))
    for line in details:
        print(line)
    return details

def main():
    print(file_listing('listing.txt'))

if __name__ == "__main__":
    main()
