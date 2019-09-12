#!/usr/bin/env python3

def reverse_dictionary(d):
    d2 = dict()
    for key, value in d.items():
        for item in value:
            if item not in d2:
                d2[item] = [key]
            else:
                d2[item].append(key)
    return d2

def main():
    d = {'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    reverse_dictionary(d)

if __name__ == "__main__":
    main()
