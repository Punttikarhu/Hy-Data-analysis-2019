#!/usr/bin/env python3

def merge(L1, L2):
    L3 = L1 + L2
    L = []
    while len(L3) > 0:
        min = L3[0]
        for num in L3:
            if num < min:
                min = num
        L.append(min)
        L3.remove(min)
    return L

def main():
    a = [5, 6, 8]
    b = [2, 4, 6]
    print(merge(a , b))

if __name__ == "__main__":
    main()
