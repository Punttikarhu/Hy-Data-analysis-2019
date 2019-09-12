#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    L = []
    with open(filename) as f:
        for i, line in enumerate(f):
            if i == 0:
                continue
            rgb = re.findall(r"(\d{1,3})", line)
            rgb = rgb[:3]
            colorname = re.findall(r"\w+[\w\s]\w+", line)
            colorname = colorname[-1]
            str = "".join(rgb[0] + '\t' + rgb[1] + '\t' + rgb[2] + '\t' + colorname)
            L.append(str)
    return L


def main():
    red_green_blue("rgb.txt")

if __name__ == "__main__":
    main()
