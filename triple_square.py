#!/usr/bin/env python3


def main():

    for i in range(1, 11):
        squareValue = square(i)
        tripleValue = triple(i)
        if squareValue > tripleValue:
            break
        print(f'triple({i})=={tripleValue} square({i})=={squareValue}')

def triple(num):
    return num * 3

def square(num):
    return num ** 2

if __name__ == "__main__":
    main()
