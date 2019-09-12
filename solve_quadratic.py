#!/usr/bin/env python3

def solve_quadratic(a, b, c):
    D = (b**2 - 4 * a * c)**(0.5)
    solution1 = (-b + D)/(2 * a)
    solution2 = (-b - D)/(2 * a)
    return (solution1, solution2)


def main():
    print(solve_quadratic(1,-3,2))

if __name__ == "__main__":
    main()
