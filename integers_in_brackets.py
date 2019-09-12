#!/usr/bin/env python3
import re


def integers_in_brackets(s):
#    result = re.findall(r"\[\s*([+-]?\d+)\s*\]", s)
    items = re.findall(r"[\[\{\(][^a-zA-Z\]]+[\}\]\)]", s)
    print(items)
    L = []

    for item in items:
        if '+-' not in item and '+]' not in item:
            num = re.findall(r"-?\d+", item)
            L.append(int(num[0]))
    return L

def main():
    str = 'afd [128+] [47 ] [a34]  [ +-43 ]tt [+12]xxx'
    print(str)
    integers_in_brackets(str)


if __name__ == "__main__":
    main()
