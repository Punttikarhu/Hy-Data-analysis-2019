'Functions for basic triangle operations'

__author__ = 'Janne'
__version__ = '0.0.1'

def hypothenuse(a, b):
    'Calculates the hypothenuse of a triangle when sides a and b are given'
    return (a**2 + b**2)**0.5

def area(width, height):
    'Calculates area of triangle when width and height are specified'
    return 0.5 * width * height