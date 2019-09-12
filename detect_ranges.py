#!/usr/bin/env python3

def detect_ranges(L):
    if len(L) == 0:
        return
    if len(L) == 1:
        return L

    L = sorted(L)
    L2 = []

    i = 0
    while True:
        if L[i+1] == L[i] + 1:
            startIndex = i
            while L[i + 1] == L[i] + 1:
                endIndex = i
                i = i + 1
                if i > len(L) - 2:
                    break
            L2.append((L[startIndex], L[endIndex+1]+1))
        else:
            L2.append(L[i])
        i = i + 1
        if i > len(L) - 2:
            break
    #add single if last was single
    if L[len(L)-1] != L[len(L)-2] + 1:
        L2.append(L[len(L)-1])

    return L2



def main():
    L = sorted([2, 5, 4, 8, 12, 6, 7, 10, 13])
    result = detect_ranges(L)
    LL = [2, 5, 4, 8, 12, 6, 7, 10, 13, 15]
    result2 = detect_ranges(LL)
    print(L)
    print(result)
    print(LL)
    print(result2)

if __name__ == "__main__":
    main()
