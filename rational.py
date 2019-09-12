#!/usr/bin/env python3

class Rational(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"{self.a}/{self.b}"

    def __add__(self, r2):
        if (self.b == r2.b):
            return Rational(self.a + r2.a, self.b)
        else:
            return Rational(self.a * r2.b + r2.a * self.b, self.b * r2.b)

    def __sub__(self, r2):
        if (self.b == r2.b):
            return Rational(self.a - r2.a, self.b)
        else:
            return Rational(self.a * r2.b - r2.a * self.b, self.b * r2.b)

    def __mul__(self, r2):
        return Rational(self.a * r2.a, self.b * r2.b)

    def __truediv__(self, r2):
        return Rational(self.a * r2.b, self.b * r2.a)

    def __eq__(self, r2):
        return self.a == r2.a and self.b == r2.b

    def __gt__(self, r2):
        return self.a * r2.b / self.b * r2.b > r2.a * self.b / self.b * r2.b

def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))

if __name__ == "__main__":
    main()
